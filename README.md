# DSD_Apache_Thrift
Este es un proyecto de [Apache Thrift](https://thrift.apache.org/) para las prácticas de Desarrollo de Sistemas Distribuidos.

En mi caso, he decidido implementarlo en [Python](https://www.python.org/) utilizando [Django](https://www.djangoproject.com/) para desarrollar una interfaz web para la calculadora.
Consiste en un archivo cliente.py que recibirá la información de la web y la procesará enviándola a servidor.py para que realice las operaciones correspondientes.

Este proyecto ha sido desarrollado utilizando [PyCharm](https://www.jetbrains.com/pycharm/) creando un entorno virtual con Python2.7.10, Apache Thrift y Django.

Puedes ejecutar el proyecto descarganzo el zip del repositorio, abriéndolo con PyCharm. El fichero "requirements.txt" contiene las dependencias que son necesarias para el correcto funcionamiento, PyCharm debería ser capaz de instalarlas automáticamente.

Si modifica el archivo de calculadora.thrift, use este comando para mantener los archivos generados dentros de "thrift_code": thrift -gen py -out thrift_code/ calculadora.thrift

Estado del Proyecto: En Producción 🔧
