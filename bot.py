from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN, LOG_CHANNEL
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
import asyncio
from utils.helpers import send_log

# -------------------------
# Fake HTTP server for Koyeb health check
# -------------------------
class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

def run_server():
    server = HTTPServer(("0.0.0.0", 8080), HealthHandler)
    server.serve_forever()

threading.Thread(target=run_server).start()

# -------------------------
# Telegram Bot Setup
# -------------------------
app = Client(
    "welcome_request_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="handlers")
)

print("🤖 Bot started successfully")

# -------------------------
# Send log on bot start
# -------------------------
async def bot_start_log():
    await send_log(app, "🤖 Bot restarted successfully")

# Schedule log after bot starts
asyncio.get_event_loop().create_task(bot_start_log())

app.run()
