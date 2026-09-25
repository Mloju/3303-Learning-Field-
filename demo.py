import requests
import time

WEBHOOK_URL = "https://hooks.slack.com/services/XXXXX/XXXXX/XXXXX"

def send_slack_message(message):
    payload = {"text": message}
    response = requests.post(WEBHOOK_URL, json=payload)

    print(response.status_code)
    print(response.text)

send_slack_message("Hello from Python! 🚀")

for epoch in range(1, 6):
    accuracy = 0.7 + epoch * 0.05

    msg = f"Training Update - Epoch {epoch}: Accuracy = {accuracy:.2f}"

    send_slack_message(msg)

    time.sleep(2)

send_slack_message("✅ Training Completed!")