A minimal Google ADK (Agent Development Kit) project that runs a single Idea Generation Agent locally and on Google Cloud Run. Use it as a quick-start template for demos, tutorials, or as a seed to grow into multi-agent apps.
What the Agent Does

Idea Generation Agent
Give it a topic, audience, or constraint and it will brainstorm concise, structured ideas. Examples:

“Video topics for explaining API gateways to beginners”

“Feature ideas for a React-based OpenAPI editor”

“LinkedIn post hooks for platform architects—keep it punchy”

You can customize prompts/instructions inside the agent file.

Prerequisites

Python 3.10+

A Google AI model key or appropriate credentials for your configured backend

(For deployment) gcloud CLI with a Google Cloud project

python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt

cp .env.example .env

Start the web UI with ADK
adk web
