import usocket as socket

s = socket.socket()
ai = socket.getaddrinfo('192.168.1.200', 80)[0][-1]
s.connect(ai)

s.send(b"GET /200 HTTP/1.0\r\nHost: 192.168.1.200\r\n\r\n")
print(s.recv(4096))
with open("/proc/uptime", 'r') as u:
    print(u.read())


s.close()
