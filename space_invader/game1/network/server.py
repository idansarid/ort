import socket
from _thread import *
import time
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = 'localhost'
port = 5555

server_ip = socket.gethostbyname(server)

try:
    s.bind((server, port))

except socket.error as e:
    print(str(e))

s.listen(2)
print("Waiting for a connection")

currentId = "0"
# pos = [("0:50,50"), ("1:100,100")]
pos = [(0, 0), (100, 100)]

coor = {0: "", 1: ""}


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


def read_pos(str):
    str1 = str.split(",")
    return int(str1[0]), int(str1[1])


def threaded_client(conn, player):
    global currentId, pos
    # conn.send(str.encode(make_pos(pos[player])))
    conn.send(str.encode(currentId))
    currentId = "1"
    reply = ''
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode('utf-8')
            if "player" in str(reply):
                players = str(player)
                conn.sendall(str.encode(players))
                continue
            elif "Coordinates" in reply:
                # coor[player] = " "
                cor = str(reply).split(":")
                coor[player] = cor[1]
                print("{} {}".format(player, reply))
                conn.sendall(str.encode(str("OK")))
                continue
            elif "getPlayerData" in reply:
                ss = str(reply).split(" ")
                player_get = int(ss[1])
                reply = coor[player_get]
                conn.sendall(str.encode(str(reply)))
                continue
            pos[player] = data

            if not data:
                print("Disconnected")
                break
            # else:
            #     pass
            #     if player == 1:
            #         reply = pos[0]
            #     else:
            #         reply = pos[1]

                # print("Received: ", data)
                # print("Sending : ", reply)

            #conn.sendall(str.encode(make_pos(reply)))
            conn.sendall(str.encode(reply))
        except:
            break

    print("Connection Closed")
    conn.close()


currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1