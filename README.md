# AI-Driven Customer Churn Retention & Decision Automation

![BPMN Process Diagram](camunda_models/churn_process.png)
*(Automated Business Process Flow via BPMN)*

![DMN Decision Table](camunda_models/churn_decision.png)
*(Automated Decision Engine via DMN based on Churn Probability)*

---

## Business Problem
In the telecommunications industry, acquiring a new customer is often 5 to 25 times more expensive than retaining an existing one. However, businesses typically face two major hurdles:
1. **Reactive Approach:** Customer service interventions only occur when the customer has already requested to cancel their subscription, which is often too late.
2. **Inefficient Budget Allocation:** Distributing promotional vouchers uniformly to all customers—including those with no intention of leaving or those with low profit margins—results in significant marketing budget waste.

## AI Solution
To address these challenges, this project leverages **Machine Learning** (trained on the Telco Customer Churn dataset) to proactively assess customer health.
Instead of a simple binary prediction (Churn vs. No Churn), the AI model is calibrated to output a **Churn Probability**. For instance, a customer might have an 85% risk of churning in the upcoming month.

By integrating this probability with the **Customer Lifetime Value (LTV)**, the system categorizes customers into distinct segments. This enables the business to identify high-value VIP customers requiring immediate retention efforts versus Standard customers who only need basic engagement.

## Business Automation with Camunda
A predictive probability is only actionable when integrated into real-world business operations. This project utilizes **Camunda (BPMN & DMN)** to fully automate the decision-making pipeline, ensuring zero-touch operations without manual intervention.

- **DMN (Decision Model and Notation):** Acts as the business logic engine. It takes the *Churn Probability* (from the AI model) and *Customer Segment* (VIP/Standard) as inputs, then evaluates them against predefined business rules to output a concrete retention action:
  - `VIP Customer + High Risk (>= 70%)` -> Issue a 30% discount voucher and trigger a direct customer care call.
  - `Standard Customer + High Risk` -> Send an automated SMS with complimentary 4G data.
- **BPMN (Business Process Model and Notation):** Orchestrates the end-to-end data flow. It manages the pipeline from retrieving customer data (Start Event), requesting the AI prediction (Service Task), passing data to the DMN engine for evaluation (Business Rule Task), to executing the final retention action such as an Email or SMS (Send Task).

## Expected Outcomes
- **Increased Retention Rate:** Ensures customers receive the right intervention at the right time through the appropriate channel.
- **Cost Optimization:** Strategically allocates promotional budgets (vouchers, data packages) exclusively to high-value customers genuinely at risk of churning.
- **Zero-touch Operations:** The entire retention pipeline operates autonomously in real-time, significantly reducing the manual workload for the Customer Success team and minimizing response latency.

---
## Tech Stack & Tools Used
- **Machine Learning & Data Processing:** `Python`, `scikit-learn`, `XGBoost`, `Pandas`, `NumPy`, `Joblib`
- **Environment & Modeling:** `Jupyter Notebook`
- **Business Process Automation:** `Camunda Modeler`, `BPMN 2.0`, `DMN 1.3`

---
## Repository Structure
- `/data`: Contains the raw Telco Customer Churn dataset (CSV).
- `/notebooks`: Contains the Jupyter Notebook for training the AI model and the exported model artifacts (`.pkl`).
- `/camunda_models`: Contains the BPMN/DMN design schemas and exported visual diagrams.
- `main.py`: A simulation script that demonstrates the end-to-end integration flow (AI Inference -> DMN Decision -> Execution).

## How to Run the Simulation
1. Install the required dependencies:
   ```bash
   pip install pandas numpy joblib scikit-learn
   ```
2. Execute the main script:
   ```bash
   python main.py
   ```
3. Observe the console logs to see the AI analysis and automated DMN decisions in action.
