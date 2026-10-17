import tkinter as tk
import model


class CalculatorGUI:
    def __init__(self):
        self.root = tk.Tk()

        self.root.title('Calculator')
        self.root.geometry('500x500')
        self.display_text = tk.StringVar()
        self.display_text.set('0')

        display = tk.Label(self.root, textvariable=self.display_text, font=('Arial', 20))
        display.pack(padx=10, pady=10)

        button_frame = tk.Frame(self.root)
        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)
        button_frame.columnconfigure(2, weight=1)
        button_frame.columnconfigure(3, weight=1)

        # row one
        btn1 = tk.Button(button_frame, text='1', font=('Arial', 18),
                         command=lambda: self.on_number_button_pressed('1'))
        btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

        btn1 = tk.Button(button_frame, text='2', font=('Arial', 18),
                         command=lambda: self.on_number_button_pressed('2'))
        btn1.grid(row=0, column=1, sticky=tk.W+tk.E)

        btn1 = tk.Button(button_frame, text='3', font=('Arial', 18),
                         command=lambda: self.on_number_button_pressed('3'))
        btn1.grid(row=0, column=2, sticky=tk.W+tk.E)

        btn1 = tk.Button(button_frame, text='%', font=('Arial', 18),
                         command=lambda: self.on_operator_button_pressed('%'))
        btn1.grid(row=0, column=3, sticky=tk.W+tk.E)

        # row two
        btn1 = tk.Button(button_frame, text='4', font=('Arial', 18),
                         command=lambda: self.on_number_button_pressed('4'))
        btn1.grid(row=1, column=0, sticky=tk.W+tk.E)

        btn1 = tk.Button(button_frame, text='5', font=('Arial', 18),
                         command=lambda: self.on_number_button_pressed('5'))
        btn1.grid(row=1, column=1, sticky=tk.W+tk.E)

        btn1 = tk.Button(button_frame, text='6', font=('Arial', 18),
                         command=lambda: self.on_number_button_pressed('6'))
        btn1.grid(row=1, column=2, sticky=tk.W+tk.E)

        btn1 = tk.Button(button_frame, text='x', font=('Arial', 18),
                         command=lambda: self.on_operator_button_pressed('x'))
        btn1.grid(row=1, column=3, sticky=tk.W+tk.E)

        # row three
        btn1 = tk.Button(button_frame, text='7', font=('Arial', 18),
                         command=lambda: self.on_number_button_pressed('7'))
        btn1.grid(row=2, column=0, sticky=tk.W+tk.E)

        btn1 = tk.Button(button_frame, text='8', font=('Arial', 18),
                         command=lambda: self.on_number_button_pressed('8'))
        btn1.grid(row=2, column=1, sticky=tk.W+tk.E)

        btn1 = tk.Button(button_frame, text='9', font=('Arial', 18),
                         command=lambda: self.on_number_button_pressed('9'))
        btn1.grid(row=2, column=2, sticky=tk.W+tk.E)

        btn1 = tk.Button(button_frame, text='+', font=('Arial', 18),
                         command=lambda: self.on_operator_button_pressed('+'))
        btn1.grid(row=2, column=3, sticky=tk.W+tk.E)

        # row four
        btn1 = tk.Button(button_frame, text='0', font=('Arial', 18),
                         command=lambda: self.on_number_button_pressed('0'))
        btn1.grid(row=3, column=0, sticky=tk.W+tk.E)

        btn1 = tk.Button(button_frame, text='c', font=('Arial', 18),
                         command= self.on_reset_button_pressed)
        btn1.grid(row=3, column=1, sticky=tk.W+tk.E)

        btn1 = tk.Button(button_frame, text='=', font=('Arial', 18),
                         command=lambda: self.on_equal_button_pressed())
        btn1.grid(row=3, column=2, sticky=tk.W+tk.E)

        btn1 = tk.Button(button_frame, text='-', font=('Arial', 18),
                         command=lambda: self.on_operator_button_pressed('-'))
        btn1.grid(row=3, column=3, sticky=tk.W+tk.E)

        button_frame.pack(fill='x')

        self.root.mainloop()

    @staticmethod
    def create_string_to_display():
        display_text = ''
        match len(model.values):
            case 0:
                display_text = str(model.values[0])
            case 1:
                display_text = str(model.values[0])
                if model.current_operator != '':
                    display_text = f'{display_text} {model.current_operator}'
            case 2:
                display_text = f'{model.values[0]} {model.current_operator} {model.values[1]}'

        return display_text

    def on_reset_button_pressed(self):
        model.reset()
        self.display_text.set('0')

    def on_equal_button_pressed(self):
        result = model.get_result()
        temp_display_text = f'{self.create_string_to_display()} = {result}'
        self.display_text.set(temp_display_text)

    def on_number_button_pressed(self, value):
        model.add_value(value)
        temp_display_text = self.create_string_to_display()
        self.display_text.set(temp_display_text)

    def on_operator_button_pressed(self, operator):
        model.on_operator_pressed(operator)
        temp_display_text = self.create_string_to_display()
        self.display_text.set(temp_display_text)

CalculatorGUI()
