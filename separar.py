#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import re

def procesaExpresion(expresion):
    result = 0.0

    cadena = is_expresion_valida(expresion)
    print("La expresión ha sido procesada y es válida:")
    for i in cadena:
        print(i),

    print("\nEl resultado de procesar la expresión es: " + str(result))
    return result


def is_expresion_valida(expresion):
    cadena = limpiar_cadena(expresion)
    num_paren = 0
    numero = False
    regex_num = re.compile('(\d+\.?\d*)')
    regex_dos_puntos = re.compile('(\d+\.+\d*\.+\d*)|(\.+\d*)')

    # Revisar la primera posición
    i = 0
    if cadena[i] == 'x' or cadena[i] == '/' or cadena[i] == '^' or cadena[i] == '+' or cadena[i] == '!':
        print("ERROR! La expresión no puede empezar por +, x, /, ^ o !")
        exit(1)

    # Revisar la última posición
    i = len(cadena) - 1
    if cadena[i] == '+' or cadena[i] == '-' or cadena[i] == 'x' or cadena[i] == '/' or cadena[i] == '^' or cadena[i] == 'r' or cadena[i] == '(':
        print("ERROR! La expresión debe acabar en !, ) o en un número")
        exit(1)    

    i = 0
    while i < (len(cadena) - 1):
        # Si es un valor numérico
        if re.match(regex_num, cadena[i]):
            try: 
                float(cadena[i])
            except:    
                print("ERROR! Uso inadecuado de \'.\'")
                exit(1)
            if numero:
                print("Error! No puede haber dos números seguidos")
                exit(1)
            else:
                numero = True
        # Valor no numérico
        else:
            if cadena[i] == '(':
                num_paren += 1
            elif cadena[i] == ')':
                num_paren -= 1
                if num_paren < 0:
                    print("ERROR! Los paréntesis no son correctos")
                    exit(1)
                elif re.match(regex_num, cadena[i+1]):
                    print("ERROR! Después de un ) no puede ir un número")
                    exit(1)
                elif cadena[i+1] == '√' or cadena[i+1] == 'sin' or cadena[i+1] == 'sin¹' or cadena[i+1] == 'cos' or cadena[i+1] == 'cos¹' or cadena[i+1] == 'tan' or cadena[i+1] == 'tan¹':
                    print("ERROR! Después de un ) no puede ir √, cos, tan o sin")
            elif cadena[i] == '√' or cadena[i] == 'sin' or cadena[i] == 'sin¹' or cadena[i] == 'cos' or cadena[i] == 'cos¹' or cadena[i] == 'tan' or cadena[i] == 'tan¹':
                if cadena[i+1] == '!' or cadena[i+1] == 'x' or cadena[i+1] == '/' or cadena[i+1] == '+' or cadena[i+1] == '-' or cadena[i+1] == '^' or cadena[i+1] == ')':
                    print("ERROR! Después de una √, cos, sin o tan no puede ir +, -, x, /, !, ) o ^")
                    exit(1)
            elif cadena[i] == '!':
                if cadena[i+1] != '+' and cadena[i+1] != '-' and cadena[i+1] != 'x' and cadena[i+1] != '/' and cadena[i+1] != '^' and cadena[i+1] != '!' and cadena[i+1] != ')':
                    print("ERROR! Después de un factorial va un operador distinto a √, sin, cos, tan o (")
                    exit(1)
            elif cadena[i].find('.') != -1:
                try: 
                    float(cadena[i])
                except:    
                    print("ERROR! Uso inadecuado de \'.\'")
                    exit(1)
            elif cadena[i] == '+' or cadena[i] == '-' or cadena[i] == 'x' or cadena[i] == '/' or cadena[i] == '^':
                if cadena[i+1] == '+' or cadena[i+1] == '-' or cadena[i+1] == 'x' or cadena[i+1] == '/' or cadena[i+1] == '^':
                    print("ERROR! Después de +, -, /, x o ^ no puede ir +, -, /, x o ^")
                    exit(1)
            numero = False
        i += 1

    if num_paren != 0:
        print("ERROR! Los paréntesis no son correctos")
        exit(1)

    return cadena


def limpiar_cadena(expresion):
    limpia = []
    cadena_limpia = []
    regex_num = re.compile('(\d+\.?\d*)')
    # Separa la expresión y la convierte en una lista
    separado = re.split('(\d+\.?\d*\.?\d*)|(sin¹?|cos¹?|tan¹?)|(\(|\)|\√|\!|\^|\/|\+|\-|x)', expresion)

    # Limpia la lista de valores nulos o vacíos
    for i in separado:
        if i != '' and i and i != '\n':
            limpia.append(i)

    # Poner los números negativos correctamente
    i = 0
    while i < len(limpia) - 2:
        if limpia[i] != ')' and limpia[i] != '!' and not re.match(regex_num, limpia[i]):
            if limpia[i+1] == '-':
                cadena_limpia.append(limpia[i])
                if re.match(regex_num, limpia[i+2]):
                    print(limpia[i+2])
                    cadena_limpia.append("-"+limpia[i+2])
                    i += 2
            else:
                cadena_limpia.append(limpia[i])
                if i == len(limpia)-3:
                    cadena_limpia.append(limpia[i+1])
                    cadena_limpia.append(limpia[i+2])
        else:
            cadena_limpia.append(limpia[i])
        i += 1

    return cadena_limpia


expresion = "9.216+62-sin¹9+(4!x√5/-6.23)x(5+-0.6)-cos¹7xtan¹cos-1"

procesaExpresion(expresion)