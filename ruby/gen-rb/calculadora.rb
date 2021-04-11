#
# Autogenerated by Thrift Compiler (0.9.1)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#

require 'thrift'
require 'calculadora_types'

module Calculadora
  class Client
    include ::Thrift::Client

    def ping()
      send_ping()
      recv_ping()
    end

    def send_ping()
      send_message('ping', Ping_args)
    end

    def recv_ping()
      result = receive_message(Ping_result)
      return
    end

    def suma(num1, num2)
      send_suma(num1, num2)
      return recv_suma()
    end

    def send_suma(num1, num2)
      send_message('suma', Suma_args, :num1 => num1, :num2 => num2)
    end

    def recv_suma()
      result = receive_message(Suma_result)
      return result.success unless result.success.nil?
      raise ::Thrift::ApplicationException.new(::Thrift::ApplicationException::MISSING_RESULT, 'suma failed: unknown result')
    end

    def resta(num1, num2)
      send_resta(num1, num2)
      return recv_resta()
    end

    def send_resta(num1, num2)
      send_message('resta', Resta_args, :num1 => num1, :num2 => num2)
    end

    def recv_resta()
      result = receive_message(Resta_result)
      return result.success unless result.success.nil?
      raise ::Thrift::ApplicationException.new(::Thrift::ApplicationException::MISSING_RESULT, 'resta failed: unknown result')
    end

    def multiplicacion(num1, num2)
      send_multiplicacion(num1, num2)
      return recv_multiplicacion()
    end

    def send_multiplicacion(num1, num2)
      send_message('multiplicacion', Multiplicacion_args, :num1 => num1, :num2 => num2)
    end

    def recv_multiplicacion()
      result = receive_message(Multiplicacion_result)
      return result.success unless result.success.nil?
      raise ::Thrift::ApplicationException.new(::Thrift::ApplicationException::MISSING_RESULT, 'multiplicacion failed: unknown result')
    end

    def division(num1, num2)
      send_division(num1, num2)
      return recv_division()
    end

    def send_division(num1, num2)
      send_message('division', Division_args, :num1 => num1, :num2 => num2)
    end

    def recv_division()
      result = receive_message(Division_result)
      return result.success unless result.success.nil?
      raise ::Thrift::ApplicationException.new(::Thrift::ApplicationException::MISSING_RESULT, 'division failed: unknown result')
    end

    def potencia(num1, num2)
      send_potencia(num1, num2)
      return recv_potencia()
    end

    def send_potencia(num1, num2)
      send_message('potencia', Potencia_args, :num1 => num1, :num2 => num2)
    end

    def recv_potencia()
      result = receive_message(Potencia_result)
      return result.success unless result.success.nil?
      raise ::Thrift::ApplicationException.new(::Thrift::ApplicationException::MISSING_RESULT, 'potencia failed: unknown result')
    end

    def raiz(num1)
      send_raiz(num1)
      return recv_raiz()
    end

    def send_raiz(num1)
      send_message('raiz', Raiz_args, :num1 => num1)
    end

    def recv_raiz()
      result = receive_message(Raiz_result)
      return result.success unless result.success.nil?
      raise ::Thrift::ApplicationException.new(::Thrift::ApplicationException::MISSING_RESULT, 'raiz failed: unknown result')
    end

    def factorial(num1)
      send_factorial(num1)
      return recv_factorial()
    end

    def send_factorial(num1)
      send_message('factorial', Factorial_args, :num1 => num1)
    end

    def recv_factorial()
      result = receive_message(Factorial_result)
      return result.success unless result.success.nil?
      raise ::Thrift::ApplicationException.new(::Thrift::ApplicationException::MISSING_RESULT, 'factorial failed: unknown result')
    end

    def sen(num1)
      send_sen(num1)
      return recv_sen()
    end

    def send_sen(num1)
      send_message('sen', Sen_args, :num1 => num1)
    end

    def recv_sen()
      result = receive_message(Sen_result)
      return result.success unless result.success.nil?
      raise ::Thrift::ApplicationException.new(::Thrift::ApplicationException::MISSING_RESULT, 'sen failed: unknown result')
    end

    def arc_sen(num1)
      send_arc_sen(num1)
      return recv_arc_sen()
    end

    def send_arc_sen(num1)
      send_message('arc_sen', Arc_sen_args, :num1 => num1)
    end

    def recv_arc_sen()
      result = receive_message(Arc_sen_result)
      return result.success unless result.success.nil?
      raise ::Thrift::ApplicationException.new(::Thrift::ApplicationException::MISSING_RESULT, 'arc_sen failed: unknown result')
    end

    def cos(num1)
      send_cos(num1)
      return recv_cos()
    end

    def send_cos(num1)
      send_message('cos', Cos_args, :num1 => num1)
    end

    def recv_cos()
      result = receive_message(Cos_result)
      return result.success unless result.success.nil?
      raise ::Thrift::ApplicationException.new(::Thrift::ApplicationException::MISSING_RESULT, 'cos failed: unknown result')
    end

    def arc_cos(num1)
      send_arc_cos(num1)
      return recv_arc_cos()
    end

    def send_arc_cos(num1)
      send_message('arc_cos', Arc_cos_args, :num1 => num1)
    end

    def recv_arc_cos()
      result = receive_message(Arc_cos_result)
      return result.success unless result.success.nil?
      raise ::Thrift::ApplicationException.new(::Thrift::ApplicationException::MISSING_RESULT, 'arc_cos failed: unknown result')
    end

    def tan(num1)
      send_tan(num1)
      return recv_tan()
    end

    def send_tan(num1)
      send_message('tan', Tan_args, :num1 => num1)
    end

    def recv_tan()
      result = receive_message(Tan_result)
      return result.success unless result.success.nil?
      raise ::Thrift::ApplicationException.new(::Thrift::ApplicationException::MISSING_RESULT, 'tan failed: unknown result')
    end

    def arc_tan(num1)
      send_arc_tan(num1)
      return recv_arc_tan()
    end

    def send_arc_tan(num1)
      send_message('arc_tan', Arc_tan_args, :num1 => num1)
    end

    def recv_arc_tan()
      result = receive_message(Arc_tan_result)
      return result.success unless result.success.nil?
      raise ::Thrift::ApplicationException.new(::Thrift::ApplicationException::MISSING_RESULT, 'arc_tan failed: unknown result')
    end

  end

  class Processor
    include ::Thrift::Processor

    def process_ping(seqid, iprot, oprot)
      args = read_args(iprot, Ping_args)
      result = Ping_result.new()
      @handler.ping()
      write_result(result, oprot, 'ping', seqid)
    end

    def process_suma(seqid, iprot, oprot)
      args = read_args(iprot, Suma_args)
      result = Suma_result.new()
      result.success = @handler.suma(args.num1, args.num2)
      write_result(result, oprot, 'suma', seqid)
    end

    def process_resta(seqid, iprot, oprot)
      args = read_args(iprot, Resta_args)
      result = Resta_result.new()
      result.success = @handler.resta(args.num1, args.num2)
      write_result(result, oprot, 'resta', seqid)
    end

    def process_multiplicacion(seqid, iprot, oprot)
      args = read_args(iprot, Multiplicacion_args)
      result = Multiplicacion_result.new()
      result.success = @handler.multiplicacion(args.num1, args.num2)
      write_result(result, oprot, 'multiplicacion', seqid)
    end

    def process_division(seqid, iprot, oprot)
      args = read_args(iprot, Division_args)
      result = Division_result.new()
      result.success = @handler.division(args.num1, args.num2)
      write_result(result, oprot, 'division', seqid)
    end

    def process_potencia(seqid, iprot, oprot)
      args = read_args(iprot, Potencia_args)
      result = Potencia_result.new()
      result.success = @handler.potencia(args.num1, args.num2)
      write_result(result, oprot, 'potencia', seqid)
    end

    def process_raiz(seqid, iprot, oprot)
      args = read_args(iprot, Raiz_args)
      result = Raiz_result.new()
      result.success = @handler.raiz(args.num1)
      write_result(result, oprot, 'raiz', seqid)
    end

    def process_factorial(seqid, iprot, oprot)
      args = read_args(iprot, Factorial_args)
      result = Factorial_result.new()
      result.success = @handler.factorial(args.num1)
      write_result(result, oprot, 'factorial', seqid)
    end

    def process_sen(seqid, iprot, oprot)
      args = read_args(iprot, Sen_args)
      result = Sen_result.new()
      result.success = @handler.sen(args.num1)
      write_result(result, oprot, 'sen', seqid)
    end

    def process_arc_sen(seqid, iprot, oprot)
      args = read_args(iprot, Arc_sen_args)
      result = Arc_sen_result.new()
      result.success = @handler.arc_sen(args.num1)
      write_result(result, oprot, 'arc_sen', seqid)
    end

    def process_cos(seqid, iprot, oprot)
      args = read_args(iprot, Cos_args)
      result = Cos_result.new()
      result.success = @handler.cos(args.num1)
      write_result(result, oprot, 'cos', seqid)
    end

    def process_arc_cos(seqid, iprot, oprot)
      args = read_args(iprot, Arc_cos_args)
      result = Arc_cos_result.new()
      result.success = @handler.arc_cos(args.num1)
      write_result(result, oprot, 'arc_cos', seqid)
    end

    def process_tan(seqid, iprot, oprot)
      args = read_args(iprot, Tan_args)
      result = Tan_result.new()
      result.success = @handler.tan(args.num1)
      write_result(result, oprot, 'tan', seqid)
    end

    def process_arc_tan(seqid, iprot, oprot)
      args = read_args(iprot, Arc_tan_args)
      result = Arc_tan_result.new()
      result.success = @handler.arc_tan(args.num1)
      write_result(result, oprot, 'arc_tan', seqid)
    end

  end

  # HELPER FUNCTIONS AND STRUCTURES

  class Ping_args
    include ::Thrift::Struct, ::Thrift::Struct_Union

    FIELDS = {

    }

    def struct_fields; FIELDS; end

    def validate
    end

    ::Thrift::Struct.generate_accessors self
  end

  class Ping_result
    include ::Thrift::Struct, ::Thrift::Struct_Union

    FIELDS = {

    }

    def struct_fields; FIELDS; end

    def validate
    end

    ::Thrift::Struct.generate_accessors self
  end

  class Suma_args
    include ::Thrift::Struct, ::Thrift::Struct_Union
    NUM1 = 1
    NUM2 = 2

    FIELDS = {
      NUM1 => {:type => ::Thrift::Types::DOUBLE, :name => 'num1'},
      NUM2 => {:type => ::Thrift::Types::DOUBLE, :name => 'num2'}
    }

    def struct_fields; FIELDS; end

    def validate
    end

    ::Thrift::Struct.generate_accessors self
  end

  class Suma_result
    include ::Thrift::Struct, ::Thrift::Struct_Union
    SUCCESS = 0

    FIELDS = {
      SUCCESS => {:type => ::Thrift::Types::DOUBLE, :name => 'success'}
    }

    def struct_fields; FIELDS; end

    def validate
    end

    ::Thrift::Struct.generate_accessors self
  end

  class Resta_args
    include ::Thrift::Struct, ::Thrift::Struct_Union
    NUM1 = 1
    NUM2 = 2

    FIELDS = {
      NUM1 => {:type => ::Thrift::Types::DOUBLE, :name => 'num1'},
      NUM2 => {:type => ::Thrift::Types::DOUBLE, :name => 'num2'}
    }

    def struct_fields; FIELDS; end

    def validate
    end

    ::Thrift::Struct.generate_accessors self
  end

  class Resta_result
    include ::Thrift::Struct, ::Thrift::Struct_Union
    SUCCESS = 0

    FIELDS = {
      SUCCESS => {:type => ::Thrift::Types::DOUBLE, :name => 'success'}
    }

    def struct_fields; FIELDS; end

    def validate
    end

    ::Thrift::Struct.generate_accessors self
  end

  class Multiplicacion_args
    include ::Thrift::Struct, ::Thrift::Struct_Union
    NUM1 = 1
    NUM2 = 2

    FIELDS = {
      NUM1 => {:type => ::Thrift::Types::DOUBLE, :name => 'num1'},
      NUM2 => {:type => ::Thrift::Types::DOUBLE, :name => 'num2'}
    }

    def struct_fields; FIELDS; end

    def validate
    end

    ::Thrift::Struct.generate_accessors self
  end

  class Multiplicacion_result
    include ::Thrift::Struct, ::Thrift::Struct_Union
    SUCCESS = 0

    FIELDS = {
      SUCCESS => {:type => ::Thrift::Types::DOUBLE, :name => 'success'}
    }

    def struct_fields; FIELDS; end

    def validate
    end

    ::Thrift::Struct.generate_accessors self
  end

  class Division_args
    include ::Thrift::Struct, ::Thrift::Struct_Union
    NUM1 = 1
    NUM2 = 2

    FIELDS = {
      NUM1 => {:type => ::Thrift::Types::DOUBLE, :name => 'num1'},
      NUM2 => {:type => ::Thrift::Types::DOUBLE, :name => 'num2'}
    }

    def struct_fields; FIELDS; end

    def validate
    end

    ::Thrift::Struct.generate_accessors self
  end

  class Division_result
    include ::Thrift::Struct, ::Thrift::Struct_Union
    SUCCESS = 0

    FIELDS = {
      SUCCESS => {:type => ::Thrift::Types::DOUBLE, :name => 'success'}
    }

    def struct_fields; FIELDS; end

    def validate
    end

    ::Thrift::Struct.generate_accessors self
  end

  class Potencia_args
    include ::Thrift::Struct, ::Thrift::Struct_Union
    NUM1 = 1
    NUM2 = 2

    FIELDS = {
      NUM1 => {:type => ::Thrift::Types::DOUBLE, :name => 'num1'},
      NUM2 => {:type => ::Thrift::Types::DOUBLE, :name => 'num2'}
    }

    def struct_fields; FIELDS; end

    def validate
    end

    ::Thrift::Struct.generate_accessors self
  end

  class Potencia_result
    include ::Thrift::Struct, ::Thrift::Struct_Union
    SUCCESS = 0

    FIELDS = {
      SUCCESS => {:type => ::Thrift::Types::DOUBLE, :name => 'success'}
    }

    def struct_fields; FIELDS; end

    def validate
    end

    ::Thrift::Struct.generate_accessors self
  end

  class Raiz_args
    include ::Thrift::Struct, ::Thrift::Struct_Union
    NUM1 = 1

    FIELDS = {
      NUM1 => {:type => ::Thrift::Types::DOUBLE, :name => 'num1'}
    }

    def struct_fields; FIELDS; end

    def validate
    end

    ::Thrift::Struct.generate_accessors self
  end

  class Raiz_result
    include ::Thrift::Struct, ::Thrift::Struct_Union
    SUCCESS = 0

    FIELDS = {
      SUCCESS => {:type => ::Thrift::Types::DOUBLE, :name => 'success'}
    }

    def struct_fields; FIELDS; end

    def validate
    end

    ::Thrift::Struct.generate_accessors self
  end

  class Factorial_args
    include ::Thrift::Struct, ::Thrift::Struct_Union
    NUM1 = 1

    FIELDS = {
      NUM1 => {:type => ::Thrift::Types::DOUBLE, :name => 'num1'}
    }

    def struct_fields; FIELDS; end

    def validate
    end

    ::Thrift::Struct.generate_accessors self
  end

  class Factorial_result
    include ::Thrift::Struct, ::Thrift::Struct_Union
    SUCCESS = 0

    FIELDS = {
      SUCCESS => {:type => ::Thrift::Types::DOUBLE, :name => 'success'}
    }

    def struct_fields; FIELDS; end

    def validate
    end

    ::Thrift::Struct.generate_accessors self
  end

  class Sen_args
    include ::Thrift::Struct, ::Thrift::Struct_Union
    NUM1 = 1

    FIELDS = {
      NUM1 => {:type => ::Thrift::Types::DOUBLE, :name => 'num1'}
    }

    def struct_fields; FIELDS; end

    def validate
    end

    ::Thrift::Struct.generate_accessors self
  end

  class Sen_result
    include ::Thrift::Struct, ::Thrift::Struct_Union
    SUCCESS = 0

    FIELDS = {
      SUCCESS => {:type => ::Thrift::Types::DOUBLE, :name => 'success'}
    }

    def struct_fields; FIELDS; end

    def validate
    end

    ::Thrift::Struct.generate_accessors self
  end

  class Arc_sen_args
    include ::Thrift::Struct, ::Thrift::Struct_Union
    NUM1 = 1

    FIELDS = {
      NUM1 => {:type => ::Thrift::Types::DOUBLE, :name => 'num1'}
    }

    def struct_fields; FIELDS; end

    def validate
    end

    ::Thrift::Struct.generate_accessors self
  end

  class Arc_sen_result
    include ::Thrift::Struct, ::Thrift::Struct_Union
    SUCCESS = 0

    FIELDS = {
      SUCCESS => {:type => ::Thrift::Types::DOUBLE, :name => 'success'}
    }

    def struct_fields; FIELDS; end

    def validate
    end

    ::Thrift::Struct.generate_accessors self
  end

  class Cos_args
    include ::Thrift::Struct, ::Thrift::Struct_Union
    NUM1 = 1

    FIELDS = {
      NUM1 => {:type => ::Thrift::Types::DOUBLE, :name => 'num1'}
    }

    def struct_fields; FIELDS; end

    def validate
    end

    ::Thrift::Struct.generate_accessors self
  end

  class Cos_result
    include ::Thrift::Struct, ::Thrift::Struct_Union
    SUCCESS = 0

    FIELDS = {
      SUCCESS => {:type => ::Thrift::Types::DOUBLE, :name => 'success'}
    }

    def struct_fields; FIELDS; end

    def validate
    end

    ::Thrift::Struct.generate_accessors self
  end

  class Arc_cos_args
    include ::Thrift::Struct, ::Thrift::Struct_Union
    NUM1 = 1

    FIELDS = {
      NUM1 => {:type => ::Thrift::Types::DOUBLE, :name => 'num1'}
    }

    def struct_fields; FIELDS; end

    def validate
    end

    ::Thrift::Struct.generate_accessors self
  end

  class Arc_cos_result
    include ::Thrift::Struct, ::Thrift::Struct_Union
    SUCCESS = 0

    FIELDS = {
      SUCCESS => {:type => ::Thrift::Types::DOUBLE, :name => 'success'}
    }

    def struct_fields; FIELDS; end

    def validate
    end

    ::Thrift::Struct.generate_accessors self
  end

  class Tan_args
    include ::Thrift::Struct, ::Thrift::Struct_Union
    NUM1 = 1

    FIELDS = {
      NUM1 => {:type => ::Thrift::Types::DOUBLE, :name => 'num1'}
    }

    def struct_fields; FIELDS; end

    def validate
    end

    ::Thrift::Struct.generate_accessors self
  end

  class Tan_result
    include ::Thrift::Struct, ::Thrift::Struct_Union
    SUCCESS = 0

    FIELDS = {
      SUCCESS => {:type => ::Thrift::Types::DOUBLE, :name => 'success'}
    }

    def struct_fields; FIELDS; end

    def validate
    end

    ::Thrift::Struct.generate_accessors self
  end

  class Arc_tan_args
    include ::Thrift::Struct, ::Thrift::Struct_Union
    NUM1 = 1

    FIELDS = {
      NUM1 => {:type => ::Thrift::Types::DOUBLE, :name => 'num1'}
    }

    def struct_fields; FIELDS; end

    def validate
    end

    ::Thrift::Struct.generate_accessors self
  end

  class Arc_tan_result
    include ::Thrift::Struct, ::Thrift::Struct_Union
    SUCCESS = 0

    FIELDS = {
      SUCCESS => {:type => ::Thrift::Types::DOUBLE, :name => 'success'}
    }

    def struct_fields; FIELDS; end

    def validate
    end

    ::Thrift::Struct.generate_accessors self
  end

end

