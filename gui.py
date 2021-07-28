from tkinter import *
import tkinter.messagebox as tkMessageBox
import trainer as tr
import main

root = Tk()
root.title("Malicious Url Detector")
img = PhotoImage(width=300, height=300)
data = ("{red red red red blue blue blue blue}")
root.attributes('-alpha', 0.9)
root.iconbitmap(r'malware.ico')

frame = Frame(root)
frame.pack()
bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

L1 = Label(frame, text="Enter the URL you want to check: ")
L1.pack(side=LEFT)
E1 = Entry(frame, bd=5, width=150)
E1.pack(side=RIGHT)


def submitCallBack():
    url = E1.get()
    main.process_test_url(url, 'test_features.csv')
    return_ans = tr.gui_caller('url_features.csv', 'test_features.csv')
    a = str(return_ans).split()
    print("-----")
    print("return_ans: ", return_ans)
    print("-----")
    if int(a[1]) == 0:
        tkMessageBox.showinfo("URL Checker Result", "The URL " + url + " is Safe to Visit")

    elif int(a[1]) == 1:
        tkMessageBox.showinfo("URL Checker Result", "The URL " + url + " is Malicious")

    else:
        tkMessageBox.showinfo("URL Checker Result", "The URL " + url + " is Malware")


B1 = Button(bottomframe, text="Check", command=submitCallBack)
B1.pack(side=RIGHT, padx=5, pady=5)
root.mainloop()
