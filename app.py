from flask import Flask, request, jsonify, render_template
import sqlite3
from datetime import datetime

app = Flask(__name__)
DB_NAME = "aceest_fitness.db"

# Core Logic: Ported from your Aceestver-3.2.4.py
PROGRAMS = {
    "Fat Loss (FL)": 22,
    "Muscle Gain (MG)": 35,
    "Beginner (BG)": 26
}

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

# Database Initialization [cite: 10, 11]
def init_db():
    conn = get_db_connection()
    conn.execute('''CREATE TABLE IF NOT EXISTS clients 
                   (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE, weight REAL, 
                    program TEXT, calories INTEGER)''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate_calories():
    data = request.json
    name = data.get('name')
    weight = data.get('weight')
    program = data.get('program')
    
    if program in PROGRAMS:
        calories = int(weight * PROGRAMS[program])
        
        # Persistent Storage 
        conn = get_db_connection()
        conn.execute("INSERT OR REPLACE INTO clients (name, weight, program, calories) VALUES (?, ?, ?, ?)",
                     (name, weight, program, calories))
        conn.commit()
        conn.close()
        
        return jsonify({"calories": calories, "status": "Saved to Database"})
    return jsonify({"error": "Invalid program"}), 400

@app.route('/clients', methods=['GET'])
def list_clients():
    conn = get_db_connection()
    clients = conn.execute('SELECT * FROM clients').fetchall()
    conn.close()
    return jsonify([dict(row) for row in clients])

@app.route('/health')
def health():
    return {"status": "ok"}

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)