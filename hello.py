# hello.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello👋, World 🌍!'

@app.route('/config')
def trino_config():
    response_data = {
        "data": {
            "catalogs": [
                {
                    "catalog": "hive_odf_s3",
                    "allow": "all"
                },
                {
                    "user": "sudip",
                    "catalog": "postgresql",
                    "allow": "read-only"
                },
                {
                    "catalog": "system",
                    "allow": "none"
                }
            ]
        }
    }
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
