import tkinter as tk
import model

NUMBER_BUTTONS = (('1', 0, 0), ('2', 0, 1), ('3', 0, 2),
                  ('4', 1, 0), ('5', 1, 1), ('6', 1, 2),
                  ('7', 2, 0), ('8', 2, 1), ('9', 2, 2),
                  ('0', 3, 0))

OPERATOR_BUTTONS = (('%', 0, 3), ('x', 1, 3), ('+', 2, 3), ('-', 3, 3))

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

        for info in NUMBER_BUTTONS:
            btn = tk.Button(button_frame, text=info[0], font=('Arial', 18),
                            command=lambda x = info[0]: self.on_number_button_pressed(x))
            btn.grid(row=info[1], column=info[2], sticky=tk.W+tk.E)

        for info in OPERATOR_BUTTONS:
            btn = tk.Button(button_frame, text=info[0], font=('Arial', 18),
                            command=lambda x = info[0]: self.on_operator_button_pressed(x))
            btn.grid(row=info[1], column=info[2], sticky=tk.W+tk.E)

        btn1 = tk.Button(button_frame, text='c', font=('Arial', 18),
                         command= self.on_reset_button_pressed)
        btn1.grid(row=3, column=1, sticky=tk.W+tk.E)

        btn1 = tk.Button(button_frame, text='=', font=('Arial', 18),
                         command=lambda: self.on_equal_button_pressed())
        btn1.grid(row=3, column=2, sticky=tk.W+tk.E)

        button_frame.pack(fill='x')

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
