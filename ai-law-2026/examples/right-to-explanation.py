#!/usr/bin/env python3
"""
Vietnam AI Law - Right to Explanation Example (Article 11)
============================================================

This example demonstrates the "Right to Explanation" provision under Vietnam's AI Law,
which gives users the right to request an explanation of AI decisions that affect them.

Under Article 11, users must be able to obtain:
- The reasons for an AI decision
- The factors that influenced the decision
- The logic behind the decision-making process
- Information about human oversight availability
- Information about appeal rights
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
    EntityType
)


class VietnamExplanationSystem:
    """
    Complete system demonstrating the Right to Explanation under Vietnam AI Law.
    
    Features:
    - Record all AI decisions with full factor breakdown
    - Generate human-readable explanations for users
    - Handle explanation requests
    - Track explanation delivery
    - Maintain audit trail of explanations provided
    - Support multiple languages (Vietnamese/English)
    """
    
    def __init__(self, organization: str):
        self.organization = organization
        self.tracker = VietnamAITracker(
            organization=organization,
            entity_type=EntityType.DEPLOYER,
            jurisdiction="vietnam"
        )
        
        self.decisions = []
        self.explanation_requests = []
        self.users = {}
        
        print("="*80)
        print(f"📋 Right to Explanation System - {organization}")
        print("="*80)
        print(f"Vietnam AI Law Effective: March 1, 2026")
        print(f"Article 11: Transparency Obligations - Right to Explanation")
        print(f"Users can request explanations of AI decisions that affect them")
    
    def register_user(self, user_data: dict) -> str:
        """Register a user in the system."""
        user_id = f"USER-{int(time.time())}-{hash(user_data['email']) % 10000:04d}"
        
        self.users[user_id] = {
            "user_id": user_id,
            "name": user_data['name'],
            "email": user_data['email'],
            "phone": user_data.get('phone'),
            "preferred_language": user_data.get('language', 'vi'),
            "created_date": time.time()
        }
        
        print(f"\n👤 User Registered: {user_data['name']} (ID: {user_id})")
        print(f"   Preferred Language: {user_data.get('language', 'vi')}")
        
        return user_id
    
    def make_decision(self, decision_data: dict) -> dict:
        """
        Make an AI decision that affects a user.
        
        Records all factors and logic for future explanation requests.
        """
        user = self.users.get(decision_data['user_id'])
        if not user:
            return {"error": "User not found"}
        
        print(f"\n🤖 Making AI Decision")
        print(f"   User: {user['name']}")
        print(f"   Decision Type: {decision_data['type']}")
        
        # Simulate AI decision logic
        decision_result = self._simulate_decision(decision_data)
        
        # Store complete decision record with all factors
        decision = {
            "decision_id": f"DEC-{int(time.time())}-{hash(str(decision_data)) % 10000:04d}",
            "user_id": user['user_id'],
            "user_name": user['name'],
            "decision_type": decision_data['type'],
            "timestamp": time.time(),
            "input_data": decision_data.get('input_data', {}),
            "decision": decision_result['decision'],
            "score": decision_result['score'],
            "factors": decision_result['factors'],  # Detailed factor breakdown
            "reasoning": decision_result['reasoning'],  # Human-readable reasoning
            "thresholds": decision_result['thresholds'],  # Decision thresholds
            "model_version": decision_result.get('model_version', 'v2.1.0'),
            "confidence": decision_result.get('confidence', 0.95),
            "human_review_available": decision_data.get('human_review_available', True),
            "appeal_deadline": time.time() + 2592000,  # 30 days
            "explanations_requested": 0,
            "explanations_provided": []
        }
        
        self.decisions.append(decision)
        
        print(f"\n📊 Decision Made: {decision['decision']}")
        print(f"   Score: {decision['score']:.1f}/100")
        print(f"   Key Factors: {', '.join(list(decision['factors'].keys())[:3])}")
        print(f"   Reasoning: {decision['reasoning'][:100]}...")
        print(f"   Human Review Available: {decision['human_review_available']}")
        print(f"   Appeal Deadline: {datetime.fromtimestamp(decision['appeal_deadline'])}")
        
        return decision
    
    def _simulate_decision(self, decision_data: dict) -> dict:
        """Simulate AI decision logic with detailed factor breakdown."""
        
        decision_type = decision_data['type']
        input_data = decision_data.get('input_data', {})
        
        if decision_type == "loan_approval":
            return self._simulate_loan_decision(input_data)
        elif decision_type == "job_application":
            return self._simulate_job_decision(input_data)
        elif decision_type == "insurance_claim":
            return self._simulate_insurance_decision(input_data)
        elif decision_type == "credit_limit":
            return self._simulate_credit_decision(input_data)
        else:
            return self._simulate_generic_decision(input_data)
    
    def _simulate_loan_decision(self, data: dict) -> dict:
        """Simulate loan approval decision with factors."""
        
        score = 0
        factors = {}
        thresholds = {}
        
        # Credit score factor
        credit_score = data.get('credit_score', 0)
        if credit_score >= 750:
            score += 35
            factors['credit_score'] = {
                "value": credit_score,
                "weight": 35,
                "rating": "excellent",
                "description": "Excellent credit score indicates reliable repayment history"
            }
        elif credit_score >= 700:
            score += 30
            factors['credit_score'] = {
                "value": credit_score,
                "weight": 30,
                "rating": "good",
                "description": "Good credit score"
            }
        elif credit_score >= 650:
            score += 20
            factors['credit_score'] = {
                "value": credit_score,
                "weight": 20,
                "rating": "fair",
                "description": "Fair credit score - slightly below optimal"
            }
        else:
            score += 10
            factors['credit_score'] = {
                "value": credit_score,
                "weight": 10,
                "rating": "below_average",
                "description": "Credit score below our preferred threshold"
            }
        
        # Debt-to-income ratio
        income = data.get('annual_income', 0)
        debt = data.get('monthly_debt', 0) * 12
        dti = (debt / income * 100) if income > 0 else 100
        
        if dti <= 30:
            score += 30
            factors['debt_to_income'] = {
                "value": dti,
                "weight": 30,
                "rating": "excellent",
                "description": f"Debt-to-income ratio of {dti:.1f}% is very healthy"
            }
        elif dti <= 40:
            score += 25
            factors['debt_to_income'] = {
                "value": dti,
                "weight": 25,
                "rating": "good",
                "description": f"Debt-to-income ratio of {dti:.1f}% is acceptable"
            }
        elif dti <= 50:
            score += 15
            factors['debt_to_income'] = {
                "value": dti,
                "weight": 15,
                "rating": "fair",
                "description": f"Debt-to-income ratio of {dti:.1f}% is higher than ideal"
            }
        else:
            score += 5
            factors['debt_to_income'] = {
                "value": dti,
                "weight": 5,
                "rating": "high",
                "description": f"Debt-to-income ratio of {dti:.1f}% is too high"
            }
        
        # Employment stability
        years_employed = data.get('employment_years', 0)
        if years_employed >= 5:
            score += 20
            factors['employment_stability'] = {
                "value": years_employed,
                "weight": 20,
                "rating": "stable",
                "description": f"{years_employed} years of stable employment"
            }
        elif years_employed >= 2:
            score += 15
            factors['employment_stability'] = {
                "value": years_employed,
                "weight": 15,
                "rating": "moderate",
                "description": f"{years_employed} years of employment"
            }
        else:
            score += 5
            factors['employment_stability'] = {
                "value": years_employed,
                "weight": 5,
                "rating": "limited",
                "description": f"Limited employment history ({years_employed} years)"
            }
        
        # Loan purpose
        purpose = data.get('loan_purpose', 'other')
        purpose_scores = {
            'home_purchase': 15,
            'home_improvement': 12,
            'debt_consolidation': 10,
            'education': 12,
            'medical': 10,
            'business': 12,
            'vehicle': 8,
            'other': 5
        }
        purpose_score = purpose_scores.get(purpose, 5)
        score += purpose_score
        factors['loan_purpose'] = {
            "value": purpose,
            "weight": purpose_score,
            "description": f"Loan purpose: {purpose.replace('_', ' ')}"
        }
        
        # Set thresholds
        thresholds = {
            "minimum_score": 70,
            "excellent_threshold": 90,
            "good_threshold": 80,
            "fair_threshold": 60
        }
        
        decision = "APPROVED" if score >= 70 else "DENIED"
        
        # Generate reasoning
        if decision == "APPROVED":
            reasoning = f"Your loan application has been APPROVED with a score of {score}. " \
                       f"The strongest factors were: {list(factors.keys())[0]} and {list(factors.keys())[1]}. " \
                       f"You met our minimum threshold of 70 points."
        else:
            reasoning = f"Your loan application has been DECLINED with a score of {score}. " \
                       f"The main limiting factors were: {list(factors.keys())[0]} and {list(factors.keys())[1]}. " \
                       f"You did not meet our minimum threshold of 70 points."
        
        return {
            "decision": decision,
            "score": score,
            "factors": factors,
            "thresholds": thresholds,
            "reasoning": reasoning,
            "confidence": 0.95,
            "model_version": "loan-model-v3.2"
        }
    
    def _simulate_job_decision(self, data: dict) -> dict:
        """Simulate job application decision."""
        # Similar structure to loan decision but for employment
        return {
            "decision": "INTERVIEW",
            "score": 85,
            "factors": {
                "experience": {"value": 5, "weight": 30, "description": "5 years relevant experience"},
                "skills_match": {"value": "85%", "weight": 25, "description": "85% skills match"},
                "education": {"value": "Bachelor", "weight": 15, "description": "Education requirement met"}
            },
            "reasoning": "Your application has been selected for an interview based on your strong experience and skills match.",
            "model_version": "hiring-model-v2.1"
        }
    
    def _simulate_insurance_decision(self, data: dict) -> dict:
        """Simulate insurance claim decision."""
        return {
            "decision": "APPROVED",
            "score": 92,
            "factors": {
                "policy_coverage": {"value": "Full", "weight": 40, "description": "Claim is fully covered"},
                "claim_amount": {"value": 5000, "weight": 30, "description": "Within policy limits"},
                "documentation": {"value": "Complete", "weight": 22, "description": "All documentation provided"}
            },
            "reasoning": "Your insurance claim has been approved. It is fully covered under your policy.",
            "model_version": "claims-model-v1.5"
        }
    
    def _simulate_credit_decision(self, data: dict) -> dict:
        """Simulate credit limit decision."""
        return {
            "decision": "INCREASE",
            "score": 78,
            "factors": {
                "payment_history": {"value": "Excellent", "weight": 35, "description": "12 months on-time payments"},
                "credit_utilization": {"value": "35%", "weight": 25, "description": "Good credit utilization"},
                "income_stability": {"value": "Stable", "weight": 18, "description": "Stable income verified"}
            },
            "reasoning": "Your credit limit has been increased based on your excellent payment history.",
            "model_version": "credit-model-v2.3"
        }
    
    def _simulate_generic_decision(self, data: dict) -> dict:
        """Generic decision for demonstration."""
        return {
            "decision": "APPROVED",
            "score": 75,
            "factors": {
                "primary_factor": {"value": "positive", "weight": 40, "description": "Primary criteria met"},
                "secondary_factor": {"value": "acceptable", "weight": 35, "description": "Secondary criteria acceptable"}
            },
            "reasoning": "Your request has been approved based on the evaluation criteria.",
            "model_version": "generic-model-v1.0"
        }
    
    def request_explanation(self, user_id: str, decision_id: str, language: str = "vi") -> dict:
        """
        User requests explanation of an AI decision (Right to Explanation).
        
        Under Article 11, users have the right to request and receive
        an explanation of AI decisions that affect them.
        """
        user = self.users.get(user_id)
        if not user:
            return {"error": "User not found"}
        
        decision = next((d for d in self.decisions if d["decision_id"] == decision_id), None)
        if not decision:
            return {"error": "Decision not found"}
        
        print(f"\n📋 Right to Explanation Requested")
        print(f"   User: {user['name']}")
        print(f"   Decision ID: {decision_id}")
        print(f"   Language: {language}")
        
        # Record the request
        request = {
            "request_id": f"EXP-{int(time.time())}-{hash(user_id) % 10000:04d}",
            "user_id": user_id,
            "user_name": user['name'],
            "decision_id": decision_id,
            "request_time": time.time(),
            "language": language,
            "status": "PROCESSING",
            "response_time": None
        }
        
        self.explanation_requests.append(request)
        
        # Generate explanation
        explanation = self.generate_explanation(decision_id, user_id, language)
        
        # Update request status
        request["status"] = "COMPLETED"
        request["response_time"] = time.time()
        request["explanation_id"] = explanation["explanation_id"]
        
        print(f"\n✅ Explanation Generated")
        print(f"   Request ID: {request['request_id']}")
        print(f"   Response Time: {request['response_time'] - request['request_time']:.2f} seconds")
        
        return explanation
    
    def generate_explanation(self, decision_id: str, user_id: str, language: str = "vi") -> dict:
        """
        Generate a comprehensive explanation for an AI decision.
        
        This implements the Right to Explanation requirement, providing:
        - Decision outcome
        - Key factors and their weights
        - Thresholds applied
        - Human review options
        - Appeal rights
        """
        decision = next((d for d in self.decisions if d["decision_id"] == decision_id), None)
        if not decision:
            return {"error": "Decision not found"}
        
        explanation_id = f"EXPL-{int(time.time())}-{hash(decision_id) % 10000:04d}"
        
        # Create explanation in requested language
        if language == "vi":
            explanation_text = self._generate_vietnamese_explanation(decision)
        else:
            explanation_text = self._generate_english_explanation(decision)
        
        # Format factor breakdown
        factor_breakdown = []
        for factor_name, factor_data in decision['factors'].items():
            factor_breakdown.append({
                "factor": factor_name.replace('_', ' ').title(),
                "value": factor_data.get('value', 'N/A'),
                "weight": factor_data.get('weight', 0),
                "description": factor_data.get('description', '')
            })
        
        # Sort factors by weight (most important first)
        factor_breakdown.sort(key=lambda x: x['weight'], reverse=True)
        
        explanation = {
            "explanation_id": explanation_id,
            "decision_id": decision_id,
            "user_id": user_id,
            "generated_at": time.time(),
            "language": language,
            "decision_outcome": decision['decision'],
            "decision_score": decision['score'],
            "factor_breakdown": factor_breakdown,
            "thresholds": decision.get('thresholds', {}),
            "explanation_text": explanation_text,
            "human_review_available": decision.get('human_review_available', True),
            "appeal_deadline": decision.get('appeal_deadline'),
            "model_version": decision.get('model_version', 'unknown'),
            "rights_notice": self._generate_rights_notice(language)
        }
        
        # Track that explanation was provided
        decision['explanations_requested'] += 1
        decision['explanations_provided'].append({
            "explanation_id": explanation_id,
            "timestamp": time.time(),
            "language": language
        })
        
        print(f"\n📄 Explanation Generated (ID: {explanation_id})")
        print(f"   Language: {language}")
        print(f"   Factors Explained: {len(factor_breakdown)}")
        print(f"   Top Factor: {factor_breakdown[0]['factor'] if factor_breakdown else 'N/A'}")
        
        return explanation
    
    def _generate_vietnamese_explanation(self, decision: dict) -> str:
        """Generate explanation in Vietnamese."""
        if decision['decision'] == "APPROVED":
            return f"""
