"""def solution(n):
    lst = [2]
    for i in range(3, 10001, 2):
        if (i > 10) and (i % 10 == 5):
            continue
        for j in lst:
            if j * j - 1 > i:
                lst.append(i)
                break
            if (i % j == 0):
                break
        else:
            lst.append(i)
    single_long_string = "".join([str(i) for i in lst])
    return single_long_string[n:n + 5]


if __name__ == "__main__":
    i = input("Draw number from a hat: ")
    print(solution((int)(i)))

players=["a","b","c","d"]
player_scores = {player: 0 for player in players}
print(player_scores)
"""
# echo-server.py

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #AF_INET is the Internet address family for IPv4. SOCK_STREAM is the socket type for TCP
    s.bind((HOST, PORT))#The .bind() method is used to associate the socket with a specific network interface and port number
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
