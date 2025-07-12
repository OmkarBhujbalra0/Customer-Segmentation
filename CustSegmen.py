import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
import tkinter as tk
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

    plot_button.config(state=tk.NORMAL,command=lambda: elbow(data))



def elbow(data):
    x = data.iloc[:,[3,4]].values

    wcss = []
    for i in range(1,11):
        kmeans = KMeans(n_clusters=i,init='k-means++',random_state=42)
        kmeans.fit(x)

        wcss.append(kmeans.inertia_)

    fig =plt.figure(figsize=(8,6))
    a = fig.add_subplot(111)
    a.plot(range(1,11),wcss)
    a.set_xlabel('Number of Clusters')
    a.set_ylabel('WCSS')
    a.set_title("The Elbow Graph")

    nxtwndw = tk.Toplevel(root)
    nxtwndw.title("Elbow Graph ")
    nxtwndw.geometry("800x600")

    canvas = FigureCanvasTkAgg(fig,master=nxtwndw)
    canvas.draw()
    canvas.get_tk_widget().pack()

    buttonin.config(state=tk.NORMAL,command=lambda: input(data))
    entry.config(state=tk.NORMAL)

def input(data):
    x = data.iloc[:, [3, 4]].values
    b = int(entry.get())
    kmeans = KMeans(n_clusters=b,init='k-means++',random_state=0)
    y = kmeans.fit_predict(x)
    print(y)

    buttonscatter.config(state=tk.NORMAL, command=lambda: plotscatter(data))



def plotscatter(data):
    x = data.iloc[:, [3, 4]].values
    b = int(entry.get())
    print(b)
    kmeans = KMeans(n_clusters=b, init='k-means++', random_state=0)
    y = kmeans.fit_predict(x)

    clustered_data = pd.DataFrame(data={'Cluster': y})
    result = pd.concat([data, clustered_data], axis=1)

    output_file = "Customers.csv"
    result.to_csv(output_file, index=False)
    print(f"Result saved to {output_file}")

    cluster_text.delete(1.0, tk.END)

    for cluster in range(b):
        cluster_data = data[y == cluster]
        print(f'\nCustomers in Cluster {cluster + 1}:\n')
        print(cluster_data)
        cluster_text.insert(tk.END, f'\nCustomers in Cluster {cluster + 1}:\n')
        cluster_text.insert(tk.END, cluster_data.to_string())
    plt.figure(figsize=(8,8))
    plt.scatter(x[y == 0,0], x[y == 0, 1], s=50, c='green', label='Cluster 1')
    plt.scatter(x[y == 1,0], x[y == 1, 1], s=50, c='red', label='Cluster 2')
    plt.scatter(x[y == 2, 0], x[y == 2, 1], s=50, c='yellow', label='Cluster 3')
    plt.scatter(x[y == 3, 0], x[y == 3, 1], s=50, c='violet', label='Cluster 4')
    plt.scatter(x[y == 4, 0], x[y == 4, 1], s=50, c='blue', label='Cluster 5')
    plt.scatter(x[y == 5, 0], x[y == 5, 1], s=50, c='purple', label='Cluster 6')
    plt.scatter(x[y == 6, 0], x[y == 6, 1], s=50, c='black', label='Cluster 7')
    plt.scatter(x[y == 7, 0], x[y == 7, 1], s=50, c='orange', label='Cluster 8')
    plt.scatter(x[y == 8, 0], x[y == 8, 1], s=50, c='brown', label='Cluster 9')
    plt.scatter(x[y == 9, 0], x[y == 9, 1], s=50, c='pink', label='Cluster 10')

    plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=100,c='cyan',label='Centroids')

    plt.xlabel('Annual Income')
    plt.ylabel('Spending Score')
    plt.title('KMeans Clustering')
    plt.legend()

    sctrwndw = tk.Toplevel(root)
    sctrwndw.title("ScatterPlot ")
    sctrwndw.geometry("800x600")

    canvas1 = FigureCanvasTkAgg(plt.gcf(), master=sctrwndw)
    canvas1.draw()
    canvas1.get_tk_widget().pack()


root = tk.Tk()
root.title("KMEANS")

label = tk.Label(root,text="CUSTOMER SEGMENTATION",font=('Segoe UI Semibold',30))
label.pack(padx=20,pady=10)

opnbutton = tk.Button(root,text="Select File",command=selecfile,width=8)
opnbutton.pack(padx=20,pady=10)

display_text = tk.Text(root,height=6,width=80)
display_text.pack(padx=20,pady=10)

plot_button = tk.Button(root, text="Display Elbow Graph", state=tk.DISABLED)
plot_button.pack()

label2 = tk.Label(root,text='Enter Valid No. of Clusters:')
label2.pack()

entry = tk.Entry(root,state=tk.DISABLED)
entry.pack()

buttonin = tk.Button(root,text="Submit",state=tk.DISABLED)
buttonin.pack()

buttonscatter = tk.Button(root, text="Plot Clusters",state=tk.DISABLED)
buttonscatter.pack()

cluster_text = tk.Text(root, height=20, width=100)
cluster_text.pack(padx=20, pady=10)

root.mainloop()

