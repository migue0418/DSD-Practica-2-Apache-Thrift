# -*- coding: utf-8 -*-
from calculadora import Calculadora

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

import re


def procesa_expresion(info, client):
    info['resultado'] = 0.0
    print(info['expresion'])

    if not is_expresion_valida(info):
        print(info['error'])
        return False
    else:
        print("La expresión ha sido procesada y es válida:")
        print(info['cadena'])
        resolver_parentesis(info, -1, len(info['cadena']), client)

    print("\nEl resultado de procesar la expresión es: " + str(info['resultado']))
    return True


def is_expresion_valida(info):
    expresion = info['expresion']
    cadena = limpiar_cadena(expresion)
    num_paren = 0
    numero = False
    regex_num = re.compile('(-?\d+\.?\d*)')

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
                elif cadena[i+1] == 'r' or cadena[i+1] == 'sin' or cadena[i+1] == 'asin' or cadena[i+1] == 'cos' or cadena[i+1] == 'acos' or cadena[i+1] == 'tan' or cadena[i+1] == 'atan':
                    info['error'] = 'ERROR! Después de un ) no puede ir √, cos, tan o sin'
            elif cadena[i] == 'r' or cadena[i] == 'sin' or cadena[i] == 'asin' or cadena[i] == 'cos' or cadena[i] == 'acos' or cadena[i] == 'tan' or cadena[i] == 'atan':
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

    info['cadena'] = cadena
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
    while i < len(limpia):
        # Cambia sin¹, cos¹, tan¹ y √ por caracteres ascii
        if limpia[i] == u'√':
            cadena_limpia.append(str('r'))
        elif limpia[i] == u'sin¹':
            cadena_limpia.append(str('asin'))
        elif limpia[i] == u'cos¹':
            cadena_limpia.append(str('acos'))
        elif limpia[i] == u'tan¹':
            cadena_limpia.append(str('atan'))
        # Si encuentra un - y después un número, podría ser un número negativo, si lo encuentra el - en la última posición, no lo comprueba
        elif limpia[i] == '-' and i < len(limpia)-1 and re.match(numero, limpia[i+1]):
            # Si lo encuentra al principio, es un número negativo
            if i == 0:
                cadena_limpia.append(str("-" + limpia[i+1]))
                i += 1
            elif i < len(limpia) - 1:
                # Antes del - no hay ni !, ) o número
                if limpia[i-1] != ')' and limpia[i-1] != '!' and not re.match(numero, limpia[i-1]):
                    cadena_limpia.append(str("-" + limpia[i + 1]))
                    i += 1
                else:
                    cadena_limpia.append(str(limpia[i]))
        # Si no hay - en esa posición y después un número no hay que comprobar nada
        else:
            cadena_limpia.append(str(limpia[i]))
        i += 1

    return cadena_limpia


def resolver_parentesis(info, pos_ini, pos_fin, client):
    numero = re.compile('(-?\d+\.?\d*)')
    expresion = info['cadena']

    # Raíces, Factoriales, Potencias y Trigonometría se resuelven primero
    i = pos_ini + 1

    while i < pos_fin:
        print("Posicion " + str(i))
        print(expresion[i])
        encontrado = False
        result = ''
        # Raíz
        if expresion[i] == 'r':
            print("Ha encontrado raiz")
            cont = i+1
            # Busca el número
            while cont < pos_fin and not encontrado:
                if re.match(numero, expresion[cont]):
                    encontrado = True
                    num1 = float(expresion[cont])
                    # Raíz
                    if expresion[i] == 'r':
                        if(num1 < 0):
                            info['Error'] = 'ERROR! No se puede hacer una raíz de un número negativo!'
                            return False
                        else:
                            result = client.raiz(num1)
                            if result or result == '':
                                expresion[i] = str(result)
                                expresion[cont] = ''
                            else:
                                return False
                            print("El resultado de la raiz es ")
                            print(expresion[i])

                else:
                    cont += 1
        # sin, cos, tan
        elif expresion[i] == 'sin' or expresion[i] == 'cos' or expresion[i] == 'tan':
            print("Ha encontrado sin, cos, tan")
            cont = i+1
            while cont < pos_fin and not encontrado:
                if re.match(numero, expresion[cont]):
                    encontrado = True
                    num1 = float(expresion[cont])
                    if expresion[i] == 'sin':
                        result = client.sen(num1)
                    elif expresion[i] == 'cos':
                        result = client.cos(num1)
                    elif expresion[i] == 'tan':
                        result = client.tan(num1)

                    if result or result == '':
                        expresion[i] = str(result)
                        expresion[cont] = ''
                    else:
                        print("ERROR al hacer el sin, cos, tan")
                        return False
                    print("El resultado de la raiz es ")
                    print(expresion[i])
                else:
                    cont += 1
        # asin, acos, atan
        elif expresion[i] == 'asin' or expresion[i] == 'acos' or expresion[i] == 'atan':
            print("Ha encontrado asin, acos, atan")
            cont = i + 1
            while cont < pos_fin and not encontrado:
                if re.match(numero, expresion[cont]):
                    encontrado = True
                    num1 = float(expresion[cont])
                    print(num1)
                    if num1 <= 1 and num1 >= -1:
                        if expresion[i] == 'asin':
                            result = client.arc_sen(num1)
                        elif expresion[i] == 'acos':
                            result = client.arc_cos(num1)
                        elif expresion[i] == 'atan':
                            result = client.arc_tan(num1)

                        if result or result == '':
                            expresion[i] = str(result)
                            expresion[cont] = ''
                        else:
                            print("ERROR al hacer el sin, cos, tan")
                            return False
                        print("El resultado del arco es ")
                        print(expresion[i])
                    else:
                        info['error'] = 'ERROR! No se puede hacer un arco de número fuera de [-1, 1]'
                else:
                    cont += 1
        i += 1


    print(expresion)
        #if  expresion[i] == 'sin' or expresion[i] == 'sin¹' or expresion[i] == 'cos' or expresion[i] == 'cos¹' or expresion[i] == 'tan' or expresion[i] == 'tan¹':
    # Multiplicaciones y Divisiones

    # Sumas y Restas

    # Limpiar info['expresion`] eliminamos los espacios vacíos

    return True


def main(expresion):
    transport = TSocket.TSocket("localhost", 9090)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    client = Calculadora.Client(protocol)

    transport.open()

    print("hacemos ping al server")
    client.ping()

    hay_error = procesa_expresion(expresion, client)

    transport.close()

    return hay_error


if __name__ == "__main__":
    main('')