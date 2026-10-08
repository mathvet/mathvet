import Lean
open Lean Meta Elab Command

namespace CmpLib

def chalToOAI (n : Name) : Name := n.replacePrefix `Chal `OAI

partial def renameConsts (e : Expr) : Expr :=
  e.replace fun x => match x with
    | .const n ls => if (`Chal).isPrefixOf n then some (.const (chalToOAI n) ls) else none
    | .proj s i b => if (`Chal).isPrefixOf s then some (.proj (chalToOAI s) i (renameConsts b)) else none
    | _ => none

def chalConsts (e : Expr) : Array Name :=
  e.getUsedConstants.filter fun n => (`Chal).isPrefixOf n

def chalClosure (env : Environment) (roots : Array Name) : Array Name := Id.run do
  let mut seen : Array Name := #[]
  let mut todo := roots
  let mut fuel := 200000
  while todo.size > 0 && fuel > 0 do
    fuel := fuel - 1
    let n := todo.back!
    todo := todo.pop
    if seen.contains n then continue
    seen := seen.push n
    if let some ci := env.find? n then
      todo := todo ++ chalConsts ci.type
      match ci with
      | .defnInfo d => todo := todo ++ chalConsts d.value
      | .inductInfo d => todo := todo ++ d.ctors.toArray
      | _ => pure ()
  return seen

def kindOf : ConstantInfo → String
  | .defnInfo _ => "def" | .thmInfo _ => "thm" | .inductInfo _ => "ind" | .ctorInfo _ => "ctor"
  | .axiomInfo _ => "axiom" | .opaqueInfo _ => "opaque" | .quotInfo _ => "quot" | .recInfo _ => "rec"

def verdictOf (a b : ConstantInfo) : String :=
  let kk := kindOf a == kindOf b
  let kt := (renameConsts a.type).eqv b.type
  let kv := match a, b with
    | .defnInfo da, .defnInfo db => (renameConsts da.value).eqv db.value
    | .inductInfo ia, .inductInfo ib =>
        ia.numParams == ib.numParams && ia.numIndices == ib.numIndices && ia.ctors.length == ib.ctors.length
    | .thmInfo _, .thmInfo _ => true
    | .ctorInfo ca, .ctorInfo cb => ca.cidx == cb.cidx
    | .opaqueInfo _, .opaqueInfo _ => true
    | .recInfo _, .recInfo _ => true
    | .quotInfo _, .quotInfo _ => true
    | .axiomInfo _, .axiomInfo _ => true
    | _, _ => false
  if !kk then "KIND_MISMATCH" else if !kt then "TYPE_MISMATCH" else if !kv then "VALUE_MISMATCH" else "ok"

elab "#cmp_closure" roots:(ppSpace ident)* : command => do
  let env ← getEnv
  let rootNames : Array Name := roots.map fun r => r.getId
  let names := chalClosure env rootNames
  for n in names do
    let m := chalToOAI n
    match env.find? n, env.find? m with
    | some a, some b => logInfo m!"CMP {m} [{kindOf a}] {verdictOf a b}"
    | some a, none => logInfo m!"CMP {m} [{kindOf a}] MISSING_IN_SOLUTION"
    | _, _ => logInfo m!"CMP {n} NOT_FOUND"

end CmpLib
