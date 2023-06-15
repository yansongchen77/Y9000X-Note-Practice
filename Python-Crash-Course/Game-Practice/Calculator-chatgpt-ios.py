import tkinter as tk
from tkinter import font

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        master.geometry("350x560")
        master.resizable(width=False, height=False)

        # 设置按钮和文本框字体
        self.button_font = font.Font(size=20)
        self.equation_font = font.Font(size=30)

        # 创建显示方程的文本框
        self.equation = tk.Entry(master, width=12, font=self.equation_font, borderwidth=0, justify=tk.RIGHT)
        self.equation.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipady=15)

        # 创建数字按钮
        self.create_button("C", 1, 0, bg="white", fg="black", width=4, height=2)
        self.create_button("±", 1, 1, bg="white", fg="black", width=4, height=2)
        self.create_button("%", 1, 2, bg="white", fg="black", width=4, height=2)
        self.create_button("÷", 1, 3, bg="#FF9500", fg="white", width=4, height=2)

        self.create_button("7", 2, 0, bg="#E4E4E4", fg="black")
        self.create_button("8", 2, 1, bg="#E4E4E4", fg="black")
        self.create_button("9", 2, 2, bg="#E4E4E4", fg="black")
        self.create_button("×", 2, 3, bg="#FF9500", fg="white", width=4, height=2)

        self.create_button("4", 3, 0, bg="#E4E4E4", fg="black")
        self.create_button("5", 3, 1, bg="#E4E4E4", fg="black")
        self.create_button("6", 3, 2, bg="#E4E4E4", fg="black")
        self.create_button("-", 3, 3, bg="#FF9500", fg="white", width=4, height=2)

        self.create_button("1", 4, 0, bg="#E4E4E4", fg="black")
        self.create_button("2", 4, 1, bg="#E4E4E4", fg="black")
        self.create_button("3", 4, 2, bg="#E4E4E4", fg="black")
        self.create_button("+", 4, 3, bg="#FF9500", fg="white", width=4, height=2)

        self.create_button("0", 5, 0, bg="#E4E4E4", fg="black", width=8)
        self.create_button(".", 5, 2, bg="#E4E4E4", fg="black")
        self.create_button("=", 5, 3, bg="#FF9500", fg="white", width=4, height=2)

    def create_button(self, text, row, column, bg="#F0F0F0", fg="black", width=2, height=1):
        # 创建按钮
        button = tk.Button(self.master, text=text, bg=bg, fg=fg, width=width, height=height, font=self.button_font,
                           borderwidth=0, command=lambda: self.button_click(text))
        button.grid(row=row, column=column, padx=5, pady=5, ipady=5, sticky="NSEW")

    def button_click(self, text):
        if text == "C":
            self.equation.delete(0, tk.END)
        elif text == "±":
            equation = self.equation.get()
            if equation.startswith("-"):
                self.equation.delete(0)
                self.equation.insert(0, equation[1:])
            elif equation:
                self.equation.insert(0, "-")
        elif text == "%":
            equation = self.equation.get()
            try:
                result = float(equation) / 100
                self.equation.delete(0, tk.END)
                self.equation.insert(0, result)
            except ValueError:
                pass
        elif text in ["+", "-", "×", "÷"]:
            if self.equation.get() and not self.equation.get().endswith(("+", "-", "×", "÷")):
                self.equation.insert(tk.END, text)
        elif text == ".":
            if self.equation.get() and "." not in self.equation.get():
                self.equation.insert(tk.END, ".")
            elif not self.equation.get():
                self.equation.insert(tk.END, "0.")
        elif text == "=":
            equation = self.equation.get()
            try:
                result = eval(equation)
                self.equation.delete(0, tk.END)
                self.equation.insert(0, result)
            except (SyntaxError, ZeroDivisionError):
                self.equation.delete(0, tk.END)
                self.equation.insert(0, "Error")

        else:
            self.equation.insert(tk.END, text)

# 创建主窗口
root = tk.Tk()

# 创建计算器 GUI
calculator = Calculator(root)

# 进入主事件循环
root.mainloop()