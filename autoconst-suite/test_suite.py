#!/usr/bin/env python3
"""
Automated Validation & Verification Test Suite
Validates the 7-Agent Orchestrator, Spec vs Drawings Reconciliation, HITL Gates, and All 20 Skills
Zero-Budget | 100% Python Standard Library | Zero Network Dependencies
"""

import csv
import json
import os
import sys
import unittest

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

from orchestrator import (
    MultiAgentOrchestrator,
    CoordinatorAgent,
    DocumentExtractionAgent,
    SpecAnalysisAgent,
    DrawingAnalysisAgent,
    DiscrepancyResolutionAgent,
    QualityAssuranceAgent,
    HumanApprovalGate,
    ReportingAgent,
    SKILLS_REGISTRY
)

class TestAutoConstLocalSuite(unittest.TestCase):

    def setUp(self):
        self.orchestrator = MultiAgentOrchestrator(non_interactive=True)
        self.test_dir = os.path.dirname(os.path.abspath(__file__))

    # ==========================================================================
    # 1. SPEC VS DRAWINGS 7-AGENT WORKFLOW VALIDATION
    # ==========================================================================

    def test_01_spec_vs_drawings_pipeline_execution(self):
        """Verify the 7-agent pipeline executes cleanly and generates the expected discrepancies."""
        spec_path = os.path.join(self.test_dir, "sample_data", "spec_33kv_substation.json")
        dwg_path = os.path.join(self.test_dir, "sample_data", "drawings_33kv_sld_ga.json")
        out_csv = os.path.join(self.test_dir, "test_run_discrepancies.csv")
        out_json = os.path.join(self.test_dir, "test_run_report.json")
        out_md = os.path.join(self.test_dir, "test_run_rfis.md")

        result = self.orchestrator.run_spec_vs_drawings(
            spec_path=spec_path,
            drawings_path=dwg_path,
            out_csv=out_csv,
            out_json=out_json,
            out_md=out_md
        )

        # Assert finding counts
        self.assertEqual(result["total_findings"], 6)
        self.assertEqual(result["critical_count"], 2)
        self.assertEqual(result["major_count"], 4)
        self.assertEqual(result["total_cost_usd"], 208000.0)
        self.assertEqual(result["max_schedule_days"], 28)
        self.assertEqual(result["qa_score"], 100.0)

        # Cleanup generated test files
        for p in [out_csv, out_json, out_md]:
            if os.path.exists(p):
                os.remove(p)

    def test_02_reconciliation_against_expected_register(self):
        """Verify generated findings match expected_discrepancies.csv ground truth line-by-line."""
        expected_csv = os.path.join(self.test_dir, "sample_data", "expected_discrepancies.csv")
        self.assertTrue(os.path.exists(expected_csv), "expected_discrepancies.csv missing")

        with open(expected_csv, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            expected_rows = {row["Finding_ID"]: row for row in reader}

        result = self.orchestrator.run_spec_vs_drawings()
        generated_map = {f.finding_id: f for f in result["findings"]}

        self.assertEqual(set(expected_rows.keys()), set(generated_map.keys()))

        for fid, exp in expected_rows.items():
            gen = generated_map[fid]
            self.assertEqual(gen.severity, exp["Severity"], f"Severity mismatch on {fid}")
            self.assertEqual(gen.cost_impact_usd, float(exp["Cost_Impact_USD"]), f"Cost mismatch on {fid}")
            self.assertEqual(gen.schedule_impact_days, int(exp["Schedule_Impact_Days"]), f"Schedule mismatch on {fid}")
            self.assertEqual(gen.qa_verified, exp["QA_Verified"].lower() == "true", f"QA mismatch on {fid}")

    def test_03_hitl_approval_gate_holds_critical_conflicts(self):
        """Verify Human Approval Gate automatically holds CRITICAL items (DSC-001 & DSC-002) in non-interactive mode."""
        result = self.orchestrator.run_spec_vs_drawings()
        for f in result["findings"]:
            if f.severity == "CRITICAL":
                self.assertEqual(
                    f.human_gate_status,
                    "HOLD_FOR_LEAD_ENGINEER",
                    f"Finding {f.finding_id} ({f.element_or_ref}) was not held at gate!"
                )
            else:
                self.assertEqual(
                    f.human_gate_status,
                    "APPROVED",
                    f"Major finding {f.finding_id} was improperly held"
                )

    def test_04_export_integrity(self):
        """Verify CSV, JSON, and Markdown RFI exports contain valid data and full citation traces."""
        out_csv = os.path.join(self.test_dir, "test_export.csv")
        out_json = os.path.join(self.test_dir, "test_export.json")
        out_md = os.path.join(self.test_dir, "test_export.md")

        result = self.orchestrator.run_spec_vs_drawings(
            out_csv=out_csv,
            out_json=out_json,
            out_md=out_md
        )

        # Check CSV
        self.assertTrue(os.path.exists(out_csv))
        with open(out_csv, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            csv_rows = list(reader)
        self.assertEqual(len(csv_rows), 6)
        self.assertEqual(csv_rows[0]["finding_id"], "DSC-001")

        # Check JSON
        self.assertTrue(os.path.exists(out_json))
        with open(out_json, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.assertEqual(data["qa_integrity_score"], 100.0)
        self.assertEqual(len(data["findings"]), 6)

        # Check Markdown RFI
        self.assertTrue(os.path.exists(out_md))
        with open(out_md, "r", encoding="utf-8") as f:
            md_content = f.read()
        self.assertIn("# Formal Request for Information (RFI)", md_content)
        self.assertIn("DSC-001", md_content)
        self.assertIn("HOLD_FOR_LEAD_ENGINEER", md_content)

        # Cleanup
        for p in [out_csv, out_json, out_md]:
            if os.path.exists(p):
                os.remove(p)

    # ==========================================================================
    # 2. MASTER 20-SKILL REGISTRY VERIFICATION
    # ==========================================================================

    def test_05_all_20_skills_presence_and_distribution(self):
        """Verify all 20 skills exist and are correctly distributed across the 5 pillars."""
        all_results = self.orchestrator.run_all_20_skills()
        self.assertEqual(len(all_results), 20, "Expected exactly 20 skills in Master Registry")

        counts = {}
        for res in all_results.values():
            cat = res["category"]
            counts[cat] = counts.get(cat, 0) + 1

        self.assertEqual(counts["Setup"], 1)
        self.assertEqual(counts["Before You Bid"], 5)
        self.assertEqual(counts["Drawings"], 5)
        self.assertEqual(counts["The Model"], 5)
        self.assertEqual(counts["Schedule + Cost"], 4)

    def test_06_100_percent_qa_trace_across_all_20_skills(self):
        """Verify 100.0% QA integrity score and zero hallucinated citations across all 20 skills."""
        all_results = self.orchestrator.run_all_20_skills()
        for sid, res in all_results.items():
            self.assertEqual(res["qa_score"], 100.0, f"QA score below 100% in {sid}")
            self.assertGreaterEqual(res["total_findings"], 2, f"Skill {sid} has insufficient findings")

    def test_07_all_critical_items_in_all_20_skills_held_at_gate(self):
        """Verify all CRITICAL findings across the entire 20-skill suite are held at the Human Gate."""
        all_results = self.orchestrator.run_all_20_skills()
        for sid, res in all_results.items():
            for f in res["findings"]:
                if f["severity"] == "CRITICAL":
                    self.assertEqual(
                        f["human_gate_status"],
                        "HOLD_FOR_LEAD_ENGINEER",
                        f"Critical item {f['finding_id']} bypassed Human Gate in {sid}"
                    )

    # ==========================================================================
    # 3. SCHEMA AND SAMPLE DATA CONTRACTS
    # ==========================================================================

    def test_08_sample_data_and_templates_validity(self):
        """Verify sample input files and reusable skill template exist and are well-formed."""
        spec_path = os.path.join(self.test_dir, "sample_data", "spec_33kv_substation.json")
        dwg_path = os.path.join(self.test_dir, "sample_data", "drawings_33kv_sld_ga.json")
        tpl_path = os.path.join(self.test_dir, "templates", "skill_template.yaml")

        self.assertTrue(os.path.exists(spec_path), "sample_data/spec_33kv_substation.json missing")
        self.assertTrue(os.path.exists(dwg_path), "sample_data/drawings_33kv_sld_ga.json missing")
        self.assertTrue(os.path.exists(tpl_path), "templates/skill_template.yaml missing")

        with open(spec_path, "r", encoding="utf-8") as f:
            spec_json = json.load(f)
            self.assertIn("sections", spec_json)
            self.assertGreaterEqual(len(spec_json["sections"]), 6)

        with open(dwg_path, "r", encoding="utf-8") as f:
            dwg_json = json.load(f)
            self.assertIn("drawings", dwg_json)
            self.assertGreaterEqual(len(dwg_json["drawings"]), 6)

        with open(tpl_path, "r", encoding="utf-8") as f:
            tpl_text = f.read()
            self.assertIn("AutoConstSkillDefinition", tpl_text)
            self.assertIn("agent_pipeline", tpl_text)

if __name__ == "__main__":
    unittest.main(verbosity=2)
