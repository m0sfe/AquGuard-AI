from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.get('/api/health')
def health():
    return jsonify({"ok": True, "service": "AquaGuard AI demo backend"})

@app.post('/api/refresh')
def refresh():
    payload = request.get_json(silent=True) or {}
    return jsonify({"ok": True, "received": payload})

@app.get('/api/state')
def state():
    # Dashboard falls back to offline simulation when no `segments` key is returned.
    return jsonify({"ok": True, "mode": "offline-fallback-ready"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
