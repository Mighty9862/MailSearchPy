import customtkinter as ctk
import tkinter
import re

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Получение адреса из текста")
        self.geometry("800x550")
        self.resizable(False, False)
        self.grid_columnconfigure((0, 1), weight=1)

        self.button_gen = ctk.CTkButton(self, text="Получить", width=130, height=30, command=self.gen)
        self.button_gen.place(x=335, y=200)

        self.button_clear = ctk.CTkButton(self, text="Отчистить", width=130, height=30, command=self.clear)
        self.button_clear.place(x=335, y=240)

        self.button_load = ctk.CTkButton(self, text="Загрузить файл", width=130, height=30, command=self.load_file)
        self.button_load.place(x=335, y=280)

        self.box_in = ctk.CTkTextbox(self, width=300, height=500)
        self.box_in.place(x=20, y=20)

        self.box_out = ctk.CTkTextbox(self, width=300, height=500)
        self.box_out.place(x=480, y=20)

    def gen(self):
        self.box_out.delete(0.0, tkinter.END)
        my_str = self.box_in.get("0.0", "end")
        emails = re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+)", my_str)

        if not emails:
            self.box_out.insert(tkinter.END, "Почта не найдена\n")
        else:
            for mail in emails:
                self.box_out.insert(tkinter.END, str(mail) + '\n')
                self.box_out.insert(tkinter.END, "-" * 70 + '\n')

    def clear(self):
        self.box_in.delete(0.0, tkinter.END)
        self.box_out.delete(0.0, tkinter.END)

    def load_file(self):
        file_path = ctk.filedialog.askopenfilename(filetypes=[("Текстовые файлы", "*.txt")])
        if file_path:
            with open(file_path, "r", encoding="utf-8") as file:
                text = file.read()
                self.box_in.delete("0.0", tkinter.END)
                self.box_in.insert(tkinter.END, text)


app = App()
app.mainloop()
