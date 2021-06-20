from tkinter import *
import tkinter.messagebox as msb
import os
import sys
import numpy as np
from mpmath import sec, tan, sqrt
import math
from functions_list import functions_list_window

def window_for_fda():
    # FDA Window's Setup.
    fda_win = Tk()
    fda_win.resizable(height = False, width = False)
    fda_win.title("FDA")
    fda_win.geometry("550x520+0+0")
    fda_win.config(bg = "gold2")

    # Control Variables For Widgets.
    sep_var = StringVar(fda_win, name = "separator", value = str("--------------------------------------------------------------------"))
    x_value_label_var = StringVar(fda_win, name = "x_val", value = str("Set X-Value = "))
    step_x_value_label_var = StringVar(fda_win, name = "step_size_val", value = str("Set Step-Size(Delta-X) = "))
    large_sep_var = StringVar(fda_win, name = "large_separator", value = str("===================================================================="))

    # FDA Window's Main Title.
    fda_title = Label(fda_win, bg = "khaki", fg = "red2", font = ("Times New Roman", 25, "bold"), text = str("FDA Method's Value Approximation"), anchor = CENTER, relief = GROOVE, padx = 14, pady = 2, height = 2, width = -10)
    fda_title.place(x = 0.0, y = 0.0)

    # Label For Function Scale.
    func_label = Label(fda_win, font = ("Times New Roman", 7, "italic", "bold"), anchor = CENTER, relief = FLAT, fg = "blue2", bg = "gold2", text = str("Select A Function To Be Derived -> F(X) = "))
    func_label.place(x = 15.0, y = 90.0)

    # Selections Scale.
    func_scale = Scale(fda_win, from_ = 1, to = 12, cursor = "dot", highlightbackground = "red2", activebackground = "cyan3")
    func_scale.place(x = 215.0, y = 90.0) 

    # Button To Access List Of Math Functions.
    # Command Set !
    help_text = str("HELP")
    help_button = Button(fda_win, justify = CENTER, height = 2, width = 10, bg = "turquoise1", fg = "black", text = help_text, font = ("Times New Roman", 14, "bold"), activebackground = "white", activeforeground = "white", relief = RAISED, command = lambda: functions_list_window())
    help_button.place(x = 45.0, y = 115.0)

    # Separator.
    sep_label = Label(fda_win, bg = "gold2", fg = "black", textvariable = sep_var)
    sep_label.place(x = -1.0, y = 195.0)

    # Label For X-Value Input.
    x_val_label = Label(fda_win, font = ("Times New Roman", 12, "italic", "bold"), anchor = CENTER, textvariable = x_value_label_var, relief = FLAT, fg = "blue2", bg = "gold2")
    x_val_label.place(x = 15.0, y = 215.0)

    # Entry To Contain X_Value Input.
    x_val_entry = Entry(fda_win, font = ("Times New Roman", 12, "bold"), bg = "snow4", fg = "black", justify = LEFT, relief = SUNKEN, width = 28)
    x_val_entry.place(x = 120.0, y = 217.0)

    # Separator #2.
    sep2_label = Label(fda_win, bg = "gold2", fg = "black", textvariable = sep_var)
    sep2_label.place(x = -1.0, y = 240.0)

    # Label For Delta-X Input.
    delta_x_label = Label(fda_win, font = ("Times New Roman", 12, "bold", "italic"), anchor = CENTER, textvariable = step_x_value_label_var, relief = FLAT, fg = "blue2", bg = "gold2")
    delta_x_label.place(x = 15.0, y = 257.0)

    # Entry To Contain Delta-X Input.
    delta_x_entry = Entry(fda_win, font = ("Times New Roman", 12, "bold"), bg = "snow4", fg = "black", justify = LEFT, relief = SUNKEN, width = 20)
    delta_x_entry.place(x = 185.0, y = 259.0)

    # A Large Separator.
    large_sep = Label(fda_win, bg = "gold2", fg = "black", textvariable = large_sep_var)
    large_sep.place(x = 0.0, y = 290.0)

    '''
    (2x3)Table With Entries For The Whole Second Row,
    Entry[1][0] Stores Exact Results.
    Entry[1][1] Stores Approximated Results.
    Entry[1][2] Stores Abs. Relative True Error Rate(%).
    '''
    exact_label = Label(fda_win, justify = CENTER, height = 1, width = 12, bg = "black", fg = "gold2", text = str("Exact Value = "), font = ("Times New Roman", 18, "bold"), relief = RIDGE)
    exact_label.place(x = 16.0, y = 370.0)

    # Entry[1][0] :
    exact_entry = Entry(fda_win, justify = LEFT, width = 29, bg = "orange", fg = "black", font = ("Times New Roman", 18, "bold"), relief = RIDGE)
    exact_entry.place(x = 190.0, y = 371.0)

    appr_label = Label(fda_win, justify = CENTER, height = 1, width = 14, bg = "black", fg = "gold2", text = str("Approx. Value = "), font = ("Times New Roman", 16, "bold"), relief = RIDGE)
    appr_label.place(x = 16.0, y = 425.0) 

    # Entry[1][1] :
    appr_entry = Entry(fda_win, justify = LEFT, width = 29, bg = "orange", fg = "black", font = ("Times New Roman", 18, "bold"), relief = RIDGE)
    appr_entry.place(x = 190.0, y = 425.0)

    abs_error_label = Label(fda_win, justify = CENTER, height = 2, width = 24, bg = "black", fg = "gold2", text = str("Abs. Relative True Error(%) = "), font = ("Times New Roman", 10, "bold"), relief = RIDGE)
    abs_error_label.place(x = 16.0, y = 475.0)

    # Entry[1][2] :
    abs_error_entry = Entry(fda_win, justify = LEFT, width = 29, bg = "orange", fg = "black", font = ("Times New Roman", 18, "bold"), relief = RIDGE)
    abs_error_entry.place(x = 190.0, y = 478.0)

    # Method Implementations.
    class FDA_Window_Methods(Exception):
        '''
        Method Implementations Within FDA Toplevel.
        '''
        def __init__(self, exact_entry_len = len(exact_entry.get()), appr_entry_len = len(appr_entry.get()), abs_entry_len = len(abs_error_entry.get()), **kwargs):
            '''
            Only Final(Const) Variables Are Allowed For Initialization.
            '''
            Exception.__init__(self)
            self.__length_of_exact_entry = exact_entry_len
            self.__length_of_appr_entry = appr_entry_len
            self.__length_of_abserror_entry = abs_entry_len

        @staticmethod
        def clear_all():
            exact_entry.delete(0, END)
            appr_entry.delete(0, END)
            abs_error_entry.delete(0, END)

        def calculate_all(self):
            '''
            FDA Method's Approach :
                F`(X) ≈ [F(X + ΔX) - F(X)] / ΔX
                    Where ΔX Is Equal To The Value Of Size Of Step.
            '''
            if(int(func_scale.get()) == 1):
                '''
                Since The Derivative Of exp(X) Is Equal To Itself, Both Results Will Be Extremely Irrelevant Towards Each Other.
                No Form Of Correlation Is Shown, Thus The Value Of Abs. Relative True Error Will Be Extremely High. 
                '''
                # Calculations.
                exact_value = np.exp(float(x_val_entry.get()))
                appr_value = (np.exp((float(x_val_entry.get()) + float(delta_x_entry.get()))) - exact_value) / float(delta_x_entry.get())
                abs_error = str(round(np.abs((exact_value - appr_value) / exact_value) * float(100.0), 5)) + " %"

                self.clear_all()

                # Insertions Where Results Are Rounded Off To At Most 5 Decimal Points.
                exact_entry.insert(self.__length_of_exact_entry, str(round(exact_value, 5)))
                appr_entry.insert(self.__length_of_appr_entry, str(round(appr_value, 5)))
                abs_error_entry.insert(self.__length_of_abserror_entry, abs_error)
            elif(int(func_scale.get()) == 2):
                '''
                Derivative Of ln(X) -> np.log(X) Is X**(-1) Which Will Be Used For Calculating Exact Values.
                '''
                try:
                    exact_val = 1 / (float(x_val_entry.get())**(1.0))
                    appr_val = (np.log((float(x_val_entry.get()) + float(delta_x_entry.get()))) - np.log(float(x_val_entry.get()))) / float(delta_x_entry.get())
                    abs_error_val = str(round(np.abs((exact_val - appr_val) / exact_val) * float(100.0), 5)) + " %"
                    self.clear_all()
                    exact_entry.insert(self.__length_of_exact_entry, str(round(exact_val, 5)))
                    appr_entry.insert(self.__length_of_appr_entry, str(round(appr_val, 5)))
                    abs_error_entry.insert(self.__length_of_abserror_entry, abs_error_val)
                except Exception:
                    msb.showerror("INFO", "An Error Occured !")
            elif(int(func_scale.get()) == 3):
                '''
                Derivative Of X**(-1) Is -1*(X**(-2)).
                '''
                try:
                    exact_val = -1 * (1 / (float(x_val_entry.get())**(2.0)))
                    appr_val = (((float(x_val_entry.get()) + float(delta_x_entry.get()))**(-1.0)) - (float(x_val_entry.get())**(-1.0))) / float(delta_x_entry.get())
                    abs_error_val = str(round(np.abs((exact_val - appr_val) / exact_val) * float(100.0), 5)) + " %"
                    self.clear_all()
                    exact_entry.insert(self.__length_of_exact_entry, str(round(exact_val, 5)))
                    appr_entry.insert(self.__length_of_appr_entry, str(round(appr_val, 5)))
                    abs_error_entry.insert(self.__length_of_abserror_entry, abs_error_val)
                except Exception:
                    msb.showerror("INFO", "An Error Occured !")
            elif(int(func_scale.get()) == 4):
                '''
                Derivative Of 10**(X) Is ln(10) * 10**(X).
                '''
                try:
                    exact_val = np.log(float(10.0)) * (10**(float(x_val_entry.get())))
                    appr_val = (10**((float(x_val_entry.get()) + float(delta_x_entry.get())))) - (10**(float(x_val_entry.get()))) / float(delta_x_entry.get())
                    abs_error_val = str(round(np.abs((exact_val - appr_val) / exact_val) * float(100.0), 5)) + " %"
                    self.clear_all()
                    exact_entry.insert(self.__length_of_exact_entry, str(round(exact_val, 5)))
                    appr_entry.insert(self.__length_of_appr_entry, str(round(appr_val, 5)))
                    abs_error_entry.insert(self.__length_of_abserror_entry, abs_error_val)
                except Exception:
                    msb.showerror("INFO", "An Error Occured !")
            elif(int(func_scale.get()) == 5):
                '''
                Derivative Of log(X)[Base = 10] Is (ln(10) * X)**(-1).
                '''
                try:
                    exact_val = 1 / (np.log(float(10.0)) * float(x_val_entry.get()))
                    appr_val = ((np.log10((float(x_val_entry.get()) + float(delta_x_entry.get())))) - np.log10(float(x_val_entry.get()))) / float(delta_x_entry.get())
                    abs_error_val = str(round(np.abs((exact_val - appr_val) / exact_val) * float(100.0), 5)) + " %"
                    self.clear_all()
                    exact_entry.insert(self.__length_of_exact_entry, str(round(exact_val, 5)))
                    appr_entry.insert(self.__length_of_appr_entry, str(round(appr_val, 5)))
                    abs_error_entry.insert(self.__length_of_abserror_entry, abs_error_val)
                except Exception:
                    msb.showerror("INFO", "An Error Occured !")
            elif(int(func_scale.get()) == 6):
                '''
                Derivative Of log(X)[Base = 2] Is (ln(2) * X)**(-1).
                '''
                try:
                    exact_val = 1 / (np.log(float(2.0)) * float(x_val_entry.get()))
                    appr_val = (np.log2((float(x_val_entry.get()) + float(delta_x_entry.get()))) - np.log2(float(x_val_entry.get()))) / float(delta_x_entry.get())
                    abs_error_val = str(round(np.abs((exact_val - appr_val) / exact_val) * float(100.0), 5)) + " %"
                    self.clear_all()
                    exact_entry.insert(self.__length_of_exact_entry, str(round(exact_val, 5)))
                    appr_entry.insert(self.__length_of_appr_entry, str(round(appr_val, 5)))
                    abs_error_entry.insert(self.__length_of_abserror_entry, abs_error_val)
                except Exception:
                    msb.showerror("INFO", "An Error Occured !")
            elif(int(func_scale.get()) == 7):
                '''
                Derivative Of Sin(X) Is Cos(X).
                '''
                try:
                    exact_val = np.cos(math.radians(float(x_val_entry.get())))
                    appr_val = (np.sin((math.radians(float(x_val_entry.get())) + math.radians(float(delta_x_entry.get())))) - np.sin(math.radians(float(x_val_entry.get())))) / math.radians(float(delta_x_entry.get()))
                    abs_error_val = str(round(np.abs((exact_val - appr_val) / exact_val) * float(100.0), 5)) + " %"
                    self.clear_all()
                    exact_entry.insert(self.__length_of_exact_entry, str(round(exact_val, 5)))
                    appr_entry.insert(self.__length_of_appr_entry, str(round(appr_val, 5)))
                    abs_error_entry.insert(self.__length_of_abserror_entry, abs_error_val)
                except Exception:
                    msb.showerror("INFO", "An Error Occured !")
            elif(int(func_scale.get()) == 8):
                '''
                Derivative Of Cos(X) Is -Sin(X).
                '''
                try:
                    exact_val = float(-1.0) * np.sin(math.radians(float(x_val_entry.get())))
                    appr_val = (np.cos((math.radians(float(x_val_entry.get())) + math.radians(float(delta_x_entry.get())))) - np.cos(math.radians(float(x_val_entry.get())))) / math.radians(float(delta_x_entry.get()))
                    abs_error_val = str(round(np.abs((exact_val - appr_val) / exact_val) * float(100.0), 5)) + " %"
                    self.clear_all()
                    exact_entry.insert(self.__length_of_exact_entry, str(round(exact_val, 5)))
                    appr_entry.insert(self.__length_of_appr_entry, str(round(appr_val, 5)))
                    abs_error_entry.insert(self.__length_of_abserror_entry, abs_error_val)
                except Exception:
                    msb.showerror("INFO", "An Error Occured !")
            elif(int(func_scale.get()) == 9):
                '''
                Derivative Of Tan(X) Is Sec^2(X).
                '''
                try:
                    exact_val = float(sec(float(math.radians(x_val_entry.get()))))**(2.0)
                    appr_val = (tan(math.radians(float(x_val_entry.get())) + math.radians(float(delta_x_entry.get()))) - tan(math.radians(float(x_val_entry.get())))) / math.radians(float(delta_x_entry.get()))
                    abs_error_val = str(round(np.abs((exact_val - appr_val) / exact_val) * float(100.0), 5)) + " %"
                    self.clear_all()
                    exact_entry.insert(self.__length_of_exact_entry, str(round(exact_val, 5)))
                    appr_entry.insert(self.__length_of_appr_entry, str(round(appr_val, 5)))
                    abs_error_entry.insert(self.__length_of_abserror_entry, abs_error_val)
                except Exception:
                    msb.showerror("INFO", "An Error Occured !")
            elif(int(func_scale.get()) == 10):
                '''
                Derivative Of X^2 Is 2 * X.
                '''
                try:
                    exact_val = float(2 * float(x_val_entry.get()))
                    appr_val = (((float(x_val_entry.get()) + float(delta_x_entry.get()))**(2.0)) - (float(x_val_entry.get())**(2.0))) / float(delta_x_entry.get())
                    abs_error_val = str(round(np.abs((exact_val - appr_val) / exact_val) * float(100.0), 5)) + " %"
                    self.clear_all()
                    exact_entry.insert(self.__length_of_exact_entry, str(round(exact_val, 5)))
                    appr_entry.insert(self.__length_of_appr_entry, str(round(appr_val, 5)))
                    abs_error_entry.insert(self.__length_of_abserror_entry, abs_error_val)
                except Exception:
                    msb.showerror("INFO", "An Error Occured !")
            elif(int(func_scale.get()) == 11):
                '''
                Derivative Of √X Is 1 / (2 * √X).
                '''
                try:
                    exact_val = float(1 / (2 * sqrt(float(x_val_entry.get()))))
                    appr_val = (sqrt((float(x_val_entry.get()) + float(delta_x_entry.get()))) - sqrt(float(x_val_entry.get()))) / float(delta_x_entry.get())
                    abs_error_val = str(round(np.abs((exact_val - appr_val) / exact_val) * float(100.0), 5)) + " %"
                    self.clear_all()
                    exact_entry.insert(self.__length_of_exact_entry, str(round(exact_val, 5)))
                    appr_entry.insert(self.__length_of_appr_entry, str(round(appr_val, 5)))
                    abs_error_entry.insert(self.__length_of_abserror_entry, abs_error_val)
                except Exception:
                    msb.showerror("INFO", "An Error Occured !")
            elif(int(func_scale.get()) == 12):
                msb.showinfo("'None' Specified !", "No Function Is Specified.")
            else:
                msb.showerror("Invalid Selection", "Please Try Again.")

        @staticmethod
        def save_results():
            if(os.path.exists("C:/Users/EDWARD/comp._math/records_of_results.txt")):
                if(int(func_scale.get()) == 1):
                    try:
                        with open("records_of_results.txt", 'a', encoding = 'utf-8') as file_obj:
                            file_obj.write("FDA Method\n")
                            file_obj.write("An Irrelevant Result !\n")
                            file_obj.write("Function -> F(X) = exp(X)\n")
                            file_obj.write("Derived Function -> F`(X) = exp(X)\n")
                            file_obj.write("X - Value = {}\n".format(str(x_val_entry.get())))
                            file_obj.write("Delta-X Value = {}\n".format(str(delta_x_entry.get())))
                            file_obj.write("Exact Result = {}\n".format(str(exact_entry.get())))
                            file_obj.write("Approx. Result = {}\n".format(str(appr_entry.get())))
                            file_obj.write("Abs. Relative True Error(%) = {}\n".format(str(abs_error_entry.get())))
                            file_obj.write("======================================================================================\n")
                            file_obj.flush()
                    finally:
                        file_obj.close()
                elif(int(func_scale.get()) == 2):
                    try:
                        with open("records_of_results.txt", 'a', encoding = 'utf-8') as file_obj:
                            file_obj.write("FDA Method\n")
                            file_obj.write("Function -> F(X) = ln(X)\n")
                            file_obj.write("Derived Function -> F`(X) = 1 / X\n")
                            file_obj.write("X - Value = {}\n".format(str(x_val_entry.get())))
                            file_obj.write("Delta-X Value = {}\n".format(str(delta_x_entry.get())))
                            file_obj.write("Exact Result = {}\n".format(str(exact_entry.get())))
                            file_obj.write("Approx. Result = {}\n".format(str(appr_entry.get())))
                            file_obj.write("Abs. Relative True Error(%) = {}\n".format(str(abs_error_entry.get())))
                            file_obj.write("======================================================================================\n")
                            file_obj.flush()
                    finally:
                        file_obj.close()
                elif(int(func_scale.get()) == 3):
                    try:
                        with open("records_of_results.txt", 'a', encoding = 'utf-8') as file_obj:
                            file_obj.write("FDA Method\n")
                            file_obj.write("Function -> F(X) = 1 / X\n")
                            file_obj.write("Derived Function -> F`(X) = - 1 / X**2\n")
                            file_obj.write("X - Value = {}\n".format(str(x_val_entry.get())))
                            file_obj.write("Delta-X Value = {}\n".format(str(delta_x_entry.get())))
                            file_obj.write("Exact Result = {}\n".format(str(exact_entry.get())))
                            file_obj.write("Approx. Result = {}\n".format(str(appr_entry.get())))
                            file_obj.write("Abs. Relative True Error(%) = {}\n".format(str(abs_error_entry.get())))
                            file_obj.write("======================================================================================\n")
                            file_obj.flush()
                    finally:
                        file_obj.close()
                elif(int(func_scale.get()) == 4):
                    try:
                        with open("records_of_results.txt", 'a', encoding = 'utf-8') as file_obj:
                            file_obj.write("FDA Method\n")
                            file_obj.write("Function -> F(X) = 10^X\n")
                            file_obj.write("Derived Function -> F`(X) = ln(10) * 10^X\n")
                            file_obj.write("X - Value = {}\n".format(str(x_val_entry.get())))
                            file_obj.write("Delta-X Value = {}\n".format(str(delta_x_entry.get())))
                            file_obj.write("Exact Result = {}\n".format(str(exact_entry.get())))
                            file_obj.write("Approx. Result = {}\n".format(str(appr_entry.get())))
                            file_obj.write("Abs. Relative True Error(%) = {}\n".format(str(abs_error_entry.get())))
                            file_obj.write("======================================================================================\n")
                            file_obj.flush()
                    finally:
                        file_obj.close()
                elif(int(func_scale.get()) == 5):
                    try:
                        with open("records_of_results.txt", 'a', encoding = 'utf-8') as file_obj:
                            file_obj.write("FDA Method\n")
                            file_obj.write("Function -> F(X) = log(X)[Base = 10]\n")
                            file_obj.write("Derived Function -> F`(X) = 1 / (ln(10) * X)\n")
                            file_obj.write("X - Value = {}\n".format(str(x_val_entry.get())))
                            file_obj.write("Delta-X Value = {}\n".format(str(delta_x_entry.get())))
                            file_obj.write("Exact Result = {}\n".format(str(exact_entry.get())))
                            file_obj.write("Approx. Result = {}\n".format(str(appr_entry.get())))
                            file_obj.write("Abs. Relative True Error(%) = {}\n".format(str(abs_error_entry.get())))
                            file_obj.write("======================================================================================\n")
                            file_obj.flush()
                    finally:
                        file_obj.close()
                elif(int(func_scale.get()) == 6):
                    try:
                        with open("records_of_results.txt", 'a', encoding = 'utf-8') as file_obj:
                            file_obj.write("FDA Method\n")
                            file_obj.write("Function -> F(X) = log(X)[Base = 2]\n")
                            file_obj.write("Derived Function -> F`(X) = 1 / (ln(2) * X)\n")
                            file_obj.write("X - Value = {}\n".format(str(x_val_entry.get())))
                            file_obj.write("Delta-X Value = {}\n".format(str(delta_x_entry.get())))
                            file_obj.write("Exact Result = {}\n".format(str(exact_entry.get())))
                            file_obj.write("Approx. Result = {}\n".format(str(appr_entry.get())))
                            file_obj.write("Abs. Relative True Error(%) = {}\n".format(str(abs_error_entry.get())))
                            file_obj.write("======================================================================================\n")
                            file_obj.flush()
                    finally:
                        file_obj.close()
                elif(int(func_scale.get()) == 7):
                    try:
                        with open("records_of_results.txt", 'a', encoding = 'utf-8') as file_obj:
                            file_obj.write("FDA Method\n")
                            file_obj.write("Function -> F(X) = Sin(X°)\n")
                            file_obj.write("Derived Function -> F`(X) = Cos(X°)\n")
                            file_obj.write("X - Value = {}°\n".format(str(x_val_entry.get())))
                            file_obj.write("Delta-X Value = {}°\n".format(str(delta_x_entry.get())))
                            file_obj.write("Exact Result = {}\n".format(str(exact_entry.get())))
                            file_obj.write("Approx. Result = {}\n".format(str(appr_entry.get())))
                            file_obj.write("Abs. Relative True Error(%) = {}\n".format(str(abs_error_entry.get())))
                            file_obj.write("======================================================================================\n")
                            file_obj.flush()
                    finally:
                        file_obj.close()
                elif(int(func_scale.get()) == 8):
                    try:
                        with open("records_of_results.txt", 'a', encoding = 'utf-8') as file_obj:
                            file_obj.write("FDA Method\n")
                            file_obj.write("Function -> F(X) = Cos(X°)\n")
                            file_obj.write("Derived Function -> F`(X) = -Sin(X°)\n")
                            file_obj.write("X - Value = {}°\n".format(str(x_val_entry.get())))
                            file_obj.write("Delta-X Value = {}°\n".format(str(delta_x_entry.get())))
                            file_obj.write("Exact Result = {}\n".format(str(exact_entry.get())))
                            file_obj.write("Approx. Result = {}\n".format(str(appr_entry.get())))
                            file_obj.write("Abs. Relative True Error(%) = {}\n".format(str(abs_error_entry.get())))
                            file_obj.write("======================================================================================\n")
                            file_obj.flush()
                    finally:
                        file_obj.close()
                elif(int(func_scale.get()) == 9):
                    try:
                        with open("records_of_results.txt", 'a', encoding = 'utf-8') as file_obj:
                            file_obj.write("FDA Method\n")
                            file_obj.write("Function -> F(X) = Tan(X°)\n")
                            file_obj.write("Derived Function -> F`(X) = Sec^2(X°)\n")
                            file_obj.write("X - Value = {}°\n".format(str(x_val_entry.get())))
                            file_obj.write("Delta-X Value = {}°\n".format(str(delta_x_entry.get())))
                            file_obj.write("Exact Result = {}\n".format(str(exact_entry.get())))
                            file_obj.write("Approx. Result = {}\n".format(str(appr_entry.get())))
                            file_obj.write("Abs. Relative True Error(%) = {}\n".format(str(abs_error_entry.get())))
                            file_obj.write("======================================================================================\n")
                            file_obj.flush()
                    finally:
                        file_obj.close()
                elif(int(func_scale.get()) == 10):
                    try:
                        with open("records_of_results.txt", 'a', encoding = 'utf-8') as file_obj:
                            file_obj.write("FDA Method\n")
                            file_obj.write("Function -> F(X) = X^2\n")
                            file_obj.write("Derived Function -> F`(X) = 2 * X\n")
                            file_obj.write("X - Value = {}\n".format(str(x_val_entry.get())))
                            file_obj.write("Delta-X Value = {}\n".format(str(delta_x_entry.get())))
                            file_obj.write("Exact Result = {}\n".format(str(exact_entry.get())))
                            file_obj.write("Approx. Result = {}\n".format(str(appr_entry.get())))
                            file_obj.write("Abs. Relative True Error(%) = {}\n".format(str(abs_error_entry.get())))
                            file_obj.write("======================================================================================\n")
                            file_obj.flush()
                    finally:
                        file_obj.close()
                elif(int(func_scale.get()) == 11):
                    try:
                        with open("records_of_results.txt", 'a', encoding = 'utf-8') as file_obj:
                            file_obj.write("FDA Method\n")
                            file_obj.write("Function -> F(X) = √X\n")
                            file_obj.write("Derived Function -> F`(X) = 1 / (2 * √X)")
                            file_obj.write("X - Value = {}\n".format(str(x_val_entry.get())))
                            file_obj.write("Delta-X Value = {}\n".format(str(delta_x_entry.get())))
                            file_obj.write("Exact Result = {}\n".format(str(exact_entry.get())))
                            file_obj.write("Approx. Result = {}\n".format(str(appr_entry.get())))
                            file_obj.write("Abs. Relative True Error(%) = {}\n".format(str(abs_error_entry.get())))
                            file_obj.write("======================================================================================\n")
                            file_obj.flush()
                    finally:
                        file_obj.close()
                elif(int(func_scale.get()) == 12):
                    msb.showinfo("INFO", "No Selected Function !")
                else:
                    msb.showerror("Invalid Selection", "Please Try Again !")          
            else:
                msb.showerror("File Error", "File Not Found !")

    # Instantiate Object.
    execute = FDA_Window_Methods()
    # CALCULATE Button(Command Set !)
    calculate_btn = Button(fda_win, justify = CENTER, height = 1, width = 12, bg = "turquoise1", fg = "IndianRed1", text = str("CALCULATE"), font = ("Times New Roman", 14, "bold"), activebackground = "white", activeforeground = "white", relief = RAISED, command = lambda: execute.calculate_all())
    calculate_btn.place(x = 15.0, y = 310.0)

    # SAVE(Write To records.txt) Button(Command Set !)
    save_btn = Button(fda_win, justify = CENTER , height = 1, width = 12, bg = "turquoise1", fg = "IndianRed1", text = str("SAVE"), font = ("Times New Roman", 14, "bold"), activebackground = "white", activeforeground = "white", relief = RAISED, command = lambda: execute.save_results())
    save_btn.place(x = 200.0, y = 310.0)

    # CLEAR Button(Command Set !)
    clear_btn = Button(fda_win, justify = CENTER , height = 1, width = 12, bg = "turquoise1", fg = "IndianRed1", text = str("CLEAR"), font = ("Times New Roman", 14, "bold"), activebackground = "white", activeforeground = "white", relief = RAISED, command = lambda: execute.clear_all())
    clear_btn.place(x = 392.0, y = 310.0)

    return None