from flask import Flask, jsonify
import json

app = Flask(__name__)

# Load dữ liệu
with open("airports.json", "r") as f:
    airports = json.load(f)

@app.route('/airport/<icao>')
def get_airport(icao):
    for airport in airports:
        if airport["icao"].lower() == icao.lower():
            return jsonify(airport)

    return jsonify({"error": "Airport not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)