# Virtual Store - Flask API

## Overview

This project is a Flask API for a virtual store, facilitating conversations between users and AI agents.

## Features

- User Conversations with AI Agents
- Integration with Django Backend for data management

## Requirements

- Python 3.10+
- Flask
- Flask-CORS
- crewai
- crewai[tools]
- gunicorn

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/bdonyan/store-crew.git
    cd store-crew
    ```

2. **Create a virtual environment:**

    ```sh
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Run the development server:**

    ```sh
    gunicorn app:app
    ```

## Usage

Once the server is running, you can access the API at `http://127.0.0.1:8000/`. Use the API endpoints to interact with the AI agents.

## API Endpoints

- `POST /get_response_tor` - Get a response from the Tor agent
- `POST /get_response_mika` - Get a response from the Mika agent
- `POST /get_response_kaa` - Get a response from the Kaa agent

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss any changes.

## License

This project is licensed under the MIT License. See the LICENSE file for more information.
