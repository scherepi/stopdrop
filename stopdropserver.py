import socket
import random
r = random.Random()

HOST = "127.0.0.1"
PORT = 46907

# TODO: actually fully implement function
def genPrompt():
    choices = ["GORGE", "PHREAK", "FIRE"]
    arg_count = r.randint(1,6)
    response = ""
    i = 0
    while (i < arg_count):
        response += choices[r.randint(0,2)] + " "
        i += 1
    print("sending prompt: " + response)


# TODO: use with s.makefile() to do socket I/O on a file-like object instead of the raw socket
# TODO: implement working server loop - currently just sends a prompt and waits for input that it might not even be able to fully receive
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print("connection from " + addr)
        while True:
            conn.sendall(genPrompt().encode())
            input = conn.recv(1024)