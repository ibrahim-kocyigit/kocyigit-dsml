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
* **Attendees:** [Name — Role]
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
