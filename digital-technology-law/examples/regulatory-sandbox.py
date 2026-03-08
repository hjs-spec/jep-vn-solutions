#!/usr/bin/env python3
"""
Vietnam Digital Technology Industry Law - Regulatory Sandbox Example (Article 21)
====================================================================================

This example demonstrates the Regulatory Sandbox mechanism under Vietnam's
Digital Technology Industry Law (No. 71/2025/QH15), which allows high-risk AI
systems to test in a controlled environment with reduced compliance obligations.

The sandbox enables:
- Testing innovative AI systems with real users
- Exemption from certain compliance requirements
- Supervised by Ministry of Science and Technology
- Time-limited (typically 6-12 months)
- Clear exit criteria for graduation or termination
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


class VietnamRegulatorySandbox:
    """
    Complete demonstration of Vietnam's AI Regulatory Sandbox under Article 21
    of the Digital Technology Industry Law.
    
    Features:
    - Sandbox application process
    - Exemption from standard compliance requirements
    - Supervised testing environment
    - Monthly reporting to MoST
    - Clear graduation/termination criteria
    """
    
    def __init__(self, company_name: str):
        self.company_name = company_name
        self.tracker = VietnamAITracker(
            organization=company_name,
            entity_type=EntityType.DEVELOPER,
            jurisdiction="vietnam"
        )
        
        self.sandbox_applications = []
        self.active_sandboxes = []
        self.completed_sandboxes = []
        self.sandbox_reports = []
        self.sandbox_incidents = []
        
        print("="*80)
        print(f"🧪 Vietnam Regulatory Sandbox System - {company_name}")
        print("="*80)
        print(f"Digital Technology Industry Law: No. 71/2025/QH15")
        print(f"Article 21: Regulatory Sandbox for High-Risk AI")
        print(f"Effective: March 1, 2026")
    
    def apply_for_sandbox(self, application_data: dict) -> dict:
        """
        Submit application for regulatory sandbox (Article 21).
        
        The application must include:
        - Innovation description
        - Risk assessment
        - Testing plan
        - Exit criteria
        - Supervision arrangements
        """
        print(f"\n📋 Submitting Sandbox Application")
        print(f"   Company: {self.company_name}")
        print(f"   Project: {application_data['project_name']}")
        print(f"   Risk Level: {application_data['risk_level']}")
        
        # Use tracker's sandbox application method
        application = self.tracker.apply_for_sandbox({
            "system_id": f"SANDBOX-{int(time.time())}",
            "innovation_description": application_data.get('innovation_description'),
            "risk_level": application_data.get('risk_level', 'HIGH'),
            "testing_period_months": application_data.get('testing_period_months', 6),
            "exit_criteria": application_data.get('exit_criteria', []),
            "supervision_plan": application_data.get('supervision_plan', {})
        })
        
        # Add sandbox-specific details
        application.update({
            "project_name": application_data['project_name'],
            "project_description": application_data.get('project_description'),
            "target_users": application_data.get('target_users', 1000),
            "expected_benefits": application_data.get('expected_benefits', []),
            "potential_risks": application_data.get('potential_risks', []),
            "mitigation_measures": application_data.get('mitigation_measures', []),
            "technical_contact": application_data.get('technical_contact'),
            "compliance_contact": application_data.get('compliance_contact'),
            "submitted_at": time.time(),
            "status": "PENDING_REVIEW"
        })
        
        self.sandbox_applications.append(application)
        
        print(f"\n✅ Sandbox Application Submitted")
        print(f"   Application ID: {application['application_id']}")
        print(f"   Testing Period: {application['testing_period_months']} months")
        print(f"   Target Users: {application['target_users']}")
        print(f"   Status: {application['status']}")
        
        return application
    
    def approve_sandbox(self, application_id: str, conditions: List[str]) -> dict:
        """
        Approve sandbox application (simulated MoST approval).
        
        When approved, the sandbox provides exemptions from certain
        compliance requirements.
        """
        application = next(
            (a for a in self.sandbox_applications if a["application_id"] == application_id),
            None
        )
        if not application:
            return {"error": "Application not found"}
        
        print(f"\n✅ Sandbox Application APPROVED")
        print(f"   Application ID: {application_id}")
        print(f"   Project: {application['project_name']}")
        
        # Define exemptions (what the sandbox participant doesn't have to do)
        standard_requirements = [
            "pre_deployment_certification",
            "full_technical_documentation",
            "third_party_audit",
            "public_disclosure"
        ]
        
        # Some requirements may still apply with reduced burden
        reduced_requirements = [
            "monthly_reporting",
            "incident_notification",
            "user_consent",
            "data_protection"
        ]
        
        # Enable sandbox mode with exemptions
        sandbox = self.tracker.enable_sandbox_mode({
            "application_id": application_id,
            "exemptions": standard_requirements,
            "reduced_obligations": reduced_requirements,
            "supervisor": "MoST_sandbox_team",
            "reporting_frequency": "monthly",
            "duration_months": application['testing_period_months']
        })
        
        sandbox.update({
            "project_name": application['project_name'],
            "project_description": application['project_description'],
            "target_users": application['target_users'],
            "start_date": time.time(),
            "end_date": time.time() + (application['testing_period_months'] * 30 * 86400),
            "conditions": conditions,
            "exemptions": standard_requirements,
            "reduced_requirements": reduced_requirements,
            "supervisor_contact": "sandbox@most.gov.vn",
            "status": "ACTIVE"
        })
        
        self.active_sandboxes.append(sandbox)
        application['status'] = "APPROVED"
        
        print(f"\n🎯 Sandbox Parameters:")
        print(f"   Duration: {application['testing_period_months']} months")
        print(f"   End Date: {datetime.fromtimestamp(sandbox['end_date'])}")
        print(f"   Target Users: Up to {sandbox['target_users']}")
        print(f"\n🔓 Exemptions Granted:")
        for ex in standard_requirements:
            print(f"   ✅ {ex}")
        print(f"\n📋 Reduced Requirements (still apply):")
        for red in reduced_requirements:
            print(f"   📋 {red}")
        
        return sandbox
    
    def submit_monthly_report(self, sandbox_id: str, report_data: dict) -> dict:
        """
        Submit monthly progress report to MoST.
        
        Sandbox participants must report regularly on:
        - Number of users
        - Incidents (if any)
        - Performance metrics
        - Compliance status
        - Issues encountered
        """
        sandbox = next((s for s in self.active_sandboxes if s.get("mode_id") == sandbox_id), None)
        if not sandbox:
            return {"error": "Active sandbox not found"}
        
        report_id = f"SR-{int(time.time())}-{hash(sandbox_id) % 10000:04d}"
        
        report = {
            "report_id": report_id,
            "sandbox_id": sandbox_id,
            "project_name": sandbox['project_name'],
            "reporting_period": report_data.get('reporting_period', datetime.now().strftime("%Y-%m")),
            "submitted_at": time.time(),
            "users_served": report_data.get('users_served', 0),
            "incidents": report_data.get('incidents', []),
            "performance_metrics": report_data.get('performance_metrics', {}),
            "compliance_status": report_data.get('compliance_status', 'COMPLIANT'),
            "issues_encountered": report_data.get('issues_encountered', []),
            "lessons_learned": report_data.get('lessons_learned', []),
            "next_steps": report_data.get('next_steps', [])
        }
        
        self.sandbox_reports.append(report)
        
        print(f"\n📊 Monthly Report Submitted")
        print(f"   Report ID: {report_id}")
        print(f"   Period: {report['reporting_period']}")
        print(f"   Users Served: {report['users_served']}")
        print(f"   Incidents: {len(report['incidents'])}")
        
        return report
    
    def log_sandbox_incident(self, sandbox_id: str, incident_data: dict) -> dict:
        """
        Log an incident during sandbox testing.
        
        Incidents must be reported immediately to MoST, even in sandbox mode.
        """
        sandbox = next((s for s in self.active_sandboxes if s.get("mode_id") == sandbox_id), None)
        if not sandbox:
            return {"error": "Active sandbox not found"}
        
        incident_id = f"SAND-INC-{int(time.time())}-{hash(sandbox_id) % 10000:04d}"
        
        incident = {
            "incident_id": incident_id,
            "sandbox_id": sandbox_id,
            "project_name": sandbox['project_name'],
            "incident_time": incident_data.get('incident_time', time.time()),
            "incident_type": incident_data.get('incident_type', 'technical'),
            "severity": incident_data.get('severity', 'LOW'),
            "description": incident_data.get('description', ''),
            "affected_users": incident_data.get('affected_users', 0),
            "root_cause": incident_data.get('root_cause', ''),
            "immediate_action": incident_data.get('immediate_action', ''),
            "reported_to_most": incident_data.get('reported_to_most', True),
            "report_time": time.time()
        }
        
        self.sandbox_incidents.append(incident)
        
        print(f"\n🚨 Sandbox Incident Reported")
        print(f"   Incident ID: {incident_id}")
        print(f"   Type: {incident['incident_type']}")
        print(f"   Severity: {incident['severity']}")
        print(f"   Affected Users: {incident['affected_users']}")
        print(f"   Reported to MoST: {incident['reported_to_most']}")
        
        return incident
    
    def evaluate_sandbox_graduation(self, sandbox_id: str) -> dict:
        """
        Evaluate whether sandbox participant can graduate to full market access.
        
        Based on:
        - All exit criteria met
        - No serious incidents
        - Performance metrics satisfactory
        - Compliance maintained
        """
        sandbox = next((s for s in self.active_sandboxes if s.get("mode_id") == sandbox_id), None)
        if not sandbox:
            return {"error": "Active sandbox not found"}
        
        print(f"\n🎓 Evaluating Sandbox Graduation")
        print(f"   Sandbox ID: {sandbox_id}")
        print(f"   Project: {sandbox['project_name']}")
        
        # Check exit criteria
        reports = [r for r in self.sandbox_reports if r['sandbox_id'] == sandbox_id]
        incidents = [i for i in self.sandbox_incidents if i['sandbox_id'] == sandbox_id]
        
        # Evaluation criteria
        evaluation = {
            "sandbox_id": sandbox_id,
            "evaluation_time": time.time(),
            "reports_submitted": len(reports),
            "incidents_count": len(incidents),
            "serious_incidents": len([i for i in incidents if i['severity'] in ['HIGH', 'CRITICAL']]),
            "exit_criteria_met": [],
            "exit_criteria_not_met": [],
            "recommendation": "PENDING"
        }
        
        # Check each exit criterion
        for criterion in sandbox.get('exit_criteria', []):
            if self._check_criterion(criterion, reports, incidents):
                evaluation['exit_criteria_met'].append(criterion)
            else:
                evaluation['exit_criteria_not_met'].append(criterion)
        
        # Make recommendation
        if (len(evaluation['exit_criteria_not_met']) == 0 and 
            evaluation['serious_incidents'] == 0 and
            evaluation['reports_submitted'] >= sandbox.get('testing_period_months', 6)):
            evaluation['recommendation'] = "GRADUATE"
            evaluation['next_steps'] = [
                "Submit final report within 30 days",
                "Apply for full market authorization",
                "Implement full compliance measures"
            ]
        else:
            evaluation['recommendation'] = "EXTEND"
            evaluation['next_steps'] = [
                f"Address {len(evaluation['exit_criteria_not_met'])} unmet criteria",
                f"Continue monitoring for {len([i for i in incidents if i['severity'] in ['HIGH', 'CRITICAL']])} serious incidents",
                "Submit extension request to MoST"
            ]
        
        print(f"\n📊 Evaluation Results:")
        print(f"   Reports Submitted: {evaluation['reports_submitted']}")
        print(f"   Incidents: {evaluation['incidents_count']} (Serious: {evaluation['serious_incidents']})")
        print(f"   Criteria Met: {len(evaluation['exit_criteria_met'])}/{len(sandbox.get('exit_criteria', []))}")
        print(f"   Recommendation: {evaluation['recommendation']}")
        
        return evaluation
    
    def _check_criterion(self, criterion: str, reports: List[dict], incidents: List[dict]) -> bool:
        """Check if a specific exit criterion is met."""
        # Simplified criteria checking
        if criterion == "accuracy > 95%":
            # Check latest report for accuracy
            if reports:
                latest = reports[-1]
                return latest.get('performance_metrics', {}).get('accuracy', 0) > 0.95
        elif criterion == "no_serious_incidents":
            return len([i for i in incidents if i['severity'] in ['HIGH', 'CRITICAL']]) == 0
        elif criterion == "user_satisfaction > 4.0":
            return True  # Simplified
        elif criterion == "compliance_maintained":
            return all(r.get('compliance_status') == 'COMPLIANT' for r in reports)
        
        return True  # Default to true for demo
    
    def graduate_from_sandbox(self, sandbox_id: str, final_report: dict) -> dict:
        """
        Graduate from sandbox to full market access.
        
        Upon graduation, the system must now comply with all
        standard AI Law requirements.
        """
        sandbox = next((s for s in self.active_sandboxes if s.get("mode_id") == sandbox_id), None)
        if not sandbox:
            return {"error": "Active sandbox not found"}
        
        graduation = {
            "graduation_id": f"GRAD-{int(time.time())}-{hash(sandbox_id) % 10000:04d}",
            "sandbox_id": sandbox_id,
            "project_name": sandbox['project_name'],
            "graduation_date": time.time(),
            "testing_period_months": sandbox.get('testing_period_months', 6),
            "final_report": final_report,
            "total_users_served": sum(r.get('users_served', 0) for r in self.sandbox_reports if r['sandbox_id'] == sandbox_id),
            "total_incidents": len([i for i in self.sandbox_incidents if i['sandbox_id'] == sandbox_id]),
            "recommendations": final_report.get('recommendations', []),
            "next_steps": [
                "Register as high-risk AI system under Article 13",
                "Implement full technical documentation",
                "Establish human oversight mechanisms",
                "Complete third-party audit within 6 months"
            ]
        }
        
        # Move from active to completed
        self.active_sandboxes.remove(sandbox)
        self.completed_sandboxes.append(graduation)
        
        print(f"\n🎉 Sandbox Graduation!")
        print(f"   Graduation ID: {graduation['graduation_id']}")
        print(f"   Testing Period: {graduation['testing_period_months']} months")
        print(f"   Total Users Served: {graduation['total_users_served']}")
        print(f"   Total Incidents: {graduation['total_incidents']}")
        print(f"\n📋 Next Steps:")
        for step in graduation['next_steps']:
            print(f"   • {step}")
        
        return graduation
    
    def run_sandbox_demo(self):
        """Run complete regulatory sandbox demonstration."""
        
        print("\n" + "="*80)
        print("📋 STEP 1: Sandbox Application")
        print("="*80)
        
        # Submit sandbox application
        application = self.apply_for_sandbox({
            "project_name": "AI-Powered Credit Scoring for Microfinance",
            "project_description": "Innovative AI system for assessing creditworthiness of unbanked individuals using alternative data",
            "risk_level": "HIGH",
            "testing_period_months": 9,
            "target_users": 5000,
            "expected_benefits": [
                "Increase financial inclusion",
                "Reduce loan processing time by 70%",
                "Lower default rates by 25%"
            ],
            "potential_risks": [
                "Algorithmic bias against certain groups",
                "Data privacy concerns",
                "Over-reliance on AI decisions"
            ],
            "mitigation_measures": [
                "Regular bias testing",
                "Encryption of personal data",
                "Human oversight for all decisions"
            ],
            "innovation_description": "Novel approach using telco data and social media activity to predict creditworthiness",
            "exit_criteria": [
                "accuracy > 95%",
                "no_serious_incidents",
                "user_satisfaction > 4.0",
                "compliance_maintained"
            ],
            "supervision_plan": {
                "reporting_frequency": "monthly",
                "monitoring_metrics": ["accuracy", "bias", "incidents", "user_satisfaction"],
                "supervisor": "MoST_fintech_team"
            },
            "technical_contact": "engineer@company.com",
            "compliance_contact": "compliance@company.com"
        })
        
        print("\n" + "="*80)
        print("✅ STEP 2: Sandbox Approval")
        print("="*80)
        
        # Simulate MoST approval
        sandbox = self.approve_sandbox(
            application_id=application['application_id'],
            conditions=[
                "Monthly reporting required",
                "Immediate incident reporting",
                "User consent must be obtained",
                "Bias testing quarterly"
            ]
        )
        
        print("\n" + "="*80)
        print("📊 STEP 3: Monthly Reporting (Month 1-3)")
        print("="*80")
        
        # Submit monthly reports
        for month in range(1, 4):
            report = self.submit_monthly_report(
                sandbox_id=sandbox['mode_id'],
                report_data={
                    "reporting_period": f"2026-{month:02d}",
                    "users_served": 500 * month,
                    "incidents": [] if month < 3 else [{"type": "minor_glitch", "resolved": True}],
                    "performance_metrics": {
                        "accuracy": 0.93 + (month * 0.01),
                        "processing_time_ms": 250 - (month * 10),
                        "user_satisfaction": 4.2 + (month * 0.1)
                    },
                    "compliance_status": "COMPLIANT",
                    "next_steps": [f"Month {month+1} expansion"]
                }
            )
        
        print("\n" + "="*80)
        print("🚨 STEP 4: Incident Handling")
        print("="*80")
        
        # Simulate an incident
        incident = self.log_sandbox_incident(
            sandbox_id=sandbox['mode_id'],
            incident_data={
                "incident_type": "data_processing_delay",
                "severity": "LOW",
                "description": "Batch processing delay of 2 hours due to infrastructure issue",
                "affected_users": 150,
                "root_cause": "Server overload during peak hours",
                "immediate_action": "Scaled up servers, resumed processing",
                "reported_to_most": True
            }
        )
        
        print("\n" + "="*80)
        print("📋 STEP 5: Monthly Reporting (Month 4-6)")
        print("="*80")
        
        # Continue reporting
        for month in range(4, 7):
            report = self.submit_monthly_report(
                sandbox_id=sandbox['mode_id'],
                report_data={
                    "reporting_period": f"2026-{month:02d}",
                    "users_served": 2000 + (month * 500),
                    "incidents": [],
                    "performance_metrics": {
                        "accuracy": 0.96,
                        "processing_time_ms": 210,
                        "user_satisfaction": 4.5
                    },
                    "compliance_status": "COMPLIANT",
                    "lessons_learned": ["Infrastructure scaling critical", "Need better monitoring"],
                    "next_steps": ["Prepare for graduation evaluation"]
                }
            )
        
        print("\n" + "="*80)
        print("🎓 STEP 6: Graduation Evaluation")
        print("="*80")
        
        # Evaluate for graduation
        evaluation = self.evaluate_sandbox_graduation(sandbox['mode_id'])
        
        print("\n" + "="*80)
        print("🎉 STEP 7: Sandbox Graduation")
        print("="*80")
        
        # Graduate from sandbox
        if evaluation['recommendation'] == "GRADUATE":
            graduation = self.graduate_from_sandbox(
                sandbox_id=sandbox['mode_id'],
                final_report={
                    "summary": "Successfully tested credit scoring AI with 5,000+ users",
                    "key_findings": [
                        "Model achieved 96% accuracy",
                        "No serious incidents",
                        "User satisfaction 4.5/5",
                        "Processing time reduced 60%"
                    ],
                    "recommendations": [
                        "Implement for full deployment",
                        "Enhance bias monitoring",
                        "Scale infrastructure"
                    ]
                }
            )
        
        print("\n" + "="*80)
        print("📊 Sandbox Summary")
        print("="*80)
        print(f"   Sandbox Duration: {sandbox['testing_period_months']} months")
        print(f"   Total Reports Submitted: {len([r for r in self.sandbox_reports if r['sandbox_id'] == sandbox['mode_id']])}")
        print(f"   Incidents Logged: {len([i for i in self.sandbox_incidents if i['sandbox_id'] == sandbox['mode_id']])}")
        print(f"   Total Users Served: {sum(r.get('users_served', 0) for r in self.sandbox_reports if r['sandbox_id'] == sandbox['mode_id'])}")
        print(f"   Final Recommendation: {evaluation['recommendation']}")
        print(f"\n📋 Article 21 Compliance Achieved:")
        print(f"   ✅ Sandbox application and approval")
        print(f"   ✅ Exemptions granted (pre-deployment certification waived)")
        print(f"   ✅ Monthly reporting to MoST")
        print(f"   ✅ Incident notification")
        print(f"   ✅ Exit criteria evaluation")
        print(f"   ✅ Graduation process")


if __name__ == "__main__":
    system = VietnamRegulatorySandbox("VietAI FinTech")
    system.run_sandbox_demo()
