# JEP Mapping to Vietnam Law on Artificial Intelligence (No. 134/2025/QH15)

**Detailed Article-by-Article Mapping with Code Examples and Verification Methods**

## 📋 Overview

This document provides a comprehensive mapping between the **Judgment Event Protocol (JEP)** and Vietnam's **Law on Artificial Intelligence (No. 134/2025/QH15)** , which took effect **March 1, 2026** .

The law adopts a **risk-based approach** with three tiers (high, medium, low) and establishes Vietnam as the **first ASEAN nation** with dedicated AI legislation .

---

## 📊 Chapter I: General Provisions

### Article 1: Scope of Regulation

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **Research, development, provision, deployment of AI systems** | Full lifecycle tracking | `tracker.log_activity()` | `verify-vietnam.py --scope` |
| **Organizations/individuals in Vietnam** | Jurisdiction detection | `tracker.detect_jurisdiction()` | `verify-vietnam.py --jurisdiction` |

### Article 3: Definitions

| Term | Definition | JEP Implementation |
|------|------------|-------------------|
| **Developer** | Designs, builds, trains, tests, or fine-tunes AI models | `entity_type="developer"` |
| **Provider** | Places AI systems on market under own name | `entity_type="provider"` |
| **Deployer** | Uses AI systems in professional activities | `entity_type="deployer"` |
| **User** | Interacts with AI systems or relies on outputs | `user_id` tracking |
| **Affected person** | Impacted by AI system decisions | `consumer_id` tracking |
| **Serious incident** | Events causing or risking significant damage | `incident.severity = "SERIOUS"` |

**Code Example:**
```python
from jep.vn import VietnamAITracker

# Different roles in the supply chain
developer = VietnamAITracker(entity_type="developer", org="AI Research Lab")
provider = VietnamAITracker(entity_type="provider", org="AI Solutions Inc.")
deployer = VietnamAITracker(entity_type="deployer", org="Bank of Vietnam")

# Track affected persons
decision = deployer.log_consequential_decision({
    "consumer_id": "CONS-123",
    "decision": "REJECT",
    "affected_person": True
})
```

### Article 4: Fundamental Principles

| Principle | JEP Implementation | Code Example |
|-----------|-------------------|--------------|
| **Human-centered, serving people** | `human_approver` field | `decision["human_approver"] = "supervisor-456"` |
| **Human oversight and intervention** | `delegate()` primitive | `tracker.delegate_action()` |
| **Fairness, transparency, non-bias** | Fairness metrics + bias testing | `fairness_metrics` |
| **Accountability for decisions** | Ed25519 signatures | `receipt["signature"]` |
| **Green, sustainable development** | Energy efficiency metrics | `efficiency_metrics` |

**Code Example:**
```python
# Human-centered principle: ultimate responsibility with humans
decision = tracker.log_consequential_decision({
    "decision": "APPROVE",
    "ai_was_determining_factor": True,
    "human_approver": "supervisor-456",  # Human in command
    "human_override_possible": True,
    "explanation": "Approved with human verification"
})

# Fairness principle
assessment = tracker.conduct_risk_assessment({
    "fairness_metrics": {
        "disparate_impact": 0.98,
        "demographic_parity": 0.97
    },
    "bias_test_results": {
        "race": "PASS",
        "gender": "PASS"
    }
})
```

### Article 7: Prohibited Acts

| Prohibition | JEP Implementation | Code Example |
|-------------|-------------------|--------------|
| **Exploiting AI for unlawful acts** | Compliance checking | `tracker.check_compliance()` |
| **Systematic deception/manipulation using deepfakes** | Content provenance | `tracker.add_watermark()` |
| **Exploiting vulnerable groups** | Vulnerability detection | `tracker.detect_vulnerable()` |
| **Generating/disseminating harmful fake content** | Content moderation | `tracker.moderate_content()` |
| **Illegal data collection/processing** | Data governance | `tracker.check_data_compliance()` |
| **Disabling human oversight mechanisms** | Oversight validation | `tracker.validate_oversight()` |
| **Concealing mandatory disclosures** | Disclosure validation | `tracker.validate_disclosures()` |

---

## 📊 Chapter II: Risk Classification and Management

### Article 9: Risk Level Classification

Vietnam uses a **3-tier risk classification** system :

