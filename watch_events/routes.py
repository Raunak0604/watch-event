from flask import Blueprint, request, jsonify
from .models import create_watch_event, get_watch_history

watch_bp = Blueprint('watch_bp', __name__)

@watch_bp.route('/watch', methods=['POST'])
def log_watch_event():
    data = request.get_json()
    if not data or 'user_id' not in data or 'video_id' not in data:
        return jsonify({'error': 'Invalid input'}), 400
    event_id = create_watch_event(data['user_id'], data['video_id'])
    return jsonify({'event_id': event_id}), 201

@watch_bp.route('/watch-history', methods=['GET'])
def watch_history():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({'error': 'Invalid input'}), 400
    history = get_watch_history(user_id)
    return jsonify(history), 200
