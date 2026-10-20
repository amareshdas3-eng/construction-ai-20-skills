---
name: "Drainage Schedule"
skill_id: "drainage-schedule"
skill_num: "09"
category: "Drawings"
description: "Drainage PDF → checked Excel."
version: "1.0.0"
deterministic: true
qa_verified: true
---

# Skill #09: Drainage Schedule

**Category:** Drawings  
**Pipeline Architecture:** 7-Agent Local Multi-Agent Architecture with Lead Engineer Human-In-The-Loop (HITL) Gate  
**Dataset Context:** 33/11 kV Industrial Receiving Substation & MRSS EPC Package  

---

## 1. Objective & Purpose
Drainage PDF → checked Excel. This playbook cross-checks **Stated Manhole & Pipe Schedule** against **Mathematical Hydraulic & Cover Audit** to deterministically detect scope gaps, commercial bid-killers, drawing clashes, and cost/schedule variances without hallucinations or external cloud dependencies.

---

## 2. Input Specifications
- **Source A (Stated Manhole & Pipe Schedule):** Contract documents, technical specifications, CSI MasterFormat divisions, or baseline schedules.
- **Source B (Mathematical Hydraulic & Cover Audit):** Drawing callouts, single-line diagrams, submittals, vendor cut sheets, or site progress records.

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

- **ID:** `DRN-001` | **Severity:** `CRITICAL`
  - **Element / Ref:** Stormwater Run SW-04 (Manhole MH-04 to MH-05, L = 45.0m, 300mm uPVC)
  - **Stated Manhole & Pipe Schedule:** Up IL = +98.420m | Down IL = +98.510m | Stated Slope = 1 in 500 *(DWG-CV-DRN-002 Schedule)*
  - **Mathematical Hydraulic & Cover Audit:** Calculated Fall = -0.090m (BACKFALL UPWARDS BY 90mm!) *(Automated Slope Check: (IL_up - IL_dn)/L)*
  - **Variance:** `BACKFALL ERROR` | **Financial Impact:** $14,500.00 | **Schedule Delta:** 5 Days
  - **Recommended Action:** CRITICAL CIVIL ERROR: Down IL at MH-05 must be +98.330m (not +98.510m) to achieve 1:500 gravity fall.
  - **Human Sign-Off Gate:** `HOLD_FOR_LEAD_ENGINEER`

- **ID:** `DRN-002` | **Severity:** `MAJOR`
  - **Element / Ref:** Transformer Oil Pit Containment Drain Run OD-02 (MH-O1 to Oil Interceptor)
  - **Stated Manhole & Pipe Schedule:** GL = +100.000m | Crown = +99.550m | Heavy Crane Access Road Crossing *(DWG-CV-DRN-002 Profile)*
  - **Mathematical Hydraulic & Cover Audit:** Cover Depth = 0.450m (< 0.900m minimum required under heavy road) *(Structural Cover Check (GL - Crown))*
  - **Variance:** `SHALLOW COVER (0.45m)` | **Financial Impact:** $6,800.00 | **Schedule Delta:** 2 Days
  - **Recommended Action:** Requires Class A150 RC concrete surround encasement over 18m road crossing.
  - **Human Sign-Off Gate:** `APPROVED`



---

## 5. Lead Engineer Sign-Off Criteria
- `APPROVE`: Discrepancy confirmed and actionable RFI / transmittal authorized for issuance.
- `HOLD_FOR_LEAD_ENGINEER`: Critical items with financial exposure >= $40,000 or contractual risk.
- `REJECT`: Finding deemed within permissible engineering tolerance or superseded by addendum.
