---
name: "Spec Compliance"
skill_id: "spec-compliance"
skill_num: "12"
category: "The Model"
description: "PASS / FAIL / MISSING checks."
version: "1.0.0"
deterministic: true
qa_verified: true
---

# Skill #12: Spec Compliance

**Category:** The Model  
**Pipeline Architecture:** 7-Agent Local Multi-Agent Architecture with Lead Engineer Human-In-The-Loop (HITL) Gate  
**Dataset Context:** 33/11 kV Industrial Receiving Substation & MRSS EPC Package  

---

## 1. Objective & Purpose
PASS / FAIL / MISSING checks. This playbook cross-checks **Project Specification Requirement** against **BIM Schedule / Vendor Submittal Value** to deterministically detect scope gaps, commercial bid-killers, drawing clashes, and cost/schedule variances without hallucinations or external cloud dependencies.

---

## 2. Input Specifications
- **Source A (Project Specification Requirement):** Contract documents, technical specifications, CSI MasterFormat divisions, or baseline schedules.
- **Source B (BIM Schedule / Vendor Submittal Value):** Drawing callouts, single-line diagrams, submittals, vendor cut sheets, or site progress records.

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

- **ID:** `CMP-001` | **Severity:** `PASS`
  - **Element / Ref:** 33kV Protection Relay Make & IEC 61850 GOOSE Performance
  - **Project Specification Requirement:** MiCOM P343 / P143 / P643 with dual optical Ethernet & <3ms GOOSE *(Spec Sec 07.2 (Class P1 < 3ms trip))*
  - **BIM Schedule / Vendor Submittal Value:** MiCOM Agile P14x/P64x tested @ 2.1ms GOOSE transfer time *(Submittal SUB-EL-014 Rev 0)*
  - **Variance:** `PASS` | **Financial Impact:** $0.00 | **Schedule Delta:** 0 Days
  - **Recommended Action:** Approve submittal code 1 (No exceptions).
  - **Human Sign-Off Gate:** `APPROVED`

- **ID:** `CMP-002` | **Severity:** `CRITICAL`
  - **Element / Ref:** 15/20 MVA Transformer No-Load & Load Losses @ 75°C
  - **Project Specification Requirement:** Max No-Load Loss <= 11.5 kW | Max Load Loss <= 78.0 kW (Tier-1 Low Loss) *(Spec Sec 06.1.8 (Max Losses))*
  - **BIM Schedule / Vendor Submittal Value:** Offered No-Load Loss = 14.2 kW (+2.7kW) | Load Loss = 89.5 kW (+11.5kW) *(Vendor Datasheet VND-TR-02)*
  - **Variance:** `FAIL (LOSS PENALTY)` | **Financial Impact:** $54,000.00 | **Schedule Delta:** 14 Days
  - **Recommended Action:** REJECT SUBMITTAL: Capitalization penalty in Spec Cl. 06.8 ($4,000/kW) equals $56,800 deduction!
  - **Human Sign-Off Gate:** `HOLD_FOR_LEAD_ENGINEER`

- **ID:** `CMP-003` | **Severity:** `MAJOR`
  - **Element / Ref:** GIS Switchgear Internal Arc Classification (IAC)
  - **Project Specification Requirement:** IAC AFLR 31.5 kA for 1.0s (4-sided operator protection including rear) *(Spec Sec 05.3.1)*
  - **BIM Schedule / Vendor Submittal Value:** Certificate shows IAC AFL 31.5 kA 1.0s (Rear access R-rating omitted!) *(Vendor Submittal VND-GIS-01)*
  - **Variance:** `MISSING REAR ARC CERT` | **Financial Impact:** $18,000.00 | **Schedule Delta:** 10 Days
  - **Recommended Action:** Hold submittal until OEM provides full AFLR (Front, Lateral & Rear) type test certificate.
  - **Human Sign-Off Gate:** `HOLD_FOR_LEAD_ENGINEER`



---

## 5. Lead Engineer Sign-Off Criteria
- `APPROVE`: Discrepancy confirmed and actionable RFI / transmittal authorized for issuance.
- `HOLD_FOR_LEAD_ENGINEER`: Critical items with financial exposure >= $40,000 or contractual risk.
- `REJECT`: Finding deemed within permissible engineering tolerance or superseded by addendum.
