# Auto Clique

🖱️ Auto Clicker com Interface Bonitinha (CustomTkinter)
Bem-vindo a primeira versão do projeto de cliques automáticos feito com Python! 😎
Simples, direto ao ponto e com uma interface elegante usando o customtkinter + um toque de automação com pyautogui.

📦 Tecnologias Usadas
🐍 Python 3+

🎨 CustomTkinter — Para deixar a interface lindona

🖱️ PyAutoGUI — Para fazer os cliques automáticos

⌨️ Keyboard — Para capturar a tecla de parada

⚙️ Como Funciona
Digite a quantidade de cliques 🧮

Digite o intervalo entre cada clique (em segundos) ⏱️

Clique no botão Iniciar 🚀

O programa espera 3 segundos... e começa a clicar sozinho!

Para parar a execução, basta apertar a tecla ESC 🛑

🧪 Exemplo
makefile
Copiar
Editar
Quantidade: 10
Intervalo: 0.5
💥 Resultado: O mouse vai clicar 10 vezes, com 0.5 segundos de intervalo entre cada clique.

📁 Estrutura do Código
entrada_dados(): Cria os campos de input e o botão Iniciar

iniciar(): Pega os valores digitados e prepara a chamada

auto_clique(): Faz os cliques automáticos usando o pyautogui

fim_cliques(): Abre um popup fofo dizendo quantos cliques foram feitos 😄

🔐 Segurança
O código usa keyboard.is_pressed('esc') para você poder parar a qualquer momento. Isso é muito útil caso você erre a quantidade ou esqueça o que estava fazendo 😅

🛠️ Instalação
Instale as dependências com:

bash
Copiar
Editar
pip install customtkinter pyautogui keyboard
E execute com:

bash
Copiar
Editar
python nome_do_arquivo.py

💡 Dica
Foi adicionado 3 segundos antes de iniciar, para posicionar o mouse. E, se precisar sair, ESC é seu melhor amigo.

