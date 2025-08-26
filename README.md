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



````markdown
# 🛡️ Zoran-Policy-Engine  

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  
[![Status](https://img.shields.io/badge/AI%20Act-Compliant-blue)]()  
[![RGPD](https://img.shields.io/badge/RGPD-Executable-orange)]()  
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.xxxxxx.svg)](https://doi.org/10.5281/zenodo.xxxxxx)  

Le **Policy Engine** de **Zoran aSiM** démontre que la conformité réglementaire (RGPD, AI Act, ISO 42001) peut être **exécutable, auditable et transparente**.  
Il charge des règles codées en YAML (`policy.yaml`) et les applique à des scénarios concrets (`demo.py`).  
Objectif : fournir une **preuve technique vivante** de conformité.  

---

## 🚀 Fonctionnalités
- 📜 Règles RGPD / AI Act définies en **YAML**.  
- ⚙️ Exécution Python stdlib (`policy_engine.py`).  
- 🔄 Rollback **ΔM11.3** si violation détectée.  
- 📝 Audit log automatique (`audit.json`).  
- ✅ Tests unitaires (`tests/test_policy.py`).  

---

## 📜 Exemples de règles
- **Consentement requis** avant traitement de données personnelles.  
- **Droit à l’oubli** (TTL → Time To Live).  
- **Biométrie interdite** sans base légale.  
- **Eco-ΔM11.3** : rollback si empreinte énergétique > seuil.  

---

## 📖 Démonstration
```bash
python demo.py
````

**Exemple de sortie :**

```
--- Scenario 1 ---
✅ Toutes les règles respectées.
--- Scenario 2 ---
⚠️ Violation: consent_required → rollback ΔM11.3
--- Scenario 3 ---
⚠️ Violation: eco_limit → rollback ΔM11.3
```

---

## 📊 Auditabilité

Chaque décision génère une entrée dans `audit.json` :

```json
{
  "rule": "consent_required",
  "description": "Consentement obligatoire avant tout traitement de données personnelles",
  "result": true,
  "timestamp": 1693051234.123
}
```

---

## 🔗 Liens associés

* White Paper : *“Executable Policy for Ethical AI: The Zoran aSiM Legal Kernel”* (à paraître, DOI en attente).
* Medium : vulgarisation publique en préparation.
* Contact : **[tabary01@gmail.com](mailto:tabary01@gmail.com)**

---

## 📄 Licence

MIT — usage libre, citation requise.
© 2025, **Frédéric Tabary** — Projet **Zoran aSiM**.

---

### 🌐 Bloc Glyphique (ZM)

```
⟦Zoran:Policy⋄ENGINE:RGPD+AIAct⟧
⟦ΔM11.3:rollback⋄AUDIT:public_good⟧
⟦ETHIC:executable⋄ASIM:Zoran⟧
```

---

```

---

👉 Ce README est déjà prêt à **booster ton SEO** et à être repris dans Zenodo / Medium / LinkedIn.  


```

## 📄 Licence
MIT — usage libre, citation requise :  
© 2025, Frédéric Tabary — contact : tabary01@gmail.com
