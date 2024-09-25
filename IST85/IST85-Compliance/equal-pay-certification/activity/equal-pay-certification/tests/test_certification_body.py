import unittest
from pathlib import Path

from verify_certification_body import evaluate


class TestVerifyCertificationBody(unittest.TestCase):
    
    def test_valid_certification_body_will_pass(self):
        with open(Path(__file__).parent / 'equal_pay_certification_agreement_2023.md') as epf:
            equal_payment_doc = epf.read()
        outcome = evaluate(equal_payment_doc.splitlines())
        self.assertEqual(outcome[0], 'pass')
    
    def test_invalid_certification_body_will_fail(self):
        with open(Path(__file__).parent / 'equal_pay_certification_agreement_2023.md') as epf:
            equal_payment_doc = epf.read()
        dodgy_standards = equal_payment_doc.replace("Super Standards", "Dodgy Standards")
        outcome = evaluate(dodgy_standards.splitlines())
        self.assertEqual(outcome[0], 'fail')
    
    def test_invalid_input_raises_error(self):
        self.assertEqual(evaluate(1)[0], 'error')