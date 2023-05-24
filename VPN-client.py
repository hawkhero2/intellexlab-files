#!/usr/bin/env python3

import os
import subprocess
import tkinter
from typing import Optional, Tuple, Union
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# class Main(customtkinter.CTk):
#     def check_creds():
#         creds.iconify()
#         vpn_status.withdraw()

#     def button_disconnect_vpn():
#         # os.system("vpnclient stop")
#         print("terminating connection...")

#     def button_connect_vpn():
#         # os.system("vpnclient start")
#         print("connecting vpnclient...")


#     def __init__(self, master):
#         super().__init__(master)
#         self.geometry("500x250")
#         self.title("VPN")
#         self.resizable(False,False)
        
#         self.disconnect_btn = customtkinter.CTkButton(self, 
#                                                 text = "Disconnect",  
#                                                 command = button_disconnect_vpn)

#         self.disconnect_btn.place(relx = 0.65, rely = 0.8)
#         self.creds_btn = customtkinter.CTkButton(self, 
#                                             text = "Settings", 
#                                             command = check_creds)

#         self.creds_btn.place(relx = 0.35, rely = 0.8)


# class Settings(customtkinter.CTk):
#     def __init__(self, master):
#         super().__init__(master)
#         self.acc_input = customtkinter.CTkEntry(self, placeholder_text="account",str= tkinter.DOTBOX)
        
#         def save_creds():
#             credentials.__setitem__("acc", acc_input)

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
    os.system("vpnclient stop >/dev/null 2>&1")
    print("terminating connection...")

def button_connect_vpn():
    os.system("sudo vpnclient start")
    print("connecting vpnclient...")

vpn_status = customtkinter.CTk()
vpn_status.geometry("500x250")
vpn_status.title("VPN")
vpn_status.resizable(False,False)


disconnect_btn = customtkinter.CTkButton(vpn_status, 
                                         text = "Disconnect",  
                                         command = button_disconnect_vpn)

disconnect_btn.place(relx = 0.65, rely = 0.8)
creds_btn = customtkinter.CTkButton(vpn_status, 
                                    text = "Settings", 
                                    command = check_creds)
connect_btn = customtkinter.CTkButton(vpn_status, 
                                      text = "Connect",
                                      command = button_connect_vpn)
connect_btn.place(relx = 0.35, rely = 0.8 )
creds_btn.place(relx = 0.35, rely = 0.8)

 # ------------------------------------------------------------------
creds = customtkinter.CTk() 
creds.geometry("300x300")
creds.title("VPN")
creds.withdraw()

def save_creds():
    # print("You connected " + acc_input.get())
    credentials.__setitem__("acc", acc_input.get())
    credentials.__setitem__("pw", pwd_input.get())

    print("your login credentials are: acc:"+
          credentials.get("acc")+
          " with the password: "+credentials.get("pw"))
    
    creds.withdraw()
    vpn_status.iconify()

acc_input = customtkinter.CTkEntry(creds, placeholder_text = "account")
acc_input.place(in_ = creds, relx = 0.25, rely = 0.3)

pwd_input = customtkinter.CTkEntry(creds, 
                                   placeholder_text = "password")
pwd_input.place(in_= creds, relx = 0.25, rely = 0.4)


button = customtkinter.CTkButton(master = creds, 
                                 text = "Save", 
                                 command = save_creds)

button.place(relx=0.25, rely=0.6)

creds.resizable(False,False)
vpn_status.mainloop()