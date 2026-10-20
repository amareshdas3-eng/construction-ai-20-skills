# 🏗️ 20 Construction AI Skills — Local Multi-Agent Suite

[![Live Demo](https://img.shields.io/badge/Live%20Demo-GitHub%20Pages-brightgreen?style=for-the-badge&logo=github)](https://amareshdas3-eng.github.io/construction-ai-20-skills/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)](LICENSE)
[![Zero Cloud](https://img.shields.io/badge/Zero%20Cloud-100%25%20Local-orange?style=for-the-badge)](https://github.com/amareshdas3-eng/construction-ai-20-skills)

> **Zero-Budget, Local-First Multi-Agent Construction AI Suite.**  
> 20 reusable engineering skills, deterministic cross-referencing engines, 100% citation verification, and Lead Engineer Human-In-The-Loop (HITL) approval gates. Zero paid APIs, zero external network calls.

---

## 🚀 Live Interactive Web Dashboard

Experience the complete 20-skill workbench directly in your browser:  
👉 **[Open Live Demo on GitHub Pages](https://amareshdas3-eng.github.io/construction-ai-20-skills/)**

---

## 🏛️ Master Registry of All 20 Construction AI Skills

| # | Skill ID | Skill Name | Category / Pillar | Primary Deliverable |
|:---:|---|---|---|---|
| **00** | `project-indexer` | Project Indexer | **Setup** | Master Document Index & Project DNA JSON |
| **01** | `spec-reviewer` | Spec Reviewer | **Before You Bid** | Bid-Killer & Hidden Cost Risk Register |
| **02** | `spec-index` | Spec Index | **Before You Bid** | Searchable CSI/IEC Section & Submittal Matrix |
| **03** | `spec-vs-drawings` | Spec vs Drawings Check | **Before You Bid** | Severity-Graded Conflict Register + Draft RFIs |
| **04** | `finishes-vs-spec` | Finishes vs Spec Check | **Before You Bid** | Orphan Code & Material Mismatch Matrix |
| **05** | `bid-hunter` | Bid Hunter | **Before You Bid** | Go/No-Go Scorecard (/100) + Bid Risk Matrix |
| **06** | `drawing-index` | Drawing Index | **Drawings** | Searchable Drawing Register + Missing Sheet Log |
| **07** | `electrical-takeoff` | Electrical Takeoff | **Drawings** | Two-Way Verified Takeoff + Sheet/Grid Proof |
| **08** | `cad-to-excel` | CAD to Excel | **Drawings** | Categorized Trade BOQ Excel Workbook |
| **09** | `drainage-schedule` | Drainage Schedule | **Drawings** | Audited Manhole/Pipe Schedule (Slope & Cover Checks) |
| **10** | `pdf-markup` | PDF Markup | **Drawings** | Coordinate Stamp Log + Batch Redline Audit |
| **11** | `bim-scorecard` | BIM Scorecard | **The Model** | 100-Point BIM Health Grade + Purge/Fix Commands |
| **12** | `spec-compliance` | Spec Compliance | **The Model** | Line-by-Line PASS / FAIL / MISSING Submittal Matrix |
| **13** | `ifc-to-boq` | IFC to Priced BOQ | **The Model** | Priced Bill of Quantities with Waste & OH&P |
| **14** | `p6-to-4d-revit` | P6 → 4D Revit | **The Model** | 4D TimeLiner/Synchro Activity-to-Element Map |
| **15** | `cut-sheet-to-revit` | Cut Sheet → Revit Family | **The Model** | Revit Family Type Catalog & Shared Parameters |
| **16** | `p6-cost-loader` | P6 Cost Loader | **Schedule + Cost** | Zero-Variance P6 Resource/Expense Import File |
| **17** | `schedule-narrative` | Monthly Schedule Narrative | **Schedule + Cost** | Critical Path Delta, DCMA 14-Pt Audit & Narrative |
| **18** | `change-order-audit` | Change Order Audit | **Schedule + Cost** | Forensic Entitlement, Quantity & Star-Rate Audit |
| **19** | `construction-cfo-pack`| Construction CFO Pack | **Schedule + Cost** | Reconciled EVM ($CPI/SPI/EAC$) & CVR Pack |

---

## ⚡ 7-Agent Architecture

```plaintext
[Raw Spec + Drawing Inputs]
         │
         ▼
┌──────────────────────────────┐
│ 1. CoordinatorAgent          │ ── Routes workflow, initializes audit trail & state
└──────────────┬───────────────┘
               ▼
┌──────────────────────────────┐
│ 2. DocumentExtractionAgent   │ ── Normalizes clauses, schedules, SLD tags & metadata
└──────┬───────────────┬───────┘
       ▼               ▼
┌─────────────┐ ┌──────────────┐
│ 3. Spec     │ │ 4. Drawing   │ ── Extracts structured parameters, units & tolerances
│ Analysis    │ │ Analysis     │
└──────┬──────┘ └──────┬───────┘
       └───────┬───────┘
               ▼
┌──────────────────────────────┐
│ 5. DiscrepancyResolutionAgent│ ── Deterministic rule engine: flags conflicts, calculates
└──────────────┬───────────────┘    cost/schedule exposure, assigns CRITICAL/MAJOR/MINOR
               ▼
┌──────────────────────────────┐
│ 6. QualityAssuranceAgent     │ ── Verifies 100% citation trace, zero hallucinated refs
└──────────────┬───────────────┘
               ▼
╔══════════════════════════════╗
║   HUMAN APPROVAL GATE (HITL) ║ ── Lead Engineer reviews findings: APPROVE / REJECT / HOLD
╚══════════════╤═══════════════╝    ("None of them signs it off. You make the call.")
               ▼
┌──────────────────────────────┐
│ 7. ReportingAgent            │ ── Exports Discrepancy Register (CSV, JSON, Markdown RFI)
└──────────────────────────────┘
```

---

## 🛠️ Quick-Start Installation & Local Execution

Everything runs with standard Python 3.10+ without installing pip dependencies:

```bash
# Clone the repository
git clone https://github.com/amareshdas3-eng/construction-ai-20-skills.git
cd construction-ai-20-skills

# 1. Run the Spec vs. Drawings Check (Autonomous mode)
python orchestrator.py --non-interactive

# 2. Run with interactive terminal Lead Engineer sign-off gates
python orchestrator.py

# 3. Run all 20 skills across all 5 pillars
python orchestrator.py --all

# 4. Run the automated verification test suite (8/8 PASS)
python test_suite.py

# 5. Open the Local UI Dashboard in any browser
# Double-click index.html or run:
python -m http.server 8080
```

---

## 📁 Repository Structure

```plaintext
construction-ai-20-skills/
├── index.html                        # Self-contained Web UI Workbench (GitHub Pages)
├── orchestrator.py                   # 7-Agent Pipeline Orchestrator + HITL Gates
├── orchestrator_all_20.py            # Master Database & 20-Skill Engine
├── test_suite.py                     # Comprehensive Validation Test Suite
├── test_all_20.py                    # 20-Skill Distribution & QA Test Suite
├── sample_data/
│   ├── spec_33kv_substation.json     # 33kV Substation Spec Clauses
│   ├── drawings_33kv_sld_ga.json     # 33kV Substation Drawing Callouts
│   └── expected_discrepancies.csv    # Discrepancy Ground Truth
├── skills/                           # 20 Modular SKILL.md Engineering Playbooks
│   ├── 00_project-indexer/SKILL.md
│   ├── 01_spec-reviewer/SKILL.md
│   └── ...
└── templates/
    └── skill_template.yaml           # Reusable Schema for All 20 Skills
```

---

## 📄 License
MIT License. Free for commercial and private engineering use.
