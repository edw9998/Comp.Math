from tkinter import *
from PIL import Image, ImageTk
from fda_win import window_for_fda
from bda_win import window_for_bda
from cdda_win import window_for_cdda

'''
A Simulation Of Custom User - Defined Math Functions(As Lambda Expressions) Is Available In Jupyter Notebook.
'''
# Layout For Main Window.
root = Tk()
# Syntax : ("width x height + pad-x + pad-y")
root.geometry("630x502+0+0")
root.resizable(height = False, width = False)
root.title("Numerical Differentiation Methods")
root.config(bg = None)

# Menu Bar.(Command For Error Comparison's tk.Toplevel() = ????????????????????????????????????????????????????????????????????????????????????)
Main_menu_bar = Menu(root)
More_Menu = Menu(Main_menu_bar, tearoff = 0)
More_Menu.add_command(label = "Quit", command = root.quit)
More_Menu.add_separator()
Main_menu_bar.add_cascade(label = 'Leave', menu = More_Menu)

# Prepare The Image(Poster) For Canvas.
this_img = Image.open("math_poster.jpg")
to_Tk_img = ImageTk.PhotoImage(this_img, Image.ANTIALIAS)

# Canvas For The Whole Window. 
whole = Canvas(root, bg = None, height = 675.0, width = 630.0)
img = whole.create_image(675.0, 630.0, anchor = CENTER, image = to_Tk_img)
whole.pack()

# Control Variable For Title & Set Universal Font Style.
main_title_var = StringVar(root, name = "main_title", value = None)
global_font_style = str("Times New Roman")

# Main Title.
main_title = Label(root, bg = "chocolate1", fg = "medium spring green", font = (global_font_style, 12, "bold"), anchor = CENTER, textvariable = main_title_var, relief = GROOVE, padx = 2, pady = 2, height = 5, width = 0)
root.setvar(name = "main_title", value = str("The Simulation Of Three Different Numerical Differentiation's Value Approximation Methods"))
main_title.place(x = 0.0, y = 0.0)

# Button To Access FDA Method's First External Master.
# Delta-Y = 150.0 Pixels.
# Command Set !
fda_text = str("Forward-Difference Approximation")
fda_access = Button(root, justify = CENTER, width = 31, height = 2, bg = "OliveDrab1", fg = "red2", text = fda_text, font = (global_font_style, 20, "bold"), activebackground = "white", activeforeground = "white", relief = RAISED, command = lambda: window_for_fda())
fda_access.place(x = 60.0, y = 100.0)

# Button To Access BDA Method's Second External Master.
# Command Set !
bda_text = str("Backward-Difference Approximation")
bda_access = Button(root, justify = CENTER, width = 31, height = 2, bg = "OliveDrab1", fg = "chartreuse2", text = bda_text, font = (global_font_style, 20, "bold"), activebackground = "white", activeforeground = "white", relief = RAISED, command = lambda: window_for_bda())
bda_access.place(x = 60.0, y = 250.0)

# Button To Access CDDA Method's Third External Master.
# Command Set !
cdda_text = str("Central-Divided-Difference Approximation")
cdda_access = Button(root, justify = CENTER, width = 31, height = 2, bg = "OliveDrab1", fg = "DodgerBlue2", text = cdda_text, font = (global_font_style, 20, "bold"), activebackground = "white", activeforeground = "white", relief = RAISED, command = lambda: window_for_cdda())
cdda_access.place(x = 60.0, y = 400.0)

if __name__ == '__main__':
    root.config(menu = Main_menu_bar)
    root.mainloop()