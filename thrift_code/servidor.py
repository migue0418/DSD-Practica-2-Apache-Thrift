from calculadora import Calculadora

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

from math import *

import logging

logging.basicConfig(level=logging.DEBUG)


class CalculadoraHandler:
    def __init__(self):
        self.log = {}

    def ping(self):
        print("me han hecho ping()")

    def suma(self, n1, n2):
        print("sumando " + str(n1) + " con " + str(n2))
        return n1 + n2

    def resta(self, n1, n2):
        print("restando " + str(n1) + " con " + str(n2))
        return n1 - n2

    def multiplicacion(self, n1, n2):
        print("multiplicando " + str(n1) + " con " + str(n2))
        return n1 * n2

    def division(self, n1, n2):
        print("dividiendo " + str(n1) + " con " + str(n2))
        return n1 / n2

    def potencia(self, n1, n2):
        print("potencia de " + str(n1) + " elevado a " + str(n2))
        return pow(n1, n2)

    def raiz(self, n1):
        print("raiz de " + str(n1))
        return sqrt(n1)

    def factorial(self, n1):
        print("factorial de " + str(n1))
        return factorial(n1)

    def sen(self, n1):
        print("seno de " + str(n1))
        return sin(radians(n1))

    def arc_sen(self, n1):
        print("arcoseno de " + str(n1))
        print(radians(n1))
        return asin(radians(n1))

    def cos(self, n1):
        print("coseno de " + str(n1))
        return cos(radians(n1))

    def arc_cos(self, n1):
        print("arcocoseno de " + str(n1))
        return acos(radians(n1))

    def tan(self, n1):
        print("tangente de " + str(n1))
        return tan(radians(n1))

    def arc_tan(self, n1):
        print("arcotangente de " + str(n1))
        return atan(radians(n1))


def main():
    handler = CalculadoraHandler()
    processor = Calculadora.Processor(handler)
    transport = TSocket.TServerSocket(host="127.0.0.1", port=9090)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    print("iniciando servidor...")
    server.serve()
    print("fin")


if __name__ == "__main__":
    main()
