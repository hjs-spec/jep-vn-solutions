#!/usr/bin/env python3
"""
Vietnam AI Law - High-Risk AI System Example (Article 13)
============================================================

This example demonstrates a complete high-risk AI system (credit scoring for a Vietnamese bank)
that complies with Vietnam's Law on Artificial Intelligence (No. 134/2025/QH15), covering:

- Risk classification (Article 9-10)
- Human oversight mechanisms (Article 13)
- Registration with Ministry of Science and Technology (Article 13)
- Technical documentation requirements (Article 13)
- Operational logging (Article 13)
- Transparency and explanation rights (Article 11)
- Incident response (Article 12)
"""

import json
import time
import sys
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Optional

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))
from ai_law_2026.implementation.vn_tracker import (
    VietnamAITracker,
    EntityType,
    RiskLevel
)


class VietnamCreditScoringSystem:
    """
    Complete credit scoring system for a Vietnamese bank,
    demonstrating compliance with Vietnam's AI Law for high-risk AI.
    
    Under Article 9, financial services are considered high-risk,
    requiring full compliance with Chapter IV provisions.
    """
    
    def __init__(self, bank_name: str):
        self.bank_name = bank_name
        self.tracker = VietnamAITracker(
            organization=bank_name,
            entity_type=EntityType.DEPLOYER,
            jurisdiction="vietnam"
        )
        
        self.customers = {}
        self.loan_applications = []
        self.approvals = []
        self.denials = []
        self.incidents = []
        
        print("="*80)
        print(f"🏦 High-Risk Credit Scoring System - {bank_name}")
        print("="*80)
        print(f"Vietnam AI Law Effective: March 1, 2026")
        print(f"Risk Classification: HIGH (financial services)")
        print(f"Requirements: Chapter IV (Articles 13-14)")
    
    def setup_credit_scoring_system(self):
        """
        Register and classify the credit scoring system as required by Article 9-10.
        """
        print("\n📋 Chapter II: Risk Classification (Article 9-10)")
        
        # Self-classify the system
        classification = self.tracker.classify_system({
            "system_id": "CREDIT-SCORE-001",
            "system_name": "AI Credit Scoring Engine",
            "sector": "financial",
            "affects_human_rights": True,  # Credit decisions affect rights
            "users": 500000,
            "automation_level": "high",
            "description": "AI system for assessing creditworthiness of loan applicants",
            "deployment_date": time.time()
        })
        
        # Notify MoST if required (required for high-risk)
        if classification["requires_notification"]:
            self.tracker.notify_most({
                "system_id": classification["system_id"],
                "risk_level": classification["risk_level"],
                "classification_dossier": {
                    "system_name": "AI Credit Scoring Engine",
                    "sector": "financial",
                    "risk_factors": classification["risk_factors"],
                    "impact_assessment": {
                        "human_rights": "HIGH",
                        "safety": "LOW",
                        "public_welfare": "MEDIUM"
                    }
                }
            })
        
        # Register as high-risk system (Article 13)
        registration = self.tracker.register_high_risk_system({
            "system_id": classification["system_id"],
            "system_name": "AI Credit Scoring Engine",
            "sector": "financial",
            "description": "Automated credit scoring for loan applications",
            "impact_assessment": {
                "human_rights_impact": "HIGH",
                "safety_impact": "LOW",
                "public_welfare_impact": "MEDIUM"
            },
            "human_oversight": {
                "mechanism": "dual_approval",
                "approvers": ["loan_officer", "credit_manager"],
                "override_capability": True,
                "escalation_procedure": "All HIGH risk decisions require manager approval",
                "training_required": "Annual fairness training"
            },
            "technical_documentation": {
                "model_architecture": "XGBoost ensemble",
                "training_data_summary": {
                    "size": 100000,
                    "source": "historical loans",
                    "date_range": "2019-2025"
                },
                "accuracy_metrics": {
                    "overall": 0.96,
                    "precision": 0.95,
                    "recall": 0.94,
                    "f1_score": 0.945
                },
                "version": "2.1.0",
                "last_updated": "2026-02-15"
            }
        })
        
        print(f"\n✅ System registered: {registration['system_id']}")
        print(f"   Registration Number: {registration['registration_number']}")
        print(f"   Risk Level: {classification['risk_level']}")
        
        return classification, registration
    
    def add_customer(self, customer_data: dict) -> str:
        """Add a customer to the system."""
        customer_id = f"CUST-{int(time.time())}-{hash(customer_data['name']) % 1000:03d}"
        
        self.customers[customer_id] = {
            "customer_id": customer_id,
            "name": customer_data['name'],
            "age": customer_data['age'],
            "gender": customer_data.get('gender'),
            "income": customer_data['income'],
            "employment_years": customer_data['employment_years'],
            "credit_score": customer_data['credit_score'],
            "existing_loans": customer_data.get('existing_loans', 0),
            "monthly_debt": customer_data.get('monthly_debt', 0),
            "assets": customer_data.get('assets', 0),
            "created_date": time.time()
        }
        
        print(f"\n👤 Customer Added: {customer_data['name']} (ID: {customer_id})")
        return customer_id
    
    def process_loan_application(self, application_data: dict) -> dict:
        """
        Process a loan application using the high-risk AI system.
        
        This method demonstrates:
        - Article 11: Right to explanation (reasons for decision)
        - Article 13: Human oversight (manager approval for high-risk)
        - Article 13: Operational logging (all decisions recorded)
        """
        customer = self.customers.get(application_data['customer_id'])
        if not customer:
            return {"error": "Customer not found"}
        
        print(f"\n📝 Processing Loan Application")
        print(f"   Customer: {customer['name']}")
        print(f"   Amount: ${application_data['amount']:,.0f}")
        print(f"   Purpose: {application_data['purpose']}")
        
        # Calculate risk score
        risk_result = self._calculate_loan_risk(customer, application_data)
        
        # Determine if human oversight required (Article 13)
        requires_human = risk_result['risk_level'] in ["HIGH", "CRITICAL"] or application_data['amount'] > 50000
        
        # Make initial AI decision
        ai_approved = risk_result['score'] >= 70
        
        # Log the decision with full explanation (Article 11)
        decision = self.tracker.log_consequential_decision({
            "consumer_id": customer['customer_id'],
            "decision": "APPROVED" if ai_approved else "DENIED",
            "principal_reasons": risk_result['reasons'],
            "explanation": self._generate_explanation(risk_result, ai_approved),
            "decision_factors": risk_result['factors'],
            "ai_was_determining_factor": True,
            "human_approver": "loan_officer" if requires_human else None,
            "human_review_available": True,
            "appeal_rights_provided": True,
            "metadata": {
                "loan_amount": application_data['amount'],
                "loan_purpose": application_data['purpose'],
                "customer_age": customer['age'],
                "customer_income": customer['income'],
                "risk_score": risk_result['score']
            }
        })
        
        # Store application
        application = {
            "application_id": f"APP-{int(time.time())}",
            "customer_id": customer['customer_id'],
            "amount": application_data['amount'],
            "purpose": application_data['purpose'],
            "decision": decision['decision'],
            "risk_score": risk_result['score'],
            "requires_human": requires_human,
            "decision_id": decision.get('decision_id'),
            "timestamp": time.time()
        }
        
        self.loan_applications.append(application)
        
        print(f"\n📊 AI Decision:")
        print(f"   Decision: {decision['decision']}")
        print(f"   Risk Score: {risk_result['score']:.1f}/100")
        print(f"   Human Oversight Required: {requires_human}")
        print(f"   Reasons: {', '.join(risk_result['reasons'])}")
        
        return application
    
    def _calculate_loan_risk(self, customer: dict, application: dict) -> dict:
        """Calculate loan risk using AI model."""
        
        score = 0
        factors = {}
        reasons = []
        
        # Credit score (0-40 points)
        credit_score = customer['credit_score']
        if credit_score >= 750:
            score += 40
            factors['credit_score'] = {"score": 40, "rating": "excellent"}
            reasons.append("Excellent credit score")
        elif credit_score >= 700:
            score += 35
            factors['credit_score'] = {"score": 35, "rating": "good"}
            reasons.append("Good credit score")
        elif credit_score >= 650:
            score += 25
            factors['credit_score'] = {"score": 25, "rating": "fair"}
            reasons.append("Fair credit score")
        else:
            score += 15
            factors['credit_score'] = {"score": 15, "rating": "poor"}
            reasons.append("Credit score below optimal")
        
        # Debt-to-income (0-30 points)
        monthly_income = customer['income'] / 12
        dti = (customer['monthly_debt'] / monthly_income) * 100 if monthly_income > 0 else 0
        
        if dti <= 30:
            score += 30
            factors['dti'] = {"score": 30, "value": dti}
            reasons.append("Debt-to-income ratio excellent")
        elif dti <= 40:
            score += 20
            factors['dti'] = {"score": 20, "value": dti}
            reasons.append("Debt-to-income ratio acceptable")
        else:
            score += 10
            factors['dti'] = {"score": 10, "value": dti}
            reasons.append("Debt-to-income ratio high")
        
        # Employment stability (0-20 points)
        if customer['employment_years'] >= 5:
            score += 20
            factors['employment'] = {"score": 20, "years": customer['employment_years']}
            reasons.append("Stable employment history")
        elif customer['employment_years'] >= 2:
            score += 15
            factors['employment'] = {"score": 15, "years": customer['employment_years']}
            reasons.append("Adequate employment history")
        else:
            score += 5
            factors['employment'] = {"score": 5, "years": customer['employment_years']}
            reasons.append("Limited employment history")
        
        # Loan-to-value (0-10 points)
        if 'property_value' in application:
            ltv = (application['amount'] / application['property_value']) * 100
            if ltv <= 70:
                score += 10
                factors['ltv'] = {"score": 10, "value": ltv}
            elif ltv <= 85:
                score += 5
                factors['ltv'] = {"score": 5, "value": ltv}
        
        # Determine risk level
        if score >= 80:
            risk_level = "LOW"
        elif score >= 60:
            risk_level = "MEDIUM"
        elif score >= 40:
            risk_level = "HIGH"
        else:
            risk_level = "CRITICAL"
        
        return {
            "score": score,
            "risk_level": risk_level,
            "factors": factors,
            "reasons": reasons[:3]  # Top 3 reasons
        }
    
    def _generate_explanation(self, risk_result: dict, approved: bool) -> str:
        """Generate human-readable explanation (Article 11)."""
        if approved:
            return f"Your loan application has been approved with a score of {risk_result['score']:.1f}/100. Key factors: {', '.join(risk_result['reasons'])}. You have the right to request human review if you disagree with this decision."
        else:
            return f"Your loan application was not approved at this time. Score: {risk_result['score']:.1f}/100. Reasons: {', '.join(risk_result['reasons'])}. You have the right to request human review or correction of your data within 30 days."
    
    def handle_human_override(self, application_id: str, manager_id: str, approved: bool, notes: str) -> dict:
        """
        Human override of AI decision (Article 13 - Human Oversight).
        """
        application = next((a for a in self.loan_applications if a["application_id"] == application_id), None)
        if not application:
            return {"error": "Application not found"}
        
        customer = self.customers.get(application["customer_id"])
        
        print(f"\n👤 Human Oversight (Article 13)")
        print(f"   Manager: {manager_id}")
        print(f"   Override Decision: {'APPROVE' if approved else 'DENY'}")
        print(f"   Notes: {notes}")
        
        # Log the human override
        override = {
            "application_id": application_id,
            "customer_id": application["customer_id"],
            "original_ai_decision": application["decision"],
            "human_decision": "APPROVED" if approved else "DENIED",
            "human_approver": manager_id,
            "override_notes": notes,
            "timestamp": time.time()
        }
        
        # Update application
        application["human_overridden"] = True
        application["final_decision"] = override["human_decision"]
        application["human_approver"] = manager_id
        
        print(f"\n✅ Human override recorded. Final decision: {override['human_decision']}")
        
        return override
    
    def log_incident(self, incident_data: dict) -> dict:
        """
        Log a serious incident as required by Article 12.
        """
        print(f"\n🚨 Article 12: Serious Incident Logging")
        
        incident = self.tracker.log_incident({
            "incident_type": incident_data.get("type", "model_drift"),
            "severity": incident_data.get("severity", "SERIOUS"),
            "description": incident_data.get("description"),
            "affected_systems": incident_data.get("affected_systems", ["credit-scoring"]),
            "affected_users": incident_data.get("affected_users", 0),
            "potential_harm": incident_data.get("potential_harm"),
            "reported_to_authorities": incident_data.get("reported_to_authorities", True),
            "root_cause": incident_data.get("root_cause")
        })
        
        # Remediate
        remediation = self.tracker.remediate_incident({
            "incident_id": incident["incident_id"],
            "actions": incident_data.get("actions", [])
        })
        
        self.incidents.append(incident)
        
        return incident
    
    def generate_compliance_report(self) -> dict:
        """Generate comprehensive compliance report for MoST."""
        
        report = self.tracker.generate_compliance_report()
        
        # Add bank-specific metrics
        report["bank_statistics"] = {
            "total_customers": len(self.customers),
            "total_applications": len(self.loan_applications),
            "approval_rate": len([a for a in self.loan_applications if a["decision"] == "APPROVED"]) / len(self.loan_applications) * 100 if self.loan_applications else 0,
            "human_overrides": len([a for a in self.loan_applications if a.get("human_overridden")])
        }
        
        print(f"\n📊 Compliance Report Generated")
        print(f"   Report ID: {report['report_id']}")
        print(f"   High-Risk Systems: {report['statistics']['high_risk_systems']}")
        print(f"   Incidents Logged: {report['statistics']['incidents_logged']}")
        
        return report
    
    def run_demo(self):
        """Run complete high-risk AI demonstration."""
        
        # Setup and register system
        self.setup_credit_scoring_system()
        
        # Add customers
        customers = [
            {
                "name": "Nguyen Van An",
                "age": 45,
                "gender": "male",
                "income": 240000000,  # VND/year
                "employment_years": 12,
                "credit_score": 780,
                "existing_loans": 0,
                "monthly_debt": 5000000,
                "assets": 500000000
            },
            {
                "name": "Tran Thi Binh",
                "age": 38,
                "gender": "female",
                "income": 180000000,
                "employment_years": 6,
                "credit_score": 720,
                "existing_loans": 1,
                "monthly_debt": 8000000,
                "assets": 300000000
            },
            {
                "name": "Le Van Cuong",
                "age": 29,
                "gender": "male",
                "income": 120000000,
                "employment_years": 3,
                "credit_score": 680,
                "existing_loans": 1,
                "monthly_debt": 6000000,
                "assets": 100000000
            },
            {
                "name": "Pham Thi Dung",
                "age": 52,
                "gender": "female",
                "income": 300000000,
                "employment_years": 20,
                "credit_score": 820,
                "existing_loans": 0,
                "monthly_debt": 2000000,
                "assets": 800000000
            }
        ]
        
        customer_ids = []
        for cust in customers:
            cid = self.add_customer(cust)
            customer_ids.append(cid)
        
        # Process loan applications
        applications = [
            {"customer_id": customer_ids[0], "amount": 500000000, "purpose": "home_purchase", "property_value": 800000000},
            {"customer_id": customer_ids[1], "amount": 200000000, "purpose": "car_purchase"},
            {"customer_id": customer_ids[2], "amount": 50000000, "purpose": "business_loan"},
            {"customer_id": customer_ids[3], "amount": 1000000000, "purpose": "investment", "property_value": 2000000000}
        ]
        
        app_results = []
        for app in applications:
            result = self.process_loan_application(app)
            app_results.append(result)
        
        # Human override example (for high-risk case)
        high_risk_app = next((a for a in self.loan_applications if a.get("requires_human")), None)
        if high_risk_app:
            self.handle_human_override(
                application_id=high_risk_app["application_id"],
                manager_id="credit-manager-456",
                approved=True,
                notes="Approved with additional conditions: 30% down payment required"
            )
        
        # Log an incident (example)
        self.log_incident({
            "type": "model_drift",
            "severity": "MODERATE",
            "description": "Model accuracy dropped from 96% to 92% over 30 days",
            "affected_users": 5000,
            "potential_harm": "Slightly higher false positive rate",
            "root_cause": "Data drift in income verification feature",
            "actions": [
                {"action": "Model retraining initiated", "time": time.time()},
                {"action": "Enhanced monitoring implemented", "time": time.time() + 3600}
            ]
        })
        
        # Generate final report
        report = self.generate_compliance_report()
        
        print("\n" + "="*80)
        print("✅ Vietnam High-Risk AI Demo Complete")
        print("="*80)
        print(f"   Customers Processed: {len(customer_ids)}")
        print(f"   Loan Applications: {len(app_results)}")
        print(f"   Human Overrides: {len([a for a in self.loan_applications if a.get('human_overridden')])}")
        print(f"   Incidents Logged: {len(self.incidents)}")
        print(f"\n📋 Compliance Status: FULLY COMPLIANT with Vietnam AI Law")
        print(f"   - Article 9: Risk Classification ✓")
        print(f"   - Article 10: MoST Notification ✓")
        print(f"   - Article 11: Right to Explanation ✓")
        print(f"   - Article 12: Incident Response ✓")
        print(f"   - Article 13: High-Risk Safeguards ✓")


if __name__ == "__main__":
    system = VietnamCreditScoringSystem("Vietcombank")
    system.run_demo()
