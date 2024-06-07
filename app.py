from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool

app = Flask(__name__)
CORS(app)

# Set environment variables
SERPER_API_KEY = os.environ.get('SERPER_API_KEY')
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

if not SERPER_API_KEY or not OPENAI_API_KEY:
    raise ValueError("Environment variables for API keys are not set.")

# Initialize agents
tor = Agent(
    role='Sales Bot',
    goal='Interacts with users, understands their needs, and communicates accordingly.',
    verbose=True,
    memory=True,
    backstory="Tor is a friendly and efficient sales bot designed to help users find the products they need.",
    tools=[],
    allow_delegation=True
)

mika = Agent(
    role='Manager',
    goal='Monitors the conversation stage, gives instructions on transitioning between stages, and ensures the conversation is on track.',
    verbose=True,
    memory=True,
    backstory="Mika oversees the conversation to ensure it is on track and helps transition between stages smoothly.",
    tools=[]
)

search_tool = SerperDevTool(api_key=SERPER_API_KEY)

kaa = Agent(
    role='Product Manager',
    goal='Searches the product inventory based on keywords provided by Tor and Mika.',
    verbose=True,
    memory=True,
    backstory="Kaa is responsible for searching the product inventory and providing accurate results.",
    tools=[search_tool],
    allow_delegation=True
)

sales_task = Task(
    description="Assist the user in finding the products they are looking for.",
    expected_output="A list of recommended products based on user input.",
    agent=tor,
    tools=[]
)

manager_task = Task(
    description="Monitor and guide the conversation.",
    expected_output="Smooth transition between conversation stages.",
    agent=mika
)

pm_task = Task(
    description="Search the product inventory based on provided keywords.",
    expected_output="Product details for the requested products.",
    agent=kaa,
    tools=[search_tool]
)

# Forming the crew
crew = Crew(
    agents=[tor, mika, kaa],
    tasks=[sales_task, manager_task, pm_task],
    process=Process.sequential,
    memory=True,
    verbose=True
)

# Define API endpoints
@app.route('/get_response_tor', methods=['POST'])
def get_response_tor():
    data = request.json
    user_input = data['user_input']
    result = search_tool.run(user_input)
    return jsonify({'response': result})

@app.route('/get_response_mika', methods=['POST'])
def get_response_mika():
    data = request.json
    user_input = data['user_input']
    result = mika.respond(user_input)
    return jsonify({'response': result})

@app.route('/get_response_kaa', methods=['POST'])
def get_response_kaa():
    data = request.json
    user_input = data['user_input']
    result = search_tool.run(user_input)
    return jsonify({'response': result})

@app.route('/')
def home():
    return "Hello, Heroku!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
