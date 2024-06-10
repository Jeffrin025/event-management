import streamlit as st
import requests
API_URL = "http://127.0.0.1:5000"

# Function to get events from the API
def get_events():
    response = requests.get(f"{API_URL}/events")
    if response.status_code == 200:
        return response.json()
    else:
        return []

# Function to get attendees from the API
def get_attendees():
    response = requests.get(f"{API_URL}/attendees")
    if response.status_code == 200:
        return response.json()
    else:
        return []

# Function to get schedules from the API
def get_schedules():
    response = requests.get(f"{API_URL}/schedules")
    if response.status_code == 200:
        return response.json()
    else:
        return []

# Function to create an event
def create_event(name, location, date):
    event_data = {"name": name, "location": location, "date": date}
    response = requests.post(f"{API_URL}/events", json=event_data)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to create event"}

# Function to create an attendee
def create_attendee(name, email):
    attendee_data = {"name": name, "email": email}
    response = requests.post(f"{API_URL}/attendees", json=attendee_data)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to create attendee"}




# Streamlit app
st.title(" Event Management System")

st.header("Create New Event")
event_name = st.text_input("Event Name")
event_location = st.text_input("Event Location")
event_date = st.date_input("Event Date")
if st.button("Create Event"):
    result = create_event(event_name, event_location, event_date.isoformat())
    st.write(result)

st.header("List of Events")
events = get_events()
for event in events:
    st.write(event)

st.header("Create New Attendee")
attendee_name = st.text_input("Attendee Name")
attendee_email = st.text_input("Attendee Email")
if st.button("Create Attendee"):
    result = create_attendee(attendee_name, attendee_email)
    st.write(result)

st.header("List of Attendees")
attendees = get_attendees()
for attendee in attendees:
    st.write(attendee)

st.header("Create New Schedule")
schedule_event_id = st.number_input("Event ID", min_value=1, step=1)
schedule_session_name = st.text_input("Session Name")
schedule_start_time = st.time_input("Start Time")
schedule_end_time = st.time_input("End Time")
if st.button("Create Schedule"):
    result = create_schedule(schedule_event_id, schedule_session_name, schedule_start_time.isoformat(), schedule_end_time.isoformat())
    st.write(result)




