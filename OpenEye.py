import socket

target_hosts = input("Enter host address url: \n").split(",")
target_port = int(input("Enter port number: \n"))

for target_host in target_hosts:
    target_host = target_host.strip()
try:    
    #----cREATE A SOCKET Object--------
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #------connect the client
    print(f"Connecting to {target_host}:{target_port}")
    client.connect((target_host, target_port))

    #-------send some data------
    request = f"GET / HTTP/1.1\r\nHost: {target_host}\r\n\r\n"
    client.send(request.encode())

    #--------Recieve some data
    response = client.recv(4096)
    print(f"Response from {target_host}:\n{response.decode()}")
    print(response.decode())
    client.close()

except Exception as e:
    print(f"Failed to connect to {target_host}:{target_port}. Error: {e}")
