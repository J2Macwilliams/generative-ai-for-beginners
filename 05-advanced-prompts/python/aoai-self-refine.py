from flask import Flask, request, escape, jsonify, url_for
import logging

# Initialize the Flask application
app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

def greet(name: str) -> str:
    return f'Hello, {escape(name)}!'

@app.route('/')
def hello() -> str:
    try:
        name = request.args.get('name', 'World')
        app.logger.info(f"Greeting requested for: {name}")
        return greet(name)
    except Exception as e:
        app.logger.error(f"Error during greeting: {e}")
        return jsonify({"error": "Something went wrong"}), 500

@app.route('/api/greet')
def api_greet():
    """
    An example API route that can be extended for JSON responses.
    """
    name = request.args.get('name', 'World')
    return jsonify({"message": greet(name)})

if __name__ == '__main__':
    # Use environment configuration for host, port, and debug settings
    app.run(host='0.0.0.0', port=5000, debug=app.config.get('DEBUG', True))
