# Projeto-Redes-de-Computadores
Projeto de redes de computadores

# Servidor de Chat Simples em Python

Este é um chat simples em Python que permite que os clientes se conectem e conversem entre si. O servidor é implementado usando soquetes (sockets) e threads para gerenciar várias conexões de clientes simultaneamente.

## Funcionalidades

- **Conexão de Clientes:** Os clientes podem se conectar ao servidor especificando o endereço IP e a porta.
  
- **Definir Nome de Remetente:** Os usuários podem definir um nome de remetente que identifica suas mensagens para outros participantes do chat.

- **Envio de Mensagens:** Os usuários podem enviar mensagens para outros participantes, especificando o destinatário, o assunto e a mensagem.

- **Recebimento de Mensagens:** O cliente recebe mensagens do servidor e exibe-as na interface gráfica.

- **Chat em Tempo Real:** Os clientes podem enviar mensagens em tempo real para todos os outros clientes conectados ao servidor.

- **Encerramento Controlado:** O servidor pode ser encerrado digitando `quit` no terminal do servidor. Isso encerra todas as conexões de clientes antes de fechar o servidor.

## Como Usar

1. Certifique-se de ter o Python instalado em seu sistema.

2. Inicialize o servidor:
   	 ```bash
   python server.py
3. Execute o cliente:

   ```bash
   python client.py

4. Preencha o campo de rementente:

