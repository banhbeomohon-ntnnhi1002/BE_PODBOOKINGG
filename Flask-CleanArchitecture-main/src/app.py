import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from flask import Flask, jsonify
from api.controllers.todo_controller import bp as todo_bp
from api.controllers.rating_controller import bp as rating_bp
from infrastructure.databases import init_db

def create_app():
    app = Flask(__name__)
    
    # Initialize database
    init_db(app)
    
    # Register blueprints
    app.register_blueprint(todo_bp)
    app.register_blueprint(rating_bp)

    @app.route("/")
    def home():
        return jsonify({
            "message": "POD Booking API",
            "status": "working",
            "endpoints": {
                "todos": "/todos/",
                "ratings": "/ratings/",
                "test": "/test"
            }
        })

    @app.route("/test")
    def test():
        return jsonify({"message": "API is working!"})

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=6868, debug=True)