import os
import requests
from datetime import datetime

# =========================
# CONFIG
# =========================

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# =========================
# CORE LOGIC
# =========================

date = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

market_permission = "ALLOWED"
positive = 3
negative = 1

report = f"""
🛡️ AUREXIS – MARKET STATUS

📅 {date}

🟢 Market Permission: {market_permission}
📈 Positive Assets: {positive}
📉 Negative Assets: {negative}

Policy:
Capital moves only with permission.

Disclaimer:
This is not investment advice.
"""

# =========================
# TELEGRAM SEND (SAFE)
# =========================

if TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID:
    try:
        response = requests.post(
            f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",
            json={
                "chat_id": TELEGRAM_CHAT_ID,
                "text": report
            },
            timeout=10
        )
        response.raise_for_status()
        print("✅ Telegram message sent")
    except Exception as e:
        print("❌ Telegram error:", e)
else:
    print("⚠️ Telegram env vars missing")

# =========================
# LOCAL OUTPUT
# =========================

print(report)
