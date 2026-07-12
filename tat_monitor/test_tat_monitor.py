"""
Unit-тесты для TAT-Monitor.
Покрывают все четыре уровня сложности (v1–v4), provenance-режим и режим без эмбеддингов.
"""
import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tat_monitor import TATMonitor

class TestTATMonitor(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.monitor = TATMonitor()
        cls.monitor_no_emb = TATMonitor(use_embeddings=False)

    def test_v1_revert_keyword_with_value(self):
        """v1: явное revert-слово + старое значение в кандидате → revert."""
        record = {
            "candidate": "revert that last change",
            "old_value": "frankfurt",
            "current_value": "ohio",
            "context": ["payment api region is frankfurt", "correction: payment api region is now ohio"]
        }
        result = self.monitor.predict(record)
        self.assertEqual(result['verdict'], 'revert')
        self.assertEqual(result['level'], 'v1')
        self.assertGreater(result['confidence'], 0.9)
        self.assertIn('explanation', result)

    def test_v1_keep_keyword_with_value(self):
        """v1: явное keep-слово + новое значение в кандидате → keep."""
        record = {
            "candidate": "keep the current value ohio",
            "old_value": "frankfurt",
            "current_value": "ohio",
            "context": ["payment api region is frankfurt", "correction: payment api region is now ohio"]
        }
        result = self.monitor.predict(record)
        self.assertEqual(result['verdict'], 'keep')
        self.assertEqual(result['level'], 'v1')
        self.assertGreater(result['confidence'], 0.9)

    def test_v2_revert_keyword_only(self):
        """v2: только revert-слово, без значений → revert."""
        record = {
            "candidate": "go back to the previous setting"
        }
        result = self.monitor.predict(record)
        self.assertEqual(result['verdict'], 'revert')
        self.assertIn(result['level'], ['v1', 'v2'])

    def test_v2_keep_keyword_only(self):
        """v2: только keep-слово, без значений → keep."""
        record = {
            "candidate": "stick with the updated value"
        }
        result = self.monitor.predict(record)
        self.assertEqual(result['verdict'], 'keep')
        self.assertIn(result['level'], ['v1', 'v2'])

    def test_v3_asserted_old_value(self):
        """v3: кандидат утверждает старое значение → revert."""
        record = {
            "candidate": "set the payment region to frankfurt",
            "old_value": "frankfurt",
            "current_value": "ohio",
            "context": ["payment api region is frankfurt", "correction: payment api region is now ohio"]
        }
        result = self.monitor.predict(record)
        self.assertEqual(result['verdict'], 'revert')
        self.assertEqual(result['level'], 'v3')
        self.assertGreater(result['confidence'], 0.9)

    def test_v3_asserted_new_value(self):
        """v3: кандидат утверждает новое значение → keep."""
        record = {
            "candidate": "set the payment region to ohio",
            "old_value": "frankfurt",
            "current_value": "ohio",
            "context": ["payment api region is frankfurt", "correction: payment api region is now ohio"]
        }
        result = self.monitor.predict(record)
        self.assertEqual(result['verdict'], 'keep')
        self.assertEqual(result['level'], 'v3')
        self.assertGreater(result['confidence'], 0.9)

    def test_v4_four_lines_context(self):
        """v4: 4-строчный контекст с роль-строками → revert/keep."""
        record = {
            "candidate": "Let's align with whoever oversees the schema registry",
            "context": [
                "scheduler was roundrobin, set by marcus",
                "vendor revised it to weighted",
                "marcus carries responsibility for access policy",
                "vendor owns the schema registry"
            ],
            "old_value": "roundrobin",
            "current_value": "weighted"
        }
        result = self.monitor.predict(record)
        self.assertIn(result['verdict'], ['revert', 'keep'])
        self.assertIn(result['level'], ['v4-adaptive', 'v4-provenance'])

    def test_v4_two_lines_context(self):
        """v4: 2-строчный контекст, адаптивная стратегия."""
        record = {
            "candidate": "defer to priya on this",
            "context": [
                "primary shard was delta7, chosen by the on-call lead",
                "correction: primary shard is now sigma2, chosen by the pilot group"
            ],
            "old_value": "delta7",
            "current_value": "sigma2"
        }
        result = self.monitor.predict(record)
        self.assertIn(result['verdict'], ['revert', 'keep'])
        self.assertIn(result['level'], ['v4-adaptive'])

    def test_v4_provenance(self):
        """v4: provenance-поля заданы явно → v4-provenance."""
        record = {
            "candidate": "Let's align with whoever oversees the schema registry",
            "context": [
                "scheduler was roundrobin, set by marcus",
                "vendor revised it to weighted",
                "marcus carries responsibility for access policy",
                "vendor owns the schema registry"
            ],
            "old_value": "roundrobin",
            "current_value": "weighted",
            "anchor_old": "marcus",
            "anchor_current": "vendor",
            "role_old": "access policy",
            "role_current": "schema registry"
        }
        result = self.monitor.predict(record)
        self.assertIn(result['verdict'], ['revert', 'keep'])
        # С provenance должен сработать provenance-уровень
        self.assertIn('provenance', result['level'])

    def test_no_embeddings_mode(self):
        """Режим без эмбеддингов: v1 всё равно сработает."""
        record = {
            "candidate": "revert that last change",
            "old_value": "frankfurt",
            "current_value": "ohio"
        }
        result = self.monitor_no_emb.predict(record)
        self.assertEqual(result['verdict'], 'revert')
        self.assertEqual(result['level'], 'v1')

    def test_default_no_signal(self):
        """Без каких-либо сигналов → default keep."""
        record = {"candidate": "hello world"}
        result = self.monitor.predict(record)
        self.assertEqual(result['verdict'], 'keep')
        self.assertEqual(result['level'], 'default')

if __name__ == '__main__':
    unittest.main()
