from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socket = SocketIO()


@socket.on('connect')
def client_connect():
    print("connected to server")


@socket.on("disconnect")
def client_disconnect():
    emit("message", "disconneted")


@socket.on('message')
def handle_room1(message):
    send(message=message, broadcast=True)


if __name__ == '__main__':
    socket.init_app(app, cors_allowed_origins="*") # allow cors origin
    socket.run(app, debug=True)