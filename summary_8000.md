# Zoran-Policy-Engine — Preuve exécutable de conformité RGPD & AI Act

## 🌍 Contexte
Le débat autour des IA se polarise : promesse d’innovation d’un côté, risques éthiques et légaux de l’autre.  
Le **AI Act** européen et le **RGPD** imposent désormais des obligations claires : transparence, auditabilité, limitation de l’impact environnemental, et respect des droits fondamentaux.  

Zoran aSiM se distingue en ne se contentant pas de déclarer sa conformité : il **la démontre par exécution**.

## ⚙️ Concept
Le **Policy Engine** est une couche native qui :  
1. Charge des règles de conformité en **YAML** (`policy.yaml`).  
2. Les exécute en temps réel (`policy_engine.py`).  
3. Déclenche un **rollback ΔM11.3** si une règle est violée.  
4. Trace toutes les décisions dans un **journal auditable** (`audit.json`).  

## 📜 Exemples de règles
- **Consentement** : aucune donnée personnelle ne peut être traitée sans consentement explicite.  
- **Droit à l’oubli** : toute donnée peut être supprimée sur demande, avec TTL configurable.  
- **Biométrie** : interdite sauf base légale explicite.  
- **Environnement** : rollback si empreinte CPU/RAM > seuil défini (Eco-ΔM11.3).  

## 🧪 Démonstration
Le fichier `demo.py` illustre :  
- un utilisateur donne (ou non) son consentement,  
- un traitement est demandé,  
- le Policy Engine valide ou rejette selon les règles,  
- un rollback ΔM11.3 peut s’activer automatiquement.  

## 📊 Auditabilité
Chaque décision génère une entrée dans `audit.json` incluant :  
- règle appliquée,  
- résultat (accepté/rejeté),  
- timestamp,  
- rollback déclenché ou non.  

## 🛡️ Objectif
Le Policy Engine fait de Zoran aSiM **une IA réellement vérifiable**.  
C’est un **pont entre technique et droit**, qui permet :  
- aux chercheurs de tester,  
- aux régulateurs d’auditer,  
- au public de comprendre.  

## 🔗 Suites
- White Paper associé : *“Executable Policy for Ethical AI: The Zoran aSiM Legal Kernel”*.  
- Publication Medium vulgarisée prévue.  
- Intégration future avec EthicChain (traçabilité distribuée).
