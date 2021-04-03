# -*- coding: utf-8 -*-
from calculadora import Calculadora

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

import re


def procesa_expresion(info):
    info['resultado'] = 0.0
    print(info['expresion'])

    if not is_expresion_valida(info):
        print(info['error'])
        return False
    else:
        print("La expresión ha sido procesada y es válida:")

    print("\nEl resultado de procesar la expresión es: " + str(info['resultado']))
    return True


def is_expresion_valida(info):
    expresion = info['expresion']
    print(expresion)
    cadena = limpiar_cadena(expresion)
    print(cadena)
    num_paren = 0
    numero = False
    regex_num = re.compile('(\d+\.?\d*)')

    # Revisar la primera posición
    i = 0
    if cadena[i] == 'x' or cadena[i] == '/' or cadena[i] == '^' or cadena[i] == '+' or cadena[i] == '!':
        info['error'] = 'ERROR! La expresión no puede empezar por +, x, /, ^ o !'
        return False

    # Revisar la última posición
    i = len(cadena) - 1
    if cadena[i] == ')':
        num_paren -= 1
    elif cadena[i] == '(':
        num_paren += 1
        info['error'] = 'ERROR! Los paréntesis no son correctos'
        return False
    elif not re.match(regex_num, cadena[i]) and cadena[i] != '!':
        info['error'] = 'ERROR! La expresión debe acabar en !, ) o en un número'
        return False

    # Revisar el resto
    i = 0
    while i < (len(cadena) - 1):
        # Si es un valor numérico
        if re.match(regex_num, cadena[i]):
            try:
                float(cadena[i])
            except:
                info['error'] = 'ERROR! Uso inadecuado de .'
                return False

            if numero:
                info['error'] = 'ERROR! No puede haber dos números seguidos'
                return False
            else:
                numero = True
        # Valor no numérico
        else:
            if cadena[i] == '(':
                num_paren += 1
            elif cadena[i] == ')':
                num_paren -= 1
                if num_paren < 0:
                    info['error'] = 'ERROR! Los paréntesis no son correctos'
                    return False
                elif re.match(regex_num, cadena[i+1]):
                    info['error'] = 'ERROR! Después de un ) no puede ir un número'
                    return False
                elif cadena[i+1] == u'√' or cadena[i+1] == 'sin' or cadena[i+1] == 'sin¹' or cadena[i+1] == 'cos' or cadena[i+1] == 'cos¹' or cadena[i+1] == 'tan' or cadena[i+1] == 'tan¹':
                    info['error'] = 'ERROR! Después de un ) no puede ir √, cos, tan o sin'
            elif cadena[i] == u'√' or cadena[i] == 'sin' or cadena[i] == u'sin¹' or cadena[i] == 'cos' or cadena[i] == u'cos¹' or cadena[i] == 'tan' or cadena[i] == u'tan¹':
                if cadena[i+1] == '!' or cadena[i+1] == 'x' or cadena[i+1] == '/' or cadena[i+1] == '+' or cadena[i+1] == '-' or cadena[i+1] == '^' or cadena[i+1] == ')':
                    info['error'] = 'ERROR! Después de una √, cos, sin o tan no puede ir +, -, x, /, !, ) o ^'
                    return False
            elif cadena[i] == '!':
                if cadena[i+1] != '+' and cadena[i+1] != '-' and cadena[i+1] != 'x' and cadena[i+1] != '/' and cadena[i+1] != '^' and cadena[i+1] != '!' and cadena[i+1] != ')':
                    info['error'] = 'ERROR! Después de un factorial va un operador distinto a √, sin, cos, tan o ('
                    return False
            elif cadena[i].find('.') != -1:
                try:
                    float(cadena[i])
                except:
                    info['error'] = 'ERROR! Uso inadecuado de \'.\''
                    return False
            elif cadena[i] == '+' or cadena[i] == '-' or cadena[i] == 'x' or cadena[i] == '/' or cadena[i] == '^':
                if cadena[i+1] == '+' or cadena[i+1] == '-' or cadena[i+1] == 'x' or cadena[i+1] == '/' or cadena[i+1] == '^':
                    info['error'] = 'ERROR! Después de +, -, /, x o ^ no puede ir +, -, /, x o ^'
                    return False
            numero = False
        i += 1

    if num_paren != 0:
        info['error'] = 'ERROR! Los paréntesis no son correctos'
        return False

    return True


def limpiar_cadena(expresion):
    limpia = []
    cadena_limpia = []
    numero = re.compile('(\d+\.?\d*)')
    # Separa la expresión y la convierte en una lista
    separado = re.split('(\d+\.?\d*\.?\d*)|(sin¹?|cos¹?|tan¹?)|(\(|\)|\√|\!|\^|\/|\+|\-|x)', expresion)

    # Limpia la lista de valores nulos o vacíos
    for i in separado:
        if i != '' and i and i != '\n':
            limpia.append(i)

    # Poner los números negativos correctamente
    i = 0

    print("Va a limpiarla: ")
    for j in limpia:
        print(j)

    i = 0
    while i < len(limpia):
        # Si encuentra un - y después un número, podría ser un número negativo, si lo encuentra el - en la última posición, no lo comprueba
        if limpia[i] == '-' and i < len(limpia)-1 and re.match(numero, limpia[i+1]):
            # Si lo encuentra al principio, es un número negativo
            if i == 0:
                cadena_limpia.append("-" + limpia[i+1])
                i += 1
            elif i < len(limpia) - 1:
                # Antes del - no hay ni !, ) o número
                if limpia[i-1] != ')' and limpia[i-1] != '!' and not re.match(numero, limpia[i-1]):
                    cadena_limpia.append("-" + limpia[i + 1])
                    i += 1
                else:
                    cadena_limpia.append(limpia[i])
        # Si no hay - en esa posición y después un número no hay que comprobar nada
        else:
            cadena_limpia.append(limpia[i])
        i += 1

    print("Esta es la cadena que sale: ")
    for i in cadena_limpia:
        print(i)

    return cadena_limpia


def main(expresion):
    transport = TSocket.TSocket("localhost", 9090)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    client = Calculadora.Client(protocol)

    transport.open()

    print("hacemos ping al server")
    client.ping()

    hayError = procesa_expresion(expresion)

    transport.close()

    return hayError


if __name__ == "__main__":
    main('')