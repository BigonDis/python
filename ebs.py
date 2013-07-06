import csv, sqlite3, os, zipfile
from Tkinter import *
import TkTreectrl as treectrl

def silentremove(filename):
    try:
        os.remove(filename)
    except:
        pass
zfile = zipfile.ZipFile('GENFEMBK.ZIP')
zfile.extractall()
silentremove('accounts.db')

f = open('GENFEMBKMN.csv','rb')
reader = csv.reader(f)

## Coverts the CSV file into a sqlite3 database that cn be used to do searches
con = sqlite3.connect('accounts.db') #creates a file that we will use as the DataBase
con.text_factory = str
cur = con.cursor()
cur.execute('CREATE TABLE ebsshort(account_type TEXT, short_name TEXT, account_number TEXT, balance REAL, officer TEXT, last_deposit_date TEXT, last_deposit REAL)')
for row in reader:
    to_db = [row[0], row[2], row[1], row[8], row[9], row[29], row[30]]
    cur.execute('INSERT OR IGNORE INTO ebsshort (account_type, short_name, account_number, balance, officer, last_deposit_date, last_deposit) VALUES (?,?,?,?,?,?,?)', to_db)
con.commit()
con.close()

class Program:
    def __init__(self, master):
        frame = Frame(master, bg = '#5577ff')
        frame.pack(fill=X)

        entry_content1 = StringVar()
        entry_content2 = StringVar()
        entry_content3 = StringVar()

        self.textAccountType = Label(frame, bg = '#5577ff', text="Account Type")
        self.textAccountType.grid(row=0, column=0, sticky=W, padx=5)

        self.textName = Label(frame, bg = '#5577ff', text="Name")
        self.textName.grid(row=0, column=1, sticky=W, padx=5)

        self.textAccount = Label(frame, bg = '#5577ff', text="Account Number")
        self.textAccount.grid(row=0, column=2, sticky=W, padx=5)

        self.TextFieldAccountType = Entry(frame, textvariable = entry_content1, width=5)
        self.TextFieldAccountType.grid(row=1, rowspan=1, column=0, sticky=W, padx=5)

        self.TextFieldName = Entry(frame, textvariable = entry_content2, width=20)
        self.TextFieldName.grid(row=1, rowspan=1, column=1, sticky=W, padx=5)

        self.TextFieldAccountNum = Entry(frame, textvariable = entry_content3, width=30)
        self.TextFieldAccountNum.grid(row=1, rowspan=1, column=2, columnspan=4, sticky=W, padx=5)

        self.btn = Button(frame, text="Search", command=self.search)
        self.btn.grid(row=1, rowspan=1, column=6, padx=5)

        # create an empty Tkinter listbox
        self.content = treectrl.MultiListbox(master, bg='#cccccc')
        self.content.configure(columns=('Account Type','Name','Account Number','Avail. Balance','Officer','Last Deposit Date','Last Depoist'))
        self.content.pack(fill = BOTH, expand =1)


    def search(self):
        
        self.content.delete(ALL)
        # if texfield is empty
        if self.TextFieldAccountNum.get() == "" and self.TextFieldAccountType.get() == "" and self.TextFieldName.get() == "":
            # then set text label text
            self.text["text"] = "Please enter a search Critera"
        else:
    
            accountnum = self.TextFieldAccountNum.get()
            name = self.TextFieldName.get()
            name = name.upper()
            accounttype = self.TextFieldAccountType.get()
            accounttype = accounttype.upper()
            conn = sqlite3.connect('accounts.db')
            c = conn.cursor()

            # select all entries from database
            accountnum = '%' + accountnum
            name = '%' + name + '%'
            accounttype = '%' + accounttype + '%'
            list = c.execute("SELECT * FROM ebsshort WHERE short_name LIKE ? AND account_number LIKE ? AND account_type LIKE ?", (name,accountnum,accounttype,))
            conn.commit()

            # list has an array so lets loop the array and insert each item to
            # our listbox

            for row in list:
                    self.content.insert('end',*map(unicode,row))                    
            c.close()



root = Tk()
root.geometry('800x600')
application = Program(root)
root.mainloop()