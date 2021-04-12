# DSD_Apache_Thrift
Este es un proyecto de [Apache Thrift](https://thrift.apache.org/) para las prácticas de Desarrollo de Sistemas Distribuidos.

En mi caso, he decidido crear una interfaz web para la calculadora implementada en [Python](https://www.python.org/) utilizando [Django](https://www.djangoproject.com/).
Consiste en un archivo cliente.py que recibirá la información de la web y la procesará enviándola a servidor.py o RubyServer.rb para que realice las operaciones correspondientes.

Este proyecto ha sido desarrollado utilizando [PyCharm](https://www.jetbrains.com/pycharm/) creando un entorno virtual con Python2.7.10, Apache Thrift y Django.
Además también usa [Ruby](https://www.ruby-lang.org/en/) junto con la [librería de thrift](https://rubygems.org/gems/thrift).

Puedes ejecutar el proyecto descargando el zip del repositorio, abriéndolo con PyCharm. 
El fichero "requirements.txt" contiene las dependencias que son necesarias para su correcto funcionamiento, PyCharm debería ser capaz de instalarlas automáticamente.
Si quieres usar el servidor de Ruby en lugar del de Python, deberás instalar las librerías necesarias para usar thrift. 

Si modifica el archivo de calculadora.thrift, use este comando para mantener los archivos generados dentros de "thrift_code": thrift -gen py -out thrift_code/ calculadora.thrift
Para los archivos de ruby usa: thrift -gen rb -out ruby/ calculadora.thrift

Estado del Proyecto: Servidor funcionando en Python y Ruby 
