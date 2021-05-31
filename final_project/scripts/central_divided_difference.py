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

    # Method Implementations.(???)   
    
    class CDA_Window_Methods(Exception):
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
                appr_value = (np.exp((float(x_val_entry.get()) + float(delta_x_entry.get()))) - (float(x_val_entry.get()) - float(delta_x_entry.get())) / (float(delta_x_entry.get()) * 2)
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
                    appr_val = (np.log((float(x_val_entry.get()) + float(delta_x_entry.get()))) - np.log(float(x_val_entry.get()) - float(delta_x_entry.get()))) / (float(delta_x_entry.get()) * 2)
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
                    appr_val = (((float(x_val_entry.get()) + float(delta_x_entry.get()))**(-1.0)) - (float(x_val_entry.get()) - float(delta_x_entry.get())**(-1.0))) / (float(delta_x_entry.get()) * 2)
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
                    appr_val = (10**((float(x_val_entry.get()) + float(delta_x_entry.get())))) - (10**(float(x_val_entry.get()) - float(delta_x_entry.get()))) / (float(delta_x_entry.get()) * 2)
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
                    appr_val = ((np.log10((float(x_val_entry.get()) + float(delta_x_entry.get())))) - np.log10(float(x_val_entry.get()) - float(delta_x_entry.get()))) / (float(delta_x_entry.get()) * 2)
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
                    appr_val = (np.log2((float(x_val_entry.get()) + float(delta_x_entry.get()))) - np.log2(float(x_val_entry.get()) - float(delta_x_entry.get()))) / (float(delta_x_entry.get()) * 2)
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
                    appr_val = (np.sin((math.radians(float(x_val_entry.get())) + math.radians(float(delta_x_entry.get())))) - np.sin(math.radians(float(x_val_entry.get())) - math.radians(float(delta_x_entry.get())))) / math.radians((float(delta_x_entry.get()) * 2))
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
                    appr_val = (np.cos((math.radians(float(x_val_entry.get())) + math.radians(float(delta_x_entry.get())))) - np.cos(math.radians(float(x_val_entry.get())) - math.radians(float(delta_x_entry.get())))) / math.radians((float(delta_x_entry.get()) * 2))
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
                    exact_val = float(sec(float(x_val_entry.get())))**(2.0)
                    appr_val = (tan(float(x_val_entry.get()) + float(delta_x_entry.get())) - tan(float(x_val_entry.get()) - float(delta_x_entry.get()))) / float((delta_x_entry.get() * 2))
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
                    appr_val = (((float(x_val_entry.get()) + float(delta_x_entry.get()))**(2.0)) - (float(x_val_entry.get() - float(delta_x_entry.get()))**(2.0))) / float((delta_x_entry.get() * 2))
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
                    appr_val = (sqrt((float(x_val_entry.get()) + float(delta_x_entry.get()))) - sqrt(float(x_val_entry.get()) - float(delta_x_entry.get()))) / float((delta_x_entry.get() * 2))
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
