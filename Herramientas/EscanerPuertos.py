import sys
import socket
import pyfiglet


ascii_banner = pyfiglet.figlet_format("d4l1 \n Python 4 Pentesters \nEscaner de puertos")
print(ascii_banner)


ip = '192.168.1.6' 
open_ports =[] 

ports = range(1, 65535)


def probe_port(ip, port, result = 1): 
  try: 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    sock.settimeout(0.5) 
    r = sock.connect_ex((ip, port))   
    if r == 0: 
      result = r 
    sock.close() 
  except Exception as e: 
    pass 
  return result


for port in ports: 
    sys.stdout.flush() 
    response = probe_port(ip, port) 
    if response == 0: 
        open_ports.append(port) 
    

if open_ports: 
  print ("Los puertos abiertos son: ") 
  print (sorted(open_ports)) 
else: 
  print ("No hay puertos abiertos :(")
