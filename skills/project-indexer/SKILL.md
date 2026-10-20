---
name: "Project Indexer"
skill_id: "project-indexer"
skill_num: "00"
category: "Setup"
description: "Project context + master document index."
version: "1.0.0"
deterministic: true
qa_verified: true
---

# Skill #00: Project Indexer

**Category:** Setup  
**Pipeline Architecture:** 7-Agent Local Multi-Agent Architecture with Lead Engineer Human-In-The-Loop (HITL) Gate  
**Dataset Context:** 33/11 kV Industrial Receiving Substation & MRSS EPC Package  

---

## 1. Objective & Purpose
Project context + master document index. This playbook cross-checks **Package Register** against **Folder Audit & Cross-Ref** to deterministically detect scope gaps, commercial bid-killers, drawing clashes, and cost/schedule variances without hallucinations or external cloud dependencies.

---

## 2. Input Specifications
- **Source A (Package Register):** Contract documents, technical specifications, CSI MasterFormat divisions, or baseline schedules.
- **Source B (Folder Audit & Cross-Ref):** Drawing callouts, single-line diagrams, submittals, vendor cut sheets, or site progress records.

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

- **ID:** `IDX-001` | **Severity:** `PASS`
  - **Element / Ref:** Vol-I Commercial & FIDIC Particular Conditions
  - **Package Register:** Signed PDF (142 Pages) *(DOC-COM-001 Rev 0)*
  - **Folder Audit & Cross-Ref:** Indexed & Complete *(Folder /01_Commercial)*
  - **Variance:** `MATCH (100%)` | **Financial Impact:** $0.00 | **Schedule Delta:** 0 Days
  - **Recommended Action:** Baseline commercial terms locked for Spec Reviewer.
  - **Human Sign-Off Gate:** `APPROVED`

- **ID:** `IDX-002` | **Severity:** `PASS`
  - **Element / Ref:** Vol-II Technical Specification (33/11kV Substation)
  - **Package Register:** Searchable PDF (218 Pages) *(SPEC-EL-33KV-001 Rev 0)*
  - **Folder Audit & Cross-Ref:** Indexed & Complete *(Folder /02_Specs)*
  - **Variance:** `MATCH (100%)` | **Financial Impact:** $0.00 | **Schedule Delta:** 0 Days
  - **Recommended Action:** Routed to Spec Index & Spec vs Drawings Check.
  - **Human Sign-Off Gate:** `APPROVED`

- **ID:** `IDX-003` | **Severity:** `MAJOR`
  - **Element / Ref:** Vol-III Tender Drawing Package (SLD, GA & Civil)
  - **Package Register:** 24 Drawings Listed on Cover *(DWG-TRANSMITTAL-01)*
  - **Folder Audit & Cross-Ref:** 22 Drawings Present (Missing E-104 & C-202) *(Folder /03_Drawings)*
  - **Variance:** `2 MISSING SHEETS` | **Financial Impact:** $15,000.00 | **Schedule Delta:** 5 Days
  - **Recommended Action:** Issue immediate pre-bid transmittal discrepancy notice for missing Earthing & Drainage sheets.
  - **Human Sign-Off Gate:** `HOLD_FOR_LEAD_ENGINEER`

- **ID:** `IDX-004` | **Severity:** `PASS`
  - **Element / Ref:** Vol-IV Unpriced & Priced Bill of Quantities + P6 Baseline
  - **Package Register:** Excel + Primavera XER (412 Activities) *(BOQ-REV-0.xlsx + SUB-BL.xer)*
  - **Folder Audit & Cross-Ref:** Indexed & Reconciled *(Folder /04_Controls)*
  - **Variance:** `MATCH (100%)` | **Financial Impact:** $0.00 | **Schedule Delta:** 0 Days
  - **Recommended Action:** Routed to P6 Cost Loader & Schedule Narrative agents.
  - **Human Sign-Off Gate:** `APPROVED`



---

## 5. Lead Engineer Sign-Off Criteria
- `APPROVE`: Discrepancy confirmed and actionable RFI / transmittal authorized for issuance.
- `HOLD_FOR_LEAD_ENGINEER`: Critical items with financial exposure >= $40,000 or contractual risk.
- `REJECT`: Finding deemed within permissible engineering tolerance or superseded by addendum.