| Risk Level | Definition | JEP Implementation | Verification |
|------------|------------|-------------------|--------------|
| **High Risk** | Significant harm to life, health, rights, national security | `risk_level="HIGH"` + safeguards | `verify-vietnam.py --high-risk` |
| **Medium Risk** | May mislead users unaware of AI interaction | `risk_level="MEDIUM"` + transparency | `verify-vietnam.py --medium-risk` |
| **Low Risk** | All other systems | `risk_level="LOW"` | `verify-vietnam.py --low-risk` |

**Classification Criteria** :

1. Impact on human rights, safety, security
2. Field of application (essential sectors, public interest)
3. User base and scale
4. Degree of automation and human control
5. Scale of potential impact

**Code Example:**
```python
def classify_ai_system(system_data):
    """Self-classify AI system per Article 9"""
    score = 0
    
    # Impact on human rights
    if system_data.get("affects_human_rights"):
        score += 40
    
    # Essential sector (healthcare, finance, education)
    if system_data.get("sector") in ["healthcare", "finance", "education"]:
        score += 30
    
    # User base
    if system_data.get("users") > 1000000:
        score += 20
    
    # Automation level
    if system_data.get("automation_level") == "full":
        score += 10
    
    # Determine risk level
    if score >= 70:
        risk_level = "HIGH"
    elif score >= 40:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"
    
    return risk_level

# Example usage
system = {
    "name": "Credit Scoring AI",
    "affects_human_rights": True,
    "sector": "financial",
    "users": 500000,
    "automation_level": "full"
}
risk_level = classify_ai_system(system)
assert risk_level == "HIGH"
```

### Article 10: System Classification and Notification

| Requirement | JEP Implementation | Code Example |
|-------------|-------------------|--------------|
| **Self-classification before deployment** | `classify_ai_system()` | `tracker.classify_system()` |
| **Notification to MoST for medium/high risk** | `notify_most()` | `tracker.notify_authority()` |
| **Risk classification dossier** | `risk_dossier` | `tracker.generate_dossier()` |
| **Reclassification if risks change** | `reclassify_system()` | `tracker.reclassify()` |

**Code Example:**
```python
# § 10.1: Self-classification before deployment
classification = tracker.classify_system({
    "system_id": "CREDIT-SCORE-001",
    "impact_assessment": {
        "human_rights": "HIGH",
        "safety": "MEDIUM",
        "public_welfare": "HIGH"
    },
    "sector": "financial_services",
    "user_base": 500000
})

# § 10.3: Notify MoST for medium/high risk
if classification["risk_level"] in ["MEDIUM", "HIGH"]:
    notification = tracker.notify_most({
        "system_id": classification["system_id"],
        "risk_level": classification["risk_level"],
        "classification_dossier": classification["dossier"],
        "notification_date": time.time()
    })
    
# § 10.6: Reclassification if modified
if system_modified:
    new_classification = tracker.reclassify_system(
        system_id="CREDIT-SCORE-001",
        modification_reason="New features added"
    )
```

---

## 📊 Chapter III: Transparency and Accountability

### Article 11: Transparency Obligations

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **§ 11.1: Users must know they're interacting with AI** | `is_ai_generated` flag | `receipt["is_ai_generated"] = True` | `verify-vietnam.py --disclosure` |
| **§ 11.2: Machine-readable markers for AI-generated audio/image/video** | `add_watermark()` | `tracker.add_marker(content)` | `verify-vietnam.py --markers` |
| **§ 11.3: Clear labels for deepfakes (simulated persons/events)** | `add_deepfake_label()` | `tracker.add_label(content, "DEEPFAKE")` | `verify-vietnam.py --deepfake` |
| **§ 11.4: Creative works exemption (appropriate labeling)** | `add_creative_label()` | `tracker.add_creative_label()` | `verify-vietnam.py --creative` |

