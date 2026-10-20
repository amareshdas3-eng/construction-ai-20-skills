---
name: "Monthly Schedule Narrative"
skill_id: "schedule-narrative"
skill_num: "17"
category: "Schedule + Cost"
description: "Two XERs → checked narrative."
version: "1.0.0"
deterministic: true
qa_verified: true
---

# Skill #17: Monthly Schedule Narrative

**Category:** Schedule + Cost  
**Pipeline Architecture:** 7-Agent Local Multi-Agent Architecture with Lead Engineer Human-In-The-Loop (HITL) Gate  
**Dataset Context:** 33/11 kV Industrial Receiving Substation & MRSS EPC Package  

---

## 1. Objective & Purpose
Two XERs → checked narrative. This playbook cross-checks **Previous Update (`M04_Aug2026.xer`)** against **Current Update (`M05_Sep2026.xer`)** to deterministically detect scope gaps, commercial bid-killers, drawing clashes, and cost/schedule variances without hallucinations or external cloud dependencies.

---

## 2. Input Specifications
- **Source A (Previous Update (`M04_Aug2026.xer`)):** Contract documents, technical specifications, CSI MasterFormat divisions, or baseline schedules.
- **Source B (Current Update (`M05_Sep2026.xer`)):** Drawing callouts, single-line diagrams, submittals, vendor cut sheets, or site progress records.

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

- **ID:** `NAR-001` | **Severity:** `CRITICAL`
  - **Element / Ref:** Terminal Milestone `MS-100: Substation Energization & Handover`
  - **Previous Update (`M04_Aug2026.xer`):** Current Forecast: 2027-05-29 (Total Float: -10 Working Days / -14 Calendar Days) *(Prev Forecast: 2027-05-15 (Total Float: +4d))*
  - **Current Update (`M05_Sep2026.xer`):** Critical path shifted from Civil Building Roof to `33kV GIS Custom Clearance & Port Delay` *(Critical Path Shift Analysis)*
  - **Variance:** `-14 DAYS FLOAT EROSION` | **Financial Impact:** $45,000.00 | **Schedule Delta:** 14 Days
  - **Recommended Action:** Initiate 2-shift GIS erection crew and air-freight secondary relay marshalling panels to recover 10 days.
  - **Human Sign-Off Gate:** `HOLD_FOR_LEAD_ENGINEER`

- **ID:** `NAR-002` | **Severity:** `MAJOR`
  - **Element / Ref:** DCMA 14-Point Schedule Integrity & Unauthorized Logic Changes
  - **Previous Update (`M04_Aug2026.xer`):** FS (Finish-to-Start) 0d lag between `Cable Trench Civil` and `33kV Cable Pulling` *(Baseline Logic (`TASKPRED` Table))*
  - **Current Update (`M05_Sep2026.xer`):** Planner changed relationship to SS+5d with -8d negative lead and added 3 Hard `Mandatory Finish` constraints *(Current XER (`M05_Sep2026.xer`))*
  - **Variance:** `3 HARD CONSTRAINTS + NEG LAG` | **Financial Impact:** $0.00 | **Schedule Delta:** 8 Days
  - **Recommended Action:** Reject unauthorized negative lag and replace hard constraints with realistic overlap logic per DCMA guidelines.
  - **Human Sign-Off Gate:** `HOLD_FOR_LEAD_ENGINEER`



---

## 5. Lead Engineer Sign-Off Criteria
- `APPROVE`: Discrepancy confirmed and actionable RFI / transmittal authorized for issuance.
- `HOLD_FOR_LEAD_ENGINEER`: Critical items with financial exposure >= $40,000 or contractual risk.
- `REJECT`: Finding deemed within permissible engineering tolerance or superseded by addendum.
