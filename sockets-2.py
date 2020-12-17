import socket
MSGLEN = 10


class MySocket:
    """demonstration class only
      - coded for clarity, not efficiency
    """

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                            socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))

    def mysend(self, msg):
        totalsent = 0
        while totalsent < MSGLEN:
            sent = self.sock.send(msg)
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent

    def myreceive(self):
        chunks = []
        bytes_recd = 0
        while bytes_recd < MSGLEN:
            # chunk = self.sock.recv(min(MSGLEN - bytes_recd, 2048))
            chunk = self.sock.recv(2048)
            if chunk == b'':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
        return b''.join(chunks)


if __name__ == '__main__':
    sock = MySocket()
    sock.connect("www.globalshop.co.il", 80)
    # sock.mysend(msg=b'Hello, world')
    sock.mysend(msg=b'''HTTP/1.0 200 OK
Content-Type: text/plain

Hello, world!

''')
    sock.myreceive()