from flask import Flask, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'Backend is running ✅'

@app.route('/api/listings')
def get_listings():
    with open(os.path.join('data', 'listings.json')) as f:
        listings = json.load(f)
    return jsonify(listings)

if __name__ == '__main__':
    # ✅ This allows Render to assign the correct port
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
