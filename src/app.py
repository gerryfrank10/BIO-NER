from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route('/')
def index():
    return "Welcome to Named Entity Recognition API"

@app.route('/ner', methods=['POST'])
def ner():
    if not request.json or 'text' not in request.json:
        return jsonify({'error': 'No text provided'}), 400

    text = request.json['text']

    # Placeholder for NER logic
    entities = {
        "PERSON": ["Alice", "Bob"],
        "ORGANIZATION": ["OpenAI"],
        "LOCATION": ["San Francisco"]
    }

    return jsonify({'entities': entities})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9000)