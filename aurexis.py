# © 2025 AUREXIS.CAPITAL
# Author: Erik Severin Thüring
# Market Permission Engine – NOT a trading system

import os
import requests
from datetime import datetime

# =========================
# CONFIG
# =========================

ASSETS = ["BTCUSDT", "ETHUSDT", "BNBUSDT"]
BINANCE_API = "https://api.binance.com/api/v3/klines"
TIMEFRAME = "1d"
LOOKBACK = 120

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# =========================
# DATA
# =========================

def fetch_klines(symbol):
    r = requests.get(
        BINANCE_API,
        params={
            "symbol": symbol,
            "interval": TIMEFRAME,
            "limit": LOOKBACK
        },
        timeout=10
    )
    r.raise_for_status()
    return r.json()

def trend_direction(closes):
    return closes[-1] - closes[0]

# =========================
# ENGINE
# =========================

positive = 0
negative = 0

for asset in ASSETS:
    klines = fetch_klines(asset)
    closes = [float(k[4]) for k in klines]

    if trend_direction(closes) > 0:
        positive += 1
    else:
        negative += 1

market_permission = "ON" if positive > negative else "OFF"
date = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

# =========================
# REPORT
# =========================

report = f"""
🛡️ AUREXIS — MARKET STATUS

📅 {date}

🟢 Market Permission: {market_permission}
🟢 Positive Assets: {positive}
🔴 Negative Assets: {negative}

Policy:
Capital moves only with permission.

Disclaimer:
This is not investment advice.
"""

# =========================
# TELEGRAM
# =========================

if TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID:
    requests.post(
        f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",
        json={
            "chat_id": TELEGRAM_CHAT_ID,
            "text": report
        },
        timeout=10
    )

# =========================
# LOCAL OUTPUT
# =========================

print(report)
