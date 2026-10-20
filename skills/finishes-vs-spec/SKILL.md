---
name: "Finishes vs Spec Check"
skill_id: "finishes-vs-spec"
skill_num: "04"
category: "Before You Bid"
description: "Finishes checked against specs."
version: "1.0.0"
deterministic: true
qa_verified: true
---

# Skill #04: Finishes vs Spec Check

**Category:** Before You Bid  
**Pipeline Architecture:** 7-Agent Local Multi-Agent Architecture with Lead Engineer Human-In-The-Loop (HITL) Gate  
**Dataset Context:** 33/11 kV Industrial Receiving Substation & MRSS EPC Package  

---

## 1. Objective & Purpose
Finishes checked against specs. This playbook cross-checks **Room Finish Schedule (DWG-AR-401)** against **Div 09 Finish Specification** to deterministically detect scope gaps, commercial bid-killers, drawing clashes, and cost/schedule variances without hallucinations or external cloud dependencies.

---

## 2. Input Specifications
- **Source A (Room Finish Schedule (DWG-AR-401)):** Contract documents, technical specifications, CSI MasterFormat divisions, or baseline schedules.
- **Source B (Div 09 Finish Specification):** Drawing callouts, single-line diagrams, submittals, vendor cut sheets, or site progress records.

---

## 3. Multi-Agent Pipeline Execution
1. **CoordinatorAgent:** Initializes audit session and routes files to parser.
2. **DocumentExtractionAgent:** Ingests and normalizes raw text and schedules into structured parameters.
3. **Spec / Source Analysis Agent:** Builds baseline criteria and technical constraints.
4. **Drawing / Source Analysis Agent:** Extracts comparison values and tolerance ranges.
5. **DiscrepancyResolutionAgent:** Executes deterministic rule checks to compute cost deltas and critical path delays.
6. **QualityAssuranceAgent:** Verifies 100% citation trace back to clause and drawing sheet references.
7. **HumanApprovalGate (HITL):** Holds all CRITICAL items for Lead Engineer sign-off before report generation.
8. **ReportingAgent:** Exports Discrepancy Registers (CSV, JSON, Markdown RFIs).

---

## 4. Audited Findings & Ground Truth Register

- **ID:** `FIN-001` | **Severity:** `MAJOR`
  - **Element / Ref:** Substation Control Room & Relay Room Floor (Code FL-04)
  - **Room Finish Schedule (DWG-AR-401):** FL-04: 600x600 Heavy-Duty Anti-Static Raised Access Floor (450mm FFH, 12kN point load) *(DWG-AR-401 Room 102/103)*
  - **Div 09 Finish Specification:** Spec states 8kN point load & 300mm FFH vinyl tile finish *(Spec Sec 09 69 00 (P.164))*
  - **Variance:** `LOAD & HEIGHT MISMATCH` | **Financial Impact:** $22,400.00 | **Schedule Delta:** 7 Days
  - **Recommended Action:** RFI: GIS panels require 12kN load & 600mm underfloor cable plenum; update Spec Sec 09 69 00.
  - **Human Sign-Off Gate:** `HOLD_FOR_LEAD_ENGINEER`

- **ID:** `FIN-002` | **Severity:** `MAJOR`
  - **Element / Ref:** Battery Room Acid-Resistant Floor & Dado (Code FL-07 / WL-05)
  - **Room Finish Schedule (DWG-AR-401):** FL-07: Acid-Proof Vitrified Tile per IS 4457 with Epoxy Furan Mortar *(DWG-AR-401 Room 105)*
  - **Div 09 Finish Specification:** No Specification Section exists for Acid-Proof Tiling in Div 09 *([MISSING SPEC SECTION])*
  - **Variance:** `ORPHAN FINISH CODE` | **Financial Impact:** $11,800.00 | **Schedule Delta:** 4 Days
  - **Recommended Action:** Issue specification section for chemical/acid-resistant tiling in Battery Room.
  - **Human Sign-Off Gate:** `APPROVED`

- **ID:** `FIN-003` | **Severity:** `MINOR`
  - **Element / Ref:** Transformer Bay Blast/Fire Wall Coating (Code PT-09)
  - **Room Finish Schedule (DWG-AR-401):** PT-09: Standard Exterior Acrylic Emulsion *(DWG-AR-401 Ext Bay)*
  - **Div 09 Finish Specification:** 2-Hour Hydrocarbon Intumescent / Fire-Retardant Coating *(Spec Sec 09 96 43 (P.178))*
  - **Variance:** `SPEC EXCEEDS DRAWING` | **Financial Impact:** $8,900.00 | **Schedule Delta:** 3 Days
  - **Recommended Action:** Align Room Finish Schedule code PT-09 with fire-retardant spec requirement.
  - **Human Sign-Off Gate:** `APPROVED`



---

## 5. Lead Engineer Sign-Off Criteria
- `APPROVE`: Discrepancy confirmed and actionable RFI / transmittal authorized for issuance.
- `HOLD_FOR_LEAD_ENGINEER`: Critical items with financial exposure >= $40,000 or contractual risk.
- `REJECT`: Finding deemed within permissible engineering tolerance or superseded by addendum.
