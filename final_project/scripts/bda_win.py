from tkinter import *
import tkinter.messagebox as msb
import os
import numpy as np
import mpmath
import math
from functions_list import functions_list_window

def window_for_bda():
    # BDA Window's Setup.
    bda_win = Tk()
    bda_win.resizable(height = False, width = False)
    bda_win.title("BDA")
    bda_win.geometry("550x520+0+0")
    bda_win.config(bg = "gold2")

    # Widget's Control Variables.
    separator_var = StringVar(bda_win, name = "sep", value = str("--------------------------------------------------------------------"))
    x_val_label_var = StringVar(bda_win, name = "x_value", value = str("Set X-Value = "))
    step_x_val_label_var = StringVar(bda_win, name = "x_step_size_val", value = str("Set Step-Size(Delta-X) = "))
    big_separator_var = StringVar(bda_win, name = "large_separator", value = str("===================================================================="))

    # BDA Window's Main Title.
    bda_title = Label(bda_win, bg = "khaki", fg = "SpringGreen2", font = ("Times New Roman", 25, "bold"), text = str("BDA Method's Value Approximation"), anchor = CENTER, relief = GROOVE, padx = 14, pady = 2, height = 2, width = -10)
    bda_title.place(x = 0.0, y = 0.0)

    # Label For Function Scale.
    label_for_func = Label(bda_win, font = ("Times New Roman", 7, "italic", "bold"), anchor = CENTER, relief = FLAT, fg = "blue2", bg = "gold2", text = str("Select A Function To Be Derived -> F(X) = "))
    label_for_func.place(x = 15.0, y = 90.0)

    # Selections Scale.
    scale_for_func = Scale(bda_win, from_ = 1, to = 12, cursor = "dot", highlightbackground = "SpringGreen2", activebackground = "cyan3")
    scale_for_func.place(x = 215.0, y = 90.0)

    # Access To List Of Math Functions.
    help_access = Button(bda_win, justify = CENTER, height = 2, width = 10, bg = "turquoise1", fg = "black", text = "HELP", font = ("Times New Roman", 14, "bold"), activebackground = "white", activeforeground = "white", relief = RAISED, command = lambda: functions_list_window())
    help_access.place(x = 45.0, y = 115.0)

    # Separator.
    little_sep = Label(bda_win, bg = "gold2", fg = "black", textvariable = separator_var)
    little_sep.place(x = -1.0, y = 195.0)

    # Label For X-Value Input.
    x_value_label = Label(bda_win, font = ("Times New Roman", 12, "italic", "bold"), anchor = CENTER, textvariable = x_val_label_var, relief = FLAT, fg = "blue2", bg = "gold2")
    x_value_label.place(x = 15.0, y = 215.0)

    # Entry To Contain X-Value Input.
    x_value_entry = Entry(bda_win, font = ("Times New Roman", 12, "bold"), bg = "snow4", fg = "black", justify = LEFT, relief = SUNKEN, width = 28)
    x_value_entry.place(x = 120.0, y = 217.0)

    # Separator 2.
    little_sep2 = Label(bda_win, bg = "gold2", fg = "black", textvariable = separator_var)
    little_sep2.place(x = -1.0, y = 240.0)

    # Label For Delta-X Input.
    delta_x_input_label = Label(bda_win, font = ("Times New Roman", 12, "bold", "italic"), anchor = CENTER, textvariable = step_x_val_label_var, relief = FLAT, fg = "blue2", bg = "gold2")
    delta_x_input_label.place(x = 15.0, y = 257.0)

    # Entry For Delta-X Input.
    delta_x_input_entry = Entry(bda_win, font = ("Times New Roman", 12, "bold"), bg = "snow4", fg = "black", justify = LEFT, relief = SUNKEN, width = 20)
    delta_x_input_entry.place(x = 185.0, y = 259.0)

    # Large Separator.
    big_sep = Label(bda_win, bg = "gold2", fg = "black", textvariable = big_separator_var)
    big_sep.place(x = 0.0, y = 290.0)

    '''
    (2x3)Table With Entries For The Whole Second Row,
    Entry[1][0] Stores Exact Results.
    Entry[1][1] Stores Approximated Results.
    Entry[1][2] Stores Abs. Relative True Error Rate(%).
    '''
    # Label For Entry[1][0]. 
    exact_label = Label(bda_win, justify = CENTER, height = 1, width = 12, bg = "black", fg = "gold2", text = str("Exact Value = "), font = ("Times New Roman", 18, "bold"), relief = RIDGE)
    exact_label.place(x = 16.0, y = 370.0)

    # Entry[1][0] :
    exact_entry = Entry(bda_win, justify = LEFT, width = 29, bg = "orange", fg = "black", font = ("Times New Roman", 18, "bold"), relief = RIDGE)
    exact_entry.place(x = 190.0, y = 371.0)

    # Label For Entry[1][1]:
    appr_label = Label(bda_win, justify = CENTER, height = 1, width = 14, bg = "black", fg = "gold2", text = str("Approx. Value = "), font = ("Times New Roman", 16, "bold"), relief = RIDGE)
    appr_label.place(x = 16.0, y = 425.0)

    # Entry[1][1] :
    appr_entry = Entry(bda_win, justify = LEFT, width = 29, bg = "orange", fg = "black", font = ("Times New Roman", 18, "bold"), relief = RIDGE)
    appr_entry.place(x = 190.0, y = 425.0)

    # Label For Entry[1][2]:
    abs_error_label = Label(bda_win, justify = CENTER, height = 2, width = 24, bg = "black", fg = "gold2", text = str("Abs. Relative True Error(%) = "), font = ("Times New Roman", 10, "bold"), relief = RIDGE)
    abs_error_label.place(x = 16.0, y = 475.0)

    # Entry[1][2] :
    abs_error_entry = Entry(bda_win, justify = LEFT, width = 29, bg = "orange", fg = "black", font = ("Times New Roman", 18, "bold"), relief = RIDGE)
    abs_error_entry.place(x = 190.0, y = 478.0)
    
    # Method Implementations.
    class BDA_Window_Methods(Exception):
        def __init__(self, exact_entry_len = len(exact_entry.get()), appr_entry_len = len(appr_entry.get()), abs_error_entry_len = len(abs_error_entry.get()), **kwargs):
            self.__length_of_exact_entry = exact_entry_len
            self.__length_of_appr_entry = appr_entry_len
            self.__length_of_abserror_entry = abs_error_entry_len
            self.__last = END
        
        def clear_all(self):
            exact_entry.delete(0, self.__last)
            appr_entry.delete(0, self.__last)
            abs_error_entry.delete(0, self.__last)

        def calculate_all(self):
            '''
            BDA Method's Approach :
                F`(X) ≈ [F(X) - F(X - ΔX)] / ΔX
                    Where ΔX Is Equal To Value Of Step Size.
            '''
            if(int(scale_for_func.get()) == 1):
                # Functions :
                func = lambda x: np.exp(x)
                derived_func = func
                # Calculations.
                exact_value = derived_func(float(x_value_entry.get()))
                appr_value = (func(float(x_value_entry.get())) - func((float(x_value_entry.get()) - float(delta_x_input_entry.get())))) / float(delta_x_input_entry.get())
                abs_error_value = (np.abs(((exact_value - appr_value) / exact_value))) * float(100.0)
                self.clear_all()
                # Insertions.
                exact_entry.insert(self.__length_of_exact_entry, str(round(exact_value, 5)))
                appr_entry.insert(self.__length_of_appr_entry, str(round(appr_value, 5)))
                abs_error_entry.insert(self.__length_of_abserror_entry, str(round(abs_error_value, 5)) + " %")
            elif(int(scale_for_func.get()) == 2):
                # Functions :
                func = lambda x: np.log(x)
                derived_func = lambda x: 1 / x
                # Calculations.
                exact_value = derived_func(float(x_value_entry.get()))
                appr_value = (func(float(x_value_entry.get())) - func((float(x_value_entry.get()) - float(delta_x_input_entry.get())))) / float(delta_x_input_entry.get())
                abs_error_value = (np.abs(((exact_value - appr_value) / exact_value))) * float(100.0)
                self.clear_all()
                # Insertions.
                exact_entry.insert(self.__length_of_exact_entry, str(round(exact_value, 5)))
                appr_entry.insert(self.__length_of_appr_entry, str(round(appr_value, 5)))
                abs_error_entry.insert(self.__length_of_abserror_entry, str(round(abs_error_value, 5)) + " %")
            elif(int(scale_for_func.get()) == 3):
                # Functions :
                func = lambda x: 1 / x
                derived_func = lambda x: -1 / (x**(2.0))
                # Calculations.
                exact_value = derived_func(float(x_value_entry.get()))
                appr_value = (func(float(x_value_entry.get())) - func((float(x_value_entry.get()) - float(delta_x_input_entry.get())))) / float(delta_x_input_entry.get())
                abs_error_value = (np.abs(((exact_value - appr_value) / exact_value))) * float(100.0)
                self.clear_all()
                # Insertions.
                exact_entry.insert(self.__length_of_exact_entry, str(round(exact_value, 5)))
                appr_entry.insert(self.__length_of_appr_entry, str(round(appr_value, 5)))
                abs_error_entry.insert(self.__length_of_abserror_entry, str(round(abs_error_value, 5)) + " %")
            elif(int(scale_for_func.get()) == 4):
                # Functions :
                func = lambda x: 10**x
                derived_func = lambda x: np.log(10) * (10**(x))
                # Calculations.
                exact_value = derived_func(float(x_value_entry.get()))
                appr_value = (func(float(x_value_entry.get())) - func((float(x_value_entry.get()) - float(delta_x_input_entry.get())))) / float(delta_x_input_entry.get())
                abs_error_value = (np.abs(((exact_value - appr_value) / exact_value))) * float(100.0)
                self.clear_all()
                # Insertions.
                exact_entry.insert(self.__length_of_exact_entry, str(round(exact_value, 5)))
                appr_entry.insert(self.__length_of_appr_entry, str(round(appr_value, 5)))
                abs_error_entry.insert(self.__length_of_abserror_entry, str(round(abs_error_value, 5)) + " %")
            elif(int(scale_for_func.get()) == 5):
                # Functions :
                func = lambda x: np.log10(x)
                derived_func = lambda x: 1 / (np.log(10) * x)
                # Calculations.
                exact_value = derived_func(float(x_value_entry.get()))
                appr_value = (func(float(x_value_entry.get())) - func((float(x_value_entry.get()) - float(delta_x_input_entry.get())))) / float(delta_x_input_entry.get())
                abs_error_value = (np.abs(((exact_value - appr_value) / exact_value))) * float(100.0)
                self.clear_all()
                # Insertions.
                exact_entry.insert(self.__length_of_exact_entry, str(round(exact_value, 5)))
                appr_entry.insert(self.__length_of_appr_entry, str(round(appr_value, 5)))
                abs_error_entry.insert(self.__length_of_abserror_entry, str(round(abs_error_value, 5)) + " %")
            elif(int(scale_for_func.get()) == 6):
                # Functions :
                func = lambda x: np.log2(x)
                derived_func = lambda x: 1 / (np.log(2) * x)
                # Calculations.
                exact_value = derived_func(float(x_value_entry.get()))
                appr_value = (func(float(x_value_entry.get())) - func((float(x_value_entry.get()) - float(delta_x_input_entry.get())))) / float(delta_x_input_entry.get())
                abs_error_value = (np.abs(((exact_value - appr_value) / exact_value))) * float(100.0)
                self.clear_all()
                # Insertions.
                exact_entry.insert(self.__length_of_exact_entry, str(round(exact_value, 5)))
                appr_entry.insert(self.__length_of_appr_entry, str(round(appr_value, 5)))
                abs_error_entry.insert(self.__length_of_abserror_entry, str(round(abs_error_value, 5)) + " %")
            elif(int(scale_for_func.get()) == 7):
                # Functions :
                func = lambda x: math.sin(math.radians(x))
                derived_func = lambda x: math.cos(math.radians(x))
                # Calculations.
                exact_value = derived_func(float(x_value_entry.get()))
                appr_value = (func(float(x_value_entry.get())) - func((float(x_value_entry.get()) - float(delta_x_input_entry.get())))) / float(delta_x_input_entry.get())
                abs_error_value = (np.abs(((exact_value - appr_value) / exact_value))) * float(100.0)
                self.clear_all()
                # Insertions.
                exact_entry.insert(self.__length_of_exact_entry, str(round(exact_value, 5)))
                appr_entry.insert(self.__length_of_appr_entry, str(round(appr_value, 5)))
                abs_error_entry.insert(self.__length_of_abserror_entry, str(round(abs_error_value, 5)) + " %")
            elif(int(scale_for_func.get()) == 8):
                # Functions :
                func = lambda x: math.cos(math.radians(x))
                derived_func = lambda x: -1 * (math.sin(math.radians(x)))
                # Calculations.
                exact_value = derived_func(float(x_value_entry.get()))
                appr_value = (func(float(x_value_entry.get())) - func((float(x_value_entry.get()) - float(delta_x_input_entry.get())))) / float(delta_x_input_entry.get())
                abs_error_value = (np.abs(((exact_value - appr_value) / exact_value))) * float(100.0)
                self.clear_all()
                # Insertions.
                exact_entry.insert(self.__length_of_exact_entry, str(round(exact_value, 5)))
                appr_entry.insert(self.__length_of_appr_entry, str(round(appr_value, 5)))
                abs_error_entry.insert(self.__length_of_abserror_entry, str(round(abs_error_value, 5)) + " %")
            elif(int(scale_for_func.get()) == 9):
                # Functions :
                func = lambda x: mpmath.tan(mpmath.radians(x))
                derived_func = lambda x: ((mpmath.sec(mpmath.radians(x)))**(2))
                # Calculations.
                exact_value = derived_func(float(x_value_entry.get()))
                appr_value = (func(float(x_value_entry.get())) - func((float(x_value_entry.get()) - float(delta_x_input_entry.get())))) / float(delta_x_input_entry.get())
                abs_error_value = (np.abs(((exact_value - appr_value) / exact_value))) * float(100.0)
                self.clear_all()
                # Insertions.
                exact_entry.insert(self.__length_of_exact_entry, str(round(exact_value, 5)))
                appr_entry.insert(self.__length_of_appr_entry, str(round(appr_value, 5)))
                abs_error_entry.insert(self.__length_of_abserror_entry, str(round(abs_error_value, 5)) + " %")
            elif(int(scale_for_func.get()) == 10):
                # Functions :
                func = lambda x: x**(2.0)
                derived_func = lambda x: 2 * x
                # Calculations.
                exact_value = derived_func(float(x_value_entry.get()))
                appr_value = (func(float(x_value_entry.get())) - func((float(x_value_entry.get()) - float(delta_x_input_entry.get())))) / float(delta_x_input_entry.get())
                abs_error_value = (np.abs(((exact_value - appr_value) / exact_value))) * float(100.0)
                self.clear_all()
                # Insertions.
                exact_entry.insert(self.__length_of_exact_entry, str(round(exact_value, 5)))
                appr_entry.insert(self.__length_of_appr_entry, str(round(appr_value, 5)))
                abs_error_entry.insert(self.__length_of_abserror_entry, str(round(abs_error_value, 5)) + " %")
            elif(int(scale_for_func.get()) == 11):
                # Functions :
                func = lambda x: math.sqrt(x)
                derived_func = lambda x: (1 / (2 * func(x)))
                # Calculations.
                exact_value = derived_func(float(x_value_entry.get()))
                appr_value = (func(float(x_value_entry.get())) - func((float(x_value_entry.get()) - float(delta_x_input_entry.get())))) / float(delta_x_input_entry.get())
                abs_error_value = (np.abs(((exact_value - appr_value) / exact_value))) * float(100.0)
                self.clear_all()
                # Insertions.
                exact_entry.insert(self.__length_of_exact_entry, str(round(exact_value, 5)))
                appr_entry.insert(self.__length_of_appr_entry, str(round(appr_value, 5)))
                abs_error_entry.insert(self.__length_of_abserror_entry, str(round(abs_error_value, 5)) + " %")
            elif(int(scale_for_func.get()) == 12):
                msb.showinfo("'None' Selected !", "Please Select Another Function !")
            else:
                msb.showerror("Error", "Please Try Again !")

        @staticmethod
        def save_results():
            if(os.path.exists("C:/Users/EDWARD/comp._math/records_of_results.txt")):
                if(int(scale_for_func.get()) == 1):
                    try:
                        with open("records_of_results.txt", 'a', encoding = 'utf-8') as file_obj:
                            file_obj.write("BDA Method\n")
                            file_obj.write("An Irrelevant Result !\n")
                            file_obj.write("Function -> F(X) = exp(X)\n")
                            file_obj.write("Derived Function -> F`(X) = exp(X)\n")
                            file_obj.write("X-Value = {}\n".format(str(x_value_entry.get())))
                            file_obj.write("Delta-X Value = {}\n".format(str(delta_x_input_entry.get())))
                            file_obj.write("Exact Result = {}\n".format(str(exact_entry.get())))
                            file_obj.write("Approx. Result = {}\n".format(str(appr_entry.get())))
                            file_obj.write("Abs. Relative True Error(%) = {}\n".format(str(abs_error_entry.get())))
                            file_obj.write("======================================================================================\n")
                            file_obj.flush()
                    finally:
                        file_obj.close()
                elif(int(scale_for_func.get()) == 2):
                    try:
                        with open("records_of_results.txt", 'a', encoding = 'utf-8') as file_obj:
                            file_obj.write("BDA Method\n")
                            file_obj.write("Function -> F(X) = ln(X)\n")
                            file_obj.write("Derived Function -> F`(X) = 1 / X\n")
                            file_obj.write("X-Value = {}\n".format(str(x_value_entry.get())))
                            file_obj.write("Delta-X Value = {}\n".format(str(delta_x_input_entry.get())))
                            file_obj.write("Exact Result = {}\n".format(str(exact_entry.get())))
                            file_obj.write("Approx. Result = {}\n".format(str(appr_entry.get())))
                            file_obj.write("Abs. Relative True Error(%) = {}\n".format(str(abs_error_entry.get())))
                            file_obj.write("======================================================================================\n")
                            file_obj.flush()
                    finally:
                        file_obj.close()
                elif(int(scale_for_func.get()) == 3):
                    try:
                        with open("records_of_results.txt", 'a', encoding = 'utf-8') as file_obj:
                            file_obj.write("BDA Method\n")
                            file_obj.write("Function -> F(X) = 1 / X\n")
                            file_obj.write("Derived Function -> F`(X) = -1 / (X^2)\n")
                            file_obj.write("X-Value = {}\n".format(str(x_value_entry.get())))
                            file_obj.write("Delta-X Value = {}\n".format(str(delta_x_input_entry.get())))
                            file_obj.write("Exact Result = {}\n".format(str(exact_entry.get())))
                            file_obj.write("Approx. Result = {}\n".format(str(appr_entry.get())))
                            file_obj.write("Abs. Relative True Error(%) = {}\n".format(str(abs_error_entry.get())))
                            file_obj.write("======================================================================================\n")
                            file_obj.flush()
                    finally:
                        file_obj.close()
                elif(int(scale_for_func.get()) == 4):
                    try:
                        with open("records_of_results.txt", 'a', encoding = 'utf-8') as file_obj:
                            file_obj.write("BDA Method\n")
                            file_obj.write("Function -> F(X) = 10^X\n")
                            file_obj.write("Derived Function -> F`(X) = ln(10) * (10^X)\n")
                            file_obj.write("X-Value = {}\n".format(str(x_value_entry.get())))
                            file_obj.write("Delta-X Value = {}\n".format(str(delta_x_input_entry.get())))
                            file_obj.write("Exact Result = {}\n".format(str(exact_entry.get())))
                            file_obj.write("Approx. Result = {}\n".format(str(appr_entry.get())))
                            file_obj.write("Abs. Relative True Error(%) = {}\n".format(str(abs_error_entry.get())))
                            file_obj.write("======================================================================================\n")
                            file_obj.flush()
                    finally:
                        file_obj.close()
                elif(int(scale_for_func.get()) == 5):
                    try:
                        with open("records_of_results.txt", 'a', encoding = 'utf-8') as file_obj:
                            file_obj.write("BDA Method\n")
                            file_obj.write("Function -> F(X) = log(X)[Base = 10]\n")
                            file_obj.write("Derived Function -> F`(X) = 1 / (ln(10) * X)\n")
                            file_obj.write("X-Value = {}\n".format(str(x_value_entry.get())))
                            file_obj.write("Delta-X Value = {}\n".format(str(delta_x_input_entry.get())))
                            file_obj.write("Exact Result = {}\n".format(str(exact_entry.get())))
                            file_obj.write("Approx. Result = {}\n".format(str(appr_entry.get())))
                            file_obj.write("Abs. Relative True Error(%) = {}\n".format(str(abs_error_entry.get())))
                            file_obj.write("======================================================================================\n")
                            file_obj.flush()
                    finally:
                        file_obj.close()
                elif(int(scale_for_func.get()) == 6):
                    try:
                        with open("records_of_results.txt", 'a', encoding = 'utf-8') as file_obj:
                            file_obj.write("BDA Method\n")
                            file_obj.write("Function -> F(X) = log(X)[Base = 2]\n")
                            file_obj.write("Derived Function -> F`(X) = 1 / (ln(2) * X)\n")
                            file_obj.write("X-Value = {}\n".format(str(x_value_entry.get())))
                            file_obj.write("Delta-X Value = {}\n".format(str(delta_x_input_entry.get())))
                            file_obj.write("Exact Result = {}\n".format(str(exact_entry.get())))
                            file_obj.write("Approx. Result = {}\n".format(str(appr_entry.get())))
                            file_obj.write("Abs. Relative True Error(%) = {}\n".format(str(abs_error_entry.get())))
                            file_obj.write("======================================================================================\n")
                            file_obj.flush()
                    finally:
                        file_obj.close()
                elif(int(scale_for_func.get()) == 7):
                    try:
                        with open("records_of_results.txt", 'a', encoding = 'utf-8') as file_obj:
                            file_obj.write("BDA Method\n")
                            file_obj.write("Function -> F(X) = Sin(X°)\n")
                            file_obj.write("Derived Function -> F`(X) = Cos(X°)\n")
                            file_obj.write("X-Value = {}°\n".format(str(x_value_entry.get())))
                            file_obj.write("Delta-X Value = {}°\n".format(str(delta_x_input_entry.get())))
                            file_obj.write("Exact Result = {}\n".format(str(exact_entry.get())))
                            file_obj.write("Approx. Result = {}\n".format(str(appr_entry.get())))
                            file_obj.write("Abs. Relative True Error(%) = {}\n".format(str(abs_error_entry.get())))
                            file_obj.write("======================================================================================\n")
                            file_obj.flush()
                    finally:
                        file_obj.close()
                elif(int(scale_for_func.get()) == 8):
                    try:
                       with open("records_of_results.txt", 'a', encoding = 'utf-8') as file_obj:
                            file_obj.write("BDA Method\n")
                            file_obj.write("Function -> F(X) = Cos(X°)\n")
                            file_obj.write("Derived Function -> F`(X) = -Sin(X°)\n")
                            file_obj.write("X-Value = {}°\n".format(str(x_value_entry.get())))
                            file_obj.write("Delta-X Value = {}°\n".format(str(delta_x_input_entry.get())))
                            file_obj.write("Exact Result = {}\n".format(str(exact_entry.get())))
                            file_obj.write("Approx. Result = {}\n".format(str(appr_entry.get())))
                            file_obj.write("Abs. Relative True Error(%) = {}\n".format(str(abs_error_entry.get())))
                            file_obj.write("======================================================================================\n")
                            file_obj.flush()
                    finally:
                        file_obj.close()
                elif(int(scale_for_func.get()) == 9):
                    try:
                        with open("records_of_results.txt", 'a', encoding = 'utf-8') as file_obj:
                            file_obj.write("BDA Method\n")
                            file_obj.write("Function -> F(X) = Tan(X°)\n")
                            file_obj.write("Derived Function -> F`(X) = Sec^2(X°)\n")
                            file_obj.write("X-Value = {}°\n".format(str(x_value_entry.get())))
                            file_obj.write("Delta-X Value = {}°\n".format(str(delta_x_input_entry.get())))
                            file_obj.write("Exact Result = {}\n".format(str(exact_entry.get())))
                            file_obj.write("Approx. Result = {}\n".format(str(appr_entry.get())))
                            file_obj.write("Abs. Relative True Error(%) = {}\n".format(str(abs_error_entry.get())))
                            file_obj.write("======================================================================================\n")
                            file_obj.flush()
                    finally:
                        file_obj.close()
                elif(int(scale_for_func.get()) == 10):
                    try:
                       with open("records_of_results.txt", 'a', encoding = 'utf-8') as file_obj:
                            file_obj.write("BDA Method\n")
                            file_obj.write("Function -> F(X) = X^2\n")
                            file_obj.write("Derived Function -> F`(X) = 2 * X\n")
                            file_obj.write("X-Value = {}\n".format(str(x_value_entry.get())))
                            file_obj.write("Delta-X Value = {}\n".format(str(delta_x_input_entry.get())))
                            file_obj.write("Exact Result = {}\n".format(str(exact_entry.get())))
                            file_obj.write("Approx. Result = {}\n".format(str(appr_entry.get())))
                            file_obj.write("Abs. Relative True Error(%) = {}\n".format(str(abs_error_entry.get())))
                            file_obj.write("======================================================================================\n")
                            file_obj.flush()
                    finally:
                        file_obj.close()
                elif(int(scale_for_func.get()) == 11):
                    try:
                        with open("records_of_results.txt", 'a', encoding = 'utf-8') as file_obj:
                            file_obj.write("BDA Method\n")
                            file_obj.write("Function -> F(X) = Sqrt(X)\n")
                            file_obj.write("Derived Function -> F`(X) = 1 / (2 * Sqrt(X))\n")
                            file_obj.write("X-Value = {}\n".format(str(x_value_entry.get())))
                            file_obj.write("Delta-X Value = {}\n".format(str(delta_x_input_entry.get())))
                            file_obj.write("Exact Result = {}\n".format(str(exact_entry.get())))
                            file_obj.write("Approx. Result = {}\n".format(str(appr_entry.get())))
                            file_obj.write("Abs. Relative True Error(%) = {}\n".format(str(abs_error_entry.get())))
                            file_obj.write("======================================================================================\n")
                            file_obj.flush()
                    finally:
                        file_obj.close()
                elif(int(scale_for_func.get()) == 12):
                    msb.showinfo("INFO", "No Selected Function !")
                else:
                    msb.showerror("Invalid Selection", "Please Try Again !")
            else:
                msb.showerror("File Error", "File Not Found !")

    # Instantiate Object.
    execute = BDA_Window_Methods()
    # Calculate Button.(Command Set)
    calculate_btn = Button(bda_win, justify = CENTER, height = 1, width = 12, bg = "turquoise1", fg = "IndianRed1", text = str("CALCULATE"), font = ("Times New Roman", 14, "bold"), activebackground = "white", activeforeground = "white", relief = RAISED, command = lambda: execute.calculate_all())
    calculate_btn.place(x = 15.0, y = 310.0)

    # Save Button.(Command Set)
    save_btn = Button(bda_win, justify = CENTER , height = 1, width = 12, bg = "turquoise1", fg = "IndianRed1", text = str("SAVE"), font = ("Times New Roman", 14, "bold"), activebackground = "white", activeforeground = "white", relief = RAISED, command = lambda: execute.save_results())
    save_btn.place(x = 200.0, y = 310.0)

    # Clear Button.(Command Set)
    clear_btn = Button(bda_win, justify = CENTER , height = 1, width = 12, bg = "turquoise1", fg = "IndianRed1", text = str("CLEAR"), font = ("Times New Roman", 14, "bold"), activebackground = "white", activeforeground = "white", relief = RAISED, command = lambda: execute.clear_all())
    clear_btn.place(x = 392.0, y = 310.0)

    return None