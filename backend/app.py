from flask import Flask, request, jsonify
import openai
from pyArango.connection import Connection

# Initialize Flask app
app = Flask(__name__)

# ArangoDB Connection
try:
    conn = Connection(arangoURL='http://localhost:8529', username='root', password='password')
    db = conn['cybersecurity']
except Exception as e:
    print(f"Database connection error: {e}")
    exit()

# Create Graph
def create_graph():
    try:
        if 'ThreatGraph' not in db.graphs:
            graph = db.createGraph('ThreatGraph')
            graph.createVertexCollection('IP_Address')
            graph.createVertexCollection('Domain')
            graph.createVertexCollection('Threat_Indicator')
            graph.createEdgeDefinition(
                edgeCollection='Connections',
                fromCollections=['IP_Address', 'Domain'],
                toCollections=['Threat_Indicator']
            )
    except Exception as e:
        print(f"Error creating graph: {e}")

@app.route('/add_threat', methods=['POST'])
def add_threat():
    data = request.json
    try:
        graph = db.graphs['ThreatGraph']
        graph['IP_Address'].createDocument({'_key': data['ip']}).save()
        graph['Domain'].createDocument({'_key': data['domain']}).save()
        graph['Threat_Indicator'].createDocument({'_key': data['threat']}).save()
        graph['Connections'].createDocument({'_from': f'IP_Address/{data["ip"]}', '_to': f'Threat_Indicator/{data["threat"]}'}).save()
        return jsonify({'message': 'Threat added successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/query_threat', methods=['GET'])
def query_threat():
    ip = request.args.get('ip')
    try:
        response = openai.ChatCompletion.create(
            model='gpt-4',
            messages=[{'role': 'system', 'content': f'Provide threat intelligence on IP: {ip}'}]
        )
        return jsonify({'threat_info': response['choices'][0]['message']['content']}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    create_graph()
    app.run(debug=True, host='0.0.0.0', port=5000)
