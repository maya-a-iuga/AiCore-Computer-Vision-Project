import os
import tkinter as tk
import requests
from tkinter import font as tkfont
from tkinter import messagebox
from PIL import ImageTk, Image
from RPS_game_GUI import RPS_game
#from kivy.core.audio import SoundLoader

base_folder = os.path.dirname(__file__)
image_path = os.path.join(base_folder, 'RPSLS.webp')
image_RS_path = os.path.join(base_folder, 'RS.jpg')


class MainFrame(tk.Tk):

    """Frame object/Controller holding all of our different pages"""

    def __init__(self, *args, **kwargs):

        """See help(MainFrame) for more details"""

        tk.Tk.__init__(self, *args, **kwargs)
    
        self.titlefont = tkfont.Font(family = 'Helvetica', size = 18, weight = 'bold', slant = 'roman')
        self.title('RPS game')
        self.geometry('600x600')
      
        # frame object that will hold all the pages 
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both")
        container.grid_rowconfigure(0, weight = 1)
        container.columnconfigure (0, weight = 1)

        # create empty dictionary to define all pages
        self.frames = {}

        # These pages are built later on as classes
        for F in (WelcomePage, PageOne):
            # new frame object for each page
            frame = F(container, self)
            self.frames[F] = frame
            # same as main frame - completely layered without distinction
            frame.grid(row = 0, column = 0, sticky = 'nesw')
            

        self.up_frame(WelcomePage)
        
    # define first page to pop up
    def up_frame(self, page_name):
        page = self.frames[page_name]
        page.tkraise()

        
class WelcomePage(tk.Frame):

    """Frame object corresponding to the first/welcome page of the GUI"""

    def __init__(self, parent, controller):

        """See help(WelcomePage) for more details"""

        tk.Frame.__init__(self, parent)
        self.controller = controller

        # set image as background of frame     
        self.background_image = ImageTk.PhotoImage(file=image_path)
        self.background_label = tk.Label(self, image = self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.background_label.image = self.background_image

        # add label
        label = tk.Label(self, text = 'Welcome to Rock, Paper, Scissors, Lizard, Spock', font = controller.titlefont)
        label.pack(pady = 100)
        # add Get Started button
        button = tk.Button(self, text = 'Get Started', command = lambda: controller.up_frame(PageOne))
        button.pack(pady = 75)


class PageOne(tk.Frame):
    
    """Frame object corresponding to page one of the GUI"""

    def __init__(self, parent, controller):

        """See help(PageOne) for more details"""

        tk.Frame.__init__(self, parent, bg = "#27408B")
        self.controller = controller

        #header label
        header = tk.Label(self, text = "Please pick a variable.", 
        bg="#27408B", fg="#FFF5EE", height = '5', width='54',font=("Helvetica 18 italic bold"))
        header.grid(row=0, column=0)

        # adds the drop down menus
        drop_down_menus = self.initialise_menus()
        drop_down_menus.grid(row=1, column=0, pady=20)

        # Start button will start the scraper & once run will navigate to final page
        start_button = tk.Button(self, text = "Start", command = lambda: self.run_app(), fg = "#548B54",
        relief = "raised", width = 12, height = 3, font = ("Helvetica 12 bold"))
        start_button.grid(column = 0, row = 4, sticky = 'e',padx = 65, pady = 2)
        # Back button to return to welcome page
        back_button = tk.Button(self, text = "Back", command = lambda: controller.up_frame(WelcomePage), fg = "#CD5B45",
        relief = "raised", width = 12, height = 3, font = ("Helvetica 12 bold"))
        back_button.grid(column = 0, row = 4, sticky = 'w', padx = 65, pady = 2)


    def user_input(self):

        """This methods allows to easily monitor changes of tinker variables"""

        self.category_menu = tk.StringVar()
        self.category_menu.set("Select Your Variable")


    def initialise_menus(self):

        """This methods initialises the options of the drop-down menus"""
        
        self.user_input()
        drop_category = tk.OptionMenu(self, self.category_menu, "Rock", "Paper", "Scissors", "Lizard", "Spock")
        drop_category.config(width = 15)
        drop_category.config(height = 2)
        drop_category.config(bg = "#27408B")

        return drop_category


    def get_winner(self):

        """ This function takes the user input from the user interface and
        feeds it to the Run_Scraper class for initilisation of an instance"""

        
        self.user_category = str(self.category_menu.get())
        game = RPS_game()
        game.get_winner(self.user_category)
        self.computer_choice = game.computer_choice
        self.winner = game.winner
        print(self.user_category)
        print(self.computer_choice)

    
    def run_app(self):

        self.get_winner()

        if (self.computer_choice == 'Scissors' and self.user_category =='Rock') or \
            (self.computer_choice == 'Rock' and self.user_category =='Scissors'):
                messagebox.showinfo("Game outcome", f"and as it always has \n Rock crushes Scissors \n The winner is {self.winner}")

        elif (self.computer_choice == 'Scissors' and self.user_category =='Paper') or \
             (self.computer_choice == 'Paper' and self.user_category =='Scissors'):
                messagebox.showinfo("Game outcome", f"Scissors cuts Paper \n The winner is {self.winner}")
        
        elif (self.computer_choice == 'Rock' and self.user_category =='Paper') or \
             (self.computer_choice == 'Paper' and self.user_category =='Rock'):
                messagebox.showinfo("Game outcome", f"Paper covers Rock \n The winner is {self.winner}")
        
        elif (self.computer_choice == 'Rock' and self.user_category =='Lizard') or \
             (self.computer_choice == 'Lizard' and self.user_category =='Rock'):
                messagebox.showinfo("Game outcome", f"Rock crushes Lizard \n The winner is {self.winner}")

        elif (self.computer_choice == 'Lizard' and self.user_category =='Spock') or \
             (self.computer_choice == 'Spock' and self.user_category =='Lizard'):
                messagebox.showinfo("Game outcome", f"Lizard poisons Spock \n The winner is {self.winner}")

        elif (self.computer_choice == 'Spock' and self.user_category =='Scissors') or \
             (self.computer_choice == 'Scissors' and self.user_category =='Spock'):
                messagebox.showinfo("Game outcome", f"Spock smashes Scissors \n The winner is {self.winner}")
        
        elif (self.computer_choice == 'Scissors' and self.user_category =='Lizard') or \
             (self.computer_choice == 'Lizard' and self.user_category =='Scissors'):
                messagebox.showinfo("Game outcome", f"Scissors decapitates Lizard \n The winner is {self.winner}")
        
        elif (self.computer_choice == 'Lizard' and self.user_category =='Paper') or \
             (self.computer_choice == 'Paper' and self.user_category =='Lizard'):
                messagebox.showinfo("Game outcome", f"Lizard eats Paper \n The winner is {self.winner}")
        
        elif (self.computer_choice == 'Spock' and self.user_category =='Paper') or \
             (self.computer_choice == 'Paper' and self.user_category =='Spock'):
                messagebox.showinfo("Game outcome", f"Paper disproves Spock \n The winner is {self.winner}")
        
        elif (self.computer_choice == 'Rock' and self.user_category =='Spock') or \
             (self.computer_choice == 'Spock' and self.user_category =='Rock'):
                messagebox.showinfo("Game outcome", f"Spock vaporazies Rock \n The winner is {self.winner}")
        
        else:
            messagebox.showinfo("Game outcome", "It's a tie!")
           

if __name__ == '__main__':
    app = MainFrame()  
    app.mainloop()