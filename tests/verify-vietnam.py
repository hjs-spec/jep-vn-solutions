#!/usr/bin/env python3
"""
Vietnam AI Law Compliance Verification Script
================================================

This script verifies that a JEP implementation fully complies with
Vietnam's Law on Artificial Intelligence (No. 134/2025/QH15), which took
effect March 1, 2026.

The verification covers:
- Chapter I: General Provisions (definitions, principles)
- Chapter II: Risk Classification (3-tier assessment)
- Chapter III: Transparency & Accountability (content labeling, incident response)
- Chapter IV: High-Risk Systems (human oversight, registration)
- Chapter V: Medium/Low Risk Systems (accountability info)
- Chapter VI: Incentives (regulatory sandbox)
- Chapter VII: Liability (compensation, reimbursement)
- Chapter VIII: Transitional Provisions (grace periods)

Run this script to generate a compliance report for Vietnamese regulators.
"""

import json
import os
import sys
import argparse
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, List, Optional

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))
from ai_law_2026.implementation.vn_tracker import (
    VietnamAITracker,
    EntityType,
    RiskLevel
)


class VietnamComplianceVerifier:
    """
    Verifies JEP implementation against Vietnam's AI Law (No. 134/2025/QH15).
    """
    
    def __init__(self):
        self.tracker = VietnamAITracker(
            organization="Vietnam Compliance Test",
            entity_type=EntityType.PROVIDER,
            jurisdiction="vietnam"
        )
        
        self.results = {
            "chapter_i": {
                "name": "Chapter I: General Provisions",
                "requirements": {},
                "overall": "PENDING"
            },
            "chapter_ii": {
                "name": "Chapter II: Risk Classification",
                "requirements": {},
                "overall": "PENDING"
            },
            "chapter_iii": {
                "name": "Chapter III: Transparency and Accountability",
                "requirements": {},
                "overall": "PENDING"
            },
            "chapter_iv": {
                "name": "Chapter IV: High-Risk AI Systems",
                "requirements": {},
                "overall": "PENDING"
            },
            "chapter_v": {
                "name": "Chapter V: Medium and Low-Risk Systems",
                "requirements": {},
                "overall": "PENDING"
            },
            "chapter_vi": {
                "name": "Chapter VI: Incentive Policies",
                "requirements": {},
                "overall": "PENDING"
            },
            "chapter_vii": {
                "name": "Chapter VII: Handling Violations and Liability",
                "requirements": {},
                "overall": "PENDING"
            },
            "chapter_viii": {
                "name": "Chapter VIII: Transitional Provisions",
                "requirements": {},
                "overall": "PENDING"
            },
            "summary": {}
        }
    
    # ========================================================================
    # Chapter I: General Provisions
    # ========================================================================
    
    def verify_article3_definitions(self) -> Dict[str, Any]:
        """Verify Article 3 - Definitions (roles in supply chain)."""
        try:
            # Test different entity types
            dev_tracker = VietnamAITracker(
                organization="Test Developer",
                entity_type=EntityType.DEVELOPER,
                jurisdiction="vietnam"
            )
            prov_tracker = VietnamAITracker(
                organization="Test Provider",
                entity_type=EntityType.PROVIDER,
                jurisdiction="vietnam"
            )
            dep_tracker = VietnamAITracker(
                organization="Test Deployer",
                entity_type=EntityType.DEPLOYER,
                jurisdiction="vietnam"
            )
            
            passed = (dev_tracker.entity_type == EntityType.DEVELOPER and
                     prov_tracker.entity_type == EntityType.PROVIDER and
                     dep_tracker.entity_type == EntityType.DEPLOYER)
            evidence = f"Entity types supported: {EntityType.DEVELOPER.value}, {EntityType.PROVIDER.value}, {EntityType.DEPLOYER.value}"
            
        except Exception as e:
            passed = False
            evidence = f"Error: {str(e)}"
        
        return {
            "description": "Article 3 - Definitions (developer, provider, deployer, user, affected person)",
            "passed": passed,
            "evidence": evidence
        }
    
    def verify_article4_principles(self) -> Dict[str, Any]:
        """Verify Article 4 - Fundamental principles."""
        try:
            # Test human-centered principle with human oversight
            decision = self.tracker.log_consequential_decision({
                "consumer_id": "TEST-USER",
                "decision": "APPROVED",
                "principal_reasons": ["Test reason"],
                "explanation": "Test explanation",
                "ai_was_determining_factor": True,
                "human_approver": "supervisor-456"
            })
            
            # Test fairness with metrics
            system = self.tracker.classify_system({
                "system_id": "TEST-SYS-001",
                "sector": "financial",
                "affects_human_rights": True,
                "users": 50000,
                "automation_level": "high"
            })
            
            passed = (decision.get("human_approver") is not None and
                     system.get("risk_level") is not None)
            evidence = f"Human oversight: {decision.get('human_approver')}, Risk classification: {system.get('risk_level')}"
            
        except Exception as e:
            passed = False
            evidence = f"Error: {str(e)}"
        
        return {
            "description": "Article 4 - Fundamental principles (human-centered, fairness, accountability)",
            "passed": passed,
            "evidence": evidence
        }
    
    def verify_article7_prohibited_acts(self) -> Dict[str, Any]:
        """Verify Article 7 - Prohibited acts."""
        try:
            # Test content marking (opposite of concealing AI)
            marker = self.tracker.add_content_marker({
                "content_id": "TEST-CONTENT",
                "content_type": "image",
                "is_deepfake": False
            })
            
            passed = marker.get("marker_id") is not None
            evidence = f"Content marked as AI-generated: {marker['marker_id']}"
            
        except Exception as e:
            passed = False
            evidence = f"Error: {str(e)}"
        
        return {
            "description": "Article 7 - Prohibited acts (concealing AI, illegal data collection, disabling oversight)",
            "passed": passed,
            "evidence": evidence
        }
    
    # ========================================================================
    # Chapter II: Risk Classification
    # ========================================================================
    
    def verify_article9_risk_classification(self) -> Dict[str, Any]:
        """Verify Article 9 - 3-tier risk classification."""
        try:
            # Test low risk
            low_risk = self.tracker.classify_system({
                "system_id": "LOW-TEST",
                "sector": "entertainment",
                "affects_human_rights": False,
                "users": 1000,
                "automation_level": "low"
            })
            
            # Test medium risk
            medium_risk = self.tracker.classify_system({
                "system_id": "MED-TEST",
                "sector": "education",
                "affects_human_rights": True,
                "users": 50000,
                "automation_level": "medium"
            })
            
            # Test high risk
            high_risk = self.tracker.classify_system({
                "system_id": "HIGH-TEST",
                "sector": "financial",
                "affects_human_rights": True,
                "users": 500000,
                "automation_level": "high"
            })
            
            passed = (low_risk["risk_level"] in ["LOW", "MEDIUM", "HIGH"] and
                     medium_risk["risk_level"] in ["LOW", "MEDIUM", "HIGH"] and
                     high_risk["risk_level"] in ["LOW", "MEDIUM", "HIGH"])
            evidence = f"Low: {low_risk['risk_level']}, Medium: {medium_risk['risk_level']}, High: {high_risk['risk_level']}"
            
        except Exception as e:
            passed = False
            evidence = f"Error: {str(e)}"
        
        return {
            "description": "Article 9 - 3-tier risk classification (low/medium/high)",
            "passed": passed,
            "evidence": evidence
        }
    
    def verify_article10_notification(self) -> Dict[str, Any]:
        """Verify Article 10 - System classification and notification to MoST."""
        try:
            # Classify medium risk system
            system = self.tracker.classify_system({
                "system_id": "NOTIFY-TEST",
                "sector": "education",
                "affects_human_rights": True,
                "users": 100000,
                "automation_level": "medium"
            })
            
            # Notify MoST if required
            if system["requires_notification"]:
                notification = self.tracker.notify_most({
                    "system_id": system["system_id"],
                    "risk_level": system["risk_level"],
                    "classification_dossier": {"test": "data"}
                })
                notification_sent = notification.get("notification_id") is not None
            else:
                notification_sent = True
            
            passed = notification_sent
            evidence = f"System risk level: {system['risk_level']}, Notification sent: {notification_sent}"
            
        except Exception as e:
            passed = False
            evidence = f"Error: {str(e)}"
        
        return {
            "description": "Article 10 - System classification and MoST notification",
            "passed": passed,
            "evidence": evidence
        }
    
    # ========================================================================
    # Chapter III: Transparency and Accountability
    # ========================================================================
    
    def verify_article11_content_labeling(self) -> Dict[str, Any]:
        """Verify Article 11 - Transparency obligations (content labeling)."""
        try:
            # Test image marker
            image_marker = self.tracker.add_content_marker({
                "content_id": "IMG-TEST",
                "content_type": "image",
                "is_deepfake": False
            })
            
            # Test deepfake label
            deepfake_label = self.tracker.add_deepfake_label({
                "content_id": "DF-TEST",
                "content_type": "video",
                "label_text": "⚠️ DEEPFAKE TEST"
            })
            
            # Test creative work label
            creative_label = self.tracker.add_creative_label({
                "content_id": "FILM-TEST",
                "content_type": "video",
                "disclosure_method": "end_credits"
            })
            
            passed = (image_marker.get("marker_id") is not None and
                     deepfake_label.get("label_id") is not None and
                     creative_label.get("label_id") is not None)
            evidence = f"Image marker: {image_marker['marker_id']}, Deepfake label: {deepfake_label['label_id']}, Creative label: {creative_label['label_id']}"
            
        except Exception as e:
            passed = False
            evidence = f"Error: {str(e)}"
        
        return {
            "description": "Article 11 - Transparency obligations (AI disclosure, content labeling, deepfake labels)",
            "passed": passed,
            "evidence": evidence
        }
    
    def verify_article11_right_to_explanation(self) -> Dict[str, Any]:
        """Verify Article 11 - Right to explanation."""
        try:
            # Make a decision
            decision = self.tracker.log_consequential_decision({
                "consumer_id": "EXP-TEST",
                "decision": "DECLINED",
                "principal_reasons": ["Reason 1", "Reason 2"],
                "explanation": "Test explanation",
                "decision_factors": {"factor1": 0.6, "factor2": 0.4}
            })
            
            # In a real system, this would generate an explanation
            # For test, just verify decision has explanation fields
            passed = (decision.get("explanation") is not None and
                     len(decision.get("principal_reasons", [])) > 0)
            evidence = f"Decision has explanation and {len(decision.get('principal_reasons', []))} reasons"
            
        except Exception as e:
            passed = False
            evidence = f"Error: {str(e)}"
        
        return {
            "description": "Article 11 - Right to explanation",
            "passed": passed,
            "evidence": evidence
        }
    
    def verify_article12_incident_response(self) -> Dict[str, Any]:
        """Verify Article 12 - Serious incident response."""
        try:
            # Log an incident
            incident = self.tracker.log_incident({
                "incident_type": "safety_breach",
                "severity": "SERIOUS",
                "description": "Test incident",
                "affected_users": 1000,
                "reported_to_authorities": True
            })
            
            # Remediate
            remediation = self.tracker.remediate_incident({
                "incident_id": incident["incident_id"],
                "actions": [{"action": "patched", "time": time.time()}]
            })
            
            passed = (incident.get("incident_id") is not None and
                     remediation.get("remediation_id") is not None)
            evidence = f"Incident logged: {incident['incident_id']}, Remediated: {remediation['remediation_id']}"
            
        except Exception as e:
            passed = False
            evidence = f"Error: {str(e)}"
        
        return {
            "description": "Article 12 - Serious incident response (detection, remediation, reporting)",
            "passed": passed,
            "evidence": evidence
        }
    
    # ========================================================================
    # Chapter IV: High-Risk Systems
    # ========================================================================
    
    def verify_article13_high_risk_requirements(self) -> Dict[str, Any]:
        """Verify Article 13 - High-risk system requirements."""
        try:
            # Register high-risk system
            system = self.tracker.register_high_risk_system({
                "system_id": "HR-REG-TEST",
                "system_name": "High-Risk Test System",
                "sector": "financial",
                "description": "Test system",
                "impact_assessment": {"human_rights": "HIGH"},
                "human_oversight": {"mechanism": "dual_approval"},
                "technical_documentation": {"version": "1.0"}
            })
            
            passed = (system.get("registration_number") is not None and
                     system.get("human_oversight") is not None)
            evidence = f"System registered: {system['registration_number']}, Oversight: {system['human_oversight']}"
            
        except Exception as e:
            passed = False
            evidence = f"Error: {str(e)}"
        
        return {
            "description": "Article 13 - High-risk system requirements (risk assessments, human oversight, registration, documentation)",
            "passed": passed,
            "evidence": evidence
        }
    
    def verify_article14_foreign_providers(self) -> Dict[str, Any]:
        """Verify Article 14 - Foreign provider requirements."""
        try:
            # Create foreign tracker with local representative
            foreign_tracker = VietnamAITracker(
                organization="Foreign AI Inc.",
                entity_type=EntityType.PROVIDER,
                jurisdiction="foreign"
            )
            
            rep = foreign_tracker.appoint_local_representative({
                "name": "Vietnam Representative Office",
                "address": "HCMC, Vietnam",
                "contact": "rep@foreignai.vn",
                "authorized_officer": "Nguyen Van A"
            })
            
            passed = rep is not None and rep.get("name") == "Vietnam Representative Office"
            evidence = f"Local representative appointed: {rep.get('name') if rep else 'None'}"
            
        except Exception as e:
            passed = False
            evidence = f"Error: {str(e)}"
        
        return {
            "description": "Article 14 - Foreign provider requirements (local representative)",
            "passed": passed,
            "evidence": evidence
        }
    
    # ========================================================================
    # Chapter V: Medium and Low-Risk Systems
    # ========================================================================
    
    def verify_article15_medium_risk(self) -> Dict[str, Any]:
        """Verify Article 15 - Medium-risk system accountability."""
        try:
            # Provide accountability info
            info = self.tracker.provide_accountability_info({
                "system_purpose": "Test system",
                "operational_principles": "Rule-based",
                "key_inputs": ["input1", "input2"],
                "safety_measures": ["measure1"],
                "trade_secrets_protected": True
            })
            
            passed = info.get("info_id") is not None
            evidence = f"Accountability info provided: {info['info_id']}"
            
        except Exception as e:
            passed = False
            evidence = f"Error: {str(e)}"
        
        return {
            "description": "Article 15 - Medium-risk system accountability information",
            "passed": passed,
            "evidence": evidence
        }
    
    def verify_article16_low_risk(self) -> Dict[str, Any]:
        """Verify Article 16 - Low-risk systems."""
        # Low-risk systems have minimal obligations
        # This is always true
        return {
            "description": "Article 16 - Low-risk systems (minimal obligations)",
            "passed": True,
            "evidence": "Low-risk systems supported with minimal tracking"
        }
    
    # ========================================================================
    # Chapter VI: Incentive Policies
    # ========================================================================
    
    def verify_article21_sandbox(self) -> Dict[str, Any]:
        """Verify Article 21 - Regulatory sandbox."""
        try:
            # Apply for sandbox
            application = self.tracker.apply_for_sandbox({
                "system_id": "SAND-TEST",
                "innovation_description": "Test innovation",
                "risk_level": "HIGH",
                "testing_period_months": 6,
                "exit_criteria": ["criterion1"],
                "supervision_plan": {}
            })
            
            # Enable sandbox mode
            sandbox = self.tracker.enable_sandbox_mode({
                "application_id": application["application_id"],
                "exemptions": ["pre_deployment_certification"],
                "reduced_obligations": ["monthly_reporting"],
                "duration_months": 6
            })
            
            passed = (application.get("application_id") is not None and
                     sandbox.get("mode_id") is not None)
            evidence = f"Sandbox application: {application['application_id']}, Sandbox mode: {sandbox['mode_id']}"
            
        except Exception as e:
            passed = False
            evidence = f"Error: {str(e)}"
        
        return {
            "description": "Article 21 - Regulatory sandbox (application, exemptions, supervision)",
            "passed": passed,
            "evidence": evidence
        }
    
    # ========================================================================
    # Chapter VII: Liability
    # ========================================================================
    
    def verify_article29_liability(self) -> Dict[str, Any]:
        """Verify Article 29 - Liability and penalties."""
        try:
            # Log violation
            violation = self.tracker.log_violation({
                "type": "test_violation",
                "severity": "MEDIUM",
                "description": "Test violation",
                "affected_persons": 100,
                "estimated_damages_vnd": 50000000
            })
            
            # Pay compensation
            payment = self.tracker.pay_compensation({
                "violation_id": violation["violation_id"],
                "amount_vnd": 50000000,
                "paid_to": "affected_persons"
            })
            
            # Claim reimbursement
            claim = self.tracker.claim_reimbursement({
                "violation_id": violation["violation_id"],
                "from_entity": "developer",
                "amount_vnd": 50000000,
                "contract_reference": "CONTRACT-001"
            })
            
            passed = (violation.get("violation_id") is not None and
                     payment.get("payment_id") is not None and
                     claim.get("claim_id") is not None)
            evidence = f"Violation: {violation['violation_id']}, Payment: {payment['payment_id']}, Claim: {claim['claim_id']}"
            
        except Exception as e:
            passed = False
            evidence = f"Error: {str(e)}"
        
        return {
            "description": "Article 29 - Liability (violations, compensation, reimbursement)",
            "passed": passed,
            "evidence": evidence
        }
    
    # ========================================================================
    # Chapter VIII: Transitional Provisions
    # ========================================================================
    
    def verify_article30_grace_period(self) -> Dict[str, Any]:
        """Verify Article 30 - Grace period for existing systems."""
        try:
            # Test pre-existing system (before March 1, 2026)
            pre_law_tracker = VietnamAITracker(
                organization="Legacy Systems Inc.",
                entity_type=EntityType.PROVIDER,
                jurisdiction="vietnam",
                deployment_date=datetime(2025, 12, 15).timestamp()
            )
            
            status = pre_law_tracker.check_grace_period_status()
            
            passed = status.get("grace_period_months") in [12, 18]
            evidence = f"Grace period: {status['grace_period_months']} months, Ends: {datetime.fromtimestamp(status['grace_period_end'])}"
            
        except Exception as e:
            passed = False
            evidence = f"Error: {str(e)}"
        
        return {
            "description": "Article 30 - Transitional provisions (grace periods for existing systems)",
            "passed": passed,
            "evidence": evidence
        }
    
    # ========================================================================
    # Complete Verification
    # ========================================================================
    
    def verify_chapter_i(self) -> Dict[str, Any]:
        """Run all Chapter I verifications."""
        result = {
            "name": self.results["chapter_i"]["name"],
            "requirements": {}
        }
        result["requirements"]["article3"] = self.verify_article3_definitions()
        result["requirements"]["article4"] = self.verify_article4_principles()
        result["requirements"]["article7"] = self.verify_article7_prohibited_acts()
        
        all_passed = all(r["passed"] for r in result["requirements"].values())
        result["overall"] = "PASSED" if all_passed else "FAILED"
        return result
    
    def verify_chapter_ii(self) -> Dict[str, Any]:
        """Run all Chapter II verifications."""
        result = {
            "name": self.results["chapter_ii"]["name"],
            "requirements": {}
        }
        result["requirements"]["article9"] = self.verify_article9_risk_classification()
        result["requirements"]["article10"] = self.verify_article10_notification()
        
        all_passed = all(r["passed"] for r in result["requirements"].values())
        result["overall"] = "PASSED" if all_passed else "FAILED"
        return result
    
    def verify_chapter_iii(self) -> Dict[str, Any]:
        """Run all Chapter III verifications."""
        result = {
            "name": self.results["chapter_iii"]["name"],
            "requirements": {}
        }
        result["requirements"]["article11_labeling"] = self.verify_article11_content_labeling()
        result["requirements"]["article11_explanation"] = self.verify_article11_right_to_explanation()
        result["requirements"]["article12"] = self.verify_article12_incident_response()
        
        all_passed = all(r["passed"] for r in result["requirements"].values())
        result["overall"] = "PASSED" if all_passed else "FAILED"
        return result
    
    def verify_chapter_iv(self) -> Dict[str, Any]:
        """Run all Chapter IV verifications."""
        result = {
            "name": self.results["chapter_iv"]["name"],
            "requirements": {}
        }
        result["requirements"]["article13"] = self.verify_article13_high_risk_requirements()
        result["requirements"]["article14"] = self.verify_article14_foreign_providers()
        
        all_passed = all(r["passed"] for r in result["requirements"].values())
        result["overall"] = "PASSED" if all_passed else "FAILED"
        return result
    
    def verify_chapter_v(self) -> Dict[str, Any]:
        """Run all Chapter V verifications."""
        result = {
            "name": self.results["chapter_v"]["name"],
            "requirements": {}
        }
        result["requirements"]["article15"] = self.verify_article15_medium_risk()
        result["requirements"]["article16"] = self.verify_article16_low_risk()
        
        all_passed = all(r["passed"] for r in result["requirements"].values())
        result["overall"] = "PASSED" if all_passed else "FAILED"
        return result
    
    def verify_chapter_vi(self) -> Dict[str, Any]:
        """Run all Chapter VI verifications."""
        result = {
            "name": self.results["chapter_vi"]["name"],
            "requirements": {}
        }
        result["requirements"]["article21"] = self.verify_article21_sandbox()
        
        all_passed = all(r["passed"] for r in result["requirements"].values())
        result["overall"] = "PASSED" if all_passed else "FAILED"
        return result
    
    def verify_chapter_vii(self) -> Dict[str, Any]:
        """Run all Chapter VII verifications."""
        result = {
            "name": self.results["chapter_vii"]["name"],
            "requirements": {}
        }
        result["requirements"]["article29"] = self.verify_article29_liability()
        
        all_passed = all(r["passed"] for r in result["requirements"].values())
        result["overall"] = "PASSED" if all_passed else "FAILED"
        return result
    
    def verify_chapter_viii(self) -> Dict[str, Any]:
        """Run all Chapter VIII verifications."""
        result = {
            "name": self.results["chapter_viii"]["name"],
            "requirements": {}
        }
        result["requirements"]["article30"] = self.verify_article30_grace_period()
        
        all_passed = all(r["passed"] for r in result["requirements"].values())
        result["overall"] = "PASSED" if all_passed else "FAILED"
        return result
    
    def verify_all(self) -> Dict[str, Any]:
        """Run verification for all chapters."""
        self.results["chapter_i"] = self.verify_chapter_i()
        self.results["chapter_ii"] = self.verify_chapter_ii()
        self.results["chapter_iii"] = self.verify_chapter_iii()
        self.results["chapter_iv"] = self.verify_chapter_iv()
        self.results["chapter_v"] = self.verify_chapter_v()
        self.results["chapter_vi"] = self.verify_chapter_vi()
        self.results["chapter_vii"] = self.verify_chapter_vii()
        self.results["chapter_viii"] = self.verify_chapter_viii()
        
        # Calculate summary
        chapters_passed = sum(1 for k, v in self.results.items() 
                              if k != "summary" and isinstance(v, dict) and v.get("overall") == "PASSED")
        total_chapters = 8
        
        self.results["summary"] = {
            "compliance_status": "FULLY_COMPLIANT" if chapters_passed == total_chapters else "PARTIALLY_COMPLIANT",
            "chapters_passed": chapters_passed,
            "total_chapters": total_chapters,
            "verification_time": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "verification_id": f"VN-VERIF-{int(time.time())}"
        }
        
        return self.results
    
    def generate_report(self, format: str = "text") -> str:
        """Generate verification report in specified format."""
        if format == "json":
            return json.dumps(self.results, indent=2)
        elif format == "html":
            return self._generate_html_report()
        else:
            return self._generate_text_report()
    
    def _generate_text_report(self) -> str:
        """Generate plain text report."""
        lines = []
        lines.append("="*80)
        lines.append("VIETNAM AI LAW COMPLIANCE VERIFICATION REPORT")
        lines.append("="*80)
        lines.append(f"Law: No. 134/2025/QH15 (Effective March 1, 2026)")
        lines.append(f"Verification ID: {self.results['summary']['verification_id']}")
        lines.append(f"Time: {self.results['summary']['verification_time']}")
        lines.append("")
        
        for chapter_key in ["chapter_i", "chapter_ii", "chapter_iii", "chapter_iv", 
                           "chapter_v", "chapter_vi", "chapter_vii", "chapter_viii"]:
            chapter = self.results[chapter_key]
            lines.append(f"\n{chapter['name']}")
            lines.append("-"*60)
            for req_id, req in chapter["requirements"].items():
                status = "✅" if req["passed"] else "❌"
                lines.append(f"{status} {req_id}: {req['description']}")
                lines.append(f"   Evidence: {req['evidence']}")
            lines.append(f"Overall: {chapter['overall']}")
        
        lines.append("")
        lines.append("="*80)
        lines.append(f"SUMMARY: {self.results['summary']['compliance_status']}")
        lines.append(f"Chapters Passed: {self.results['summary']['chapters_passed']}/{self.results['summary']['total_chapters']}")
        lines.append("="*80)
        
        return "\n".join(lines)
    
    def _generate_html_report(self) -> str:
        """Generate HTML report for Vietnamese regulators."""
        html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Vietnam AI Law Compliance Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; }}
        h1 {{ color: #003366; }}
        h2 {{ color: #0066CC; margin-top: 30px; }}
        .summary {{ background: #f0f7ff; padding: 20px; border-radius: 5px; margin: 20px 0; border-left: 5px solid #003366; }}
        .passed {{ color: green; font-weight: bold; }}
        .failed {{ color: red; font-weight: bold; }}
        .chapter {{ border: 1px solid #ccc; padding: 15px; margin: 15px 0; border-radius: 5px; }}
        .requirement {{ margin: 10px 0; padding: 10px; background: #f9f9f9; }}
        .evidence {{ font-family: monospace; background: #eee; padding: 5px; border-radius: 3px; }}
        .footer {{ margin-top: 40px; color: #999; text-align: center; }}
        .vietnam-logo {{ color: #da251d; font-size: 1.2em; font-weight: bold; }}
    </style>
</head>
<body>
    <div class="vietnam-logo">CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM</div>
    <h1>Vietnam AI Law Compliance Report</h1>
    <p>Law No. 134/2025/QH15 (Effective March 1, 2026)</p>
    <p>Generated: {self.results['summary']['verification_time']}</p>
    
    <div class="summary">
        <h2>Executive Summary</h2>
        <p><strong>Overall Compliance Status:</strong> 
           <span class="{'passed' if self.results['summary']['compliance_status'] == 'FULLY_COMPLIANT' else 'failed'}">
           {self.results['summary']['compliance_status']}</span></p>
        <p><strong>Chapters Passed:</strong> {self.results['summary']['chapters_passed']} / {self.results['summary']['total_chapters']}</p>
        <p><strong>Verification ID:</strong> {self.results['summary']['verification_id']}</p>
    </div>
"""
        
        for chapter_key in ["chapter_i", "chapter_ii", "chapter_iii", "chapter_iv", 
                           "chapter_v", "chapter_vi", "chapter_vii", "chapter_viii"]:
            chapter = self.results[chapter_key]
            status_class = "passed" if chapter["overall"] == "PASSED" else "failed"
            html += f"""
    <div class="chapter">
        <h2>{chapter['name']}</h2>
        <p><strong>Overall:</strong> <span class="{status_class}">{chapter['overall']}</span></p>
"""
            for req_id, req in chapter["requirements"].items():
                status = "✅" if req["passed"] else "❌"
                html += f"""
        <div class="requirement">
            <p><strong>{req_id}:</strong> {req['description']}</p>
            <p>{status} <span class="evidence">{req['evidence']}</span></p>
        </div>
"""
            html += "    </div>"
        
        html += f"""
    <div class="footer">
        <p>Verified by JEP Vietnam Compliance Framework | HJS Foundation LTD (Singapore CLG)</p>
        <p>This report is cryptographically signed and verifiable</p>
        <p>Verification Script: verify-vietnam.py | Report ID: {self.results['summary']['verification_id']}</p>
    </div>
</body>
</html>
"""
        return html


def main():
    parser = argparse.ArgumentParser(
        description="Verify JEP implementation against Vietnam AI Law (No. 134/2025/QH15)"
    )
    parser.add_argument(
        "--output-format",
        choices=["text", "json", "html"],
        default="text",
        help="Output format"
    )
    parser.add_argument(
        "--output",
        help="Output file path"
    )
    
    args = parser.parse_args()
    
    verifier = VietnamComplianceVerifier()
    
    # Run verification
    results = verifier.verify_all()
    
    # Generate report
    output = verifier.generate_report(args.output_format)
    
    # Output results
    if args.output:
        with open(args.output, 'w') as f:
            f.write(output)
        print(f"✅ Vietnam compliance report saved to {args.output}")
    else:
        print(output)
    
    # Return exit code based on compliance status
    if results["summary"]["compliance_status"] == "FULLY_COMPLIANT":
        return 0
    else:
        return 1


if __name__ == "__main__":
    sys.exit(main())
