
# MapleFreight Delivery Delay Prediction

# Problem
You are a Data Scientist at MapleFreight. Delays are currently found only after the delivery window has passed, which means paid-out service credits, expedited re-deliveries and complaints that reach the account manager before dispatch knows anything is wrong.

Build an end-to-end system that predicts which in-transit shipments will arrive late and alerts dispatch in Slack while there is still time to re-route or warn the customer.

# Dataset
- Dataset: (maplefreight_delivery_delay_dataset.csv)
- Source: [Add the original dataset source or link]
- Target variable: [Add the exact target column]
- Data preparation: []
- Leakage prevention: actual_transit_hours is excluded from
  the prediction features because it may reveal information
  that would affect model predictions.

# Models
- Logistic Regression - balanced weights
- XGBoost

# How to Run
1. Install the required dependencies:
   pip install -r requirements.txt
2. Configure the Slack webhook using your local .env file.
3. Open the notebook in Jupyter or Google Colab.
4. Ensure the dataset is available at the expected path.
5. Run the notebook from top to bottom.

# Key Findings using logistic regression 
- Best-performing model: logistic regression
- Accuracy : 75.19
- Recall: 74%
- Precision: 44%
- F1-score: 55%
- Main findings: I chose to use logistic regression because its 74% recall was higher than XGBoost's 56%. Although XGBoost had better overall accuracy, with the condition of this assignment it was best to use the model with the better recall to detect late delivery. 

# Chosen Classification Threshold
- Threshold: 0.5 the standard for logistic regression
- Rationale: I mainly used the standard threshold for model prediction. However, I will play around with the code to see if when the treshold is change, the model could make better predications. 

## Slack Alerts
The system sends an alert for each shipment predicted to be late. The message includes the shipment ID, a likely reason when supported by the model, and a recommended action.

Screenshot: (<Slack Screenshot.png>) Also included in file strucute

# AI Usage
I used ChatGPT/Codex to assist with code development, debugging, and understanding the implementation. I reviewed each code line by line to understand how it all works together. I also used materials from class such as Webhook acticity for slack activation. 

