from flask import Flask
from watch_events.routes import watch_bp

app = Flask(__name__)
app.register_blueprint(watch_bp)

if __name__ == '__main__':
    app.run(debug=True)
