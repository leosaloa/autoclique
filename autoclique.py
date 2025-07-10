import customtkinter as ctk
import pyautogui as p
from time import sleep
import keyboard

# Função entrada de dados
def entrada_dados():
    # Entrada quantidade
    cliques_txt = ctk.CTkLabel(janela,
                            text='Digite a quantidade:')
    cliques_txt.pack()
    cliques_input = ctk.CTkEntry(janela,
                        placeholder_text='Quantidade')
    cliques_input.pack()

    # Entrada intervalo
    intervalo_txt = ctk.CTkLabel(janela,
                                text='Digite o intervalo:')
    intervalo_txt.pack()
    intervalo_input = ctk.CTkEntry(janela,
                            placeholder_text='Intervalo')
    intervalo_input.pack()

    botao = ctk.CTkButton(janela,
                    text='Iniciar',
                    width=50,
                    height=50,
                    corner_radius=100,
                    fg_color='#0E53B5',
                    hover_color='#1370F5',
                    command=lambda: iniciar(cliques_input, intervalo_input))
    botao.pack(pady=6)

# Função obter dados com botão
def iniciar(entrada_cliques, entrada_intervalo):
    qtde = int(entrada_cliques.get())
    intervalo_tratar = entrada_intervalo.get().replace(',', '.')

    if intervalo_tratar == '':
        intervalo = 0.1
    else:
        intervalo = float(intervalo_tratar)

    auto_clique(qtde, intervalo)

# Função rodar o auto clique
def auto_clique(qtde_cliques, intervalo):
    sleep(3)
    count = 0
    for _ in range(qtde_cliques):
        while keyboard.is_pressed('esc') != True:
            count += 1
            p.click()
            sleep(intervalo)
            break
    fim_cliques(count)

# Função finalizar cliques
def fim_cliques(qtde_cliques):
    popup = ctk.CTkToplevel(janela)
    popup.title('Fim')
    popup.geometry('180x60')

    if qtde_cliques <= 1:
        label = ctk.CTkLabel(popup, text=f'Clique finalizado.')
    else:
        label = ctk.CTkLabel(popup, text=f'Quantidade de cliques: {qtde_cliques}.')
    label.pack()
    botao_fechar = ctk.CTkButton(popup, text='Fechar', width=20, height=10,command=popup.destroy)
    botao_fechar.pack(pady=5)
    
# Criar interface
janela = ctk.CTk()
janela.geometry('220x150')
janela.title('Cliques')

entrada_dados()
 
janela.mainloop()
#teste