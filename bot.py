from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

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

app.run()
