import unittest
from policies import evaluate_policy,summary
class PolicyTests(unittest.TestCase):
    def test_missing_not_pass(self):
        f=evaluate_policy({"secure":{"encryption":"high","patch":"medium"}},{"secure":{"encryption":True}})
        self.assertEqual(summary(f)["passed"],1)
        self.assertEqual(f[1].status,"missing")
    def test_severity(self):
        f=evaluate_policy({"secure":{"encryption":"high"}},{"secure":{"encryption":False}})
        self.assertEqual(summary(f)["high_priority_gaps"],["secure.encryption"])
    def test_invalid_evidence(self):
        with self.assertRaises(ValueError):
            evaluate_policy({"secure":{"encryption":"high"}},{"secure":{"encryption":"yes"}})
if __name__=="__main__": unittest.main()
