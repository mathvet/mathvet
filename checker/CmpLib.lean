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

/-- Structural verdict: alpha-equivalence of types (and values for definitions) after renaming `Chal.` to `OAI.`. -/
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

/-- Fallback for structural mismatches: are the two types (and definition values) definitionally equal, with the
universe parameters identified positionally? Definitional equality absorbs differences that come from re-elaborating
the challenge source in a richer environment: a different (but equal) instance path found by typeclass resolution,
differently generated auxiliary proofs (proof irrelevance), or a tactic block that elaborated to another term for the
same value. -/
def defeqOf (a b : ConstantInfo) : MetaM (Bool × Bool) := do
  if a.levelParams.length != b.levelParams.length then return (false, false)
  let us ← a.levelParams.mapM fun _ => mkFreshLevelMVar
  let inst (e : Expr) (ps : List Name) := e.instantiateLevelParams ps us
  let tyOk ← try withTransparency .all <| isDefEq (inst (renameConsts a.type) a.levelParams) (inst b.type b.levelParams)
    catch _ => pure false
  let valOk ← match a, b with
    | .defnInfo da, .defnInfo db =>
        try withTransparency .all <| isDefEq (inst (renameConsts da.value) a.levelParams) (inst db.value b.levelParams)
        catch _ => pure false
    | _, _ => pure true
  return (tyOk, valOk)

elab "#cmp_closure" roots:(ppSpace ident)* : command => do
  let env ← getEnv
  let rootNames : Array Name := roots.map fun r => r.getId
  let names := chalClosure env rootNames
  for n in names do
    let m := chalToOAI n
    match env.find? n, env.find? m with
    | some a, some b =>
      let v := verdictOf a b
      if v == "ok" then logInfo m!"CMP {m} [{kindOf a}] ok"
      else
        let (tyOk, valOk) ← liftTermElabM (defeqOf a b)
        let note := if tyOk && valOk then " (DEFEQ: definitionally equal; structural difference only)"
                    else if tyOk then " (types definitionally equal, values NOT)"
                    else " (types NOT definitionally equal)"
        logInfo m!"CMP {m} [{kindOf a}] {v}{note}"
    | some a, none => logInfo m!"CMP {m} [{kindOf a}] MISSING_IN_SOLUTION"
    | _, _ => logInfo m!"CMP {n} NOT_FOUND"

end CmpLib
