from flask import Flask, jsonify
import os
import socket
from datetime import datetime, timezone

app = Flask(__name__)

VERSION = os.getenv("APP_VERSION", "v1.0.0")

@app.route("/")
def home():
    return f"""
    <html>
    <head>
        <title>PlatformOps Kubernetes Lab</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #eef4fb;
                text-align: center;
                padding: 70px 20px;
            }}
            .card {{
                background: white;
                padding: 35px;
                border-radius: 14px;
                max-width: 550px;
                margin: auto;
                box-shadow: 0 8px 30px #c9d6e5;
            }}
            h1 {{ color: #205b9f; }}
            .version {{ color: #14805e; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>PlatformOps - Automated GitOps Release</h1>
            <h2 class="version">{VERSION}</h2>
            <p>Containerized Flask Application</p>
            <p>Pod: {socket.gethostname()}</p>
            <p>Release: v1.2.0</p>
	    <p>Deployment: GitHub Actions + GHCR + Argo CD</p>
	    <p>Managed using Kubernetes + Helm</p>
        </div>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify(status="healthy"), 200

@app.route("/ready")
def ready():
    return jsonify(status="ready"), 200

@app.route("/api/info")
def info():
    return jsonify(
        application="PlatformOps",
        version=VERSION,
        hostname=socket.gethostname(),
        timestamp=datetime.now(timezone.utc).isoformat()
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5252)
