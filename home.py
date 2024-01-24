import tkinter as tk

class LexerAppView:
    def __init__(self, root):
        self.root = root
        self.root.title("Lexer App")

        self.input_label = tk.Label(root, text="Input:")
        self.input_label.pack()

        self.input_entry = tk.Entry(root)
        self.input_entry.pack()

        self.result_label = tk.Label(root, text="Result:")
        self.result_label.pack()

        self.result_text = tk.Text(root, height=10, width=50)
        self.result_text.pack()

        self.run_button = tk.Button(root, text="Run Lexer", command=self.run_lexer)
        self.run_button.pack()

    def run_lexer(self):
        print(self.input_entry.get())

if __name__ == "__main__":
    root = tk.Tk()
    app = LexerAppView(root)
    root.mainloop()