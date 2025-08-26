import os
import uvicorn
from google.adk.cli.fast_api import get_fast_api_app

AGENT_DIR = os.path.dirname(os.path.abspath(__file__))
SESSION_SERVICE_URI ="sqlite:///./sessions.db"
ALLOWED_ORIGINS = ["http://localhost", "http://localhost:8080", "*"]

SERVE_WEB_INTERFACE = True

app = get_fast_api_app(
    agents_dir  = AGENT_DIR,
    session_db_kwargs = {"database_url":SESSION_SERVICE_URI},
    allow_origins = ALLOWED_ORIGINS,
    web = SERVE_WEB_INTERFACE
)

if __name__ == "__main__":
        uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT",8080)))
        