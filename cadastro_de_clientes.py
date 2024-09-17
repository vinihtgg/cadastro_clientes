from tkinter import *

root = Tk()

class Application:
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        root.mainloop()
        
    #CRIA A TELA DA APLICAÇÃO
    def tela(self):
        self.root.title("Cadastro de Clientes")
        self.root.configure(background= "blue")
        self.root.geometry("600x500")
        self.root.resizable(True, True)
        self.root.maxsize(width= 900, height= 700)
        self.root.minsize(width= 500,height= 400)
    
    #CRIAS OS DOIS FRAMES DA TELA
    def frames_da_tela(self):
        self.frame_1 = Frame(self.root,
                             bd= 4.0, 
                             bg= "white",
                             highlightbackground= "lightblue",
                             highlightthickness= 3)
        self.frame_1.place(relx= 0.02, 
                           rely= 0.02,
                           relwidth= 0.96,
                           relheight= 0.46,)
        self.frame_2 = Frame(self.root,
                             bd= 4.0, 
                             bg= "white",
                             highlightbackground= "lightblue",
                             highlightthickness= 3)
        self.frame_2.place(relx= 0.02, 
                           rely= 0.5,
                           relwidth= 0.96,
                           relheight= 0.46,)
    
    #CRIA OS BOTÕES E CAMPO DE TEXTO
    def widgets_frame1(self):
        self.bt_limpar = Button(self.frame_1,
                                text= "Limpar")
        self.bt_limpar.place(relx= 0.2,
                             rely=0.1,
                             relwidth= 0.1,
                             relheight= 0.15)
        self.bt_limpar = Button(self.frame_1,
                                text= "Buscar")
        self.bt_limpar.place(relx= 0.3,
                             rely=0.1,
                             relwidth= 0.1,
                             relheight= 0.15)
        self.bt_limpar = Button(self.frame_1,
                                text= "Novo")
        self.bt_limpar.place(relx= 0.7,
                             rely=0.1,
                             relwidth= 0.1,
                             relheight= 0.15)
        self.bt_limpar = Button(self.frame_1,
                                text= "Alterar")
        self.bt_limpar.place(relx= 0.8,
                             rely=0.1,
                             relwidth= 0.1,
                             relheight= 0.15)
        self.bt_limpar = Button(self.frame_1,
                                text= "Apagar")
        self.bt_limpar.place(relx= 0.9,
                             rely=0.1,
                             relwidth= 0.1,
                             relheight= 0.15)
        
        self.lb_codigo = Label(self.frame_1, 
                               text= "Código")
        self.lb_codigo.place(relx= 0.05,
                             rely=0.05)
        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.05,
                                rely=0.15,
                                relwidth=0.08)
        self.lb_nome = Label(self.frame_1, 
                               text= "Nome")
        self.lb_nome.place(relx= 0.05,
                             rely=0.35)
        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.05,
                                rely=0.45,
                                relwidth=0.8)
        self.lb_telefone = Label(self.frame_1, 
                               text= "Telefone")
        self.lb_telefone.place(relx= 0.05,
                             rely=0.6)
        self.telefone_entry = Entry(self.frame_1)
        self.telefone_entry.place(relx=0.05,
                                rely=0.7,
                                relwidth=0.4)
        self.lb_telefone = Label(self.frame_1, 
                               text= "Cidade")
        self.lb_telefone.place(relx= 0.5,
                             rely=0.6)
        self.telefone_entry = Entry(self.frame_1)
        self.telefone_entry.place(relx=0.5,
                                rely=0.7,
                                relwidth=0.4)
    
Application()
