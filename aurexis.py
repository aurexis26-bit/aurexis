import os
import requests
from datetime import datetime

# =========================
# ENV VARS (GitHub Secrets)
# =========================
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# =========================
# BASIC MARKET LOGIC (DEMO)
# =========================
date = datetime.utcnow().strftime("%Y-%m-%d")

market_permission = "ALLOWED"
positive = 5
negative = 2

# =========================
# REPORT
# =========================
report = f"""
🟢 AUREXIS — MARKET STATUS

📅 Date: {date}

🟢 Market Permission: {market_permission}
📈 Positive Assets: {positive}
📉 Negative Assets: {negative}

Policy:
Capital moves only with permission.

Disclaimer:
This is not investment advice.
"""

# =========================
# TELEGRAM SEND
# =========================
if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
    raise ValueError("Missing TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID")

response = requests.post(
    f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",
    json={
        "chat_id": TELEGRAM_CHAT_ID,
        "text": report
    },
    timeout=10
)

if response.status_code != 200:
    raise RuntimeError(f"Telegram error: {response.text}")

print("Message sent successfully")
print(report)

