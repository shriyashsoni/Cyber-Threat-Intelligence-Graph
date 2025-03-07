Cyber Threat Intelligence Graph

Overview

The Cyber Threat Intelligence Graph is a cybersecurity tool that helps detect malicious IPs, domains, and threats using a graph database. It integrates ArangoDB for threat data storage and OpenAI's ChatGPT API for intelligent threat analysis.

Features

Threat Data Storage: Store IP addresses, domains, and threat indicators in a graph database.

Graph-Based Analysis: Use ArangoDB to visualize connections between threats.

AI-Powered Threat Intelligence: Utilize ChatGPT to analyze and provide insights on threats.

Frontend Interface: User-friendly UI to add and query threats.

Flask Backend API: Handles threat insertion, queries, and AI-based threat analysis.

Installation

Prerequisites

Ensure you have the following installed on your system:

Python 3.8+

ArangoDB (running on http://localhost:8529)

Node.js (for frontend, optional)

Backend Setup

Clone the repository:

git clone https://github.com/your-repo/cyber-threat-graph.git
cd cyber-threat-graph/backend

Install dependencies:

pip install -r requirements.txt

Set up environment variables for OpenAI API:

export OPENAI_API_KEY='your-openai-api-key'

Start the backend server:

python app.py

The backend runs at http://localhost:5000.

Frontend Setup

Navigate to the frontend folder:

cd ../frontend

Open index.html in your browser.

API Endpoints

1. Add Threat Data

URL: /add_threat

Method: POST

Payload:

{
  "ip": "192.168.1.100",
  "domain": "malicious-site.com",
  "threat": "Phishing"
}

Response:

{ "message": "Threat added successfully" }

2. Query Threat Intelligence

URL: /query_threat?ip=192.168.1.100

Method: GET

Response:

{
  "threat_info": "This IP (192.168.1.100) is linked to phishing activities."
}

Usage

Open Frontend UI: Load index.html in a browser.

Add Threat Data: Enter an IP, domain, and threat type, then submit.

Query Threats: Search for an IP to get AI-based threat insights.

View Results: See stored threat relationships and AI responses.

Troubleshooting

Database Connection Issues? Ensure ArangoDB is running on http://localhost:8529.

OpenAI API Errors? Check your API key and network connection.

Flask Server Not Starting? Ensure all dependencies are installed correctly.

Contributors

Your Name - SHRIYASH SONI

License

This project is licensed under the MIT License.

Future Enhancements

Real-time Threat Alerts

Integration with VirusTotal API

User Authentication & Role-Based Access

