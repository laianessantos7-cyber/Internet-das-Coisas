import customtkinter as ctk
ctk.set_appearance_mode('dark')

#j  ----- JANELA -----

janela = ctk.CTk()
janela.geometry("500x300")
janela.resizable(False,False)
janela.title("Sistema de Acesso - 2026")
janela.iconbitmap("appviagem/icone.ico")


# CORPO DA JANELA
titulo = ctk.CTkLabel(janela,
                    text="Sistema de Login",
                    text_color="#030430",
                    font=('arial',40))


titulo.pack()
login = ctk.CTkEntry(janela,
                    width=400,
                    height=40,
                    border_color="#030430",
                    placeholder_text="Digite Seu Login")
login.pack(pady=30)



senha = ctk.CTkEntry(janela,
                    width=400,
                    height=40,
                    border_color="#030430",
                    placeholder_text="Digite Sua Senha",
                    show="•")
senha.pack()



botao =ctk.CTkButton(janela,
                    width=200,
                    height=40,
                    text="Acessar",
                    fg_color="#030430",
                    text_color="white",
                    cursor ="heart",
                    font=('arial', 30))
botao.pack(pady=30)




janela.mainloop()