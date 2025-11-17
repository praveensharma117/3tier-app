from flask import Flask, jsonify, request
import os
app = Flask(__name__)
@app.route('/api/health')
def health():
    return jsonify({'status': 'ok'})
@app.route('/api/greet')
def greet():
    name = request.args.get('name', 'world')
    return jsonify({'message': f'Hello, {name}'})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
