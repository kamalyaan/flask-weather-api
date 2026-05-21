from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Bhai Pydroid se backend chal raha! LPA pakka 🔥"

@app.route('/garmi')
def garmi_ka_haal():
    return jsonify({
        "temp": "41°C", 
        "location": "New Chandigarh",
        "status": "Replit gaya bhaad mein, Pydroid zindabad"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