Kính gửi Quý khách,

Chúng tôi xin thông báo rằng yêu cầu của bạn đã được **PHÊ DUYỆT** với số điểm {decision['score']}/100.

Các yếu tố chính ảnh hưởng đến quyết định:
- {list(decision['factors'].keys())[0].replace('_', ' ')}: Đạt yêu cầu
- {list(decision['factors'].keys())[1].replace('_', ' ')}: Tốt

Quyết định này được đưa ra bởi hệ thống AI dựa trên các tiêu chí đã được xác định trước.

Nếu bạn không đồng ý với quyết định này, bạn có quyền:
1. Yêu cầu xem xét lại bởi con người
2. Khiếu nại trong vòng 30 ngày

Trân trọng,
Hệ thống đánh giá tự động
            """
        else:
            return f"""
Kính gửi Quý khách,

Chúng tôi rất tiếc phải thông báo rằng yêu cầu của bạn đã **KHÔNG ĐƯỢC PHÊ DUYỆT** với số điểm {decision['score']}/100.

Các yếu tố chính ảnh hưởng đến quyết định:
- {list(decision['factors'].keys())[0].replace('_', ' ')}: Chưa đạt yêu cầu
- {list(decision['factors'].keys())[1].replace('_', ' ')}: Cần cải thiện

