from tkinter import *
from PIL import ImageTk, Image
import subprocess
import PyPDF2
import numpy as np
import nltk
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import datetime
def openroot():
    root.deiconify()
    new_window.withdraw()
    new_window2.withdraw()

def openwindow():
    new_window.deiconify()
    root.withdraw()

def openwindow2():
    new_window2.deiconify()
    root.withdraw()

def previous():
    new_window.withdraw()
    new_window2.withdraw()
    root.deiconify()

def journal(key):
    if key==1:
        file_path = "OECDPolicy.pdf"
        subprocess.Popen([file_path], shell=True)
    elif key==2:
        file_path = "Vaccine Trial.pdf"
        subprocess.Popen([file_path], shell=True)
    elif key==3:
        file_path = "Brand Equity and covid 19 stock market crash.pdf"
        subprocess.Popen([file_path], shell=True)
    elif key==4:
        file_path = "Covid  impact on emerging stock markets[[dynamic analysis].pdf"
        subprocess.Popen([file_path], shell=True)
    elif key==5:
        file_path ="Impact of covid on E-commerce.pdf"
        subprocess.Popen([file_path], shell=True)
    elif key==6:
        file_path = "Impact on digital company stock return.pdf"
        subprocess.Popen([file_path], shell=True)
    elif key==7:
        file_path = "Impact on Covid on emerging Stocks.pdf"
        subprocess.Popen([file_path], shell=True)
    elif key==8:
        file_path = "Pre and Post Covid impact on stocks.pdf"
        subprocess.Popen([file_path], shell=True)
    elif key == 9:
        file_path = "Apparel Market.pdf"
        subprocess.Popen([file_path], shell=True)
    elif key == 10:
        file_path = "Fashion Industry stocks.pdf"
        subprocess.Popen([file_path], shell=True)


def company(file):
    data = pd.read_csv(file)
    x1 = np.array(data['Date'].iloc[17:21]).reshape(-1, 1)
    if file=="amazon.csv":
        data['Date'] = pd.to_datetime(data['Date'], format='%d-%m-%Y')
    else:
        data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m-%d')

    data['Date'] = (data['Date'] - pd.Timestamp("1970-01-01")) // pd.Timedelta('1s')
    x_test = np.array(data['Date'].iloc[17:21]).reshape(-1, 1)
    x = np.array(data['Date'].iloc[:21]).reshape(-1, 1)
    y = np.array(data['Stock Value (INR)'].iloc[:21]).reshape(-1, 1)
    LR = LinearRegression()
    LR.fit(x, y)
    yp_test = LR.predict(x_test)
    b = yp_test[0]
    plt.scatter(x_test, yp_test, color="blue", marker="o")
    plt.plot(x_test, yp_test, color="blue", label="Regression")
    plt.scatter(x, y, color="green", marker="x")
    plt.plot(x, y, color="green", label="Actual")
    plt.xlabel('Time Stamp')
    plt.ylabel('Stock Value (INR)')
    if file=="puma.csv":

        a = [1588374412.2580645, 5293.78242857143]
        b = [1590926121.2903225, 5861.889214285715]
    elif file=="sun.csv":
        a = [1589212567.7419355, 441.0497640509014]
        b = [1590953690.3225806, 449.8975901378579]
    elif file=="amazon.csv":
        a = [1588263468.3870966, 170866.72933333332]
        b = [1590748611.096774, 175493.14]

    list1_score = get_list_score(list1)
    list2_score = get_list_score(list2)
    list3_score = get_list_score(list3)
    print("E-COMMERCE avg Score:", list1_score / 5)
    e_commerce = list1_score / 5
    print("PHARMA  avg Score:", list2_score / 2)
    pharma = get_list_score(list2)
    print("FASHION avg Brand", list3_score / 5)
    fashion = get_list_score(list2)

    y_s=[]
    for i in range(3):
        n=yp_test[i]
        y_s.append(n)
        

    y_s = np.array(y_s)
    y_d1 = y_s * (1 + e_commerce)

    y_d2= y_s * (1 + pharma)
    y_d3 = y_s * (1 + fashion)
    if file == "puma.csv":
        plt.scatter(x_test, y_d1, color="red", marker="o")
        plt.plot(x_test, y_d1, color="red",label="Doc2Vec")

        c=[1588152524.516129, 5303.749214285715]
        d=[1590926121.2903225, 6021.357785714286]
        plt.scatter(c[0], c[1], color="green", marker="o")
        plt.scatter(d[0], d[1], color="red", marker="o")
        plt.plot([c[0], d[0]], [c[1], d[1]], color="red")
    elif file=="amazon.csv":
        plt.scatter(x_test, y_d2, color="red", marker="o")
        plt.plot(x_test, y_d2, color="red",label="Doc2Vec")
        e=[1588152524.516129, 170216.14033333334]
        f=[1591037065.1612902, 179613.537]
        plt.scatter(e[0], e[1], color="green", marker="o")
        plt.scatter(f[0], f[1], color="red", marker="o")
        plt.plot([e[0], f[0]], [e[1], f[1]], color="red")
    elif file=="sun.csv":
        plt.scatter(x_test, y_d3, color="red", marker="o")
        plt.plot(x_test, y_d3, color="red",label="Doc2Vec")
        g=[1588249393.548387, 420.59770833333334]
        h=[1591027780.6451612, 462.145625]
        plt.scatter(g[0], g[1], color="green", marker="o")
        plt.scatter(h[0], h[1], color="red", marker="o")
        plt.plot([g[0], h[0]], [g[1], h[1]], color="red")



    
    plt.scatter(a[0], a[1], color="green", marker="o")
    plt.scatter(b[0], b[1], color="blue", marker="o")
    plt.plot([a[0], b[0]], [a[1], b[1]], color="blue")
    plt.legend()
    plt.legend(loc='upper right')
    plt.show()