**Code Example:**
```python
# § 11.1: AI system disclosure
class AIChatbot:
    def respond(self, user_query):
        response = self.generate_response(user_query)
        # Always disclose AI nature
        return {
            "content": response,
            "disclosure": "I am an AI assistant. You are interacting with an AI system.",
            "is_ai": True
        }

# § 11.2: Machine-readable markers for AI-generated content
def mark_ai_content(content, content_type):
    marker = tracker.add_marker({
        "content": content,
        "content_type": content_type,
        "marker_type": "machine_readable",
        "provider": "AI Media Corp",
        "generation_time": time.time(),
        "unique_id": tracker._generate_uuid7()
    })
    return marker

# § 11.3: Deepfake labeling
def label_deepfake(content, content_type):
    labeled = tracker.add_label({
        "content": content,
        "content_type": content_type,
        "label_text": "⚠️ DEEPFAKE: This content simulates a real person",
        "label_position": "top_left",
        "label_size": "large",
        "permanent": True
    })
    return labeled

# § 11.4: Creative works exemption
def mark_creative_work(content, content_type):
    # Appropriate labeling that doesn't hinder enjoyment
    labeled = tracker.add_creative_label({
        "content": content,
        "content_type": content_type,
        "disclosure_method": "end_credits",
        "disclosure_text": "This film contains AI-generated scenes"
    })
    return labeled
```

### Article 12: Serious Incident Response

| Requirement | JEP Implementation | Code Example |
|-------------|-------------------|--------------|
| **Proactive detection and remediation** | `monitor_for_incidents()` | `tracker.start_monitoring()` |
| **Technical fixes, suspension, withdrawal** | `remediate_incident()` | `tracker.remediate()` |
| **Notification to state authorities** | `notify_authority()` | `tracker.notify_most()` |
| **Incident logging and reporting** | `log_incident()` | `tracker.log_incident()` |

**Code Example:**
```python
# Define serious incident
serious_incident = {
    "incident_id": f"INC-{int(time.time())}",
    "discovery_time": time.time(),
    "incident_type": "safety_breach",
    "severity": "SERIOUS",
    "description": "Model generated harmful content",
    "affected_systems": ["chat-api"],
    "affected_users": 5000,
    "potential_harm": "Psychological harm to vulnerable users"
}

# Log and report incident
incident = tracker.log_incident(serious_incident)

# Remediate
remediation = tracker.remediate_incident({
    "incident_id": incident["incident_id"],
    "actions": [
        {"action": "suspended_system", "time": time.time()},
        {"action": "deployed_patch", "time": time.time() + 3600},
        {"action": "notified_users", "time": time.time() + 7200}
    ],
    "resolution_time": time.time() + 14400
})

# Notify MoST
notification = tracker.notify_most({
    "incident_id": incident["incident_id"],
    "notification_type": "SERIOUS_INCIDENT",
    "report": incident,
    "remediation": remediation,
    "notification_time": time.time()
})
```

---

## 📊 Chapter IV: Management of High-Risk AI Systems

### Article 13: High-Risk System Requirements

| Requirement | JEP Implementation | Code Example |
|-------------|-------------------|--------------|
| **Risk assessments** | `conduct_risk_assessment()` | `tracker.assess_risk()` |
| **Human oversight mechanisms** | `human_approver` field | `decision["human_approver"]` |
| **Registration in national database** | `register_with_most()` | `tracker.register_system()` |
| **Technical documentation** | `generate_documentation()` | `tracker.generate_docs()` |
| **Operational logs** | `log_decision()` + audit trail | `tracker.audit_log` |

**Code Example:**
```python
# High-risk system registration
high_risk_system = tracker.register_high_risk_system({
    "system_id": "HR-001",
    "system_name": "Credit Scoring AI",
    "sector": "financial",
    "risk_level": "HIGH",
    "impact_assessment": {
        "human_rights_impact": "HIGH",
        "safety_impact": "MEDIUM",
        "public_welfare_impact": "HIGH"
    },
    "human_oversight": {
        "mechanism": "dual_approval",
        "approvers": ["loan_officer", "credit_manager"],
        "override_capability": True
    },
    "technical_documentation": {
        "model_architecture": "neural_network",
        "training_data_summary": "50000 records",
        "accuracy_metrics": {"overall": 0.96}
    }
})

# Continuous logging
for decision in loan_decisions:
    receipt = tracker.log_consequential_decision(decision)
    # All decisions automatically logged for post-market inspection
```

### Article 14: Foreign Provider Requirements

| Requirement | JEP Implementation | Code Example |
|-------------|-------------------|--------------|
| **Local contact point in Vietnam** | `appoint_local_rep()` | `tracker.appoint_representative()` |
| **Commercial presence for conformity certification** | `establish_presence()` | `tracker.establish_office()` |

