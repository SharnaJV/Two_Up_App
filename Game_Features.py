from tkinter import *

default_font_size = 10
selected_colour = {
    "bg_colour": "#EFE0B9", 
    "text_colour": "black"  
}

def change_font():
    global default_font_size
    new_font = ("Arial", default_font_size)

def font_options(screen):
    font_sizes = {
    "Small": ("Arial", 10),
    "Medium": ("Arial", 14),
    "Large": ("Arial", 20)
    }

    def font_selection(option_pick):
        print(f"Selected option: {option_pick}")

    label_font = Label(screen, text="Font Size", bg="#EFE0B9")
    label_font.pack(side=TOP)
    
    font_menu_frame = Frame(screen, bg="black")
    font_menu_frame.pack()
    
    font_size = ["Small", "Medium", "Large"]
    menu_01 = StringVar(screen)
    menu_01.set(font_size[0])
    font_menu = OptionMenu(font_menu_frame, menu_01, *font_size, command= lambda x: font_selection(menu_01.get()))
    font_menu.pack()

def change_colour_scheme(root):
    global selected_colour
    root.configure(bg=selected_colour["bg_colour"])
    for widget in root.winfo_children():
        try:
            widget.configure(bg=selected_colour["bg_colour"], fg=selected_colour["text_colour"])
        except TclError:
            pass

def colour_selection(option_pick,screen):
    global selected_colour
    colour_schemes = {
        "default": {"bg_color": "#EFE0B9", "text_color": "black"},
        "colour_blind": {"bg_color": "#FFFFCC", "text_color": "black"},  # Example color scheme for color blind users
        # Add more color schemes as needed
    }
    selected_colour = colour_schemes[option_pick]
    change_colour_scheme()

    label_colour = Label(screen, text="Color Scheme", bg="#EFE0B9")
    label_colour.pack()

    colour_menu_frame = Frame(screen, bg="black")
    colour_menu_frame.pack()

    colour_schemes = ["default", "colour_blind"]  # Add more color scheme options here
    menu_02 = StringVar(screen)
    menu_02.set(colour_schemes[0])
    colour_menu = OptionMenu(colour_menu_frame, menu_02, *colour_schemes, command=lambda x: colour_selection(menu_02.get()))
    colour_menu.pack()