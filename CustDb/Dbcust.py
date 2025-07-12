import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import DBSCAN
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import  FigureCanvasTkAgg
def selecfile():
    path = filedialog.askopenfilename()
    if path.endswith('.csv'):
        data = pd.read_csv(path)
    elif path.endswith('.xlsx') or path.endswith('.xls'):
        data = pd.read_excel(path)
    else:
        print('''This Application only supports CSV or Excel File.
        Please select appropriate file!''')
        return

    display_text.delete(1.0,tk.END)
    display_text.insert(tk.END,data.to_string())

    nrows, ncolumns = data.shape
    missvalues = data.isnull().sum()

    if missvalues.all() !=0:
        miss = tk.Label(root,text="There are Incomplete Values!")
        miss.pack()
    else:
        miss = tk.Label(root, text="OK!")
        miss.pack()

    rows_label = tk.Label(root, text=f"Number of Rows are {nrows} and Number of Columns are {ncolumns}")
    rows_label.pack()


input1 = entry1.get()
input2 = entry2.get()

if not input1 or not input2:
    messagebox.showwarning("Warning",'Please fill both inputs.')
else:
    dbscan = DBSCAN(eps=input1,min_samples=input2)
    labels = dbscan.fit_predict(data)

    plt.xlabel('Annual Income')
    plt.ylabel('Spending Score')
    plt.title('KMeans Clustering')
    plt.legend()




root = tk.Tk()
root.title("DBSCAN")

label = tk.Label(root,text="DBSCAN",font=('Segoe UI Semibold',30))
label.pack(padx=20,pady=10)

opnbutton = tk.Button(root,text="Select File",command=selecfile,width=8)
opnbutton.pack(padx=20,pady=10)

display_text = tk.Text(root,height=6,width=80)
display_text.pack(padx=20,pady=10)



root.mainloop()

