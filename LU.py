import tkinter as tk
import pandas as pd

class App(tk.Frame):
    def __init__(calc, master):
        super().__init__(master)
        calc.pack()

        # program initialization
        calc.master.geometry('500x400')
        calc.master.title('LU Decomposition By MFT')
        calc.master.iconbitmap(r'calculator.ico')

        # Main Lables
        calc.t0 = tk.Label(calc,bg='#FF4', text='    Matrix Formula:    ', borderwidth=5 ,padx=20 ,pady=10).grid(row=0,column=0)
        calc.t1 = tk.Label(calc,bg='#FF4', text='[ a11     a12     a13 ]', borderwidth=5 ,padx=20 ,pady=10).grid(row=1,column=0)
        calc.t2 = tk.Label(calc,bg='#FF4', text='[ a21     a22     a23 ]', borderwidth=5 ,padx=20 ,pady=10).grid(row=2,column=0)
        calc.t3 = tk.Label(calc,bg='#FF4', text='[ a31     a32     a33 ]', borderwidth=5 ,padx=20 ,pady=10).grid(row=3,column=0)
        calc.l1 = tk.Label(calc, text='      a11').grid(row=1,column=1)
        calc.l2 = tk.Label(calc, text='      a12').grid(row=1,column=3)
        calc.l3 = tk.Label(calc, text='      a13').grid(row=1,column=5)
        calc.l4 = tk.Label(calc, text='      a21').grid(row=2,column=1)
        calc.l5 = tk.Label(calc, text='      a22').grid(row=2,column=3)
        calc.l6 = tk.Label(calc, text='      a23').grid(row=2,column=5)
        calc.l7 = tk.Label(calc, text='      a31').grid(row=3,column=1)
        calc.l8 = tk.Label(calc, text='      a32').grid(row=3,column=3)
        calc.l9 = tk.Label(calc, text='      a33').grid(row=3,column=5)
        calc.l10 = tk.Label(calc, text='                                             \n                                            \n             U (Upper Matrix)               \n                                                   \n                                          ').grid(row=4,column=0)
        calc.l11 = tk.Label(calc, text='                                             \n                                            \n             L (Lower Matrix)               \n                                                   \n                                          ').grid(row=5,column=0)

        # Main Button
        calc.b0= tk.Button(calc, bg='#1F2', text='Calculate',padx=100 ,pady=20,command=calc.solve).grid(row=0,column=1,padx=7,pady=7,columnspan=6)

        # Main input Widgets
        calc.e1= tk.Entry(calc,borderwidth=1 , width= 5)
        calc.e1.grid(row=1,column=2,padx=10 ,pady=5)
        calc.n1=tk.DoubleVar()
        calc.n1.set(2)
        calc.e1["textvariable"] = calc.n1

        calc.e2= tk.Entry(calc,borderwidth=1 , width= 5)
        calc.e2.grid(row=1,column=4,padx=10 ,pady=5)
        calc.n2=tk.DoubleVar()
        calc.n2.set(0)
        calc.e2["textvariable"] = calc.n2

        calc.e3= tk.Entry(calc,borderwidth=1 , width= 5)
        calc.e3.grid(row=1,column=6,padx=10 ,pady=5)
        calc.n3=tk.DoubleVar()
        calc.n3.set(1)
        calc.e3["textvariable"] = calc.n3

        calc.e4= tk.Entry(calc,borderwidth=1 , width= 5)
        calc.e4.grid(row=2,column=2,padx=10 ,pady=5)
        calc.n4=tk.DoubleVar()
        calc.n4.set(2)
        calc.e4["textvariable"] = calc.n4

        calc.e5= tk.Entry(calc,borderwidth=1 , width= 5)
        calc.e5.grid(row=2,column=4,padx=10 ,pady=5)
        calc.n5=tk.DoubleVar()
        calc.n5.set(5)
        calc.e5["textvariable"] = calc.n5

        calc.e6= tk.Entry(calc,borderwidth=1 , width= 5)
        calc.e6.grid(row=2,column=6,padx=10 ,pady=5)
        calc.n6=tk.DoubleVar()
        calc.n6.set(-9)
        calc.e6["textvariable"] = calc.n6

        calc.e7= tk.Entry(calc,borderwidth=1 , width= 5)
        calc.e7.grid(row=3,column=2,padx=10 ,pady=5)
        calc.n7=tk.DoubleVar()
        calc.n7.set(-5)
        calc.e7["textvariable"] = calc.n7

        calc.e8= tk.Entry(calc,borderwidth=1 , width= 5)
        calc.e8.grid(row=3,column=4,padx=10 ,pady=5)
        calc.n8=tk.DoubleVar()
        calc.n8.set(7)
        calc.e8["textvariable"] = calc.n8

        calc.e9= tk.Entry(calc,borderwidth=1 , width= 5)
        calc.e9.grid(row=3,column=6,padx=10 ,pady=5)
        calc.n9=tk.DoubleVar()
        calc.n9.set(4)
        calc.e9["textvariable"] = calc.n9

        # Main Function
    def solve(calc):

        # bring the data in the input widgets into variables for furthur calcuations
        a11=float(calc.n1.get())
        a12=float(calc.n2.get())
        a13=float(calc.n3.get())
        a21=float(calc.n4.get())
        a22=float(calc.n5.get())
        a23=float(calc.n6.get())
        a31=float(calc.n7.get())
        a32=float(calc.n8.get())
        a33=float(calc.n9.get())

        ##########CALCULATIONS###########
        # Main Matrix
        a =[
        [a11,a12,a13],
        [a21,a22,a23],
        [a31,a32,a33]]

        # first column factors of elemination
        k21 =-1*a21/a11
        k31 =-1*a31/a11

        # Result Matrix after first column elemination
        m0=[
        [a11  ,  a12          ,  a13],
        [0.0  ,  k21*a12+a22  ,  k21*a13+a23],
        [0.0  ,  k31*a12+a32  ,  k31*a13+a33]]

        # second column factor of elemination
        k32=-1*m0[2][1]/m0[1][1]

        # Upper Matrix
        U=[
        {'0':a11  ,  '1':a12          ,  '2':a13},
        {'0':"0"  ,  '1':k21*a12+a22  ,  '2':k21*a13+a23},
        {'0':"0"  ,  '1':"0"          ,  '2':k32*m0[1][2]+m0[2][2]}]

        # Upper Matrix to DataFrame
        U_df = pd.DataFrame(U,columns = ['0','1','2'], index = ['','','']).rename(columns = {'0':'','1':'','2':'' })

        # Lower Matrix
        L=[
        {'0': "1"  ,  '1': "0"  ,  '2': "0"},
        {'0': k21  ,  '1': "1"  ,  '2': "0"},
        {'0': k31  ,  '1': k32  ,  '2': "1"}]

        # Lower Matrix to DataFrame
        L_df = pd.DataFrame(L,columns = ['0','1','2'], index = ['','','']).rename(columns = {'0':'','1':'','2':'' })

        # display L & U Matrix
        calc.d1 = tk.Label(calc,text=('                                             \n                                                   \n                                                   \n                                          ')).grid(row=4,column=1,padx=7,pady=7,columnspan=6)
        calc.d1 = tk.Label(calc,text=(U_df)).grid(row=4,column=1,padx=7,pady=7,columnspan=6)

        calc.d2 = tk.Label(calc,text=('                                             \n                                                   \n                                                   \n                                          ')).grid(row=5,column=1,padx=7,pady=7,columnspan=6)
        calc.d2 = tk.Label(calc,text=(L_df)).grid(row=5,column=1,padx=7,pady=7,columnspan=6)

root = tk.Tk()
myapp = App(root)
myapp.mainloop()
