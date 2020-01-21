from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socket = SocketIO()

# Nhận xử lý các sự kiện connect tới server
@socket.on("connect")
def connect():
    print("connect to server")

  
# Nhận xử lý các sự kiện connect tới server
@socket.on("disconnect")
def disconnect():
    print("disconnect to server")  

@socket.on("login")
def login(user_info=None):
    print("user_info", user_info)
    if user_info is not None:
        username = user_info.get("username", "")
        password = user_info.get("password", "")
        print("login with: ")
        print("username: ", username)
        print("password: ", password)
        socket.emit("event", f"login with {username} and {password} success")


if __name__ == "__main__":
    socket.init_app(app, cors_allowed_origins="*") # allow cors origin
    socket.run(app, debug=True)