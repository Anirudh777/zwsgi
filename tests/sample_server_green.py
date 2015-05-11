# -*- coding: utf-8 -*-

from zwsgi import monkey
monkey.patch_all()

from zwsgi.servers import *


def main():

    server = ZMQRouterReqServer(('127.0.0.1', 7000))
    print server
    server.serve_forever()


if __name__ == "__main__":
    main()
