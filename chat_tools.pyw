# coding: utf-8
from tkinter import *
from api import *
import time
import os
pseudo="Poloisirs"
class Application(Tk):
    lblConnecte=None;
    
    lblPseudo=None;
    
    btnEnable=None;
    btnDisable=None;
    lblOnOff=None;
    
    btnDebut=None;
    btnFin=None;
    
    moteur=None;
    
    def onClose(self):
        #self.moteur.stop();
        self.destroy()

    def __init__(self):
        Tk.__init__(self)
        
        self.title("chat_tools minetest")
        self.minsize(200, 200)
        self.maxsize(200, 200)
        self.resizable(0,0)
        self.attributes("-toolwindow", 1)
        self.protocol("WM_DELETE_WINDOW", self.onClose)

        self.creer_widgets()
        
        
         
        
        #self.after(1000, self.updateStatus)     

    
    def actualiser(self):
        if os.system('ping 192.168.1.29'):
            self.déconnecté()
        else:

            self.lblConnecte.config(bg='green',fg='black',text='Connecté');
            self.btnSend.config(state=NORMAL)
            self.saisi.config(state=NORMAL)
            self.lblPseudo.config(text="pseudo:%s" % pseudo)
    def déconnecté(self):
        self.lblConnecte.config(bg='gray',fg='white',text='Non connecté');
        self.btnSend.config(state=DISABLED)
        self.saisi.config(state=DISABLED)
        self.lblPseudo.config(text="pseudo:?")
        self.after(10000, self.actualiser)
    def env(pseudo, message):
        minetest.postToChat(pseudo, message)
    def envoyer(self):
        message = self.saisi.get()
        Application.env(pseudo, message)

    def creer_widgets(self):
        self.lblConnecte = Label ( self,
              text="Non connecté",
              height=1,
              font=("Arial Bold",10),
              bg='gray',
              border=4
              );            
        self.lblConnecte.pack(side=TOP,fill=X)
        
        frm=Frame(self)
        frm.pack(side=TOP,fill=X);         
        self.lblPseudo = Label ( frm,
              text="pseudo=?",
              height=1,
              font=("Arial Bold",10)
              );            
        self.lblPseudo.grid(row=0,column=1)


        # Activation
        frm=Frame(self)
        frm.pack(side=TOP,fill=X);
        self.saisi = Entry(self, width=10)
        self.saisi.pack(side=TOP,fill=X)
        self.btnSend=Button(self,
                              text="Envoyer",
                              font=("Arial Bold",10),
                              command=self.envoyer,
                              state='disabled'                               
                               )
        self.btnSend.pack(side=TOP,fill=X) 

if __name__ == "__main__":
    app = Application()
    #app.update()
    app.actualiser()
    app.mainloop()


#panel_state=PanedWindow(bd=4,orient=HORIZONTAL,relief='raised',bg='red');
#panel_state.pack(fill=BOTH);


# sp1 = Label ( w,
#               text="1",
#               width=5,
#               height=5,
#               font=("Arial Bold",10),
#               bg='red',
#               border=4
#               );
# sp1.grid(row = 0, column = 0, sticky = W, pady = 5) 
# 
# sp2 = Label ( w,
#               text="2",
#               width=5,
#               height=5,
#               font=("Arial Bold",10),
#               bg='red',
#               border=4
#               );
# sp2.grid(row = 0, column = 1, sticky = W, pady = 5) 




#Button = (button
