import numpy as np
import tkinter as tk
def checker(x,y,n):
    global grid
    for i in range(0,9):
        if grid[x,i]==n:
            return False
    for i in range(0,9):
        if grid[i,y]==n:
            return False
    x0=(x//3)*3
    y0=(y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if grid[x0+i,y0+j]==n:
                return False
    return True
def solve():
    global grid
    for x in range(9):
        for y in range(9):
            if grid [x,y]==0:
                for n in range(1,10):
                    if checker(x,y,n)==True:
                        grid[x,y]=n
                        solve()
                        grid[x,y]=0
                return
    for i in range(9):
        for j in range(9):
            message = tk.StringVar()
            message.set(str(grid[i,j]))
            EntryList[i][j]=tk.Entry(root, width=3,state='disabled',textvariable=message,justify='center')
            EntryList[i][j].grid(column=j, row=i)
def test():
    for x in range(9):
        for y in range(9):
            n=EntryList[x][y].get()
            count=0
            for i in range(9):
                if EntryList[x][i].get()==n:
                    count+=1
            for i in range(9):
                if EntryList[i][y].get()==n:
                    count+=1
            x0=(x//3)*3
            y0=(y//3)*3
            for i in range(0,3):
                for j in range(0,3):
                    if EntryList[x0+i][y0+j].get()==n:
                        count+=1
            if count>3:
                lbl.configure(text='Неверно')
                return
    lbl.configure(text='Верно')
def start():
    global grid
    global btn2
    grid=[]
    for i in range(9):
        row=[]
        for j in range(9):
            if EntryList[i][j].get()!='':
                row.append(int(EntryList[i][j].get()))
                message = tk.StringVar()
                message.set(str(EntryList[i][j].get()))
                entry=tk.Entry(root, width=3,state='disabled',textvariable=message,justify='center')
                entry.grid(column=j, row=i)
            else:
                row.append(0)
        grid.append(row)
    grid=np.array(grid)
    btn2.destroy()
    btn2 = tk.Button(root, text="Ресет", command=reset)
    btn2.grid(column=11, row=11)
def reset():
    global btn2
    global EntryList
    del EntryList
    global grid
    del grid
    EntryList=[]
    for i in range(9):
        EntryRow=[]
        for j in range(9):
            entry=tk.Entry(root, width=3,justify='center')
            entry.grid(column=j, row=i)
            EntryRow.append(entry)
        EntryList.append(EntryRow)
    btn2.destroy()
    btn2 = tk.Button(root, text="Начать", command=start)
    btn2.grid(column=11, row=11)
root=tk.Tk()
root.title('Sudoku')
root.geometry('600x400')
EntryList=[]
for i in range(9):
    EntryRow=[]
    for j in range(9):
        entry=tk.Entry(root, width=3,justify='center')
        entry.grid(column=j, row=i)
        EntryRow.append(entry)
    EntryList.append(EntryRow)
btn1 = tk.Button(root, text="Тест", command=test)
btn1.grid(column=12, row=11)
btn2 = tk.Button(root, text="Начать", command=start)
btn2.grid(column=11, row=11)
lbl = tk.Label(root, text='', font=("Arial Bold", 10))  
lbl.grid(column=13, row=11)
btn3 = tk.Button(root, text="Решить", command=solve)
btn3.grid(column=12, row=12)
root.mainloop()


print(np.array([[5,3,0,0,7,0,0,0,0],
      [6,0,0,1,9,5,0,0,0],
      [0,9,8,0,0,0,0,6,0],
      [8,0,0,0,6,0,0,0,3],
      [4,0,0,8,0,3,0,0,1],
      [7,0,0,0,2,0,0,0,6],
      [0,6,0,0,0,0,2,8,0],
      [0,0,0,4,1,9,0,0,5],
      [0,0,0,0,8,0,0,7,9]]))






