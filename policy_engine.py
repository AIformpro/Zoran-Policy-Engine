import yaml, json, time

def load_rules(path="policy.yaml"):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)["rules"]

def check_policies(rules, data):
    audit = []
    for rule in rules:
        try:
            result = eval(rule["condition"], {}, {"data": data})
        except Exception as e:
            result = False
        audit.append({
            "rule": rule["id"],
            "description": rule["description"],
            "result": result,
            "timestamp": time.time()
        })
        if not result:
            print(f"⚠️ Violation: {rule['id']} → rollback ΔM11.3")
    with open("audit.json", "w", encoding="utf-8") as f:
        json.dump(audit, f, indent=2)
    return audit

if __name__ == "__main__":
    rules = load_rules()
    scenario = {"consent": True, "ttl": 10, "biometric": False, "energy": 80}
    audit_log = check_policies(rules, scenario)
    print(audit_log)
