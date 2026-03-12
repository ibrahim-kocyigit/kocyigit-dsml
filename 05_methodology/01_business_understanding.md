# Stage 1: Business Understanding

_"Every project starts with business understanding. The business sponsors who need the analytic solution play the most critical role in this stage by defining the problem, project objectives and solution requirements from a business perspective. This first stage lays the foundation for a successful resolution of the business problem. To help guarantee the project's success, the sponsors should be involved throughout the project to provide the domain expertise, review intermediate findings and ensure the work remains on track to generate the intended solution."_ — **John B. Rollins**

---


## Purpose

Everything in this stage is expressed in **business language** — no algorithms, no metrics, no technical jargon. The goal is to leave this stage with a crystal-clear understanding of what the client needs, why they need it, and how they will measure success. The translation into an analytical problem happens in [Stage 2: Analytic Approach](./02_analytic_approach.md).

> 💡 **Freelancer's note:** This is the stage where projects are won or lost. A poorly understood business problem leads to a technically correct but useless solution. Invest time here.

---


## Step 1: Stakeholder Meeting & Information Gathering

Meet with all relevant stakeholders — business sponsors, domain experts, and end-users — to gather the information you need to define the problem.

**Actions:**
- Schedule and attend initial meeting(s).
- Identify who the **decision-maker** is (the person who defines "done").
- Identify **domain experts** you can consult throughout the project.
- Take detailed notes.

**Guiding Questions:**

| Category | Questions |
| :--- | :--- |
| **The Problem** | What specific problem are we trying to solve? What is happening now that shouldn't be? What is *not* happening that should be? |
| **The Desired Outcome** | What does success look like in business terms? How will the business measure impact (revenue, cost reduction, time saved, customer satisfaction)? |
| **The Current Process** | How is this task currently performed? What are the pain points? What decisions are being made, and by whom? |
| **The End-User** | Who will use the solution? What is their technical level? How will they interact with it (dashboard, report, API, spreadsheet)? |
| **Constraints** | What is the timeline? What is the budget? Are there regulatory or data privacy constraints (GDPR, HIPAA, etc.)? |
| **Data Intuition** | What data does the client think is relevant? Do they already collect it? Where does it live? |

```markdown
## Meeting Notes
* **Date:** [YYYY-MM-DD]
* **Attendees:** 
    * [Name — Role]
* **Key Takeaways:**
    * [Summarize the most important points]
* **Open Questions:**
    * [List anything that needs follow-up]
* **Action Items:**
    * [Who does what by when]
```



---

## Step 2: Define the Business Problem

Distill everything from Step 1 into a single, clear problem statement. This is the anchor for the entire project — every decision downstream should trace back to this statement.

**Actions:**
- Write a one-to-three sentence business problem statement.
- Ensure it describes the **current situation**, the **negative impact**, and the **desired change**.
- Validate the statement with the stakeholder: *"Is this what we're solving?"*

```markdown
## Business Problem Statement
[A clear, concise summary of the business problem.

Example (classification): "Customer churn in the premium subscription tier has increased
by 15% over the last two quarters, resulting in ~$2M annual revenue loss. The business
needs to identify at-risk customers early enough to intervene with targeted retention offers."

Example (regression): "The manual process for estimating property values takes 3 days per
assessment and produces inconsistent results across assessors. The business needs a faster,
more consistent estimation method."

Example (clustering/exploration): "The marketing team sends the same campaign to all 50,000
customers. They believe distinct customer segments exist but have no data-driven way to
identify them."]
```

---

## Step 3: Define Project Objectives & Success Criteria

Translate the business problem into **specific, measurable goals**. These are still in business terms — not model metrics. Model metrics come in [Stage 2](./02_analytic_approach.md).

**Actions:**
- Define a primary objective (the main goal).
- Define secondary objectives (nice-to-haves, insights).
- Define how the business will measure success (the **business metric**, not the model metric).

```markdown
## Project Objectives & Success Criteria
1. **Primary Objective:** [What must the solution achieve?]
   Example: "Reduce premium-tier churn rate from 15% to below 10% within six months."

2. **Secondary Objective(s):** [What additional value should the solution provide?]
   Example: "Identify the top factors driving churn to inform product and marketing strategy."

3. **Success Criteria:** [How will the business judge whether the project succeeded?]
   Example: "The retention campaigns informed by the model must outperform the current
   blanket-email approach by at least 20% in conversion rate."
```

> ⚠️ **Common pitfall:** Don't let the success criteria be "build a model with 95% accuracy." That's a technical metric, not a business outcome. The business cares about reduced churn, increased revenue, or faster decisions — not F1 scores.



---

## Step 4: Define Solution Requirements

Outline what the final deliverable must look like from the client's perspective. This shapes every downstream decision — from the [Analytic Approach](./02_analytic_approach.md) to the [Deployment](./09_deployment.md) strategy.

**Actions:**
- Define the **output format** (What does the client receive?).
- Define the **delivery mechanism** (How do they receive it?).
- Define **interpretability needs** (Do they need to understand *why*?).
- Define the **update cadence** (One-time analysis or recurring predictions?).

```markdown
## Solution Requirements
* **Output:** [What the solution produces]
  Example: "A ranked list of at-risk customers with a risk score and the top 3 contributing factors."

* **Delivery:** [How it reaches the end-user]
  Example: "An interactive Streamlit dashboard refreshed weekly."
  Example: "A CSV report emailed every Monday."
  Example: "A REST API that the client's CRM system can call in real-time."

* **Interpretability:** [How explainable does it need to be?]
  Example: "The business team must understand why each customer was flagged."
  Example: "A black-box prediction score is acceptable."

* **Cadence:** [One-time or recurring?]
  Example: "One-time segmentation analysis with a final report."
  Example: "Recurring weekly predictions integrated into the CRM."
```

> 💡 The delivery requirement directly influences your [Deployment](./09_deployment.md) approach. A one-time report is a Jupyter Notebook export. A recurring prediction needs an [API](../04_mlops/02_api_development/) or a scheduled pipeline. A visual deliverable needs a [dashboard](../04_mlops/05_interactive_dashboards/). Clarify this now.

---

## Step 5: Documentation & Stakeholder Sign-Off

Package everything from Steps 1–4 into a single document and get formal agreement before any technical work begins.

**Actions:**
- Compile the Business Understanding document (this file, filled in).
- Send to stakeholders for review.
- Incorporate feedback and resolve any ambiguities.
- Secure sign-off — this is the agreement on *what* you're building.

```markdown
## Sign-Off
* **Date:** [YYYY-MM-DD]
* **Reviewed By:** [Name — Role]
* **Key Revisions:**
    * [Summarize any changes made during the review]
* **Status:** [Approved / Pending Revisions]
```

> ⚠️ **Why sign-off matters:** Without it, scope creep is inevitable. The client may later say *"But I also wanted X."* This document is your mutual agreement. It protects both sides.

---

## Checklist

Before moving to [Stage 2: Analytic Approach](./02_analytic_approach.md), confirm:

- [ ] I met with stakeholders and documented the discussion.
- [ ] The business problem is stated in one clear sentence.
- [ ] Project objectives are specific and measurable in business terms.
- [ ] Success criteria are defined from the business perspective (not model metrics).
- [ ] The output format, delivery mechanism, and cadence are agreed upon.
- [ ] The stakeholder has reviewed and signed off on this document.

---

**Next:** [Analytic Approach](./02_analytic_approach.md) — Translating the business problem into an analytical framework.