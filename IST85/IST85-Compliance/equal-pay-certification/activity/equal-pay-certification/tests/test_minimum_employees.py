import unittest
import json
from pathlib import Path
from verify_minimum_employees import evaluate


class TestMaximumInterval(unittest.TestCase):
    
    def test_evaluate_with_24_employees_returns_fail(self):
        with open(Path(__file__).parent / 'employee_export.json') as eef:
            employees = json.load(eef)
        # Employee test data has 30 employees
        employees['results'] = employees['results'][0:23]
        outcome = evaluate(employees)
        self.assertEqual(outcome[0], 'fail')

    def test_evaluate_with_30_default_employees_returns_pass(self):
        with open(Path(__file__).parent / 'employee_export.json') as eef:
            employees = json.load(eef)
        # Employee test data has 30 employees
        outcome = evaluate(employees)
        self.assertEqual(outcome[0], 'pass')
        
    def test_evaluate_with_missing_employee_data_returns_inconclusive(self):
        with open(Path(__file__).parent / 'employee_export.json') as eef:
            employees = json.load(eef)
        # Employee test data has 30 employees
        del employees['results']
        outcome = evaluate(employees)
        self.assertEqual(outcome[0], 'inconclusive')
    
    # def test_evaluate_with_