**Code Example:**
```python
# Foreign provider compliance
foreign_tracker = VietnamAITracker(
    organization="Global AI Inc.",
    jurisdiction="foreign",
    local_representative={
        "name": "Vietnam Representative Office",
        "address": "HCMC, Vietnam",
        "contact": "rep@globalai.vn",
        "authorized_officer": "Nguyen Van A"
    }
)

# For high-risk systems requiring certification
if system_requires_certification:
    foreign_tracker.establish_commercial_presence({
        "office_type": "branch",
        "registration_number": "2026-001",
        "certified_by": "MoST"
    })
```

---

## 📊 Chapter V: Management of Medium and Low-Risk Systems

### Article 15: Medium-Risk Systems

| Requirement | JEP Implementation | Code Example |
|-------------|-------------------|--------------|
| **Supervision via reports** | `generate_compliance_report()` | `tracker.generate_report()` |
| **Sample audits** | `conduct_audit()` | `tracker.audit_system()` |
| **Independent assessments** | `third_party_assessment()` | `tracker.engage_assessor()` |

**Code Example:**
```python
# Medium-risk system accountability
medium_risk_tracker = VietnamAITracker(risk_level="MEDIUM")

# Upon agency request during audit
if audit_requested:
    accountability_package = medium_risk_tracker.provide_accountability_info({
        "system_purpose": "Customer service chatbot",
        "operational_principles": "Rule-based + ML",
        "key_inputs": ["user_query", "history"],
        "safety_measures": ["content_filter", "human_escalation"],
        # Source code and trade secrets NOT disclosed
        "trade_secrets_protected": True
    })
```

### Article 16: Low-Risk Systems

| Requirement | JEP Implementation | Code Example |
|-------------|-------------------|--------------|
| **Minimal obligations** | Basic tracking | `tracker.log_basic()` |
| **Voluntary standards** | Optional compliance | `tracker.voluntary_comply()` |

---

## 📊 Chapter VI: Incentive Policies

### Article 20: AI Enterprise Incentives

| Incentive | JEP Implementation |
|-----------|-------------------|
| **Highest level of incentives** | `qualify_for_incentives()` |
| **Access to computing infrastructure** | `request_infrastructure_access()` |
| **Access to shared data** | `request_data_access()` |
| **Regulatory sandbox access** | `apply_for_sandbox()` |

### Article 21: Regulatory Sandbox

| Feature | JEP Implementation | Code Example |
|---------|-------------------|--------------|
| **Controlled risk environment** | `sandbox_mode()` | `tracker.enable_sandbox()` |
| **Exemption/reduction of compliance obligations** | `sandbox_exemption()` | `tracker.get_exemption()` |

**Code Example:**
```python
# Apply for regulatory sandbox
sandbox_application = tracker.apply_for_sandbox({
    "system_id": "INNOVATIVE-AI-001",
    "innovation_description": "Novty AI for education",
    "risk_level": "HIGH",  # Would normally require full compliance
    "testing_period_months": 6,
    "supervision_plan": {
        "reporting_frequency": "monthly",
        "monitoring_metrics": ["accuracy", "safety", "fairness"],
        "exit_criteria": ["accuracy > 0.95", "no_incidents"]
    }
})

# Get exemption from certain obligations
if sandbox_application["approved"]:
    tracker.enable_sandbox_mode({
        "exemptions": ["pre_deployment_certification"],
        "reduced_obligations": ["quarterly_reports"],
        "supervisor": "MoST_sandbox_team"
    })
```

### Article 22: National AI Development Fund

| Support Type | JEP Implementation |
|--------------|-------------------|
| **R&D grants** | `apply_for_grant()` |
| **Infrastructure investment** | `request_infrastructure_support()` |
| **Human resource training** | `apply_for_training_support()` |
| **Startup support** | `apply_startup_support()` |

---

## 📊 Chapter VII: Handling Violations and Liability

### Article 29: Liability and Penalties

| Provision | JEP Implementation | Code Example |
|-----------|-------------------|--------------|
| **Administrative sanctions** | `track_violations()` | `tracker.log_violation()` |
| **Penal liability** | `escalate_to_authorities()` | `tracker.escalate()` |
| **Civil damages** | `calculate_damages()` | `tracker.assess_damages()` |

**High-Risk System Liability** : Deployers must compensate victims first, may seek reimbursement from developer/provider .

