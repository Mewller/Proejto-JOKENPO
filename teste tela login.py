from tkinter import *
users = [ 'adimin', '123'

             
]
class LoginScreen:
    def __init__(self, master):
        self.master = master
        master.title("Tela de Login")

        # Cria os rótulos e campos de entrada
        self.label_username = Label(master, text="Usuário:")
        self.label_password = Label(master, text="Senha:")
        self.entry_username = Entry(master)
        self.entry_password = Entry(master, show="*")

        # Posiciona os rótulos e campos de entrada na tela
        self.label_username.grid(row=0, sticky=E)
        self.label_password.grid(row=1, sticky=E)
        self.entry_username.grid(row=0, column=1)
        self.entry_password.grid(row=1, column=1)

        # Cria o botão de login e cadastro
        self.login_button = Button(master, text="Login", command=self.login)
        self.register_button = Button(master, text="Registrar", command=self.register)

        # Posiciona os botões na tela
        self.login_button.grid(row=2, column=0, sticky=E)
        self.register_button.grid(row=2, column=1, sticky=W)

    def login(self):
        # Verifica se o usuário e senha estão corretos
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username and password in users:
            print("Login realizado com sucesso!")
        else:
            print("Usuário ou senha incorretos.")

    def register(self):
        # Cria uma nova janela para o cadastro de usuários
        register_window = Toplevel(self.master)
        register_screen = RegisterScreen(register_window)

class RegisterScreen:
    def __init__(self, master):
        self.master = master
        master.title("Cadastro de Usuário")

        # Cria os rótulos e campos de entrada
        self.label_username = Label(master, text="Usuário:")
        self.label_password = Label(master, text="Senha:")
        self.entry_username = Entry(master)
        self.entry_password = Entry(master, show="*")

        # Posiciona os rótulos e campos de entrada na tela
        self.label_username.grid(row=0, sticky=E)
        self.label_password.grid(row=1, sticky=E)
        self.entry_username.grid(row=0, column=1)
        self.entry_password.grid(row=1, column=1)

        # Cria o botão de cadastro
        self.register_button = Button(master, text="Cadastrar", command=self.register)

        # Posiciona o botão na tela
        self.register_button.grid(row=2, column=1, sticky=W)

    def register(self):
        # Adiciona o novo usuário ao dicionário de usuários
        username = self.entry_username.get()
        password = self.entry_password.get()


        if username in users:
            print("Usuário já cadastrado.")
        else:
            users = username, password
            print("Usuário cadastrado com sucesso!")
            print(users)

root = Tk()
login_screen = LoginScreen(root)
root.mainloop()


