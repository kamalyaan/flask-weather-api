from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Backend running successfully on Android! 🔥"

@app.route('/garmi')
def weather_status():
    return jsonify({
        "temp": "41°C",
        "location": "New Chandigarh",
        "status": "Server running on mobile, no cloud needed"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)