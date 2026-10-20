---
name: "P6 Cost Loader"
skill_id: "p6-cost-loader"
skill_num: "16"
category: "Schedule + Cost"
description: "BOQ costs → P6 activities."
version: "1.0.0"
deterministic: true
qa_verified: true
---

# Skill #16: P6 Cost Loader

**Category:** Schedule + Cost  
**Pipeline Architecture:** 7-Agent Local Multi-Agent Architecture with Lead Engineer Human-In-The-Loop (HITL) Gate  
**Dataset Context:** 33/11 kV Industrial Receiving Substation & MRSS EPC Package  

---

## 1. Objective & Purpose
BOQ costs → P6 activities. This playbook cross-checks **Contract BOQ Package Value** against **P6 Activity Resource Allocation** to deterministically detect scope gaps, commercial bid-killers, drawing clashes, and cost/schedule variances without hallucinations or external cloud dependencies.

---

## 2. Input Specifications
- **Source A (Contract BOQ Package Value):** Contract documents, technical specifications, CSI MasterFormat divisions, or baseline schedules.
- **Source B (P6 Activity Resource Allocation):** Drawing callouts, single-line diagrams, submittals, vendor cut sheets, or site progress records.

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

- **ID:** `PCL-001` | **Severity:** `PASS`
  - **Element / Ref:** WBS 01 — Preliminaries, Engineering, Bonds & Site Establishment
  - **Contract BOQ Package Value:** Allocated across 6 Level-of-Effort (LOE) & Design Submittal Milestones *(BOQ Div 01 Total: $380,000.00)*
  - **P6 Activity Resource Allocation:** Allocated Total: $380,000.00 | Variance: $0.00 (8.44% of Contract) *(P6 `TASKRSRC` Export)*
  - **Variance:** `RECONCILED ($0 DIFF)` | **Financial Impact:** $380,000.00 | **Schedule Delta:** 0 Days
  - **Recommended Action:** Front-end design and mobilization cash-flow curve balanced.
  - **Human Sign-Off Gate:** `APPROVED`

- **ID:** `PCL-002` | **Severity:** `PASS`
  - **Element / Ref:** WBS 02 & 03 — Substation Civil Works, Transformer Bunds & Control Building
  - **Contract BOQ Package Value:** Distributed across 48 Civil/Structural Activities weighted by m3 concrete & m2 finish *(BOQ Div 02-09 Total: $1,120,000.00)*
  - **P6 Activity Resource Allocation:** Allocated Total: $1,120,000.00 | Variance: $0.00 (24.89% of Contract) *(P6 `TASKRSRC` Export)*
  - **Variance:** `RECONCILED ($0 DIFF)` | **Financial Impact:** $1,120,000.00 | **Schedule Delta:** 0 Days
  - **Recommended Action:** Mapped to Cost Account `CA-CIV-100`.
  - **Human Sign-Off Gate:** `APPROVED`

- **ID:** `PCL-003` | **Severity:** `PASS`
  - **Element / Ref:** WBS 04 & 05 — 33/11kV Switchgear, Transformers, Cabling, Relay Testing & SAT
  - **Contract BOQ Package Value:** Split 15% FAT, 65% Site Delivery, 15% Erection, 5% Secondary Injection & Commissioning *(BOQ Div 26 Total: $3,000,000.00)*
  - **P6 Activity Resource Allocation:** Allocated Total: $3,000,000.00 | Contract Sum Reconciled = $4,500,000.00 ($0.00 Error) *(P6 `TASKRSRC` Export)*
  - **Variance:** `100% BALANCED ($4.50M)` | **Financial Impact:** $3,000,000.00 | **Schedule Delta:** 0 Days
  - **Recommended Action:** Ready for Primavera P6 XER/XLSX resource import.
  - **Human Sign-Off Gate:** `APPROVED`



---

## 5. Lead Engineer Sign-Off Criteria
- `APPROVE`: Discrepancy confirmed and actionable RFI / transmittal authorized for issuance.
- `HOLD_FOR_LEAD_ENGINEER`: Critical items with financial exposure >= $40,000 or contractual risk.
- `REJECT`: Finding deemed within permissible engineering tolerance or superseded by addendum.
