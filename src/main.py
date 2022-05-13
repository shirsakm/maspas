from tkinter import *
from orjson import *
from tkextrafont import Font

class App(Tk):
  def __init__(self) -> None:
    # Initiating the Tk() class
    super().__init__()

    # Loading the assets
    self.load_assets()

    # Loading the data
    with open('data/master_pass.txt', 'rt') as f:
      self.master_pass = f.read()

    # Configuring the main window
    self.title('Maspas')
    self.iconphoto(False, self.icon)
    
    # Configuring the main frame layout
    self.top = self.winfo_toplevel()
    self.top.grid_rowconfigure(0, weight=1)
    self.top.grid_rowconfigure(1, weight=2)
    self.top.grid_rowconfigure(2, weight=1)
    self.top.grid_columnconfigure(0, weight=1)

    # Initiating the three main frames
    self.header = Frame(self)
    self.body = Frame(self)
    self.footer = Frame(self)

    # Placing the frames on the grid
    self.header.grid(row=0, column=0)
    self.body.grid(row=1, column=0)
    self.footer.grid(row=2, column=0)

    # Functions
    self.match = lambda data: self.master_pass == data

    # Initiating the widgets
    self.start()




  def start(self):
    # Making the widgets
    self.prompt = Label(self.header, text='Please enter the master password.', font=('Ubuntu', 15))
    self.master_input = Entry(self.body, show='*', font=('Fira Code Retina', 12))
    self.enter = Button(self.body, image=self.down_arr, command=self.unlock)
    self.err = Label(self.footer, text='Wrong password', fg='red', font=('Times New Roman', 10))

    # Placing the widgets
    self.prompt.grid()
    self.master_input.grid(row=0, column=0)
    self.enter.grid(row=0, column=1)


  def load_assets(self):
    self.icon = PhotoImage(file='assets/icons/icon.png')
    self.gear = PhotoImage(file='assets/icons/gear.png').subsample(20, 20)
    self.down_arr = PhotoImage(file='assets/icons/down_arr.png').subsample(40, 40)
    # self.fira_code = Font(file='fonts/Fira Code Retina.ttf', family='Fira Code')
    


  def unlock(self):
    data = self.master_input.get()
    valid = self.match(data)

    if valid:
      self.clear_win()
      self.open_app()
    else:
      self.err.grid()


  def open_app(self):
    # Making the widgets
    self.title = Label(self.header, text='ADD NEW RECORD', font=('Ubuntu', 30))
    self.records = Listbox(self.body, activestyle='dotbox', exportselection=0)
    self.body_scroll = Scrollbar(self.records)
    self.data_frame = Frame(self.header)
    self.name = Label(self.data_frame, text='Name:', font=('Fira Code Retina', 10))
    self.name_entry = Entry(self.data_frame, font=('Fira Code Retina', 10))
    self.email = Label(self.data_frame, text='Email:', font=('Fira Code Retina', 10))
    self.email_entry = Entry(self.data_frame, font=('Fira Code Retina', 10))
    self.pswd = Label(self.data_frame, text='Password:', font=('Fira Code Retina', 10))
    self.pswd_entry = Entry(self.data_frame, font=('Fira Code Retina', 10))

    # PLacing the widgets
    self.title.grid(row=0, column=0)
    self.records.grid(row=0, column=0)
    self.body_scroll.grid(row=0, column=0)
    self.data_frame.grid(row=1, column=0)
    self.name.grid(row=0, column=0)
    self.name_entry.grid(row=0, column=1)
    self.email.grid(row=1, column=0)
    self.email_entry.grid(row=1, column=1)
    self.pswd.grid(row=3, column=0)
    self.pswd_entry.grid(row=3, column=1)

  def clear_win(self):
    for frame in self.winfo_children():
      for widgets in frame.winfo_children():
        widgets.destroy()


def main():
  app = App()
  
  print('Starting the app....')
  app.mainloop()


if __name__ == '__main__':
  main()