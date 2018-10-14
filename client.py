import socket
import json




ADDRESS = "localhost"
PORT = 7777

def get_client_socket():
    s = socket.socket()
    s.connect((ADDRESS, PORT))
    data = {
        "text": input("Input text: "),
        "user": input("Input username: "),
        "age": int(input("Input age: "))
    }

    s.send(json.dumps(data).encode("utf-8"))

    print("Data sended")
    return s
