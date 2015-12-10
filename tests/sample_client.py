# -*- coding: utf-8 -*-

import time
import uuid

import zmq
import ujson as json
import signal
import sys

def client(pattern=zmq.DEALER, addr='tcp://localhost:7000'):
    c = zmq.Context()
    sock = c.socket(pattern)
    sock.connect(addr)
    return sock

#sigint handler
def signal_handler(signal, frame):
	print("SIGINT used, Exiting")
	sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.pause()

def run(sock, req='hello world'):

    # sock.setsockopt_string(zmq.IDENTITY, u'fancy client'),

    req = {
        'from': sock.getsockopt_string(zmq.IDENTITY),
        'id': "%s" % uuid.uuid4(),
        'type': 'data',
        'method': 'GET',
        'uri': '/ping?a=b&c=d',
        'auth': ('username', 'passwd'),
        'headers': {
            'Content-type': 'application/json',
            'Accept': 'text/plain'
        },
        'body': 'sample body',
        'user-data': 'test client',
    }

    request = json.dumps(req)
    sock.send(request)

    return sock.recv_multipart()

    """
    while True:
        print sock.recv_multipart()
        time.sleep(1)
    """

def main():
    sock = client()
    print run(sock)

if __name__ == '__main__':
    main()
