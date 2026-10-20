---
name: "Cut Sheet → Revit Family"
skill_id: "cut-sheet-to-revit"
skill_num: "15"
category: "The Model"
description: "Manufacturer PDF → Revit family."
version: "1.0.0"
deterministic: true
qa_verified: true
---

# Skill #15: Cut Sheet → Revit Family

**Category:** The Model  
**Pipeline Architecture:** 7-Agent Local Multi-Agent Architecture with Lead Engineer Human-In-The-Loop (HITL) Gate  
**Dataset Context:** 33/11 kV Industrial Receiving Substation & MRSS EPC Package  

---

## 1. Objective & Purpose
Manufacturer PDF → Revit family. This playbook cross-checks **OEM Cut Sheet Extracted Spec** against **Revit Shared Parameter / Type Catalog** to deterministically detect scope gaps, commercial bid-killers, drawing clashes, and cost/schedule variances without hallucinations or external cloud dependencies.

---

## 2. Input Specifications
- **Source A (OEM Cut Sheet Extracted Spec):** Contract documents, technical specifications, CSI MasterFormat divisions, or baseline schedules.
- **Source B (Revit Shared Parameter / Type Catalog):** Drawing callouts, single-line diagrams, submittals, vendor cut sheets, or site progress records.

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

- **ID:** `CUT-001` | **Severity:** `PASS`
  - **Element / Ref:** ABB ZX2 Air-Insulated / SF6 33kV GIS Single Busbar Bay (1250A, 31.5kA)
  - **OEM Cut Sheet Extracted Spec:** Width: 800mm | Depth: 1450mm | Height: 2300mm | Weight: 1,150 kg | Rear Clearance: 800mm *(OEM PDF `ABB_ZX2_Catalog_p18.pdf`)*
  - **Revit Shared Parameter / Type Catalog:** `##Width##LENGTH##MILLIMETERS` = 800, `Apparent_Load` = 71.4 MVA, `Short_Circuit_Rating` = 31.5 kA *(Revit Type Catalog `ABB_ZX2_33kV.txt`)*
  - **Variance:** `TYPE CATALOG READY` | **Financial Impact:** $0.00 | **Schedule Delta:** 0 Days
  - **Recommended Action:** Import `.txt` alongside `.rfa` to generate all 6 feeder/incomer family types automatically.
  - **Human Sign-Off Gate:** `APPROVED`

- **ID:** `CUT-002` | **Severity:** `PASS`
  - **Element / Ref:** 15/20 MVA 33/11kV ONAN/ONAF Power Transformer with OLTC
  - **OEM Cut Sheet Extracted Spec:** L: 5200mm | W: 3650mm | H: 4150mm | Total Mass: 41,500 kg | Oil Mass: 11,200 kg *(OEM GA Cut Sheet `TR_15MVA_GA.pdf`)*
  - **Revit Shared Parameter / Type Catalog:** Populated COBie parameters (`AssetIdentifier`, `SerialNumber`, `WarrantyDuration=24m`, `HeatRejection=92kW`) *(Revit Type Catalog `PWR_TR_15_20MVA.txt`)*
  - **Variance:** `COBIE & MEP READY` | **Financial Impact:** $0.00 | **Schedule Delta:** 0 Days
  - **Recommended Action:** Includes parametric 3D clearance maintenance box for radiator removal.
  - **Human Sign-Off Gate:** `APPROVED`



---

## 5. Lead Engineer Sign-Off Criteria
- `APPROVE`: Discrepancy confirmed and actionable RFI / transmittal authorized for issuance.
- `HOLD_FOR_LEAD_ENGINEER`: Critical items with financial exposure >= $40,000 or contractual risk.
- `REJECT`: Finding deemed within permissible engineering tolerance or superseded by addendum.
