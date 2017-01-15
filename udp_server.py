from socketserver import BaseRequestHandler, UDPServer
import time
class TimeHandler(BaseRequestHandler):
def handle(self):
print('I have a connection from', self.client_address)
# wait for message and client socket
msg, sock = self.request
resp = time.ctime()
sock.sendto(resp.encode('ascii'), self.client_address)
if __name__ == '__main__':
serv = UDPServer(('', 30000), TimeHandler)
serv.serve_forever()


