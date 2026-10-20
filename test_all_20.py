#!/usr/bin/env python3

"""

Master Verification & Validation Test Suite for All 20 Construction Skills

"""

import os

import unittest

from orchestrator_all_20 import MasterMultiAgentOrchestrator, SKILLS_REGISTRY

class TestAll20ConstructionSkills(unittest.TestCase):

    def setUp(self):

        self.orch = MasterMultiAgentOrchestrator()

        self.all_results = self.orch.run_all_20_skills()

    def test_01_exact_20_skills_present_and_grouped(self):

        """Verify all 20 skills exist across Setup (1), Before You Bid (5), Drawings (5), The Model (5), Schedule + Cost (4)."""

        self.assertEqual(len(self.all_results), 20)

        cats = {}

        for res in self.all_results.values():

            cats[res["category"]] = cats.get(res["category"], 0) + 1

        self.assertEqual(cats["Setup"], 1)

        self.assertEqual(cats["Before You Bid"], 5)

        self.assertEqual(cats["Drawings"], 5)

        self.assertEqual(cats["The Model"], 5)

        self.assertEqual(cats["Schedule + Cost"], 4)

    def test_02_100_percent_qa_citation_trace_across_all_20_skills(self):

        """Verify every single finding across all 20 skills has 100.0% QA citation integrity."""

        for sid, res in self.all_results.items():

            self.assertEqual(res["qa_integrity_score"], 100.0, f"QA failed on {sid}")

            self.assertGreaterEqual(res["total_findings"], 2, f"Insufficient findings in {sid}")

    def test_03_human_approval_gate_holds_all_critical_items(self):

        """Verify every CRITICAL finding across all 20 skills is held at the Human Approval Gate."""

        for sid, res in self.all_results.items():

            for f in res["findings"]:

                if f["severity"] == "CRITICAL":

                    self.assertEqual(

                        f["human_gate_status"],

                        "HOLD_FOR_LEAD_ENGINEER",

                        f"Critical item {f['finding_id']} bypassed gate in {sid}"

                    )

    def test_04_master_csv_export_all_20_skills(self):

        """Verify master CSV export writes all 55+ audited findings across all 20 skills cleanly."""

        out_path = "test_master_20_register.csv"

        self.orch.export_all_to_csv(out_path)

        self.assertTrue(os.path.exists(out_path))

        with open(out_path, "r", encoding="utf-8") as fp:

            lines = fp.readlines()

        self.assertGreaterEqual(len(lines), 50)

        os.remove(out_path)

if __name__ == "__main__":

    unittest.main(verbosity=2)
