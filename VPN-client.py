import tkinter
from typing import Optional, Tuple, Union
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

def get_conn_status():
    status : bool = True
    return status

connection_status : bool = get_conn_status()

credentials = {
    "acc":"",
    "pw":""
}

def check_creds():
    creds.iconify()
    vpn_status.withdraw()

def button_disconnect_vpn():
    print("terminating connection...")

vpn_status = customtkinter.CTk()
vpn_status.geometry("500x250")
vpn_status.title("VPN")
vpn_status.resizable(False,False)

if(connection_status == True):
    pass


disconnect_btn = customtkinter.CTkButton(vpn_status,text = "Disconnect",command = button_disconnect_vpn)
disconnect_btn.place(relx = 0.65, rely = 0.8)
creds_btn = customtkinter.CTkButton( vpn_status, text = "Settings", command = check_creds )
creds_btn.place(relx = 0.35, rely = 0.8)
disconnect_btn._text_color_disabled

# ------------------------------------------------------------------
creds = customtkinter.CTk() 
creds.geometry("300x300")
creds.title("VPN")
creds.withdraw()

def save_creds():
    # print("You connected " + acc_input.get())
    credentials.__setitem__("acc", acc_input.get())
    credentials.__setitem__("pw", pwd_input.get())

    print("your login credentials are: acc:"+credentials.get("acc")+" with the password: "+credentials.get("pw"))
    creds.withdraw()
    vpn_status.iconify()

acc_input = customtkinter.CTkEntry(creds, placeholder_text = "account")
acc_input.place(in_ = creds, relx = 0.25, rely = 0.3)

pwd_input = customtkinter.CTkEntry(creds, placeholder_text = "password")
pwd_input.place(in_=creds, relx=0.25, rely=0.4)


button = customtkinter.CTkButton(master = creds, text = "Connect", command = save_creds)
button.place(relx=0.25, rely=0.6)

creds.resizable(False,False)
vpn_status.mainloop()