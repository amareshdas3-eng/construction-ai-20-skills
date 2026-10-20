---
name: "PDF Markup"
skill_id: "pdf-markup"
skill_num: "10"
category: "Drawings"
description: "Stamps + bulk drawing edits."
version: "1.0.0"
deterministic: true
qa_verified: true
---

# Skill #10: PDF Markup

**Category:** Drawings  
**Pipeline Architecture:** 7-Agent Local Multi-Agent Architecture with Lead Engineer Human-In-The-Loop (HITL) Gate  
**Dataset Context:** 33/11 kV Industrial Receiving Substation & MRSS EPC Package  

---

## 1. Objective & Purpose
Stamps + bulk drawing edits. This playbook cross-checks **Target Drawing & Coordinate Box** against **PyMuPDF Batch Redline Action** to deterministically detect scope gaps, commercial bid-killers, drawing clashes, and cost/schedule variances without hallucinations or external cloud dependencies.

---

## 2. Input Specifications
- **Source A (Target Drawing & Coordinate Box):** Contract documents, technical specifications, CSI MasterFormat divisions, or baseline schedules.
- **Source B (PyMuPDF Batch Redline Action):** Drawing callouts, single-line diagrams, submittals, vendor cut sheets, or site progress records.

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

- **ID:** `MRK-001` | **Severity:** `PASS`
  - **Element / Ref:** DWG-EL-SLD-001.pdf (Page 1, Rect [410, 220, 580, 290])
  - **Target Drawing & Coordinate Box:** Apply Red Revision Cloud + Callout Box `RFI-001 & RFI-002 HOLD` *(Grid B4 & D2 Conflict Zones)*
  - **PyMuPDF Batch Redline Action:** Stamped 'HOLD - SPEC DISCREPANCY' + Red Cloud around 33kV Busbar & Feeder Notes *(PyMuPDF Batch Script)*
  - **Variance:** `STAMP SCRIPT READY` | **Financial Impact:** $0.00 | **Schedule Delta:** 0 Days
  - **Recommended Action:** Run generated `apply_markups.py` to batch-stamp all 22 PDF sheets.
  - **Human Sign-Off Gate:** `APPROVED`

- **ID:** `MRK-002` | **Severity:** `PASS`
  - **Element / Ref:** All 22 Tender PDFs (Title Block Stamp Area [1020, 740, 1160, 790])
  - **Target Drawing & Coordinate Box:** Apply Blue Watermark Stamp: `TENDER REVIEW SET - CHECKED BY AUTOCONST` *(Batch Tender Control Stamp)*
  - **PyMuPDF Batch Redline Action:** 22/22 Sheets queued with non-destructive PDF annotation layer *(PyMuPDF Batch Script)*
  - **Variance:** `BATCH QUEUED` | **Financial Impact:** $0.00 | **Schedule Delta:** 0 Days
  - **Recommended Action:** Zero manual PDF editing required.
  - **Human Sign-Off Gate:** `APPROVED`



---

## 5. Lead Engineer Sign-Off Criteria
- `APPROVE`: Discrepancy confirmed and actionable RFI / transmittal authorized for issuance.
- `HOLD_FOR_LEAD_ENGINEER`: Critical items with financial exposure >= $40,000 or contractual risk.
- `REJECT`: Finding deemed within permissible engineering tolerance or superseded by addendum.
