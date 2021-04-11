#!/usr/bin/env ruby

require 'thrift'
$:.push('gen-rb')
require 'calculadora'
require 'calculadora_types'

class CalculadoraHandler
  def initialize()
    @log = {}
  end

  def ping()
    puts "ping()"
  end

  def suma(n1, n2)
    print "sumando ", n1, " y ", n2, "\n"
    return n1 + n2
  end

  def resta(n1, n2)
    print "restando ", n1, " y ", n2, "\n"
    return n1 - n2
  end

  def multiplicacion(n1, n2)
    print "multiplicando ", n1, " y ", n2, "\n"
    return n1 * n2
  end

  def division(n1, n2)
    print "dividiendo ", n1, " y ", n2, "\n"
    return n1 / n2
  end

  def potencia(n1, n2)
    print "potencia de ", n1, " elevado a ", n2, "\n"
    return n1 ** n2
  end

  def raiz(n1)
    print "raiz de ", n1, "\n"
    return Math.sqrt(n1)
  end

  def factorial(n1)
    print "factorial de ", n1, "\n"
    return (1..n1).inject(:*) || 1
  end

  def sen(n1)
    print "seno de ", n1, "\n"
    res = Math.sin(n1 * Math::PI / 180)
    return res.round(3)
  end

  def arc_sen(n1)
    print "arcoseno de ", n1, "\n"
    res = Math::asin(n1) /  (Math::PI / 180)
    return res.round(2)
  end

  def cos(n1)
    print "coseno de ", n1, "\n"
    res = Math.cos(n1 * Math::PI / 180)
    return res.round(3)
  end

  def arc_cos(n1)
    print "arcocoseno de ", n1, "\n"
    res = Math::acos(n1) /  (Math::PI / 180)
    return res.round(2)
  end

  def tan(n1)
    print "tangente de ", n1, "\n"
    res = Math.tan(n1 * Math::PI / 180)
    return res.round(3)
  end

  def arc_tan(n1)
    print "arcotangente de ", n1, "\n"
    res = Math::atan(n1) /  (Math::PI / 180)
    return res.round(2)
  end
end

handler = CalculadoraHandler.new()
processor = Calculadora::Processor.new(handler)
transport = Thrift::ServerSocket.new(9090)
transportFactory = Thrift::BufferedTransportFactory.new()
server = Thrift::SimpleServer.new(processor, transport, transportFactory)

puts "Starting the server..."
server.serve()
puts "done."
