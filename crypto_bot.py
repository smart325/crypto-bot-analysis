import time, os, schedule, requests, pandas as pd
from indicators import compute_indicators
from utils import send_email

COINS = [
    "bitcoin", "ethereum", "floki", "ordinals", "0x", "elrond",
    "axie-infinity", "smooth-love-potion", "celer-network",
    "ether-fi", "pingu", "manta-network", "metis-token", "scroll",
    "dydx", "lukso-token", "optimism", "bonfida", "dymension",
    "dodo", "layerzero", "rocket-pool"
]

def fetch_prices(coin):
    url = f"https://api.coingecko.com/api/v3/coins/{coin}/market_chart?vs_currency=usd&days=1&interval=5m"
    res = requests.get(url).json()
    data = pd.DataFrame(res['prices'], columns=['timestamp', 'close'])
    data['close'] = data['close'].astype(float)
    return compute_indicators(data)

def scan_and_alert():
    for coin in COINS:
        df = fetch_prices(coin)
        last = df.iloc[-1]
        msg = []
        if last['rsi'] < 30:
            msg.append('🔵 BUY signal (RSI < 30)')
        elif last['rsi'] > 70:
            msg.append('🔴 SELL signal (RSI > 70)')
        if last['ma50'] > last['ma200']:
            msg.append('📈 bullish (MA50 > MA200)')
        elif last['ma50'] < last['ma200']:
            msg.append('📉 bearish (MA50 < MA200)')
        if msg:
            subject = f"{coin.upper()} Signal"
            body = f"{coin.upper()} price {last['close']:.4f}\n" + "\n".join(msg)
            send_email(subject, body)

def main():
    schedule.every(5).minutes.do(scan_and_alert)
    while True:
        schedule.run_pending()
        time.sleep(1)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