Quyết định này được đưa ra bởi hệ thống AI dựa trên các tiêu chí đã được xác định trước.

Bạn có quyền:
1. Yêu cầu giải thích chi tiết hơn (quyền này đang được thực hiện)
2. Yêu cầu xem xét lại bởi con người
3. Khiếu nại trong vòng 30 ngày

Trân trọng,
Hệ thống đánh giá tự động
            """
    
    def _generate_english_explanation(self, decision: dict) -> str:
        """Generate explanation in English."""
        if decision['decision'] == "APPROVED":
            return f"""
Dear Customer,

We are pleased to inform you that your request has been **APPROVED** with a score of {decision['score']}/100.

Key factors influencing this decision:
- {list(decision['factors'].keys())[0].replace('_', ' ')}: Met requirements
- {list(decision['factors'].keys())[1].replace('_', ' ')}: Good

This decision was made by our AI system based on pre-defined criteria.

If you disagree with this decision, you have the right to:
1. Request human review
2. Appeal within 30 days

Sincerely,
Automated Decision System
            """
        else:
            return f"""
Dear Customer,

We regret to inform you that your request has been **DECLINED** with a score of {decision['score']}/100.

Key factors influencing this decision:
- {list(decision['factors'].keys())[0].replace('_', ' ')}: Did not meet requirements
- {list(decision['factors'].keys())[1].replace('_', ' ')}: Needs improvement

