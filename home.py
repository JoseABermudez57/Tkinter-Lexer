import tkinter as tk
import tkinter.font as tkFont
import Lexer as lx

class LexerAppView:
    def __init__(self, root):
        # setting title
        root.title("Analizador léxico")
        # setting window size
        width = 479
        height = 362
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.configure(bg="#ACB7E4")


        self.lbl_input = tk.Label(root)
        self.lbl_input["anchor"] = "center"
        ft = tkFont.Font(family='Times', size=15, weight='bold')
        self.lbl_input["font"] = ft
        self.lbl_input["bg"] = "#ACB7E4"
        self.lbl_input["fg"] = "#333333"
        self.lbl_input["justify"] = "center"
        self.lbl_input["text"] = "Ingresa una cadena para evaluarla"
        self.lbl_input.place(x=90, y=10, width=300, height=25)

        self.input_entry = tk.Entry(root)
        self.input_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.input_entry["font"] = ft
        self.input_entry["fg"] = "#333333"
        self.input_entry["justify"] = "center"
        self.input_entry["text"] = "Entry"
        self.input_entry.place(x=40, y=40, width=311, height=30)

        self.result_text = tk.Text(root)
        self.result_text["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.result_text["font"] = ft
        self.result_text["fg"] = "#333333"
        self.result_text.place(x=40, y=110, width=390, height=215)

        self.result_button = tk.Button(root)
        self.result_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        self.result_button["font"] = ft
        self.result_button["fg"] = "#000000"
        self.result_button["justify"] = "center"
        self.result_button["text"] = "Validar"
        self.result_button.place(x=360, y=40, width=70, height=30)
        self.result_button["command"] = self.run_lexer

    def run_lexer(self):
        input_text = self.input_entry.get()
        lexer = lx.Lexer(input_text)
        result = []
        token = lexer.next_token()
        while token:
            result.append(token)
            token = lexer.next_token()
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, "\n".join(map(str, result)))

if __name__ == "__main__":
    root = tk.Tk()
    app = LexerAppView(root)
    root.mainloop()
