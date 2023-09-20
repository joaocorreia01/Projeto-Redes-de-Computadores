from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

# Dicionário para rastrear os clientes conectados
clients = {}
addresses = {}  # Dicionário para rastrear os endereços dos clientes

# Configurações do servidor
HOST = "localhost"
PORT = 50000
ADDR = (HOST, PORT)

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
    client.send(bytes(f"Bem-vindo, {name}! Digite {quit} para sair.", "utf8"))
    msg = f"{name} entrou no chat."
    broadcast(bytes(msg, "utf8"))
    clients[client] = name

    while True:
        try:
            msg = client.recv(1024)
            if msg != bytes("{quit}", "utf8"):
                broadcast(msg, name + ": ")
            else:
                client.send(bytes("{quit}", "utf8"))
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

# ... Seu código de servidor existente ...

def send_to_all(message, sender="Servidor"):
    """Envia uma mensagem para todos os clientes conectados."""
    for client in clients:
        client.send(bytes(sender + ": " + message, "utf8"))


if __name__ == "__main__":
    SERVER = socket(AF_INET, SOCK_STREAM)
    SERVER.bind(ADDR)
    SERVER.listen(5)
    print(f"Servidor ouvindo em {HOST}:{PORT}")


    while True:
        # Aguarda a entrada do servidor a partir do terminal
        server_input = input("Digite uma mensagem para enviar para todos os clientes (ou 'quit' para sair): ")

        if server_input.lower() == "quit":
            # Se o servidor digitar 'quit', fecha o servidor e encerra o programa
            SERVER.close()
            break
        else:
            # Caso contrário, envia a mensagem para todos os clientes
            accept_thread = Thread(target=accept_connections)
            accept_thread.start()
            accept_thread.join()
            send_to_all(server_input, sender="Servidor")
