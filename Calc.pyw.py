from tkinter import *
from tkinter import ttk
from math import sin,cos,tan,log,exp,log10,pow,sqrt,pi,factorial,acos,asin,atan,e

class Calculator:

    def __init__(self, root):
        #Configure Root window
        root.title('CALCULATOR')
        root.geometry('700x410')
        root.configure(bg='white')
        root.resizable(width=False, height = False)

        #Use text box to display input and calculted values
        self.text_box = Text(root,width=100,height=2,font='Calibri 28')
        self.text_box.grid(row=1,column=0,columnspan=60)
        self.text_box.insert(END, 0.0)

        #set general config of 'Buttons' to be drawn
        style = ttk.Style()
        style.configure('TButton',width=8, font='Serif 14',background='white',
                        forground ='black', padding=11)

        
        #Draw Buttons in window
        #__Row 2
        self.button_sin = ttk.Button(root, text='Sin',
                    command = lambda:self.button_click('sin(')).grid(row=2,column=0)
        self.button7 = ttk.Button(root, text='7',
                    command = lambda:self.button_click('7')).grid(row=2,column=1)
        self.button8 = ttk.Button(root, text='8',
                    command = lambda:self.button_click('8')).grid(row=2,column=2)
        self.button9 = ttk.Button(root, text='9',
                    command = lambda:self.button_click('9')).grid(row=2,column=3)
        self.button_div = Button(root, text='/',width=5, fg='yellow',font='bold 15',bg='grey',
                    command = lambda:self.button_click('/')).grid(row=2,column=4)
        #__Row 3
        self.button_cos = ttk.Button(root, text='Cos',
                    command = lambda:self.button_click('cos(')).grid(row=3,column=0)
        self.button4 = ttk.Button(root, text='4',
                    command = lambda:self.button_click('4')).grid(row=3,column=1)
        self.button5 = ttk.Button(root, text='5',
                    command = lambda:self.button_click('5')).grid(row=3,column=2)
        self.button6 = ttk.Button(root, text='6',
                    command = lambda:self.button_click('6')).grid(row=3,column=3)
        self.button_mult = Button(root,text='*',width=5, fg='yellow',font='bold 15',bg='grey',
                    command = lambda:self.button_click('*')).grid(row=3,column=4)

        #__Row 4
        self.button_tan = ttk.Button(root, text='TAN',
                    command = lambda:self.button_click('tan(')).grid(row=4,column=0)
        self.button1 = ttk.Button(root, text='1',
                    command = lambda:self.button_click('1')).grid(row=4,column=1)
        self.button2 = ttk.Button(root, text='2',
                    command = lambda:self.button_click('2')).grid(row=4,column=2)
        self.button3 = ttk.Button(root, text='3',
                    command = lambda:self.button_click('3')).grid(row=4,column=3)
        self.button_add = Button(root, text='+',width=5, fg='yellow',font='bold 15',bg='grey',
                    command = lambda:self.button_click('+')).grid(row=4,column=4)

        #__Row 5
        self.button_Obrace = ttk.Button(root,text='(',
                    command = lambda:self.button_click('(')).grid(row=5,column=0)
        self.button_Cbrace = ttk.Button(root, text=')',
                    command = lambda:self.button_click(')')).grid(row=5,column=1)
        self.button0 = ttk.Button(root, text='0',
                    command = lambda:self.button_click('0')).grid(row=5,column=2)
        self.button_float = ttk.Button(root, text='.',
                    command = lambda:self.button_click('.')).grid(row=5,column=3)
        self.button_add = Button(root, text='-',width=5, fg='yellow',font='bold 15',bg='grey',
                    command = lambda:self.button_click('-')).grid(row=5,column=4)
        #__Row 6
        self.button_LN = ttk.Button(root, text='LN',
                    command = lambda:self.button_click('log(')).grid(row=6,column=0)
        
        self.button_LOG10 = ttk.Button(root, text='LOG',
                    command = lambda:self.button_click('log10(')).grid(row=6,column=1)
        
        self.button_pi = ttk.Button(root, text='π',
                    command = lambda:self.button_click('pi')).grid(row=6,column=2)
        
        self.button_euler = ttk.Button(root, text='e',
                    command = lambda:self.button_click('e')).grid(row=6,column=3)

        self.button_factorial = ttk.Button(root, text='DEL',
                    command = lambda:self.button_click('DEL')).grid(row=6,column=4)
       

        #__Row 7
        self.button_Result = Button(root, width=10, text='ENTER', fg='blue',font='bold 15',
                    command = lambda:self.button_click('ENTER')).grid(row=7,column=4)

        button_Reset = Button(root,width=10,text='C',fg='red', font='bold 15',
                    command = lambda:self.button_click('C')).grid(row=7,column=3)


        #__2nd Func() button
        button_2ndf = Button(root,width=8,text='2ndf',font='bold 15',fg='red',
                             command=lambda:self.button_click('2ndf')).grid(row=7,column=0)
        
        label_2ndf = Label(root,text='>>acos, asin, atan, e^x, x^y',font='15',fg='grey')
        label_2ndf.grid(row=7,columnspan=4)


    #Function to handle 2nd func    
    def Secnd_Clicked(self,T): #
        '''Displays 2ndf buttons'''
        if T == True:
            root.geometry('700x520')
            Label(root,text=' ').grid(row=8,columnspan=40) #just for extra space between upper and lower sections
            self.button_pow = ttk.Button(root, text='x^y',
                        command = lambda:self.button_click('pow(')).grid(row=9,column=0)
            
            self.button = ttk.Button(root, text='e^x',
                        command = lambda:self.button_click('exp(')).grid(row=9,column=1)
            
            self.button_sqrt= ttk.Button(root, text='√x',
                        command = lambda:self.button_click('sqrt(')).grid(row=9,column=2)
            
            self.button_factorial = ttk.Button(root, text='X!',
                    command = lambda:self.button_click('factorial(')).grid(row=9,column=3)
            
            self.button_asin = ttk.Button(root, text='aSin',
                        command = lambda:self.button_click('asin(')).grid(row=10,column=0)
            
            self.button_acos= ttk.Button(root, text='aCos',
                        command = lambda:self.button_click('acos(')).grid(row=10,column=1)
            
            self.button_atan= ttk.Button(root, text='aTan',
                        command = lambda:self.button_click('atan(')).grid(row=10,column=2)
            
            self.button_Comma = ttk.Button(root, text=',',
                    command = lambda:self.button_click(',')).grid(row=10,column=3)
            
        else: 
            root.geometry('700x410')#resize window to original
        


    #define Math function to evaluate expressions     
    def Math(self, expression):
        '''compute and return the given "expression"'''
        try:
            return float(eval(expression))
        except:
            return 'Error'
    
    #ButtonClick function
    prevButton = 'ENTER'#To keep track of when the 'ENTER' key is pressed;initialy set to ENTER.
    sec_value = False #Control variable for 2ndf button
    
    def button_click(self,value):
        '''this function executes anytime a button is clicked'''
        expression = self.text_box.get(1.0,END)#get expression in entry box
        
        if not(value in ['C','ENTER','2ndf','DEL']): #Deal with numeric and operation values access by user
        
            if value.isdigit() and self.prevButton!='ENTER':
    
                self.text_box.insert(END,value)
                    
            elif self.prevButton=='ENTER' and value in '+-*/':#if user is operations on previous results
                self.text_box.insert(END,value)
                self.prevButton = ''
                    
            elif expression!='' and self.prevButton!='ENTER': #if user is entering on empty box
                self.text_box.insert(END,value)
                    
            else:# if user starts new operation after previous
                self.text_box.delete(1.0,END)
                self.text_box.insert(END,value)
                self.prevButton = ''

                
        elif value == '2ndf':
                if self.sec_value== False: #Turn On functions for 2ndf button
                    self.Secnd_Clicked(True)
                    global sec_value 
                    self.sec_value = True
                elif self.sec_value == True:
                    global sec_value 
                    self.sec_value = False
                    self.Secnd_Clicked(False)
                    
        elif value == 'DEL':
            if self.prevButton == 'ENTER':
                self.text_box.delete(1.0,END)
            elif expression != 0.0:
                expression = str(self.text_box.get(1.0,END))[0:-2]
                self.text_box.delete(1.0,END)
                self.text_box.insert(END,expression)
                
        elif value=='C': # C, clears entry box
            self.text_box.delete(1.0,END)
            self.text_box.insert(END, 0.0)
            
        elif value=='ENTER':
                result = self.Math(expression)
                
                self.text_box.delete(1.0,END)
                self.text_box.insert(END,result)
                self.prevButton = 'ENTER' #assign 'ENTER' to prevButton after ENTER button is clicked
        

root = Tk()
Calculator(root)
root.mainloop()
