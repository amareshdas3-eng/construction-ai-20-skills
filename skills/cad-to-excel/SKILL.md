---
name: "CAD to Excel"
skill_id: "cad-to-excel"
skill_num: "08"
category: "Drawings"
description: "CAD objects → Excel takeoff."
version: "1.0.0"
deterministic: true
qa_verified: true
---

# Skill #08: CAD to Excel

**Category:** Drawings  
**Pipeline Architecture:** 7-Agent Local Multi-Agent Architecture with Lead Engineer Human-In-The-Loop (HITL) Gate  
**Dataset Context:** 33/11 kV Industrial Receiving Substation & MRSS EPC Package  

---

## 1. Objective & Purpose
CAD objects → Excel takeoff. This playbook cross-checks **DXF Layer & Block Entities** against **Normalized Excel BOQ Output** to deterministically detect scope gaps, commercial bid-killers, drawing clashes, and cost/schedule variances without hallucinations or external cloud dependencies.

---

## 2. Input Specifications
- **Source A (DXF Layer & Block Entities):** Contract documents, technical specifications, CSI MasterFormat divisions, or baseline schedules.
- **Source B (Normalized Excel BOQ Output):** Drawing callouts, single-line diagrams, submittals, vendor cut sheets, or site progress records.

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

- **ID:** `CAD-001` | **Severity:** `PASS`
  - **Element / Ref:** Block `BLK_HV_CB_33KV` & `BLK_CT_33KV` on Layer `E-POWR-EQPM`
  - **DXF Layer & Block Entities:** 9x 33kV Vacuum/SF6 Breakers, 27x Protection Core CTs, 9x Line VTs *(Substation_GA.dxf (412 Block Inserts))*
  - **Normalized Excel BOQ Output:** Stripped AutoCAD `\A1;` formatting codes and grouped by bay tag *(Excel Sheet `01_HV_Equipment`)*
  - **Variance:** `100% EXTRACTED` | **Financial Impact:** $0.00 | **Schedule Delta:** 0 Days
  - **Recommended Action:** Ready for unit rate pricing.
  - **Human Sign-Off Gate:** `APPROVED`

- **ID:** `CAD-002` | **Severity:** `MAJOR`
  - **Element / Ref:** Polyline Containment Runs on Layer `E-TRAY-600W` & `E-TRAY-300W`
  - **DXF Layer & Block Entities:** Raw 2D CAD Length = 640.5m (Contains 14 overlapping duplicate line segments totaling 68.0m) *(Cable_Routing.dxf (84 LWPOLYLINEs))*
  - **Normalized Excel BOQ Output:** De-duplicated Net Length = 572.5m + 18 vertical riser blocks (54.0m) = 626.5m *(Excel Sheet `02_Containment`)*
  - **Variance:** `DEDUPED 68m OVERLAP` | **Financial Impact:** $6,120.00 | **Schedule Delta:** 0 Days
  - **Recommended Action:** Prevented 68m double-counting from overlapping CAD polylines while adding missing 3D risers.
  - **Human Sign-Off Gate:** `APPROVED`



---

## 5. Lead Engineer Sign-Off Criteria
- `APPROVE`: Discrepancy confirmed and actionable RFI / transmittal authorized for issuance.
- `HOLD_FOR_LEAD_ENGINEER`: Critical items with financial exposure >= $40,000 or contractual risk.
- `REJECT`: Finding deemed within permissible engineering tolerance or superseded by addendum.
