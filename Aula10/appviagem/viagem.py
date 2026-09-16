import customtkinter as ctk

ctk.set_appearance_mode('dark')

ctk.set_default_color_theme('blue')
# funcoes --------
def calcular():
    d = int (distancia.get())
    c = float (consumo.get())
    p = float (preco.get())
    
    formula =(d/c) *p
    
    resultado.configure(text=f'O valor para a viagem é de R$ {formula:.2f}')
    

janela = ctk.CTk()

janela.geometry("500x450")

janela.resizable(False, False)

janela.title("Calculadora de Viagem")

try:
    janela.iconbitmap("appviagem/icone.ico")
except Exception:
    pass

titulo = ctk.CTkLabel(
    janela,
    text="APP VIAGEM",
    text_color="#FFFFFF",
    font=('Arial', 32, 'bold')
)

titulo.pack(pady=(35, 20))

distancia = ctk.CTkEntry(
    janela,
    width=340,
    height=42,
    border_width=2,
    border_color="#82A79C",
    fg_color="#2B2B2B",
    placeholder_text="Digite a distância da viagem em KM",
    font=('Arial', 13)
)

distancia.pack(pady=10)

consumo = ctk.CTkEntry(
    janela,
    width=340,
    height=42,
    border_width=2,
    border_color="#82A79C",
    fg_color="#2B2B2B",
    placeholder_text="Digite o consumo do seu veículo",
    font=('Arial', 13)
)

consumo.pack(pady=10)

preco = ctk.CTkEntry(
    janela,
    width=340,
    height=42,
    border_width=2,
    border_color="#82A79C",
    fg_color="#2B2B2B",
    placeholder_text="Digite o preço atual do combustível",
    font=('Arial', 13)
)

preco.pack(pady=10)

botao = ctk.CTkButton(
    janela,
    width=180,
    height=42,
    text="Calcular Gasto",
    fg_color="#FFE2DC",
    hover_color="#FCD0C7",
    text_color="#1F1F1F",
    border_color="#FF3B30",
    border_width=2,
    corner_radius=6,
    font=('Arial', 14, 'bold'),
    command=calcular)

botao.pack(pady=(25, 20))

resultado = ctk.CTkLabel(
    janela,
    text='',
    text_color='white',
    font=('Arial', 20)
)

resultado.pack(pady=10)

janela.mainloop()