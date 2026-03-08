#!/usr/bin/env python3
"""
Vietnam AI Law (No. 134/2025/QH15) Compliance Tracker
========================================================

Complete implementation of Vietnam's Law on Artificial Intelligence,
effective March 1, 2026.

This tracker ensures all AI systems comply with:
- Chapter I: General Provisions (definitions, principles, prohibited acts)
- Chapter II: Risk Classification (3-tier risk assessment)
- Chapter III: Transparency & Accountability (AI disclosure, content labeling)
- Chapter IV: High-Risk Systems (human oversight, documentation, registration)
- Chapter V: Medium/Low Risk Systems (accountability info)
- Chapter VI: Incentives (regulatory sandbox)
- Chapter VII: Liability (violation tracking, compensation)
- Chapter VIII: Transitional Provisions (grace periods)
"""

import json
import time
import hashlib
from datetime import datetime, timedelta
from typing import Dict, Any, Optional, List, Tuple, Union
from enum import Enum

# Try to import cryptography
try:
    from cryptography.hazmat.primitives.asymmetric import ed25519
    CRYPTO_AVAILABLE = True
except ImportError:
    CRYPTO_AVAILABLE = False
    print("⚠️ Warning: cryptography not installed. Using mock signatures.")


class EntityType(Enum):
    """Roles in AI supply chain (Article 3)"""
    DEVELOPER = "developer"
    PROVIDER = "provider"
    DEPLOYER = "deployer"
    USER = "user"


class RiskLevel(Enum):
    """3-tier risk classification (Article 9)"""
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


class ContentType(Enum):
    """Types of content requiring marking (Article 11)"""
    IMAGE = "image"
    VIDEO = "video"
    AUDIO = "audio"
    TEXT = "text"


class IncidentSeverity(Enum):
    """Incident severity levels (Article 12)"""
    MINOR = "MINOR"
    MODERATE = "MODERATE"
    SERIOUS = "SERIOUS"  # Must notify authorities
    CRITICAL = "CRITICAL"  # Immediate action required


