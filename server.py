import paramiko
import socket
import threading
import getpass

# Prompt for the passphrase
passphrase = getpass.getpass("Enter passphrase for the key:")

# Load the key with the passphrase
HOST_KEY = paramiko.RSAKey(filename='test_rsa.key', password=passphrase)

class SimpleSSHServer(paramiko.ServerInterface):
    def check_channel_request(self, kind, chanid):
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_auth_password(self, username, password):
        if username == 'user' and password == 'password':
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED
    
    def check_channel_pty_request(self, channel, term, width, height, pixelwidth, pixelheight, modes):
        return True
    
    def check_channel_shell_request(self, channel):
        return True

def handle_client(client_socket):
    transport = paramiko.Transport(client_socket)
    transport.add_server_key(HOST_KEY)
    server = SimpleSSHServer()
    transport.start_server(server=server)

    channel = transport.accept()
    if channel is not None:
        channel.send("Welcome to the SSH Server\r\n")
        while True:
            command = channel.recv(1024).decode('utf-8')
            if command.strip() == "exit":
                break
            else:
                channel.send(f"Command received: {command}\r\n")

        channel.close()

    transport.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 2222))
    server_socket.listen(100)

    print("SSH Server running on port 2222...")
    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == '__main__':
    main()