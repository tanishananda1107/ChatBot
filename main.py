from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/extract', methods=['POST'])
def extract_outline():
    file = request.files['pdf']
    # Your PDF logic here
    return jsonify({"result": "outline here"})

if __name__ == '__main__':
    app.run()
