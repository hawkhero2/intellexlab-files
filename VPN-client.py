import tkinter
from typing import Optional, Tuple, Union
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

def button_disconnect_vpn():
    print("you disconnected the vpn")
    login.iconify()
    vpn_status.withdraw()
    
vpn_status = customtkinter.CTk()
vpn_status.geometry("500x250")
vpn_status.title("VPN")
vpn_status.resizable(False,False)

disconnect_btn = customtkinter.CTkButton(vpn_status,text = "Disconnect",command = button_disconnect_vpn)
disconnect_btn.place( relx = 0.5, rely = 0.5)

login = customtkinter.CTk()  # create CTk window like you do with the Tk window
login.geometry("300x300")
login.title("VPN")

def connect_button():
    print("You connected " + acc_input.get())
    login.withdraw()
    vpn_status.iconify()

acc_input = customtkinter.CTkEntry(login, placeholder_text = "account")
acc_input.place(in_ = login, relx = 0.25, rely = 0.3)

pwd_input = customtkinter.CTkEntry(login, placeholder_text = "password")
pwd_input.place(in_=login, relx=0.25, rely=0.4)



# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master = login, text = "Connect", command =connect_button)
button.place(relx=0.25, rely=0.6)

# login._deactivate_windows_window_header_manipulation = True

login.resizable(False,False)
login.mainloop()