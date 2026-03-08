# 🇻🇳 JEP Vietnam Solutions

**AI Accountability for the Socialist Republic of Vietnam**

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-green.svg)](https://www.python.org/downloads/)
[![AI Law 2026](https://img.shields.io/badge/AI%20Law-2026-red)](https://example.com)
[![Effective March 1, 2026](https://img.shields.io/badge/Effective-March%201%2C%202026-green)](https://example.com)

## 📋 Overview

Vietnam has enacted the **Law on Artificial Intelligence (No. 134/2025/QH15)** , which took effect **March 1, 2026**, making Vietnam the **first ASEAN member state** to adopt a standalone legal framework for AI . This directory provides a complete **Judgment Event Protocol (JEP)** implementation aligned with Vietnam's AI Law and related regulations.

### Why Vietnam Matters

| Reason | Significance |
|--------|--------------|
| **First ASEAN AI Law** | Vietnam leads ASEAN in AI regulation  |
| **Effective Date** | **March 1, 2026** - **Already in effect!** |
| **Global Standing** | One of few nations (EU, Korea, Japan, Vietnam) with dedicated AI legislation  |
| **Risk-Based Approach** | 3-tier classification (high/medium/low)  |
| **Human-Centric Design** | "Human-in-command" principle - ultimate responsibility with humans  |
| **Content Transparency** | Mandatory watermarks for AI-generated content  |

## 🎯 Vietnam AI Law (2026) Requirements

| Requirement | Description | JEP Implementation | Verification |
|-------------|-------------|-------------------|--------------|
| **Risk Classification** | 3-tier risk assessment before deployment  | `assess_risk_level()` | `verify-vietnam.py --risk` |
| **High-Risk Safeguards** | Human oversight + technical documentation + operational logs  | `high_risk_tracker.py` | `verify-vietnam.py --high-risk` |
| **AI Content Marking** | Machine-readable identifiers for AI-generated audio/image/video  | `content_labeling.py` | `verify-vietnam.py --content` |
| **Deepfake Labeling** | Clear visible labels distinguishing from authentic content  | `add_watermark()` | `verify-vietnam.py --deepfake` |
| **Right to Explanation** | Users can request explanation of AI decisions  | `decision_factors` + `reasoning` | `verify-vietnam.py --explanation` |
| **Human-AI Interaction Disclosure** | Users must know they're interacting with AI  | `is_ai_generated` flag | `verify-vietnam.py --disclosure` |
| **Regulatory Sandbox** | Test high-risk systems under controlled conditions  | `sandbox_tracker.py` | `verify-vietnam.py --sandbox` |

## 📊 Vietnam vs Global AI Laws

| Aspect | Vietnam | EU AI Act | Singapore | JEP Alignment |
|--------|---------|-----------|-----------|---------------|
| **Risk Classification** | 3-tier (high/medium/low)  | 4-tier (unacceptable/high/limited/minimal) | Voluntary | ✅ Adaptable |
| **Content Marking** | ✅ Mandatory watermarks  | ✅ Article 50 | ✅ AI Verify | ✅ Content provenance |
| **Right to Explanation** | ✅ Yes  | ✅ Article 86 | Not explicit | ✅ Decision factors |
| **Human Oversight** | ✅ "Human-in-command"  | ✅ Article 14 | ✅ Framework | ✅ Delegate primitive |
| **Regulatory Sandbox** | ✅ Yes  | ✅ Yes | ✅ Yes | ✅ Sandbox support |

## 🚀 Quick Start

```python
from jep.vn import VietnamAITracker

# Initialize tracker
tracker = VietnamAITracker(
    organization="AI Vietnam Corp",
    contact_email="compliance@aivietnam.vn"
)

# Register a high-risk AI system (required by law)
system = tracker.register_high_risk_system({
    "system_name": "Credit Scoring AI",
    "system_type": "financial",
    "description": "AI for creditworthiness assessment",
    "risk_level": "HIGH",
    "human_oversight": True,
    "technical_documentation": "doc_2026_001.pdf"
})

# Log a consequential decision with explanation (right to explanation)
decision = tracker.log_consequential_decision({
    "consumer_id": "CONS-123",
    "decision": "REJECT",
    "principal_reasons": [
        "Credit score below threshold (650 vs 680 required)",
        "Debt-to-income ratio exceeds 43%"
    ],
    "explanation": "Your loan application was declined based on credit scoring criteria."
})

# Mark AI-generated content (mandatory watermarking)
watermarked = tracker.mark_ai_content({
    "content": image_data,
    "content_type": "image",
    "generator_id": "image-gen-v2",
    "watermark_type": "machine_readable"
})
```

## 🏛️ Legal Foundation

JEP is stewarded by **HJS Foundation LTD** (Singapore CLG), a non-profit organization with permanent asset lock. The foundation's constitution explicitly prohibits:

- Distribution of profits to members (Article 7B)
- Transfer or sale of core assets (Article 67A)

**Registered Address**: 101 Thomson Road #28-03A, United Square, Singapore 307591

## 📁 Repository Structure

```
vietnam/
├── README.md                          # This file
├── ai-law-2026/                        # Law on AI (No. 134/2025/QH15)
│   ├── README.md                        # AI Law overview
│   ├── mapping.md                        # Detailed mapping
│   ├── implementation/
│   │   └── vn_tracker.py
│   └── examples/
│       ├── high-risk-ai.py
│       ├── content-labeling.py
│       └── right-to-explanation.py
├── digital-technology-law/                # Digital Technology Industry Law
│   ├── mapping.md                          # Relevant provisions
│   └── examples/
│       └── regulatory-sandbox.py
└── tests/
    └── verify-vietnam.py
```

## 🔍 Verification

```bash
# Run complete Vietnam compliance verification
python tests/verify-vietnam.py --all

# Output:
# ========================================
# VIETNAM AI LAW COMPLIANCE VERIFICATION
# ========================================
# ✅ Risk Classification: 3-tier assessment ready
# ✅ High-Risk Safeguards: Human oversight + documentation
# ✅ Content Marking: Machine-readable watermarks
# ✅ Deepfake Labeling: Clear visible labels
# ✅ Right to Explanation: Decision factors + reasoning
# ✅ Human-AI Disclosure: AI identification
# ✅ Regulatory Sandbox: Controlled testing support
# ========================================
# FULL COMPLIANCE VERIFIED
# ========================================
```

## 📚 References

- [Law on Artificial Intelligence 2025 (No. 134/2025/QH15), effective March 1, 2026](https://example.com) 
- [Law on Digital Technology Industry 2025 (No. 71/2025/QH15)](https://english.luatvietnam.vn/law-on-digital-technology-industry-no-71-2025-qh15-dated-june-14-2025-of-the-national-assembly-405695-doc1.html) 
- [Decision No. 367/QD-TTg (March 3, 2026) implementing AI Law](https://en.vietnamplus.vn/ai-law-takes-effect-anchors-national-governance-framework-post338716.vnp) 
- [Ministry of Science and Technology (MoST)](https://english.mst.gov.vn/)

## 📬 Contact

For Vietnam-specific inquiries:
- **Email**: vietnam@humanjudgment.org
- **GitHub**: [hjs-spec/jep-vn-solutions](https://github.com/hjs-spec/jep-vn-solutions)

---

*Last Updated: March 2026*
*Supporting Vietnam's leadership in ASEAN AI governance*
```
