from tkinter import (Tk, Entry, CENTER, END)

def functions_list_window():
    class Table_Like_Layout:
        def __init__(self, root):
            for i in range(n_rows):
                for j in range(n_cols):
                    self.entries = Entry(root, width = 32, bg = "gold3", fg = "blue", font = ("Times New Roman", 16, "bold"), justify = CENTER, state = None)
                    self.entries.grid(row = i, column = j)
                    self.entries.insert(END, Table[i][j])
  
    Table = [
                (str("Options"), str("Functions"), str("Derived Functions")),
                (int(1), str("F(X) = exp(X)"), str("F`(X) = exp(X)")),
                (int(2), str("F(X) = ln(X) #(Base = e)"), str("F`(X) = 1 / X")),
                (int(3), str("F(X) = 1 / X"), str("F`(X) = - 1 / X**(2)")),
                (int(4), str("F(X) = 10^X"), str("F`(X) = ln(10) * 10**(X)")),
                (int(5), str("F(X) = Log(X) #(Base = 10)"), str("F`(X) = 1 / (ln(10) * X)")),
                (int(6), str("F(X) = Log2(X) #(Base = 2)"), str("F`(X) = 1 / (ln(2) * X)")),
                (int(7), str("F(X) = Sin(X)"), str("F`(X) = Cos(X)")),
                (int(8), str("F(X) = Cos(X)"), str("F`(X) = -1 * Sin(X)")),
                (int(9), str("F(X) = Tan(X)"), str("F`(X) = Sec^2(X)")),
                (int(10), str("F(X) = X^2"), str("F`(X) = 2 * X")),
                (int(11), str("F(X) = Sqrt(X)"), str("F`(X) = 1 / (2 * Sqrt(X))")),
                (int(12), str("NONE"), str("NONE"))
            ]

    n_rows = len(Table)
    n_cols = len(Table[0])
   
    root = Tk()
    root.resizable(height = False, width = False)
    root.title("Functions List")
    T = Table_Like_Layout(root)