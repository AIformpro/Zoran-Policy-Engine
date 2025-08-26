from policy_engine import load_rules, check_policies

if __name__ == "__main__":
    rules = load_rules()
    scenarios = [
        {"consent": True, "ttl": 5, "biometric": False, "energy": 50},
        {"consent": False, "ttl": 5, "biometric": False, "energy": 50},
        {"consent": True, "ttl": 0, "biometric": False, "energy": 120}
    ]
    for i, s in enumerate(scenarios, 1):
        print(f"--- Scenario {i} ---")
        log = check_policies(rules, s)
        print(log)
