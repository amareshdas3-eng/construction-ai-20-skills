---
name: "BIM Scorecard"
skill_id: "bim-scorecard"
skill_num: "11"
category: "The Model"
description: "Revit health grade + audit."
version: "1.0.0"
deterministic: true
qa_verified: true
---

# Skill #11: BIM Scorecard

**Category:** The Model  
**Pipeline Architecture:** 7-Agent Local Multi-Agent Architecture with Lead Engineer Human-In-The-Loop (HITL) Gate  
**Dataset Context:** 33/11 kV Industrial Receiving Substation & MRSS EPC Package  

---

## 1. Objective & Purpose
Revit health grade + audit. This playbook cross-checks **Revit Model Audit Metric** against **BEP Standard Threshold & Score** to deterministically detect scope gaps, commercial bid-killers, drawing clashes, and cost/schedule variances without hallucinations or external cloud dependencies.

---

## 2. Input Specifications
- **Source A (Revit Model Audit Metric):** Contract documents, technical specifications, CSI MasterFormat divisions, or baseline schedules.
- **Source B (BEP Standard Threshold & Score):** Drawing callouts, single-line diagrams, submittals, vendor cut sheets, or site progress records.

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

- **ID:** `BIM-001` | **Severity:** `MAJOR`
  - **Element / Ref:** Model Warnings & Duplicate Instances (`SUB_EL_CENTRAL_R24.rvt`)
  - **Revit Model Audit Metric:** 16.2 Warnings per 1,000 elements (Includes 38 identical overlapping cable tray fittings) *(684 Warnings across 42,100 Elements)*
  - **BEP Standard Threshold & Score:** Category Score: 14 / 25 pts (Overall Model Health Grade: 78/100 = B-) *(Target: <2.0 Warnings / 1,000 Elements)*
  - **Variance:** `38 DUPLICATE ELEMENTS` | **Financial Impact:** $0.00 | **Schedule Delta:** 2 Days
  - **Recommended Action:** Run PyRevit 'Select Identical Instances in Same Place' and purge 38 duplicate fittings.
  - **Human Sign-Off Gate:** `APPROVED`

- **ID:** `BIM-002` | **Severity:** `CRITICAL`
  - **Element / Ref:** Imported / Exploded CAD DWGs Inside Revit Families
  - **Revit Model Audit Metric:** 2 Exploded CAD topography/detail blocks polluting Line Styles & Materials *(7 Imported DWGs Found (File Size: 418 MB))*
  - **BEP Standard Threshold & Score:** Category Score: 9 / 20 pts — Causes severe slow sync times *(BEP Rule: 0 Imported DWGs (Link Only))*
  - **Variance:** `7 IMPORTED DWGs` | **Financial Impact:** $0.00 | **Schedule Delta:** 3 Days
  - **Recommended Action:** Remove imported DWGs and replace with `Link CAD (Current View Only)` to cut model size by ~110 MB.
  - **Human Sign-Off Gate:** `HOLD_FOR_LEAD_ENGINEER`



---

## 5. Lead Engineer Sign-Off Criteria
- `APPROVE`: Discrepancy confirmed and actionable RFI / transmittal authorized for issuance.
- `HOLD_FOR_LEAD_ENGINEER`: Critical items with financial exposure >= $40,000 or contractual risk.
- `REJECT`: Finding deemed within permissible engineering tolerance or superseded by addendum.
