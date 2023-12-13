from tkinter import *
from tkinter import Scrollbar
from bs4 import BeautifulSoup 
import requests   
import webbrowser  

# Headers contain protocol specific information that appear at the beginning of the raw message that is sent over TCP connection
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

flipkart=''

def flipkart(name = ""):
    #For Exception Handling
    try:
        global flipkart
        name1 = name.replace(" ","+")   #for replacing null character with + sign

        #
        flipkart=f'https://www.flipkart.com/search?q={name1}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off'
        res = requests.get(f'https://www.flipkart.com/search?q={name1}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off',headers=headers)

        soup = BeautifulSoup(res.text,'html.parser')
        flipkart_name = soup.select('._4rR01T')[0].getText().strip()  #Extraction of text from the Product Name class
        flipkart_name = flipkart_name.upper()
        if name.upper() in flipkart_name:
            flipkart_price = soup.select('._1_WHN1')[0].getText().strip()   #Extraction of text from the Product Price class 
            flipkart_name = soup.select('._4rR01T')[0].getText().strip()

            return f"{flipkart_name}\nPrice : {flipkart_price}\n"
        else:

            flipkart_price='           Product Not Found'
        return flipkart_price
    except:

        flipkart_price= '           Product Not Found'
    return flipkart_price

# Function for conversion of special characters to null Character 
def convert(a):
    b=a.replace(" ",'')
    c=b.replace("INR",'')
    d=c.replace(",",'')
    f=d.replace("₹",'')
    g=int(float(f))
    return g

# Function for collecting the urls
def urls():
    global flipkart
    return f"{flipkart}"


def open_url(event):
        global flipkart
        webbrowser.open_new(flipkart)


#Graphical User Interface Creation

# Function for creation of the search Button
def search():
    box1.insert(1.0,"LOADING...")

    search_button.place_forget()


    box1.delete(1.0,"end")
   
   

    t1=flipkart(product_name.get())
    box1.insert(1.0,t1)


    t2 = urls()
    box2.insert(1.0,t2)

# Creation of the GUI window

window = Tk()
window.wm_title("PRICE COMPARISON")
window.minsize(1500,700)

lable_one =  Label(window, text="Enter Product Name :", font=("courier", 10))
lable_one.place(relx=0.2, rely=0.1, anchor="center") 

product_name =  StringVar()
product_name_entry =  Entry(window, textvariable=product_name, width=50)
product_name_entry.place(relx=0.5, rely=0.1, anchor="center")

search_button =  Button(window, text="SEARCH", width=12, command= search)
search_button.place(relx=0.5, rely=0.2, anchor="center")


l1 =  Label(window, text="FLIPKART", font=("courier", 20))
l2 =  Label(window, text="All URLs.....", font=("courier", 30))

l1.place(relx=0.1, rely=0.3, anchor="center")
l2.place(relx=0.8, rely=0.3, anchor="center")


scrollbar = Scrollbar(window)
box1 =  Text(window, height=7, width=50, yscrollcommand=scrollbar.set)


box1.place(relx=0.2, rely=0.4, anchor="center")

box2 =  Text(window, height=15, width=50, yscrollcommand=scrollbar.set, fg="blue", cursor="hand2")
box2.place(relx=0.8, rely=0.8, anchor="center")
box2.bind("<Button-1>", open_url)


window.mainloop()

