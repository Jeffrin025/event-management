import psycopg2
from flask import Flask, request, jsonify
import streamlit as st
import requests
import json

app = Flask(__name__)

conn = psycopg2.connect(
    database="user",
    user="postgres",
    password="root",
    host="127.0.0.1",
    port="5432"
)

cur = conn.cursor()

@app.route('/events', methods=['POST'])
def create_event():
    data = request.get_json()
    cur.execute("INSERT INTO events (name, location, date) VALUES (%s, %s, %s) RETURNING event_id",
                (data['name'], data['location'], data['date']))
    conn.commit()
    return jsonify({"event_id": cur.fetchone()[0]})

@app.route('/events', methods=['GET'])
def list_events():
    cur.execute("SELECT * FROM events")
    return jsonify(cur.fetchall())

@app.route('/attendees', methods=['POST'])
def create_attendee():
    data = request.get_json()
    cur.execute("INSERT INTO attendees (name, email) VALUES (%s, %s) RETURNING attendee_id",
                (data['name'], data['email']))
    conn.commit()
    return jsonify({"attendee_id": cur.fetchone()[0]})

@app.route('/attendees', methods=['GET'])
def list_attendees():
    cur.execute("SELECT * FROM attendees")
    return jsonify(cur.fetchall())


@app.route('/schedules', methods=['POST'])
def create_schedule():
    data = request.get_json()
    cur.execute("INSERT INTO schedules (event_id, session_name, start_time, end_time) VALUES (%s, %s, %s, %s) RETURNING schedule_id",
                (data['event_id'], data['session_name'], data['start_time'], data['end_time']))
    conn.commit()
    return jsonify({"schedule_id": cur.fetchone()[0]})

@app.route('/schedules', methods=['GET'])
def list_schedules():
    cur.execute("SELECT * FROM schedules")
    return jsonify(cur.fetchall())




if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)

