# Zoran-Policy-Engine

Le **Policy Engine** de Zoran aSiM démontre que la conformité réglementaire (RGPD, AI Act, ISO 42001) peut être **exécutable, auditable et transparente**.  
Il charge des règles codées en YAML (`policy.yaml`) et les applique à des scénarios concrets (`demo.py`).  
Objectif : fournir une **preuve technique vivante** de conformité.

## 🚀 Fonctionnalités
- Règles RGPD / AI Act définies en YAML.
- Exécution Python stdlib (`policy_engine.py`).
- Rollback ΔM11.3 si violation détectée.
- Audit log automatique (`audit.json`).
- Tests unitaires (`tests/test_policy.py`).

## 📜 Exemples de règles
- Consentement requis avant traitement de données personnelles.
- Droit à l’oubli (TTL → Time To Live).
- Interdiction de traitement biométrique sans base légale.
- Limitation d’impact environnemental (Eco-ΔM11.3).

## 📖 Démonstration
```bash
python demo.py
```

## 📄 Licence
MIT — usage libre, citation requise :  
© 2025, Frédéric Tabary — contact : tabary01@gmail.com
