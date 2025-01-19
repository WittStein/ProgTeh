from tkinter import *
import math
from tkinter import ttk

root = Tk()

# Херня, на которой находятся наши виджеты
Frm1 = Frame()
Frm1.pack(expand=YES, fill=BOTH)
Frm2 = Frame()
Frm2.pack(expand=YES, fill=BOTH)
Frm3 = Frame()
Frm3.pack(expand=YES, fill=BOTH)
Frm4 = Frame()
Frm4.pack(expand=YES, fill=BOTH)
Frm5 = Frame()
Frm5.pack(expand=YES, fill=BOTH)
Frm6 = Frame()
Frm6.pack(expand=YES, fill=BOTH)

# Функция для обновления значений при изменении системы счисления
def update_system(*args):
    selection = int(combobox.get())
    try:
        if entrya.get():
            var1 = int(entrya.get(), 2)
            if selection == 8:
                entrya1.delete(0, END)
                entrya1.insert(0, oct(var1)[2:])
            elif selection == 10:
                entrya1.delete(0, END)
                entrya1.insert(0, str(var1))
            elif selection == 16:
                entrya1.delete(0, END)
                entrya1.insert(0, hex(var1)[2:])

        if entryb1.get():
            var2 = int(entryb1.get(), selection)
            entryb.delete(0, END)
            entryb.insert(0, bin(var2)[2:])
    except ValueError:
        entrya1.delete(0, END)
        entryb.delete(0, END)

# Функция для обновления значений при вводе в первое окно
def update_entrya(event):
    try:
        var1 = int(entrya.get(), 2)
        selection = int(combobox.get())
        if selection == 8:
            entrya1.delete(0, END)
            entrya1.insert(0, oct(var1)[2:])
        elif selection == 10:
            entrya1.delete(0, END)
            entrya1.insert(0, str(var1))
        elif selection == 16:
            entrya1.delete(0, END)
            entrya1.insert(0, hex(var1)[2:])
    except ValueError:
        entrya1.delete(0, END)

def update_entryb(event):
    try:
        var2 = int(entryb.get(), 2)
        selection = int(combobox.get())
        if selection == 8:
            entryb1.delete(0, END)
            entryb1.insert(0, oct(var2)[2:])
        elif selection == 10:
            entryb1.delete(0, END)
            entryb1.insert(0, str(var2))
        elif selection == 16:
            entryb1.delete(0, END)
            entryb1.insert(0, hex(var2)[2:])
    except ValueError:
        entryb1.delete(0, END)

# # Функция для обновления значений при вводе во второе окно
# def update_entryb(event):
#     try:
#         selection = int(combobox.get())
#         var2 = int(entryb1.get(), selection)
#         entryb.delete(0, END)
#         entryb.insert(0, bin(var2)[2:])
#     except ValueError:
#         entryb.delete(0, END)

# Функция для выполнения вычислений
def calculate():
    try:
        var1 = int(entrya.get(), 2)
        selection = int(combobox.get())
        var2 = int(entryb1.get(), selection)
        operation = combobox1.get()

        if operation == '+':
            result = var1 + var2
        elif operation == '-':
            result = var1 - var2
        elif operation == '*':
            result = var1 * var2
        elif operation == '/':
            if var2 == 0:
                raise ZeroDivisionError("Division by zero")
            result = var1 / var2
        elif operation == '%':
            result = var1 % var2
        elif operation == 'and':
            result = var1 & var2

        result_bin = bin(int(result))[2:]
        if selection == 8:
            result_base = oct(int(result))[2:]
        elif selection == 10:
            result_base = str(int(result))
        elif selection == 16:
            result_base = hex(int(result))[2:]

        result_label_bin.config(text=result_bin)
        result_label_base.config(text=result_base)
    except Exception as e:
        result_label_bin.config(text="Error")
        result_label_base.config(text="Error")

# Переключение системы исчисления
Bruh = ['8', '10', '16']
combobox_Bruh = StringVar(value=Bruh[0])
combobox = ttk.Combobox(Frm1, textvariable=combobox_Bruh, values=Bruh)
combobox.pack(side=RIGHT)
combobox_Bruh.trace("w", update_system)

# Переключение знака
Boo = ['+', '-', '*', '/', '%', 'and']
combobox_Boo = StringVar(value=Boo[0])
combobox1 = ttk.Combobox(Frm3, textvariable=combobox_Boo, values=Boo)
combobox1.pack(side=LEFT, expand=YES)

# Ввод значений
entrya = Entry(Frm2)
entrya1 = Entry(Frm2)
entryb = Entry(Frm4)
entryb1 = Entry(Frm4)

# Окно
root.title('Калькулятор')
root.geometry('500x350')

# Расположение виджетов
entrya.pack(side=LEFT, expand=YES)
entrya1.pack(side=LEFT, expand=YES)
entryb.pack(side=LEFT, expand=YES)
entryb1.pack(side=LEFT, expand=YES)

# События
entrya.bind('<KeyRelease>', update_entrya)
# entrya1.bind('<KeyRelease>', update_entrya1)
entryb.bind('<KeyRelease>', update_entryb)
# entryb1.bind('<KeyRelease>', update_entryb1)

# Кнопка для выполнения вычислений
calculate_button = Button(Frm6, text="Calculate", command=calculate)
calculate_button.pack(side=LEFT, expand=YES)

# Метки для отображения результатов
result_label_bin = Label(Frm5, text="")
result_label_bin.pack(side=LEFT, expand=YES)
result_label_base = Label(Frm5, text="")
result_label_base.pack(side=LEFT, expand=YES)

root.mainloop()
