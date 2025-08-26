import unittest
from policy_engine import load_rules, check_policies

class TestPolicyEngine(unittest.TestCase):
    def test_consent_required(self):
        rules = load_rules()
        data = {"consent": True, "ttl": 10, "biometric": False, "energy": 80}
        audit = check_policies(rules, data)
        assert all([entry["result"] for entry in audit])

    def test_violation(self):
        rules = load_rules()
        data = {"consent": False, "ttl": 0, "biometric": True, "energy": 200}
        audit = check_policies(rules, data)
        assert any([not entry["result"] for entry in audit])

if __name__ == "__main__":
    unittest.main()
