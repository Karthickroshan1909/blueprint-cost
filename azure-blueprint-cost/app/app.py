from flask import Flask, jsonify
from datetime import datetime, timezone
import os

app = Flask(__name__)
STARTED_AT = datetime.now(timezone.utc).isoformat()

@app.get("/")
def index():
    return jsonify({
        "service": "azure-service-blueprint-demo",
        "message": "Small web service demo",
        "started_at_utc": STARTED_AT,
        "note": "Demo only: persistent storage integration is not enabled yet."
    })

@app.get("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.get("/ready")
def ready():
    # Add real dependency checks here when Blob Storage is integrated.
    return jsonify({"status": "ready"}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))
    app.run(host="0.0.0.0", port=port)
