import tkinter
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("500x600")

def button_function():
    print("Hello there: "+acc_input.get())

# acc_label = customtkinter.CTkLabel(master=app, text="Account")

acc_input = customtkinter.CTkEntry(app, placeholder_text="account")
acc_input.place(in_ = app, relx = 0.1, rely = 0.1)

pwd_input = customtkinter.CTkEntry(app, placeholder_text = "password")
pwd_input.place(in_=app, relx=0.1, rely=0.17)

# textbox.place(in_=app, relx=0.2, rely=0.1,anchor=tkinter.N)
# acc_label.place(in_=app, relx=0.4,rely=0.4,anchor=tkinter.CENTER)

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master = app, text = "Connect", command = button_function)
button.place(relx=0.1, rely=0.25)

# app._deactivate_windows_window_header_manipulation = True

app.resizable(False,False)
app.mainloop()