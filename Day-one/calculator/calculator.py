import tkinter as tk
from tkinter import messagebox
import math, ast, operator as op

# ---------- Safe Evaluator ----------
BIN_OPS = {
    ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul,
    ast.Div: op.truediv, ast.FloorDiv: op.floordiv,
    ast.Mod: op.mod, ast.Pow: op.pow,
}
UNARY_OPS = {ast.UAdd: op.pos, ast.USub: op.neg}
ALLOWED_FUNCS = {"sqrt": math.sqrt, "abs": abs, "round": round}

class SafeEvaluator:
    def __init__(self, names):
        self.names = names
    def eval(self, expr):
        node = ast.parse(expr, mode="eval")
        return self._eval(node.body)
    def _eval(self, node):
        if isinstance(node, ast.Constant): return float(node.value)
        if isinstance(node, ast.BinOp): return BIN_OPS[type(node.op)](self._eval(node.left), self._eval(node.right))
        if isinstance(node, ast.UnaryOp): return UNARY_OPS[type(node.op)](self._eval(node.operand))
        if isinstance(node, ast.Name): return self.names.get(node.id, 0.0)
        if isinstance(node, ast.Call):
            if node.func.id not in ALLOWED_FUNCS: raise ValueError("Function not allowed")
            args = [self._eval(a) for a in node.args]
            return ALLOWED_FUNCS[node.func.id](*args)
        raise ValueError("Invalid expression")

# ---------- Stylish Calculator ----------
class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Beautiful Calculator")
        self.root.configure(bg="#2C3E50")  # dark background
        self.expression = ""
        self.ans = 0.0
        self.mem = 0.0

        # Display
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right", bd=10, relief="flat", bg="#ECF0F1", fg="#2C3E50")
        self.entry.grid(row=0, column=0, columnspan=4, pady=15, padx=10, ipady=10)

        # Buttons layout
        buttons = [
            ("7",1,0),("8",1,1),("9",1,2),("/",1,3),
            ("4",2,0),("5",2,1),("6",2,2),("*",2,3),
            ("1",3,0),("2",3,1),("3",3,2),("-",3,3),
            ("0",4,0),(".",4,1),("(",4,2),(")",4,3),
            ("C",5,0),("M+",5,1),("M-",5,2),("+",5,3),
            ("MR",6,0),("MC",6,1),("ANS",6,2),("=",6,3),
        ]

        for (text,row,col) in buttons:
            self.create_button(text, row, col)

    def create_button(self, text, row, col):
        btn_color = "#34495E" if text not in ["=", "C"] else ("#27AE60" if text=="=" else "#E74C3C")
        fg_color = "#ECF0F1"
        button = tk.Button(self.root, text=text, width=6, height=2, font=("Arial",16,"bold"),
                           bg=btn_color, fg=fg_color, activebackground="#16A085", relief="flat",
                           command=lambda t=text: self.on_click(t))
        button.grid(row=row, column=col, padx=6, pady=6, sticky="nsew")

    def on_click(self, char):
        if char == "=":
            self.calculate()
        elif char == "C":
            self.expression = ""
            self.entry.delete(0, tk.END)
        elif char == "M+":
            try: self.mem += float(self.entry.get())
            except: messagebox.showerror("Error", "Invalid number for M+")
        elif char == "M-":
            try: self.mem -= float(self.entry.get())
            except: messagebox.showerror("Error", "Invalid number for M-")
        elif char == "MR":
            self.entry.insert(tk.END, str(self.mem))
        elif char == "MC":
            self.mem = 0.0
        elif char == "ANS":
            self.entry.insert(tk.END, str(self.ans))
        else:
            self.entry.insert(tk.END, char)

    def calculate(self):
        expr = self.entry.get()
        try:
            evaluator = SafeEvaluator({"pi": math.pi, "e": math.e, "ans": self.ans, "mem": self.mem})
            result = evaluator.eval(expr)
            self.ans = result
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", f"Invalid Expression:\n{e}")

# ---------- Run ----------
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    # Make window resize-friendly
    for i in range(7): root.rowconfigure(i, weight=1)
    for j in range(4): root.columnconfigure(j, weight=1)
    root.mainloop()
