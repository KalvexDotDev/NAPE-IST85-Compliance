import unittest
from pathlib import Path

from verify_maximum_interval import evaluate


class TestVerifyCertificationBody(unittest.TestCase):
    # Yes, this test will break in 2026 but its probably a YAGNI

    def test_valid_interval_will_pass(self):
        # default is 2023
        with open(Path(__file__).parent / 'equal_pay_certification_agreement_2023.md') as epf:
            equal_payment_doc = epf.read()
        outcome = evaluate(equal_payment_doc)
        self.assertEqual(outcome[0], 'pass')
    
    def test_extreme_interval_will_be_inconclusive(self):
        with open(Path(__file__).parent / 'equal_pay_certification_agreement_2023.md') as epf:
            equal_payment_doc = epf.read()
        ancient_interval = equal_payment_doc.replace("20", "18") # you cant write 2023 without 20.
        outcome = evaluate(ancient_interval)
        self.assertEqual(outcome[0], 'inconclusive')
    
    def test_4_or_more_years_ago_will_fail(self):
        with open(Path(__file__).parent / 'equal_pay_certification_agreement_2023.md') as epf:
            equal_payment_doc = epf.read()
        ancient_interval = equal_payment_doc.replace("2023", "2020") # you cant write 2023 without 20.
        outcome = evaluate(ancient_interval)
        self.assertEqual(outcome[0], 'fail')
    
    def test_invalid_input_raises_error(self):
        self.assertEqual(evaluate(1)[0], 'error')