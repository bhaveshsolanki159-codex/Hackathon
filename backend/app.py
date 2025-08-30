from flask import Flask
from flask_cors import CORS
from routes.chat_routes import chat_bp

app = Flask(__name__)

# Enable CORS for frontend requests (localhost:5173)
CORS(app)

# Register blueprints (routes)
app.register_blueprint(chat_bp, url_prefix="/api")


@app.route("/ping", methods=["GET"])
def ping():
    """Health check route"""
    return {"message": "Server is running"}, 200


if __name__ == "__main__":
    # Run Flask backend
    app.run(host="0.0.0.0", port=5000, debug=True)
