from flask import Blueprint, jsonify
from services.db_service import get_history

history_bp = Blueprint("history", __name__)

@history_bp.route("/<user_id>", methods=["GET"])
def history(user_id):
    chats = get_history(user_id)
    return jsonify(chats)
