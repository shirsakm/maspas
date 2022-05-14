from tkinter import *
from orjson import *
from pyparsing import col

class App(Tk):
  def __init__(self) -> None:
    # Initiating the Tk() class
    super().__init__()

    # Loading the assets
    self.load_assets()

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
    # Loading the images
    self.icon = PhotoImage(file='assets/icons/icon.png')
    self.gear = PhotoImage(file='assets/icons/gear.png').subsample(20, 20)
    self.down_arr = PhotoImage(file='assets/icons/down_arr.png').subsample(40, 40)

    # Loading the master password
    with open('data/master.txt', 'rt') as f:
      self.master_pass = f.read()

    # Loading the records
    with open('data/records.json', 'rt') as f:
      self.records = loads(f.read())


  def unlock(self):
    data = self.master_input.get()
    valid = self.match(data)

    if valid:
      self.clear_win()
      self.open_app()
    else:
      self.err.grid()


  def open_app(self):
    # The title which changes based on the current action
    # for example,
    # if adding a new record "New record"
    # if updating an existing record "Edit record"
    self.title = Label(self.header, text='New record', font=('Ubuntu', 15))

    # The already existing records are shown here
    self.y_scroll = Scrollbar(self.body, orient=VERTICAL)
    self.records_list = Listbox(self.body, font=('Fira Code Retina', 10), activestyle='dotbox', exportselection=0, yscrollcommand=self.y_scroll)
    self.y_scroll['command'] = self.records_list.yview

    # The frame where I will get the datd for the records
    self.data_frame = Frame(self.header)

    # The data entry point names
    self.name = Label(self.data_frame, text='Name:', font=('Fira Code Retina', 10))
    self.email = Label(self.data_frame, text='Email:', font=('Fira Code Retina', 10))
    self.pswd = Label(self.data_frame, text='Password:', font=('Fira Code Retina', 10))
    self.notes = Label(self.data_frame, text='Notes:', font=('Fira Code Retina', 10))

    # The data entry points
    self.name_entry = Entry(self.data_frame, font=('Fira Code Retina', 10))
    self.email_entry = Entry(self.data_frame, font=('Fira Code Retina', 10))
    self.pswd_entry = Entry(self.data_frame, font=('Fira Code Retina', 10))

    # Button to add the record or change it or whatever
    self.save = Button(self.header, text='Save', font=('Times New Roman', 10), command=self.add_record)

    # Placing the title at the top
    self.title.grid(row=0, column=0)

    # Placing the records in the body
    self.records_list.grid(row=0, column=0)
    self.y_scroll.grid(row=0, column=1)

    # Placing the data frame in the middle of the haeader
    self.data_frame.grid(row=1, column=0)

    # Placing the data entry points in the data frame
    self.name.grid(row=0, column=0)
    self.name_entry.grid(row=0, column=1)
    self.email.grid(row=1, column=0)
    self.email_entry.grid(row=1, column=1)
    self.pswd.grid(row=3, column=0)
    self.pswd_entry.grid(row=3, column=1)
    
    # Placing the save option below the data frame
    self.save.grid(row=3, column=0)

    # Adding to the records
    for name in self.records.keys():
      self.records_list.insert(END, name)


  def add_record(self):
    # Getting the name from the entry
    name_data = self.name_entry.get()

    # Adding the name to the list
    self.records_list.insert(END, name_data)


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