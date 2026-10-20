---
name: "Construction CFO Pack"
skill_id: "construction-cfo-pack"
skill_num: "19"
category: "Schedule + Cost"
description: "Reconciled Excel finance pack."
version: "1.0.0"
deterministic: true
qa_verified: true
---

# Skill #19: Construction CFO Pack

**Category:** Schedule + Cost  
**Pipeline Architecture:** 7-Agent Local Multi-Agent Architecture with Lead Engineer Human-In-The-Loop (HITL) Gate  
**Dataset Context:** 33/11 kV Industrial Receiving Substation & MRSS EPC Package  

---

## 1. Objective & Purpose
Reconciled Excel finance pack. This playbook cross-checks **Earned Value & Budget Baseline** against **Actual Cost, Billing WIP & EAC Forecast** to deterministically detect scope gaps, commercial bid-killers, drawing clashes, and cost/schedule variances without hallucinations or external cloud dependencies.

---

## 2. Input Specifications
- **Source A (Earned Value & Budget Baseline):** Contract documents, technical specifications, CSI MasterFormat divisions, or baseline schedules.
- **Source B (Actual Cost, Billing WIP & EAC Forecast):** Drawing callouts, single-line diagrams, submittals, vendor cut sheets, or site progress records.

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

- **ID:** `CFO-001` | **Severity:** `PASS`
  - **Element / Ref:** Earned Value Performance (BAC = $4,500,000 | Period 05)
  - **Earned Value & Budget Baseline:** Earned Value (EV) = $1,890,000 (42.0%) | Actual Cost (AC) = $1,785,000 *(Planned Value (PV) = $1,980,000 (44.0%))*
  - **Actual Cost, Billing WIP & EAC Forecast:** Cost Variance (CV) = +$105,000 (Under Budget) | Schedule Variance (SV) = -$90,000 *(EVM Indices: CPI = 1.059 | SPI = 0.955)*
  - **Variance:** `CPI 1.06 / SPI 0.96` | **Financial Impact:** $105,000.00 | **Schedule Delta:** 5 Days
  - **Recommended Action:** Strong cost control on HV procurement (+5.9% CPI); focus expedition on GIS shipping to lift SPI > 1.0.
  - **Human Sign-Off Gate:** `APPROVED`

- **ID:** `CFO-002` | **Severity:** `MAJOR`
  - **Element / Ref:** WIP / Over-Under Billing & Retention Cash Flow Reconciliation
  - **Earned Value & Budget Baseline:** Earned Revenue (EV): $1,890,000 | Unbilled WIP (Under-Billed): $180,000 | 10% Retention Held: $171,000 *(Gross Certified to Date (IPC #04): $1,710,000)*
  - **Actual Cost, Billing WIP & EAC Forecast:** Working Capital Gap = -$246,000 due to unbilled transformer delivery milestone ($180k) *(Net Cash Collected: $1,539,000 vs AC $1,785,000)*
  - **Variance:** `$180k UNBILLED WIP` | **Financial Impact:** $180,000.00 | **Schedule Delta:** 0 Days
  - **Recommended Action:** Submit IPC #05 immediately with Transformer Materials-on-Site (MOS) indemnity bond to unlock $180k cash.
  - **Human Sign-Off Gate:** `HOLD_FOR_LEAD_ENGINEER`



---

## 5. Lead Engineer Sign-Off Criteria
- `APPROVE`: Discrepancy confirmed and actionable RFI / transmittal authorized for issuance.
- `HOLD_FOR_LEAD_ENGINEER`: Critical items with financial exposure >= $40,000 or contractual risk.
- `REJECT`: Finding deemed within permissible engineering tolerance or superseded by addendum.
