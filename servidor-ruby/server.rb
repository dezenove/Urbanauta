require 'socket'

urbanauta_server = TCPServer.new('localhost', 20000);
loop do
  Thread.start(urbanauta_server.accept) do |s|
    print(s, " is accepted.\n")
    s.write(Time.now)
    print(s, " is gone.\n")
    s.close
  end
end
