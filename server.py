from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

# Dicionário para rastrear os clientes conectados
clients = {}
addresses = {}  # Dicionário para rastrear os endereços dos clientes

# Configurações do servidor
HOST = "localhost"
PORT = 50000
ADDR = (HOST, PORT)

quit = "{quit}"  # Definindo a mensagem de saída


def accept_connections():
    """Esse loop aguarda eternamente as conexões de clientes."""
    while True:
        try:
            client, client_address = SERVER.accept()
            print(f"Conexão aceita de {client_address}")
            client.send(bytes("Digite seu nome e pressione Enter:", "utf8"))
            addresses[client] = client_address  # Armazena o endereço do cliente
            Thread(target=handle_client, args=(client,)).start()
        except Exception as e:
            print(f"Erro ao aceitar conexão: {str(e)}")
            break


def handle_client(client):
    """Lida com uma única conexão de cliente."""
    name = client.recv(1024).decode("utf8")
    client.send(bytes(f"Bem-vindo, {name}! Digite '{quit}' para sair.", "utf8"))
    msg = f"{name} entrou no chat."
    broadcast(bytes(msg, "utf8"))
    clients[client] = name

    while True:
        try:
            msg = client.recv(1024)
            if msg != bytes(quit, "utf8"):
                broadcast(msg, f"{name}: ")
            else:
                client.send(bytes(quit, "utf8"))
                client.close()
                del clients[client]
                broadcast(bytes(f"{name} saiu do chat.", "utf8"))
                break
        except Exception as e:
            print(f"Erro ao lidar com cliente {name}: {str(e)}")
            break


def broadcast(msg, prefix=""):
    """Envia uma mensagem para todos os clientes conectados."""
    for sock in clients:
        sock.send(bytes(prefix, "utf8") + msg)


if __name__ == "__main__":
    SERVER = socket(AF_INET, SOCK_STREAM)
    SERVER.bind(ADDR)
    SERVER.listen(5)
    print(f"Servidor ouvindo em {HOST}:{PORT}")

    accept_thread = Thread(target=accept_connections)
    accept_thread.start()

    while True:
        # Aguarda a entrada do servidor a partir do terminal
        server_input = input("Digite uma mensagem para enviar para todos os clientes (ou 'quit' para sair): ")

        if server_input.lower() == "quit":
            # Encerra o servidor e desconecta todos os clientes
            for client_socket in clients:
                client_socket.send(bytes(quit, "utf8"))
                client_socket.close()
            SERVER.close()
            break
        else:
            # Caso contrário, envia a mensagem para todos os clientes
            broadcast(bytes(server_input, "utf8"))