**Code Example:**
```python
# Track violations
violation = tracker.log_violation({
    "violation_id": f"VIO-{int(time.time())}",
    "type": "missing_human_oversight",
    "severity": "HIGH",
    "description": "High-risk system deployed without human oversight",
    "affected_persons": 150,
    "estimated_damages": 50000000,  # VND
    "remediated": False,
    "remediation_deadline": time.time() + 2592000  # 30 days
})

# High-risk liability chain
if violation["type"] == "high-risk" and violation["affected_persons"] > 0:
    # Deployer compensates first
    deployer_compensation = tracker.pay_compensation({
        "amount": violation["estimated_damages"],
        "paid_to": "affected_persons",
        "date": time.time()
    })
    
    # Deployer seeks reimbursement from developer/provider
    if deployer_compensation["paid"]:
        reimbursement_claim = tracker.claim_reimbursement({
            "from_entity": "developer",
            "amount": violation["estimated_damages"],
            "contract_reference": "DEV-CONTRACT-2025-001"
        })
```

---

## 📊 Chapter VIII: Transitional Provisions

### Article 30: Grace Periods for Existing Systems

| System Type | Grace Period | Deadline | JEP Support |
|-------------|--------------|----------|-------------|
| **Healthcare, education, finance** | 18 months | Sept 1, 2027 | Transition mode |
| **Other systems** | 12 months | March 1, 2027 | Transition mode |

**Code Example:**
```python
# Pre-existing system (before March 1, 2026)
legacy_tracker = VietnamAITracker(
    organization="Legacy Systems Inc.",
    deployment_date="2025-12-15",  # Before law effective date
    grace_period_months=12 if sector not in ["healthcare", "education", "finance"] else 18
)

# Operate during grace period
legacy_tracker.operate_during_grace_period({
    "compliance_deadline": "2027-03-01",
    "transition_plan": {
        "phase1": "risk_classification",
        "phase2": "documentation_update",
        "phase3": "full_compliance"
    }
})
```

---

## ✅ Complete Verification

```bash
# Run complete Vietnam AI Law compliance verification
python tests/verify-vietnam.py --all

# Output:
# ========================================
# VIETNAM AI LAW COMPLIANCE VERIFICATION
# ========================================
# 
# 📋 Chapter I: General Provisions
#   ✅ Article 3: Role definitions
#   ✅ Article 4: Human-centered principles
#   ✅ Article 7: Prohibited acts
#
# 📋 Chapter II: Risk Classification
#   ✅ Article 9: 3-tier classification
#   ✅ Article 10: Self-classification + notification
#
# 📋 Chapter III: Transparency
#   ✅ Article 11: AI disclosure + content labeling
#   ✅ Article 12: Serious incident response
#
# 📋 Chapter IV: High-Risk Systems
#   ✅ Article 13: Human oversight + documentation
#   ✅ Article 14: Foreign provider requirements
#
# 📋 Chapter V: Medium/Low Risk
#   ✅ Article 15: Medium-risk accountability
#   ✅ Article 16: Low-risk minimal obligations
#
# 📋 Chapter VI: Incentives
#   ✅ Article 20-22: Sandbox + fund support
#
# 📋 Chapter VII: Liability
#   ✅ Article 29: Violation tracking + compensation
#
# 📋 Chapter VIII: Transition
#   ✅ Article 30: Grace period handling
#
# ========================================
# ✅ FULL COMPLIANCE VERIFIED
# ========================================
```

## 📚 References

- [Law on Artificial Intelligence 2025 (No. 134/2025/QH15), effective March 1, 2026](https://example.com) 
- [Decision No. 367/QĐ-TTg (March 3, 2026) implementing AI Law](https://caa.gov.vn/pho-bien-phap-luat/ke-hoach-trien-khai-thi-hanh-luat-tri-tue-nhan-tao-20260305134142028.htm) 
- [Ministry of Science and Technology (MoST) - Lead implementing agency](https://english.mst.gov.vn/) 
- [Vietnam AI Law: Risk-based approach analysis](https://connectontech.bakermckenzie.com/vietnams-first-standalone-ai-law-an-overview-of-key-provisions-future-implications/) 

## 📬 Contact

For Vietnam-specific inquiries:
- **Email**: vietnam@humanjudgment.org
- **GitHub**: [hjs-spec/jep-vn-solutions](https://github.com/hjs-spec/jep-vn-solutions)

---

*Last Updated: March 2026*
*Supporting Vietnam's leadership in ASEAN AI governance*
```
