# Projeto-Redes-de-Computadores
Projeto de redes de computadores

# Servidor de Chat Simples em Python

Este é um servidor de chat simples em Python que permite que os clientes se conectem e conversem entre si. O servidor é implementado usando soquetes (sockets) e threads para gerenciar várias conexões de clientes simultaneamente.

## Funcionalidades

- **Conexão de Clientes:** Os clientes podem se conectar ao servidor especificando o endereço IP e a porta.

- **Chat em Tempo Real:** Os clientes podem enviar mensagens em tempo real para todos os outros clientes conectados ao servidor.

- **Bem-vindo Personalizado:** Quando um cliente se conecta, ele recebe uma mensagem de boas-vindas personalizada com seu nome.

- **Desconexão Graciosa:** Os clientes podem digitar `quit` para sair do chat. Quando um cliente se desconecta, todos os outros clientes são notificados.

- **Encerramento Controlado:** O servidor pode ser encerrado digitando `quit` no terminal do servidor. Isso encerra todas as conexões de clientes antes de fechar o servidor.

## Como Usar

1. Certifique-se de ter o Python instalado em seu sistema.

2. Clone este repositório:

   ```bash
   git clone https://github.com/seu-usuario/servidor-de-chat-python.git
   cd servidor-de-chat-python