def get_score(file):
    pdf_file = open(file, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    keyword_list = []
    num_pages = len(pdf_reader.pages)

    for page in range(num_pages):
        page_obj = pdf_reader.pages[page]
        text = page_obj.extract_text()
        words = text.split()
        keywords = ['cases', 'effect', 'effects', 'corelated', 'related', 'dynamism', 'scope', 'costs', 'financial',
                    'in', 'stock', 'risk', 'cash', 'impact', 'impact', 'emotions', 'effect', 'effects', 'relationship',
                    'emotions', 'correlation', 'in demand', 'effects', 'impacts', 'aspects', 'response']

        for i, word in enumerate(words):
            if word in keywords and i > 0:
                keyword_list.append((words[i - 1], word))


    new_word_list = [word.lower() for (word, pos) in nltk.pos_tag([word for (word, pos) in keyword_list]) if
                     pos.startswith('V') or pos.startswith('J') or pos.startswith('RB') or pos.startswith(
                         'VBD') or pos.startswith('VB')]


    positive_words = ['positive', 'disruptive', 'Positive', 'beneficial', 'higher', 'stable', 'increase', 'Increase',
                      'enhanced', 'increasing', 'enhancing', 'positively']
    negative_words = ['decrease', 'negative', 'Negative', 'detrimental', 'idiosyncratic', 'decreasing', 'confirmed',
                      'lower']


    score = 0
    count=0
    for word in new_word_list:
        count=count+1
        if word in positive_words:
            score += 1
        elif word in negative_words:
            score -= 1
    pdf_file.close()
    return score,count


list1 = ['Covid  impact on emerging stock markets[[dynamic analysis].pdf','Impact of covid on E-commerce.pdf','Impact on digital company stock return.pdf','OECDPolicy.pdf','Pre and Post Covid impact on stocks.pdf']
list2 = ['OECDPolicy.pdf', 'Vaccine Trial.pdf']
list3 = ['Apparel Market.pdf','Brand Equity and covid 19 stock market crash.pdf','Fashion Industry stocks.pdf','Covid  impact on emerging stock markets[[dynamic analysis].pdf','Pre and Post Covid impact on stocks.pdf']


def get_list_score(file_list):
    total_score = 0
    for file in file_list:
        score,count = get_score(file)
        avg_score=score/count
        total_score += avg_score
    return total_score




root=Tk()


bg_image = PhotoImage(file="dsg3.png")
bg_label = Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

root.geometry("500x333")
root.title("STOCK PREDICTION")
root.resizable(False,False)

btn77=Button(root,text="JOURNALS",command=openwindow, font=("Arial", 25),relief='groove',activebackground="blue")
btn77.place(x=55,y=140)
btn3=Button(root,text="STOCKS",command=openwindow2, font=("Arial", 25),relief='groove',activebackground="blue")
btn3.place(x=300,y=140)


new_window=Toplevel()
new_window.geometry("500x500")
bg_image2 = PhotoImage(file="dsg10.png")
bg_label2= Label(new_window, image=bg_image2)
bg_label2.place(x=0, y=0, relwidth=1, relheight=1)
new_window.title("JOURNALS")
new_window.resizable(False,False)
new_window.attributes("-alpha",0.9)
new_window.geometry("800x560")

my_font = ("Trebuchet MS", 30, "bold")
btn2=Button(new_window,text="Previous",command=previous,relief='sunken')
btn2.pack(side=BOTTOM, padx=10, pady=10)
btn10 = Button(new_window, text="E-commerce ", command=lambda:journal(5), font=("Arial", 25),width=15,height=1)
btn10.place(x=50, y=360)
btn11 = Button(new_window, text="Dynamic Analysis ", command=lambda:journal(4), font=("Arial", 25),width=15,height=1)
btn11.place(x=50, y=300)
btn12 = Button(new_window, text="Brand Equity ", command=lambda:journal(3), font=("Arial", 25),width=15,height=1)
btn12.place(x=50, y=240)
btn12 = Button(new_window, text="Vaccine Trial ", command=lambda:journal(2), font=("Arial", 25),width=15,height=1)
btn12.place(x=50, y=180)
btn13= Button(new_window, text="OECDP POLICY", font=("Arial", 25),command=lambda:journal(1),width=15,height=1)
btn13.place(x=50, y=120)
btn14 = Button(new_window, text="Fashion Industry", command=lambda:journal(10), font=("Arial", 25),width=15,height=1)
btn14.place(x=450, y=360)
btn15 = Button(new_window, text="Apparel Market", command=lambda:journal(9), font=("Arial", 25),width=15,height=1)
btn15.place(x=450, y=300)
btn16 = Button(new_window, text="Pre and Post Covid", command=lambda:journal(8), font=("Arial", 25),width=15,height=1)
btn16.place(x=450, y=240)
btn17 = Button(new_window, text="Emerging Stocks ", command=lambda:journal(7), font=("Arial", 25),width=15,height=1)
btn17.place(x=450, y=180)
btn18 = Button(new_window, text="Digital Company ", command=lambda:journal(6), font=("Arial", 25),width=15,height=1)
btn18.place(x=450, y=120)
#openroot()


new_window2=Toplevel()
new_window2.geometry("550x465")
bg_image3 = PhotoImage(file="dsg16 (2).png")
bg_label3= Label(new_window2, image=bg_image3)
bg_label3.place(x=0, y=0, relwidth=1, relheight=1)
new_window2.title("COMPANIES")
new_window2.resizable(False,False)

btn21=Button(new_window2,text="Previous",command=previous,relief='sunken')
btn21.pack(side=BOTTOM, padx=10, pady=10)
image_c1=PhotoImage(file="Puma2.png")
btn22 = Button(new_window2,image=image_c1, width=250,height=60,command=lambda: company("puma.csv"), font=("Arial", 25))
btn22.place(x=0, y=120)
image_c2 = PhotoImage(file="Amazon-India-Logo-PNG-HD2.png")
btn23 = Button(new_window2,image=image_c2,width=250,height=60, command=lambda:company("amazon.csv"), font=("Arial", 25))
btn23.place(x=250, y=240)
image_c3 = PhotoImage(file="sun3.png")
btn24 = Button(new_window2, image=image_c3,width=250,height=60, command=lambda: company("sun.csv"), font=("Arial", 25))
btn24.place(x=0, y=360)

# Call openroot() to initially show only the root window
openroot()

root.mainloop()

