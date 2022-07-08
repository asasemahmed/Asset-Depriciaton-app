import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry('886x650')
root.resizable(width=False, height=False)
root.title("Asset Application")

x = 100

label1 = tk.Label(root, text="ASSET DEPRCIATION APPLICATION", bg="#38b000", font=(50), width=76, height=2)
label1.pack()
label1.place(y=15, x=18)

asset_label = tk.Label(root, text="Asset Name", font=(30))
asset_label.pack()
asset_label.place(x=x, y=120)

cost_label = tk.Label(root, text="Cost", font=(30))
cost_label.pack()
cost_label.place(x=x, y=170)

assetLife_label = tk.Label(root, text="Asset Life",font=(30))
assetLife_label.pack()
assetLife_label.place(x=x, y=220)

Depreciation_label = tk.Label(root, text="Depreciation Rate",font=(30))
Depreciation_label.pack()
Depreciation_label.place(x=x, y=270)

#----------------------------------------------------------------

asset = tk.StringVar()
cost = tk.StringVar()
assetLife = tk.StringVar()
assetLife.set("7")
depreciation = tk.StringVar()


asset_entry = tk.Entry(root, width=30, font=(15), textvariable=asset, bg="#a9def9")
asset_entry.pack()
asset_entry.place(x=300, y=120)

cost_entry = tk.Entry(root, width=30, font=(15), textvariable=cost, bg="#a9def9")
cost_entry.pack()
cost_entry.place(x=300, y=170)

assetLife_entry = tk.Entry(root, width=30, font=(15), textvariable=assetLife, bg="#a9def9")
assetLife_entry.pack()
assetLife_entry.place(x=300, y=220)

depreciation_entry = tk.Entry(root, width=30, font=(15), textvariable=depreciation, bg="#a9def9")
depreciation_entry.pack()
depreciation_entry.place(x=300, y=270)


text1 = "      Year 1       Year 2        Year 3        Year4       Year 5      Year 6      Year 7" 

years_label = tk.Label(root, text=text1, width=80, font=(1), borderwidth=1, relief="solid", height=2, bg="#a9def9")
years_label.pack()
years_label.place(x=0, y=380)

depreciation_label = tk.Label(root, text="Depreciation \t\t\t\t\t\t\t\t\t", 
width=80, font=(2), height=2, bg="#a9def9")
depreciation_label.pack()
depreciation_label.place(x=0, y=431)

assetValue_label = tk.Label(root, text="Asset Value \t \t\t\t\t\t\t\t\t",
 width=80, font=(2), height=2, bg="#a9def9")
assetValue_label.pack()
assetValue_label.place(x=0, y=483)

#---------------------------------------------------


dl = []
al = []

def calculate():

    if not asset.get():
        messagebox.showerror("Error", "please input the information")

    if  not depreciation.get():
        messagebox.showerror("index Error", "please input the information")
    else:
        try:
            int(depreciation.get())
        except:
            messagebox.showerror("Error", "something Eror \nplease sheck your input and try again")

    if not cost.get():
        messagebox.showerror("index Error", "please input the information")
    else:
        try:
            int(cost.get())
        except:
            messagebox.showerror("Error", "something Eror \nplease sheck your input and try again")

    
    salvage, costfun, life = int(depreciation.get()), int(cost.get()), 7
    rate = 1 - ((salvage / costfun) ** (1 / life))

    for year in range(1, life + 1):
        dv = costfun * rate
        costfun -= dv
        dl.append(round(dv, 2))
        al.append(costfun)

    dep_text = f"{dl[0]}      {dl[1]}     {dl[3]}      {dl[4]}      {dl[5]}      {dl[6]}       {dl[7]}"
    as_text = "{:.2f}     {:.2f}       {:.2f}        {:.2f}     {:.2f}      {:.2f}      {:.2f} ".format(al[0],
      al[1], al[2], al[3], al[4], al[5], al[6])
    label_wep = tk.Label(root, text=dep_text, font=(2), bg="#a9def9")
    label_wep.pack()
    label_wep.place(x=130, y=444)
    

    label_asset = tk.Label(root, text=as_text, font=(2), bg="#a9def9")
    label_asset.pack()
    label_asset.place(x=130, y=500)

    file = open("asset_app.txt", "a")
    file.write(f"ASSET NAME : {asset.get()}\n")
    file.write("year\t depreciation\t Assetvalue\n")
    for n in range(7):
        file.write(f"{n + 1} \t\t {str(dl[n]).zfill(6)} \t\t {al[n] :.2f}\n")
    file.write("-----------------------------------------------\n")

    dl.clear()
    al.clear()


def reset():
    asset.set("")
    cost.set("")
    assetLife.set(7)
    depreciation.set("")

    hiden_label = tk.Label(root, width=120, text="  ", bg="#a9def9", height=6)
    hiden_label.pack()
    hiden_label.place(x=118, y=437)



exit_button = tk.Button(root, text="Exit", command=root.quit, width=12, height=0, font=(20))
exit_button.pack()
exit_button.place(x=720, y=590)

reset_button = tk.Button(root, text="Reset", command=reset, width=12, height=0, font=(20))
reset_button.pack()
reset_button.place(x=400, y=590)

calculate_button = tk.Button(root, text="Calculate", command=calculate, width=12, height=0, font=(20))
calculate_button.pack()
calculate_button.place(x=20, y=590)


tk.mainloop()



