import tkinter
from typing import Optional, Tuple, Union
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

class VpnStatus(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.geometry("500x250")
        self.title("VPN")

        self.disconnect_btn = customtkinter.CTkButton(self,text = "Disconnect",command = button_disconnect_vpn)
        self.disconnect_btn.place( relx = 0.5, rely = 0.5)
        self.mainloop()

def button_disconnect_vpn():
    print("you disconnected the vpn")
    app.iconify()
    
    
    # check Softether page to make use of the terminal commands?
    # https://www.softether.org/4-docs/1-manual/7._Installing_SoftEther_VPN_Server/7.3_Install_on_Linux_and_Initial_Configurations

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("300x300")
app.title("VPN")

def button_function():
    print("Hello there: "+acc_input.get())
    app.withdraw()
    vpn_status = VpnStatus()

# acc_label = customtkinter.CTkLabel(master=app, text="Account")

acc_input = customtkinter.CTkEntry(app, placeholder_text = "account")
acc_input.place(in_ = app, relx = 0.25, rely = 0.3)

pwd_input = customtkinter.CTkEntry(app, placeholder_text = "password")
pwd_input.place(in_=app, relx=0.25, rely=0.4)



# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master = app, text = "Connect", command = button_function)
button.place(relx=0.25, rely=0.6)

# app._deactivate_windows_window_header_manipulation = True

app.resizable(False,False)
app.mainloop()