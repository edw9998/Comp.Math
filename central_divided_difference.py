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
