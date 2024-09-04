# PocketAPI Flask Template

## Overview
PocketAPI is a lightweight Flask API template designed to be modular and easy to use, with support for multiple environments and Docker deployment.

## Features
- **Environment Management:** Configurations for development, testing, and production.
- **Modular Routing:** Organize routes in separate files for better maintainability.
- **Logging:** Integrated logging configurable via environment variables.
- **Error Handling:** Custom error pages for better user feedback and debugging.

## Setup

### Prerequisites
- Python 3.7+
- pip (Python package manager)
- Virtual environment (recommended)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/PocketAPI.git
   cd PocketAPI
2. Set up a virtual environment
    ```bash
    python3 -m venv venv
    source venv/bin/activate
3. Install dependencies
    ```bash 
    pip install -r requirements.txt
4. Set the environment variables in your .env file as needed for each environment. (e.g., FLASK_CONFIG, SECRET_KEY, DATABASE_URL, LOG_LEVEL).

## Contributing
Feel free to submit issues or pull requests if you have suggestions or improvements.

