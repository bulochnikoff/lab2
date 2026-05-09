import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from database import db
from models import SensorReading
from datetime import datetime

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})

@app.route('/api/readings', methods=['GET'])
def get_readings():
    readings = SensorReading.query.all()
    return jsonify([r.to_dict() for r in readings]), 200

@app.route('/api/readings', methods=['POST'])
def add_reading():
    data = request.json
    required = ['sensor_id', 'value', 'timestamp', 'lat', 'lon']
    if not all(k in data for k in required):
        return jsonify({"error": "Missing fields"}), 400
    try:
        timestamp = datetime.fromisoformat(data['timestamp'].replace('Z', '+00:00'))
    except:
        return jsonify({"error": "Invalid timestamp"}), 400
    reading = SensorReading(
        sensor_id=data['sensor_id'],
        value=data['value'],
        timestamp=timestamp,
        lat=data['lat'],
        lon=data['lon']
    )
    db.session.add(reading)
    db.session.commit()
    return jsonify(reading.to_dict()), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)