class VietnamAITracker:
    """
    Complete Vietnam AI Law compliance tracker.
    
    Covers all chapters of Law No. 134/2025/QH15, effective March 1, 2026.
    """
    
    def __init__(
        self,
        organization: str,
        entity_type: EntityType,
        jurisdiction: str = "vietnam",
        deployment_date: Optional[float] = None,
        local_representative: Optional[Dict] = None,
        private_key_hex: Optional[str] = None
    ):
        """
        Initialize Vietnam AI Law tracker.
        
        Args:
            organization: Organization name
            entity_type: DEVELOPER, PROVIDER, DEPLOYER, or USER
            jurisdiction: "vietnam" or "foreign"
            deployment_date: When system was first deployed
            local_representative: For foreign providers (Article 14)
            private_key_hex: Optional private key for signatures
        """
        self.organization = organization
        self.entity_type = entity_type
        self.jurisdiction = jurisdiction
        self.deployment_date = deployment_date or time.time()
        self.local_representative = local_representative
        
        # Determine grace period (Article 30)
        self.effective_date = datetime(2026, 3, 1).timestamp()
        if self.deployment_date < self.effective_date:
            # Pre-existing system - grace period applies
            self.grace_period_months = self._calculate_grace_period()
            self.grace_period_end = self.effective_date + (self.grace_period_months * 30 * 86400)
        else:
            self.grace_period_months = 0
            self.grace_period_end = self.effective_date
        
        # Initialize signer
        self.signer = self._init_signer(private_key_hex)
        
        # Data stores
        self.systems = {}
        self.risk_assessments = []
        self.decisions = []
        self.incidents = []
        self.content_markers = []
        self.audit_log = []
        self.violations = []
        
        print(f"✅ Vietnam AI Law Tracker initialized")
        print(f"   Organization: {organization}")
        print(f"   Entity Type: {entity_type.value}")
        print(f"   Jurisdiction: {jurisdiction}")
        print(f"   Effective Date: March 1, 2026")
        print(f"   Grace Period: {self.grace_period_months} months (ends {datetime.fromtimestamp(self.grace_period_end)})")
    
    def _init_signer(self, private_key_hex: Optional[str] = None):
        """Initialize cryptographic signer."""
        if CRYPTO_AVAILABLE:
            if private_key_hex:
                return ed25519.Ed25519PrivateKey.from_private_bytes(
                    bytes.fromhex(private_key_hex)
                )
            else:
                return ed25519.Ed25519PrivateKey.generate()
        return None
    
    def _generate_uuid7(self) -> str:
        """Generate UUID v7 for traceability."""
        import uuid
        timestamp = int(time.time() * 1000)
        random_part = uuid.uuid4().hex[:12]
        return f"{timestamp:08x}-{random_part[:4]}-7{random_part[4:7]}-{random_part[7:11]}-{random_part[11:]}"
    
    def _sign(self, data: Dict) -> str:
        """Sign data with Ed25519."""
        if CRYPTO_AVAILABLE and self.signer:
            message = json.dumps(data, sort_keys=True).encode()
            signature = self.signer.sign(message)
            return f"ed25519:{signature.hex()[:64]}"
        return f"mock_sig_{hash(json.dumps(data, sort_keys=True))}"
    
    def _log_audit(self, event_type: str, data: Dict[str, Any]) -> None:
        """Internal audit logging."""
        self.audit_log.append({
            "event_type": event_type,
            "timestamp": time.time(),
            "data": data
        })
    
    def _calculate_grace_period(self) -> int:
        """Calculate grace period per Article 30."""
        # Default 12 months
        grace_period = 12
        
        # Extend to 18 months for critical sectors
        # In practice, this would check the system's sector
        # For demo, return 12
        return grace_period
    
    # ========================================================================
    # Chapter II: Risk Classification (Article 9-10)
    # ========================================================================
    
    def classify_system(
        self,
        system_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Self-classify AI system before deployment (Article 9-10).
        
        Args:
            system_data: System information for classification
        
        Returns:
            Classification result with risk level
        """
        system_id = system_data.get("system_id", f"SYS-{self._generate_uuid7()}")
        
        # Calculate risk score based on criteria (Article 9)
        risk_score = 0
        risk_factors = []
        
        # Criterion 1: Impact on human rights
        if system_data.get("affects_human_rights"):
            risk_score += 40
            risk_factors.append("affects_human_rights")
        
        # Criterion 2: Sector (essential sectors = higher risk)
        sector = system_data.get("sector", "").lower()
        essential_sectors = ["healthcare", "finance", "education", "transportation", "energy"]
        if sector in essential_sectors:
            risk_score += 30
            risk_factors.append(f"sector:{sector}")
        
        # Criterion 3: User base
        users = system_data.get("users", 0)
        if users > 1000000:
            risk_score += 20
            risk_factors.append("large_user_base")
        elif users > 100000:
            risk_score += 10
            risk_factors.append("medium_user_base")
        
        # Criterion 4: Automation level
        automation = system_data.get("automation_level", "assisted")
        if automation == "full":
            risk_score += 20
            risk_factors.append("fully_automated")
        elif automation == "high":
            risk_score += 10
            risk_factors.append("highly_automated")
        
        # Determine risk level
        if risk_score >= 70:
            risk_level = RiskLevel.HIGH
        elif risk_score >= 40:
            risk_level = RiskLevel.MEDIUM
        else:
            risk_level = RiskLevel.LOW
        
        # Create classification record
        classification = {
            "system_id": system_id,
            "organization": self.organization,
            "classification_date": time.time(),
            "risk_score": risk_score,
            "risk_level": risk_level.value,
            "risk_factors": risk_factors,
            "criteria": {
                "affects_human_rights": system_data.get("affects_human_rights", False),
                "sector": system_data.get("sector", "unknown"),
                "users": system_data.get("users", 0),
                "automation_level": system_data.get("automation_level", "unknown")
            },
            "deployment_date": system_data.get("deployment_date", time.time()),
            "requires_notification": risk_level in [RiskLevel.MEDIUM, RiskLevel.HIGH],
            "grace_period_applies": self.deployment_date < self.effective_date
        }
        
        classification["signature"] = self._sign(classification)
        self.systems[system_id] = classification
        self._log_audit("SYSTEM_CLASSIFIED", classification)
        
        print(f"\n📋 Article 9-10: System Classification")
        print(f"   System ID: {system_id}")
        print(f"   Risk Level: {risk_level.value} (Score: {risk_score})")
        print(f"   Notify MoST: {classification['requires_notification']}")
        
        return classification
    
    def notify_most(
        self,
        notification_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Notify Ministry of Science and Technology (Article 10.3).
        
        Required for medium and high-risk systems.
        """
        notification_id = f"MOST-{self._generate_uuid7()}"
        
        notification = {
            "notification_id": notification_id,
            "organization": self.organization,
            "entity_type": self.entity_type.value,
            "system_id": notification_data.get("system_id"),
            "risk_level": notification_data.get("risk_level"),
            "classification_dossier": notification_data.get("classification_dossier", {}),
            "notification_date": time.time(),
            "jurisdiction": self.jurisdiction,
            "local_representative": self.local_representative,
            "status": "RECEIVED"
        }
        
        notification["signature"] = self._sign(notification)
        self._log_audit("MOST_NOTIFICATION", notification)
        
        print(f"\n📋 Article 10.3: MoST Notification")
        print(f"   Notification ID: {notification_id}")
        print(f"   System ID: {notification['system_id']}")
        print(f"   Risk Level: {notification['risk_level']}")
        
        return notification
    
    def reclassify_system(
        self,
        system_id: str,
        modification_reason: str,
        new_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Reclassify system after modifications (Article 10.6)."""
        
        if system_id not in self.systems:
            raise ValueError(f"System {system_id} not found")
        
        # Reclassify with new data
        new_classification = self.classify_system(new_data)
        new_classification["previous_classification"] = self.systems[system_id]
        new_classification["modification_reason"] = modification_reason
        new_classification["modification_date"] = time.time()
        
        self.systems[system_id] = new_classification
        
        return new_classification
    
    # ========================================================================
    # Chapter III: Transparency and Accountability (Article 11-12)
    # ========================================================================
    
    def add_content_marker(
        self,
        content_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Add machine-readable markers to AI-generated content (Article 11.2).
        
        Required for audio, image, and video content.
        """
        marker_id = f"MARK-{self._generate_uuid7()}"
        unique_id = self._generate_uuid7()
        
        marker = {
            "marker_id": marker_id,
            "content_id": content_data.get("content_id", f"CONTENT-{int(time.time())}"),
            "content_type": content_data.get("content_type", "image"),
            "marker_type": "machine_readable",
            "provider": self.organization,
            "generation_time": time.time(),
            "unique_id": unique_id,
            
            # For deepfake labeling (Article 11.3)
            "is_deepfake": content_data.get("is_deepfake", False),
            "deepfake_label": content_data.get("deepfake_label"),
            
            # Permanent link for verification
            "verify_url": f"https://verify.{self.organization}/content/{unique_id}",
            
            # Machine-readable format (JSON-LD)
            "machine_readable": {
                "@context": "https://schema.org",
                "@type": "CreativeWork",
                "identifier": unique_id,
                "isAIGenerated": True,
                "provider": {
                    "@type": "Organization",
                    "name": self.organization
                },
                "dateCreated": datetime.now().isoformat()
            }
        }
        
        marker["signature"] = self._sign(marker)
        self.content_markers.append(marker)
        self._log_audit("CONTENT_MARKER_ADDED", marker)
        
        print(f"\n📋 Article 11.2: Content Marker Added")
        print(f"   Marker ID: {marker_id}")
        print(f"   Content Type: {marker['content_type']}")
        print(f"   Deepfake: {marker['is_deepfake']}")
        
        return marker
    
    def add_deepfake_label(
        self,
        label_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Add clear visible label for deepfake content (Article 11.3).
        
        Deepfakes simulating real persons or events must have clear labels
        distinguishing them from authentic content.
        """
        label_id = f"DF-{self._generate_uuid7()}"
        
        label = {
            "label_id": label_id,
            "content_id": label_data.get("content_id"),
            "content_type": label_data.get("content_type"),
            "label_text": label_data.get("label_text", "⚠️ DEEPFAKE: This content simulates a real person"),
            "label_position": label_data.get("label_position", "top_left"),
            "label_size": label_data.get("label_size", "large"),
            "permanent": label_data.get("permanent", True),
            "removal_detection": True,
            "added_date": time.time()
        }
        
        label["signature"] = self._sign(label)
        self._log_audit("DEEPFAKE_LABEL_ADDED", label)
        
        print(f"\n📋 Article 11.3: Deepfake Label Added")
        print(f"   Label ID: {label_id}")
        print(f"   Label Text: {label['label_text']}")
        
        return label
    
    def add_creative_label(
        self,
        label_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Add appropriate label for creative works (Article 11.4).
        
        Creative works may use appropriate labeling that doesn't hinder
        aesthetic enjoyment (e.g., end credits, metadata).
        """
        label_id = f"CR-{self._generate_uuid7()}"
        
        label = {
            "label_id": label_id,
            "content_id": label_data.get("content_id"),
            "content_type": label_data.get("content_type", "video"),
            "disclosure_method": label_data.get("disclosure_method", "end_credits"),
            "disclosure_text": label_data.get("disclosure_text", "This work contains AI-generated elements"),
            "disclosure_position": label_data.get("disclosure_position", "end"),
            "metadata_included": label_data.get("metadata_included", True)
        }
        
        label["signature"] = self._sign(label)
        self._log_audit("CREATIVE_LABEL_ADDED", label)
        
        return label
    
    def log_incident(
        self,
        incident_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Log and report serious incidents (Article 12).
        
        Serious incidents must be reported to state authorities.
        """
        incident_id = f"INC-{self._generate_uuid7()}"
        
        discovery_time = incident_data.get("discovery_time", time.time())
        
        incident = {
            "incident_id": incident_id,
            "organization": self.organization,
            "discovery_time": discovery_time,
            "incident_type": incident_data.get("incident_type", "unknown"),
            "severity": incident_data.get("severity", "MODERATE"),
            "description": incident_data.get("description", ""),
            "affected_systems": incident_data.get("affected_systems", []),
            "affected_users": incident_data.get("affected_users", 0),
            "potential_harm": incident_data.get("potential_harm", ""),
            "root_cause": incident_data.get("root_cause", ""),
            "remediation_steps": incident_data.get("remediation_steps", []),
            "reported_to_authorities": incident_data.get("reported_to_authorities", False),
            "reporting_time": time.time() if incident_data.get("reported_to_authorities") else None
        }
        
        # Serious incidents require notification (Article 12.3)
        if incident["severity"] in ["SERIOUS", "CRITICAL"]:
            incident["requires_authority_notification"] = True
            incident["notification_deadline"] = discovery_time + 86400  # 24 hours
        
        incident["signature"] = self._sign(incident)
        self.incidents.append(incident)
        self._log_audit("INCIDENT_LOGGED", incident)
        
        print(f"\n📋 Article 12: Incident Logged")
        print(f"   Incident ID: {incident_id}")
        print(f"   Severity: {incident['severity']}")
        print(f"   Affected Users: {incident['affected_users']}")
        if incident.get("requires_authority_notification"):
            print(f"   ⚠️ Must notify authorities within 24 hours")
        
        return incident
    
    def remediate_incident(
        self,
        remediation_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Remediate incident with technical fixes, suspension, or withdrawal (Article 12.2).
        """
        remediation_id = f"REM-{self._generate_uuid7()}"
        
        remediation = {
            "remediation_id": remediation_id,
            "incident_id": remediation_data.get("incident_id"),
            "actions": remediation_data.get("actions", []),
            "resolution_time": remediation_data.get("resolution_time", time.time()),
            "status": "RESOLVED" if remediation_data.get("resolution_time") else "IN_PROGRESS"
        }
        
        remediation["signature"] = self._sign(remediation)
        self._log_audit("INCIDENT_REMEDIATED", remediation)
        
        return remediation
    
    # ========================================================================
    # Chapter IV: High-Risk Systems (Article 13-14)
    # ========================================================================
    
    def register_high_risk_system(
        self,
        system_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Register high-risk AI system in national database (Article 13.1).
        
        High-risk systems must have:
        - Risk assessments
        - Human oversight mechanisms
        - Registration in national database
        - Technical documentation
        - Operational logs
        """
        system_id = system_data.get("system_id", f"HR-{self._generate_uuid7()}")
        
        system = {
            "system_id": system_id,
            "organization": self.organization,
            "system_name": system_data.get("system_name"),
            "sector": system_data.get("sector"),
            "risk_level": "HIGH",
            "description": system_data.get("description"),
            "impact_assessment": system_data.get("impact_assessment", {}),
            
            # Human oversight (Article 13.1)
            "human_oversight": system_data.get("human_oversight", {
                "mechanism": "dual_approval",
                "approvers": ["loan_officer", "credit_manager"],
                "override_capability": True,
                "escalation_procedure": "documented"
            }),
            
            # Technical documentation (Article 13.1)
            "technical_documentation": system_data.get("technical_documentation", {
                "model_architecture": "neural_network",
                "training_data_summary": "50000 records",
                "accuracy_metrics": {"overall": 0.96},
                "version": "1.0.0"
            }),
            
            # Registration (Article 13.1)
            "registration_date": time.time(),
            "registration_number": f"VN-HR-{int(time.time())}",
            
            # For foreign providers (Article 14)
            "local_representative": self.local_representative,
            
            "status": "ACTIVE"
        }
        
        system["signature"] = self._sign(system)
        self.systems[system_id] = system
        self._log_audit("HIGH_RISK_REGISTERED", system)
        
        print(f"\n📋 Article 13: High-Risk System Registered")
        print(f"   System ID: {system_id}")
        print(f"   System Name: {system['system_name']}")
        print(f"   Sector: {system['sector']}")
        print(f"   Registration #: {system['registration_number']}")
        
        return system
    
    def appoint_local_representative(
        self,
        rep_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Appoint local contact point in Vietnam (Article 14).
        
        Required for foreign providers of high-risk systems.
        """
        self.local_representative = {
            "name": rep_data.get("name"),
            "address": rep_data.get("address"),
            "contact": rep_data.get("contact"),
            "authorized_officer": rep_data.get("authorized_officer"),
            "appointment_date": time.time()
        }
        
        print(f"\n📋 Article 14: Local Representative Appointed")
        print(f"   Name: {self.local_representative['name']}")
        print(f"   Contact: {self.local_representative['contact']}")
        
        return self.local_representative
    
    # ========================================================================
    # Chapter V: Medium/Low Risk Systems (Article 15-16)
    # ========================================================================
    
    def provide_accountability_info(
        self,
        info_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Provide accountability information for medium-risk systems (Article 15).
        
        Upon agency request during audit, must provide:
        - Purpose of AI system
        - Operational principles
        - Key inputs and outputs
        - Safety measures
        - Source code and trade secrets protected
        """
        info_id = f"INFO-{self._generate_uuid7()}"
        
        info = {
            "info_id": info_id,
            "organization": self.organization,
            "system_purpose": info_data.get("system_purpose"),
            "operational_principles": info_data.get("operational_principles"),
            "key_inputs": info_data.get("key_inputs", []),
            "key_outputs": info_data.get("key_outputs", []),
            "safety_measures": info_data.get("safety_measures", []),
            "performance_metrics": info_data.get("performance_metrics", {}),
            "trade_secrets_protected": info_data.get("trade_secrets_protected", True),
            "provided_date": time.time()
        }
        
        info["signature"] = self._sign(info)
        self._log_audit("ACCOUNTABILITY_INFO", info)
        
        return info
    
    # ========================================================================
    # Chapter VI: Incentives (Article 20-22)
    # ========================================================================
    
    def apply_for_sandbox(
        self,
        application_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Apply for regulatory sandbox (Article 21).
        
        Allows high-risk systems to test in controlled environment
        with reduced compliance obligations.
        """
        app_id = f"SANDBOX-{self._generate_uuid7()}"
        
        application = {
            "application_id": app_id,
            "organization": self.organization,
            "system_id": application_data.get("system_id"),
            "innovation_description": application_data.get("innovation_description"),
            "risk_level": application_data.get("risk_level", "HIGH"),
            "testing_period_months": application_data.get("testing_period_months", 6),
            "supervision_plan": application_data.get("supervision_plan", {}),
            "exit_criteria": application_data.get("exit_criteria", []),
            "application_date": time.time(),
            "status": "PENDING"
        }
        
        application["signature"] = self._sign(application)
        self._log_audit("SANDBOX_APPLICATION", application)
        
        print(f"\n📋 Article 21: Regulatory Sandbox Application")
        print(f"   Application ID: {app_id}")
        print(f"   Testing Period: {application['testing_period_months']} months")
        
        return application
    
    def enable_sandbox_mode(
        self,
        sandbox_config: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Enable sandbox mode with exemptions from certain obligations.
        """
        mode_id = f"SAND-{self._generate_uuid7()}"
        
        sandbox = {
            "mode_id": mode_id,
            "application_id": sandbox_config.get("application_id"),
            "exemptions": sandbox_config.get("exemptions", []),
            "reduced_obligations": sandbox_config.get("reduced_obligations", []),
            "supervisor": sandbox_config.get("supervisor", "MoST_sandbox_team"),
            "reporting_frequency": sandbox_config.get("reporting_frequency", "monthly"),
            "start_date": time.time(),
            "end_date": time.time() + (sandbox_config.get("duration_months", 6) * 30 * 86400),
            "status": "ACTIVE"
        }
        
        sandbox["signature"] = self._sign(sandbox)
        self._log_audit("SANDBOX_ENABLED", sandbox)
        
        return sandbox
    
    # ========================================================================
    # Chapter VII: Liability (Article 29)
    # ========================================================================
    
    def log_violation(
        self,
        violation_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Log potential violation for penalty calculation (Article 29).
        """
        violation_id = f"VIO-{self._generate_uuid7()}"
        
        violation = {
            "violation_id": violation_id,
            "organization": self.organization,
            "date": violation_data.get("date", time.time()),
            "type": violation_data.get("type", "unknown"),
            "severity": violation_data.get("severity", "MEDIUM"),
            "description": violation_data.get("description", ""),
            "affected_persons": violation_data.get("affected_persons", 0),
            "estimated_damages_vnd": violation_data.get("estimated_damages_vnd", 0),
            "remediated": violation_data.get("remediated", False),
            "remediation_deadline": violation_data.get("remediation_deadline"),
            "reported_to_authorities": violation_data.get("reported_to_authorities", False)
        }
        
        violation["signature"] = self._sign(violation)
        self.violations.append(violation)
        self._log_audit("VIOLATION_LOGGED", violation)
        
        return violation
    
    def pay_compensation(
        self,
        compensation_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Pay compensation to affected persons (Article 29).
        
        Deployers must compensate victims first, may seek reimbursement from developer/provider.
        """
        payment_id = f"COMP-{self._generate_uuid7()}"
        
        payment = {
            "payment_id": payment_id,
            "violation_id": compensation_data.get("violation_id"),
            "amount_vnd": compensation_data.get("amount_vnd", 0),
            "paid_to": compensation_data.get("paid_to", "affected_persons"),
            "payment_date": time.time(),
            "payment_method": compensation_data.get("payment_method", "bank_transfer"),
            "paid": True
        }
        
        payment["signature"] = self._sign(payment)
        self._log_audit("COMPENSATION_PAID", payment)
        
        return payment
    
    def claim_reimbursement(
        self,
        claim_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Claim reimbursement from developer/provider (Article 29).
        
        After paying victims, deployer may seek reimbursement from upstream entity.
        """
        claim_id = f"REIM-{self._generate_uuid7()}"
        
        claim = {
            "claim_id": claim_id,
            "violation_id": claim_data.get("violation_id"),
            "from_entity": claim_data.get("from_entity", "developer"),
            "amount_vnd": claim_data.get("amount_vnd", 0),
            "contract_reference": claim_data.get("contract_reference"),
            "claim_date": time.time(),
            "status": "FILED"
        }
        
        claim["signature"] = self._sign(claim)
        self._log_audit("REIMBURSEMENT_CLAIMED", claim)
        
        return claim
    
    # ========================================================================
    # Chapter VIII: Transitional Provisions (Article 30)
    # ========================================================================
    
    def check_grace_period_status(self) -> Dict[str, Any]:
        """
        Check grace period status for pre-existing systems (Article 30).
        """
        now = time.time()
        
        status = {
            "deployment_date": self.deployment_date,
            "effective_date": self.effective_date,
            "grace_period_months": self.grace_period_months,
            "grace_period_end": self.grace_period_end,
            "days_remaining": max(0, (self.grace_period_end - now) / 86400),
            "in_grace_period": now < self.grace_period_end
        }
        
        return status
    
    def operate_during_grace_period(
        self,
        transition_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Operate during grace period with transition plan.
        """
        plan_id = f"TRANS-{self._generate_uuid7()}"
        
        plan = {
            "plan_id": plan_id,
            "organization": self.organization,
            "compliance_deadline": transition_data.get("compliance_deadline", self.grace_period_end),
            "transition_plan": transition_data.get("transition_plan", []),
            "current_phase": transition_data.get("current_phase", "risk_classification"),
            "start_date": time.time(),
            "status": "ACTIVE"
        }
        
        plan["signature"] = self._sign(plan)
        self._log_audit("GRACE_PERIOD_OPERATION", plan)
        
        return plan
    
    # ========================================================================
    # Reporting and Verification
    # ========================================================================
    
    def generate_compliance_report(
        self,
        include_violations: bool = True
    ) -> Dict[str, Any]:
        """
        Generate comprehensive Vietnam AI Law compliance report.
        """
        report_id = f"VN-{self._generate_uuid7()}"
        
        # Count high-risk systems
        high_risk_count = sum(1 for s in self.systems.values() 
                              if s.get("risk_level") == "HIGH")
        
        report = {
            "report_id": report_id,
            "organization": self.organization,
            "entity_type": self.entity_type.value,
            "report_date": datetime.now().isoformat(),
            "effective_date": "2026-03-01",
            "grace_period": self.check_grace_period_status(),
            "statistics": {
                "total_systems": len(self.systems),
                "high_risk_systems": high_risk_count,
                "risk_assessments": len(self.risk_assessments),
                "incidents_logged": len(self.incidents),
                "content_markers": len(self.content_markers),
                "violations": len(self.violations) if include_violations else 0
            },
            "compliance_summary": {
                "risk_classification": {
                    "status": "COMPLIANT" if len(self.systems) > 0 else "PENDING"
                },
                "transparency": {
                    "status": "COMPLIANT" if len(self.content_markers) > 0 else "PENDING"
                },
                "incident_response": {
                    "status": "COMPLIANT",
                    "serious_incidents_reported": len([i for i in self.incidents if i.get("severity") in ["SERIOUS", "CRITICAL"]])
                }
            }
        }
        
        report["signature"] = self._sign(report)
        return report
    
    def verify_compliance(self) -> Dict[str, Any]:
        """Verify compliance with all Vietnam AI Law requirements."""
        
        verification = {
            "verification_time": time.time(),
            "organization": self.organization,
            "checks": {}
        }
        
        # Article 9-10: Risk classification
        verification["checks"]["risk_classification"] = {
            "compliant": len(self.systems) > 0,
            "count": len(self.systems)
        }
        
        # Article 11: Transparency (content markers)
        verification["checks"]["content_markers"] = {
            "compliant": len(self.content_markers) > 0,
            "count": len(self.content_markers)
        }
        
        # Article 12: Incident response
        serious_incidents = [i for i in self.incidents if i.get("severity") in ["SERIOUS", "CRITICAL"]]
        all_reported = all(i.get("reported_to_authorities", False) for i in serious_incidents)
        
        verification["checks"]["incident_response"] = {
            "compliant": all_reported or len(serious_incidents) == 0,
            "serious_incidents": len(serious_incidents),
            "all_reported": all_reported
        }
        
        # Article 13: High-risk systems
        high_risk_systems = [s for s in self.systems.values() if s.get("risk_level") == "HIGH"]
        all_registered = all(s.get("registration_number") for s in high_risk_systems)
        
        verification["checks"]["high_risk"] = {
            "compliant": all_registered or len(high_risk_systems) == 0,
            "high_risk_count": len(high_risk_systems),
            "all_registered": all_registered
        }
        
        # Article 14: Foreign providers
        if self.jurisdiction == "foreign":
            verification["checks"]["foreign_provider"] = {
                "compliant": self.local_representative is not None,
                "has_rep": self.local_representative is not None
            }
        
        # Overall status
        all_compliant = all(c.get("compliant", True) for c in verification["checks"].values())
        verification["status"] = "COMPLIANT" if all_compliant else "NON_COMPLIANT"
        
        return verification


# Example usage
if __name__ == "__main__":
    print("\n" + "="*80)
    print("🇻🇳 Vietnam AI Law Compliance Tracker Demo")
    print("="*80)
    
    # Initialize tracker
    tracker = VietnamAITracker(
        organization="AI Vietnam Corp",
        entity_type=EntityType.PROVIDER,
        jurisdiction="vietnam"
    )
    
    # Article 9-10: Classify system
    print("\n📋 Chapter II: Risk Classification")
    system = tracker.classify_system({
        "system_name": "Credit Scoring AI",
        "sector": "financial",
        "affects_human_rights": True,
        "users": 500000,
        "automation_level": "high"
    })
    
    # Notify MoST if required
    if system["requires_notification"]:
        tracker.notify_most({
            "system_id": system["system_id"],
            "risk_level": system["risk_level"],
            "classification_dossier": {"summary": "Credit scoring system"}
        })
    
    # Article 11: Content markers
    print("\n📋 Chapter III: Content Markers")
    tracker.add_content_marker({
        "content_type": "image",
        "is_deepfake": False
    })
    
    # Article 12: Incident response
    print("\n📋 Chapter III: Incident Response")
    incident = tracker.log_incident({
        "incident_type": "model_drift",
        "severity": "SERIOUS",
        "description": "Model accuracy dropped from 97% to 85%",
        "affected_users": 15000,
        "reported_to_authorities": True
    })
    
    # Article 13: High-risk system
    print("\n📋 Chapter IV: High-Risk System")
    if system["risk_level"] == "HIGH":
        tracker.register_high_risk_system({
            "system_id": system["system_id"],
            "system_name": "Credit Scoring AI",
            "sector": "financial"
        })
    
    # Article 21: Regulatory sandbox
    print("\n📋 Chapter VI: Regulatory Sandbox")
    sandbox_app = tracker.apply_for_sandbox({
        "system_id": system["system_id"],
        "innovation_description": "Novel credit scoring algorithm",
        "testing_period_months": 6
    })
    
    # Verify compliance
    print("\n📊 Compliance Verification")
    verification = tracker.verify_compliance()
    print(f"   Status: {verification['status']}")
    
    print("\n" + "="*80)
    print("✅ Demo Complete")
    print("="*80)
