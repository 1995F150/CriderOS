
from flask import Flask, request, jsonify
from flask_cors import CORS
import google.oauth2.id_token
import google.auth.transport.requests

app = Flask(__name__)
CORS(app)

@app.route('/verify', methods=['POST'])
def verify_token():
    token = request.json.get('token')
    request_adapter = google.auth.transport.requests.Request()
    try:
        id_info = google.oauth2.id_token.verify_oauth2_token(token, request_adapter)
        email = id_info.get('email')
        return jsonify({'email': email})
    except Exception as e:
        return jsonify({'error': str(e)}), 401

if __name__ == '__main__':
    app.run(debug=True)