This decision was made by our AI system based on pre-defined criteria.

You have the right to:
1. Request detailed explanation (this right is being exercised)
2. Request human review
3. Appeal within 30 days

Sincerely,
Automated Decision System
            """
    
    def _generate_rights_notice(self, language: str) -> dict:
        """Generate notice of rights under Vietnam AI Law."""
        if language == "vi":
            return {
                "right_to_explanation": "Bạn có quyền yêu cầu giải thích về quyết định của AI",
                "right_to_human_review": "Bạn có quyền yêu cầu xem xét lại bởi con người",
                "right_to_appeal": "Bạn có quyền khiếu nại trong vòng 30 ngày",
                "right_to_correction": "Bạn có quyền yêu cầu sửa dữ liệu cá nhân",
                "contact": "Vui lòng liên hệ hotline 1900 1234 để được hỗ trợ"
            }
        else:
            return {
                "right_to_explanation": "You have the right to request an explanation of AI decisions",
                "right_to_human_review": "You have the right to request human review",
                "right_to_appeal": "You have the right to appeal within 30 days",
                "right_to_correction": "You have the right to request correction of your data",
                "contact": "Please contact our hotline at 1900 1234 for assistance"
            }
    
    def handle_appeal(self, user_id: str, decision_id: str, appeal_reason: str) -> dict:
        """
        Handle user appeal of an AI decision.
        
        Under Article 11, users have the right to appeal decisions.
        """
        user = self.users.get(user_id)
        decision = next((d for d in self.decisions if d["decision_id"] == decision_id), None)
        
        if not user or not decision:
            return {"error": "User or decision not found"}
        
        print(f"\n⚖️ Appeal Filed")
        print(f"   User: {user['name']}")
        print(f"   Decision ID: {decision_id}")
        print(f"   Reason: {appeal_reason[:100]}...")
        
        appeal = {
            "appeal_id": f"APP-{int(time.time())}-{hash(user_id) % 10000:04d}",
            "user_id": user_id,
            "user_name": user['name'],
            "decision_id": decision_id,
            "appeal_reason": appeal_reason,
            "appeal_date": time.time(),
            "status": "RECEIVED",
            "assigned_reviewer": "human_review_team",
            "review_deadline": time.time() + 604800,  # 7 days
            "resolution": None,
            "resolution_date": None
        }
        
        print(f"\n✅ Appeal Recorded")
        print(f"   Appeal ID: {appeal['appeal_id']}")
        print(f"   Status: {appeal['status']}")
        print(f"   Review Deadline: {datetime.fromtimestamp(appeal['review_deadline'])}")
        
        return appeal
    
    def generate_explanation_report(self) -> dict:
        """Generate report on explanation requests and compliance."""
        
        report = {
            "report_id": f"EXP-RPT-{int(time.time())}",
            "organization": self.organization,
            "generated_at": datetime.now().isoformat(),
            "statistics": {
                "total_decisions": len(self.decisions),
                "total_explanation_requests": len(self.explanation_requests),
                "requests_by_decision": {},
                "avg_response_time": 0
            },
            "compliance_summary": {
                "right_to_explanation": "COMPLIANT",
                "explanations_provided": len(self.explanation_requests),
                "appeals_processed": 0,
                "human_review_available": all(d.get('human_review_available', True) for d in self.decisions)
            }
        }
        
        # Calculate average response time
        completed_requests = [r for r in self.explanation_requests if r.get('response_time')]
        if completed_requests:
            total_time = sum(r['response_time'] - r['request_time'] for r in completed_requests)
            report['statistics']['avg_response_time'] = total_time / len(completed_requests)
        
        print(f"\n📊 Explanation Report Generated")
        print(f"   Total Decisions: {report['statistics']['total_decisions']}")
        print(f"   Explanation Requests: {report['statistics']['total_explanation_requests']}")
        print(f"   Avg Response Time: {report['statistics']['avg_response_time']:.2f}s")
        
        return report
    
    def run_demo(self):
        """Run complete Right to Explanation demonstration."""
        
        print("\n" + "="*80)
        print("👤 STEP 1: Register Users")
        print("="*80)
        
        # Register users
        user1 = self.register_user({
            "name": "Nguyễn Văn An",
            "email": "nguyenvanan@email.com",
            "phone": "0912345678",
            "language": "vi"
        })
        
        user2 = self.register_user({
            "name": "Tran Thi Binh",
            "email": "tranthibinh@email.com",
            "language": "en"
        })
        
        print("\n" + "="*80)
        print("🤖 STEP 2: Make AI Decisions")
        print("="*80)
        
        # Make loan decisions
        decision1 = self.make_decision({
            "user_id": user1,
            "type": "loan_approval",
            "input_data": {
                "credit_score": 680,
                "annual_income": 240000000,  # VND
                "monthly_debt": 8000000,
                "employment_years": 3,
                "loan_purpose": "home_purchase"
            },
            "human_review_available": True
        })
        
        decision2 = self.make_decision({
            "user_id": user2,
            "type": "loan_approval",
            "input_data": {
                "credit_score": 720,
                "annual_income": 360000000,
                "monthly_debt": 5000000,
                "employment_years": 7,
                "loan_purpose": "home_improvement"
            },
            "human_review_available": True
        })
        
        decision3 = self.make_decision({
            "user_id": user1,
            "type": "credit_limit",
            "input_data": {
                "payment_history": "excellent",
                "credit_utilization": 35,
                "income_stability": "stable"
            }
        })
        
        print("\n" + "="*80)
        print("📋 STEP 3: Exercise Right to Explanation")
        print("="*80)
        
        # User requests explanation (Vietnamese)
        explanation1 = self.request_explanation(
            user_id=user1,
            decision_id=decision1['decision_id'],
            language="vi"
        )
        
        # User requests explanation (English)
        explanation2 = self.request_explanation(
            user_id=user2,
            decision_id=decision2['decision_id'],
            language="en"
        )
        
        print("\n" + "="*80)
        print("📄 Sample Explanation (Vietnamese)")
        print("="*80)
        print(explanation1['explanation_text'])
        
        print("\n" + "="*80)
        print("📄 Sample Explanation (English)")
        print("="*80)
        print(explanation2['explanation_text'])
        
        print("\n" + "="*80)
        print("⚖️ STEP 4: File Appeal")
        print("="*80)
        
        # User appeals decision
        appeal = self.handle_appeal(
            user_id=user1,
            decision_id=decision1['decision_id'],
            appeal_reason="Tôi không đồng ý với kết quả. Thu nhập của tôi cao hơn mức trung bình và tôi có tài sản đảm bảo."
        )
        
        print("\n" + "="*80)
        print("📊 STEP 5: Generate Report")
        print("="*80)
        
        # Generate final report
        report = self.generate_explanation_report()
        
        print("\n" + "="*80)
        print("✅ Right to Explanation Demo Complete")
        print("="*80)
        print(f"   Users Registered: 2")
        print(f"   AI Decisions Made: {len(self.decisions)}")
        print(f"   Explanations Requested: {len(self.explanation_requests)}")
        print(f"   Appeals Filed: 1")
        print(f"\n📋 Article 11 Compliance:")
        print(f"   ✅ Right to Explanation: Implemented")
        print(f"   ✅ Factor Breakdown: Provided")
        print(f"   ✅ Human-Readable Explanations: Available")
        print(f"   ✅ Human Review Option: Available")
        print(f"   ✅ Appeal Rights: Provided")
        
        return report


if __name__ == "__main__":
    system = VietnamExplanationSystem("Vietnam Financial Services")
    report = system.run_demo()
    
    # Save report
    with open("vietnam_explanation_report.json", "w") as f:
        json.dump(report, f, indent=2, default=str)
    print(f"\n✅ Report saved: vietnam_explanation_report.json")
    print(f"\n📋 Vietnam AI Law Article 11 (Right to Explanation) fully implemented:")
    print(f"   - Users can request explanations of AI decisions")
    print(f"   - Detailed factor breakdown provided")
    print(f"   - Human-readable explanations in Vietnamese/English")
    print(f"   - Appeal rights clearly communicated")
    print(f"   - Human review option available")
