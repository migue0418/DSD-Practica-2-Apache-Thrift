#!/usr/bin/env ruby

require 'thrift'
$:.push('gen-rb')
require 'calculadora'

begin
  port = ARGV[0] || 9090

  transport = Thrift::BufferedTransport.new(Thrift::Socket.new('localhost', port))
  protocol = Thrift::BinaryProtocol.new(transport)
  client = Calculadora::Client.new(protocol)

  transport.open()

  client.ping()
  print "ping()\n"

  sum = client.suma(1,1)
  print "1+1=", sum, "\n"

  sum = client.resta(1,4)
  print "1-4=", sum, "\n"

  sum = client.multiplicacion(2,5)
  print "2*5=", sum, "\n"

  sum = client.division(1,4)
  print "1/4=", sum, "\n"

  sum = client.potencia(2,5)
  print "2^5=", sum, "\n"

  sum = client.raiz(4)
  print "r4=", sum, "\n"

  sum = client.factorial(4)
  print "4!=", sum, "\n"
  
  sum = client.sen(4)
  print "sen(4)=", sum, "\n"

  sum = client.arc_sen(0.5)
  print "asen(0.5)=", sum, "\n"
  
  sum = client.cos(4)
  print "cos(4)=", sum, "\n"

  sum = client.arc_cos(0.5)
  print "acos(0.5)=", sum, "\n"
  
  sum = client.tan(4)
  print "tan(4)=", sum, "\n"

  sum = client.arc_tan(0.5)
  print "atan(0.5)=", sum, "\n"

  transport.close()

rescue Thrift::Exception => tx
  print 'Thrift::Exception: ', tx.message, "\n"
end