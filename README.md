# QA Chatbot

## Overview
The QA Chatbot is an AI-powered question-answering system that provides precise and relevant responses to user queries. It leverages Gemini Pro models to understand and respond intelligently.

## Features
- **Context Awareness:** Retains context for better conversational flow.
- **Chat History:** Tracks conversations for insights and improvements.

## Installation
### Prerequisites
- Python 3.8+ (tested and run on Python 3.12)
- pip
- Virtual environment (recommended)

### Setup Instructions
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/qa-chatbot.git
   cd qa-chatbot
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
- Start the chatbot and input your queries.
   ```sh
   streamlit run qachat.py
   ```
- The bot will process the input and return an appropriate response.
- Can be integrated with web or mobile applications using APIs.

## Configuration
- Create a .env file and add the following:
   ```sh
   GOOGLE_API_KEY="your api key"
   ```
