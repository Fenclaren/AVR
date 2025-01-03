from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'Client')  # Получаем параметр 'name' из строки запроса
    return jsonify({"message": f"Hello, {name}!"})


@app.route('/action', methods=['POST'])
def action():
    data = request.get_json()  # Получаем JSON из тела запроса
    if not data or 'action' not in data:
        return jsonify({"error": "Invalid request, 'action' is required"}), 400

    if data['action'] == 'ping':
        return jsonify({"status": "success", "response": "pong"})
    else:
        return jsonify({"error": "Unknown action"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001, debug=True)
