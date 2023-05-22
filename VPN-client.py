
import tkinter
from typing import Optional, Tuple, Union
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

credentials = {
    "acc":"",
    "pw":""
}

def check_creds():
    login.iconify()
    vpn_status.withdraw()

def button_disconnect_vpn():
    print("terminating connection...")

vpn_status = customtkinter.CTk()
vpn_status.geometry("500x250")
vpn_status.title("VPN")
vpn_status.resizable(False,False)

disconnect_btn = customtkinter.CTkButton(vpn_status,text = "Disconnect",command = button_disconnect_vpn)
disconnect_btn.place(relx = 0.7, rely = 0.8)
creds_btn = customtkinter.CTkButton( vpn_status, text = "Settings", command = check_creds )
creds_btn.place(relx = 0.4, rely = 0.8)


# ------------------------------------------------------------------
login = customtkinter.CTk() 
login.geometry("300x300")
login.title("VPN")
login.withdraw()

def save_creds():
    # print("You connected " + acc_input.get())
    credentials.__setitem__("acc", acc_input.get())
    credentials.__setitem__("pw", pwd_input.get())

    login.withdraw()
    vpn_status.iconify()

acc_input = customtkinter.CTkEntry(login, placeholder_text = "account")
acc_input.place(in_ = login, relx = 0.25, rely = 0.3)

pwd_input = customtkinter.CTkEntry(login, placeholder_text = "password")
pwd_input.place(in_=login, relx=0.25, rely=0.4)



# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master = login, text = "Connect", command =save_creds)
button.place(relx=0.25, rely=0.6)

# login._deactivate_windows_window_header_manipulation = True

login.resizable(False,False)
vpn_status.mainloop()