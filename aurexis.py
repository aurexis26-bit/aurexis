import os
import requests
from datetime import datetime

# ======================
# CONFIG
# ======================
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# ======================
# MARKET LOGIC (DUMMY – stabil)
# ======================
date = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

market_permission = "GRANTED"
positive = 3
negative = 1

# ======================
# REPORT
# ======================
report = f"""
🛡️ AUREXIS – MARKET STATUS

📅 {date}

🟢 Market Permission: {market_permission}
🟢 Positive Assets: {positive}
🔴 Negative Assets: {negative}

Policy:
Capital moves only with permission.

Disclaimer:
This is not investment advice.
"""

# ======================
# TELEGRAM SEND
# ======================
if TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID:
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": report
    }

    r = requests.post(url, json=payload, timeout=10)
    print("Telegram status:", r.status_code)
else:
    print("Telegram credentials missing")

# ======================
# LOCAL OUTPUT
# ======================
print(report)
