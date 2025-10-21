from tkinter import*
from databases import*
def add():
    line=id.get()+'-'+name.get()+'-'+year.get()
    save(line)
def show():
    sv=read()
    for i in sv:
        
root=Tk()
#Var
id=StringVar
name=StringVar
year=StringVar
root.title('Quản lý Sinh Viên')
root.minsize(height=400,width=500)

Label(root,text='ỨNG DỤNG QUẢN LÝ SINH VIÊN',fg='red',font=('cambria',16),width=25).grid(row=0)
Listbox(root,width=80,height=20).grid(row=1,columnspan=2)
Label(root,text='MSSV: ').grid(row=2,column=0)
Entry(root,width=30,textvariable=id).grid(row=2,column=1)
Label(root,text='Ten SV: ').grid(row=3,column=0)
Entry(root,width=30,textvariable=name).grid(row=3,column=1)
Label(root,text='Nam sinh: ').grid(row=4,column=0)
Entry(root,width=30,textvariable=year).grid(row=4,column=1)
button=Frame(root)
Button(button,text='Them',comand=add).pack(side=LEFT)
Button(button,text='Xem').pack(side=LEFT)
Button(button,text='Sap xep').pack(side=LEFT)
Button(button,text='Thoat',command=root.quit).pack(side=LEFT)
button.grid(row=5,column=1)


root.mainloop()

