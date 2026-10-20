---
name: "P6 → 4D Revit"
skill_id: "p6-to-4d-revit"
skill_num: "14"
category: "The Model"
description: "Schedule → linked 3D elements."
version: "1.0.0"
deterministic: true
qa_verified: true
---

# Skill #14: P6 → 4D Revit

**Category:** The Model  
**Pipeline Architecture:** 7-Agent Local Multi-Agent Architecture with Lead Engineer Human-In-The-Loop (HITL) Gate  
**Dataset Context:** 33/11 kV Industrial Receiving Substation & MRSS EPC Package  

---

## 1. Objective & Purpose
Schedule → linked 3D elements. This playbook cross-checks **Primavera P6 Activity ID & Dates** against **Revit 3D Category & Filter Rule** to deterministically detect scope gaps, commercial bid-killers, drawing clashes, and cost/schedule variances without hallucinations or external cloud dependencies.

---

## 2. Input Specifications
- **Source A (Primavera P6 Activity ID & Dates):** Contract documents, technical specifications, CSI MasterFormat divisions, or baseline schedules.
- **Source B (Revit 3D Category & Filter Rule):** Drawing callouts, single-line diagrams, submittals, vendor cut sheets, or site progress records.

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

- **ID:** `4D-001` | **Severity:** `PASS`
  - **Element / Ref:** Act `SUB-CIV-1040`: GIS Basement Wall & Cable Trench Concreting
  - **Primavera P6 Activity ID & Dates:** Task Type: Construct | WBS: 02.Civil.Substructure *(Start: 2026-11-10 | Finish: 2026-12-08)*
  - **Revit 3D Category & Filter Rule:** 124 Revit Elements auto-linked (`4D_Activity_ID = SUB-CIV-1040`) *(Revit Filter: `Category=Walls/Floors AND Level=B1_Basement`)*
  - **Variance:** `124 ELEMENTS LINKED` | **Financial Impact:** $0.00 | **Schedule Delta:** 0 Days
  - **Recommended Action:** Exported to Navisworks TimeLiner CSV.
  - **Human Sign-Off Gate:** `APPROVED`

- **ID:** `4D-002` | **Severity:** `PASS`
  - **Element / Ref:** Act `SUB-EL-2110`: 33kV GIS Erection, Busbar Torqueing & SF6 Gas Filling
  - **Primavera P6 Activity ID & Dates:** Task Type: Construct | WBS: 04.Electrical.HV_Equipment *(Start: 2027-02-15 | Finish: 2027-03-12)*
  - **Revit 3D Category & Filter Rule:** 9 GIS Bay Assemblies + Busbar Trunking linked (`4D_Activity_ID = SUB-EL-2110`) *(Revit Filter: `Category=Electrical Equipment AND Zone=GIS_Hall`)*
  - **Variance:** `9 ASSEMBLIES LINKED` | **Financial Impact:** $0.00 | **Schedule Delta:** 0 Days
  - **Recommended Action:** Verified spatial clash clearance during crane erection sequence.
  - **Human Sign-Off Gate:** `APPROVED`

- **ID:** `4D-003` | **Severity:** `MAJOR`
  - **Element / Ref:** Orphan 3D Elements with No Matching P6 Schedule Activity
  - **Primavera P6 Activity ID & Dates:** 18 Outdoor HV Lightning Masts & 4 Security Camera Poles have no P6 Activity ID *(Revit Model Audit)*
  - **Revit 3D Category & Filter Rule:** External Lighting/Lightning Mast erection activity omitted from P6 WBS *(P6 Schedule `SUB-BL.xer`)*
  - **Variance:** `22 ORPHAN 3D OBJECTS` | **Financial Impact:** $0.00 | **Schedule Delta:** 6 Days
  - **Recommended Action:** Add Activity `SUB-EL-2450: Outdoor Lightning Mast & Perimeter Pole Erection` to P6 schedule.
  - **Human Sign-Off Gate:** `HOLD_FOR_LEAD_ENGINEER`



---

## 5. Lead Engineer Sign-Off Criteria
- `APPROVE`: Discrepancy confirmed and actionable RFI / transmittal authorized for issuance.
- `HOLD_FOR_LEAD_ENGINEER`: Critical items with financial exposure >= $40,000 or contractual risk.
- `REJECT`: Finding deemed within permissible engineering tolerance or superseded by addendum.
