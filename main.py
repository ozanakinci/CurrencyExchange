from tkinter import *
import requests
from tkinter import messagebox
def clearAll() :
    fromField.delete(0, END)
    toField.delete(0, END)
    amountField.delete(0, END)
    finField.delete(0, END)
def checkError() :
    if (fromField.get() == "" or toField.get() == "" or amountField.get() == "") :
        messagebox.showerror("Input Error")
        clearAll()
        return
def prior():
    from_currency = (fromField.get())
    to_currency = (toField.get())
    amount = int(amountField.get())
    currency_conversion(from_currency,to_currency,amount)
def currency_conversion():
    from_currency = (fromField.get())
    to_currency = (toField.get())
    amount = int(amountField.get())
    response=requests.get(url)
    rate=response.json()['rates'][from_currency]
    amount_in_EUR=amount/rate
    amount=amount_in_EUR*(response.json()['rates'][to_currency])
    finField.insert(10, str(amount))
if __name__ == "__main__" :
    url = str.__add__('http://data.fixer.io/api/latest?access_key=', '7cdf410b0b856588f3c1f803302d1834')
    window = Tk()
    window.configure(background = "light green")
    window.title("Currency Convertor")
    window.geometry("525x300")
    dob = Label(window, text = "Enter Details", bg = "orange")
    from_label = Label(window, text = "from", bg = "turquoise")
    to_label = Label(window, text = "To", bg = "turquoise")
    amount_label = Label(window, text = "Amount", bg = "turquoise")
    convAmt = Label(window, text = "Converted Amount", bg = "turquoise")
    convert = Button(window, text = "Convert", fg = "white", bg = "black", command =currency_conversion)
    clearAllEntry = Button(window, text = "Clear All", fg = "white", bg = "black", command = clearAll)
    fromField= Entry(window)
    toField= Entry(window)
    amountField= Entry(window)
    finField=Entry(window)
    dob.grid(row = 0, column = 1)
    from_label.grid(row = 1, column = 0)
    fromField.grid(row = 1, column = 1)
    to_label.grid(row = 2, column = 0)
    toField.grid(row = 2, column = 1)
    amount_label.grid(row = 3, column = 0)
    amountField.grid(row = 3, column = 1)
    convert.grid(row = 4, column = 2)
    convAmt.grid(row = 9, column = 2)
    finField.grid(row = 10, column = 2)
    clearAllEntry.grid(row = 12, column = 2)
    window.mainloop()