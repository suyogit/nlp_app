from tkinter import *
from mydb import Database
from tkinter import messagebox
from myapi import API
class Nlpapp:
    def __init__(self):
        #creating database object
        self.dbo=Database()
        self.apio=API()
        self.root = Tk()#create box of gui
        self.root.iconbitmap('favicon.ico')# inserting icon must be ico format
        self.root.title('nlpapp')# title on top
        self.root.geometry('350x600') #opening dialogue box size
        #self.root.configure(bg='#34495E')# background color
        self.root.configure(bg='#333333')# background color
        self.login_gui()
        self.root.mainloop()# holds the menu in screen
    def login_gui(self):
        self.clear()
        heading= Label(self.root, text='NLPAPP', bg='#333333', fg='red')
        heading.pack(pady=(30,30))# pack is a geometry manager
        heading.configure(font=('verdana',24,'bold'))

        label1=Label(self.root,text='Enter Email',bg='#333333', fg='white')
        label1.pack(pady=(10,10))

        self.email_input= Entry(self.root, width=50)
        self.email_input.pack(pady=(5,10), ipady=4)

        label2 = Label(self.root, text='Enter Password',bg='#333333', fg='white')
        label2.pack(pady=(10, 10))

        self.password_input= Entry(self.root, width=50, show='*')
        self.password_input.pack(pady=(5, 10), ipady=4)

        login_btn=Button(self.root, text='Login', width=10, height=1, fg='white', bg='red',command= self.perform_login)
        login_btn.pack(pady=(10,10))

        label3 = Label(self.root, text='Not a member?', bg='#333333', fg='white')
        label3.pack(pady=(10, 10))

        redirect_btn= Button(self.root, text='Register now',fg='white', bg='red', command=self.register_gui) #when registernow is clicked register_gui function is called
        redirect_btn.pack(pady=(5,5))
    def register_gui(self):
        #now we need to clear previous gui
        self.clear()
        heading = Label(self.root, text='NLPAPP', bg='#333333', fg='red')
        heading.pack(pady=(30, 30))  # pack is a geometry manager
        heading.configure(font=('verdana', 24, 'bold'))

        label0 = Label(self.root, text='Enter Name', bg='#333333', fg='white')
        label0.pack(pady=(10, 10))

        self.name_input = Entry(self.root, width=50)
        self.name_input.pack(pady=(5, 10), ipady=4)

        label1 = Label(self.root, text='Enter Email', bg='#333333', fg='white')
        label1.pack(pady=(10, 10))

        self.email_input = Entry(self.root, width=50)
        self.email_input.pack(pady=(5, 10), ipady=4)

        label2 = Label(self.root, text='Enter Password', bg='#333333', fg='white')
        label2.pack(pady=(10, 10))

        self.password_input = Entry(self.root, width=50, show='*')
        self.password_input.pack(pady=(5, 10), ipady=4)

        register_btn = Button(self.root, text='Register', width=10, height=1,bg='red', fg='white',command=self.perform_registration)
        register_btn.pack(pady=(10, 10))

        label3 = Label(self.root, text='Already a member?', bg='#333333', fg='white')
        label3.pack(pady=(20, 10))

        redirect_btn = Button(self.root, text='Login',  bg='red', fg='white', command=self.login_gui)  # when registernow is clicked register_gui function is called
        redirect_btn.pack(pady=(10, 10))

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()
    def perform_registration(self):
        #fetching data from the gui
        name= self.name_input.get()
        email = self.email_input.get()
        password= self.password_input.get()

        response = self.dbo.add_data(name, email, password)
        #print(name, email, password)

        if response:
            messagebox.showinfo('Success', 'Registration Successful')
        else:
            messagebox.showerror('Error', 'Email already exists')

    def perform_login(self):
        email=self.email_input.get()
        password= self.password_input.get()

        response=self.dbo.search(email,password)

        if response:
            #messagebox.showinfo('Success' ,'Login successful')
            self.home_gui()
        else:
            messagebox.showerror('Error', 'Incorrect email/password')

    def home_gui(self):
        self.clear()

        heading = Label(self.root, text='NLPAPP', bg='#333333', fg='red')
        heading.pack(pady=(30, 30))  # pack is a geometry manager
        heading.configure(font=('verdana', 24, 'bold'))

        sentiment_btn = Button(self.root, text='Sentiment Analysis', width=30, height=2 ,command=self.sentiment_gui)
        sentiment_btn.pack(pady=(10, 10))

        grammar_btn = Button(self.root, text='Grammar and Spelling Correction', width=30, height=2, command=self.grammar_gui)
        grammar_btn.pack(pady=(10, 10))

        emotion_btn = Button(self.root, text='Headline Generation', width=30, height=2, command=self.headline_gui)
        emotion_btn.pack(pady=(10, 10))

        logout_btn = Button(self.root, text='Logout',bg='red', fg='black', command=self.login_gui)  # when registernow is clicked register_gui function is called
        logout_btn.pack(pady=(10, 10))

    def sentiment_gui(self):
        self.clear()
        heading = Label(self.root, text='NLPAPP', bg='#333333', fg='red')
        heading.pack(pady=(30, 30))  # pack is a geometry manager
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='Sentiment Analysis', bg='#333333', fg='white')
        heading2.pack(pady=(10, 20))  # pack is a geometry manager
        heading2.configure(font=('verdana', 20))

        label1 = Label(self.root, text='Enter the text', bg='#333333', fg='white')
        label1.pack(pady=(10, 10))

        self.sentiment_input = Entry(self.root, width=50)
        self.sentiment_input.pack(pady=(5, 10), ipady=4)

        sentiment_btn = Button(self.root, text='Analyze sentiment',command=self.do_sentiment_analysis)  # when registernow is clicked register_gui function is called
        sentiment_btn.pack(pady=(10, 10))

        self.sentiment_result = Label(self.root, text='', bg='#333333', fg='white')
        self.sentiment_result.pack(pady=(10, 10))
        self.sentiment_result.configure(font=('verdana',16))

        goback_btn = Button(self.root, text='👈 Back',bg='red', fg='black',command=self.home_gui)  # when registernow is clicked register_gui function is called
        goback_btn.pack(pady=(3,3))

    def do_sentiment_analysis(self):
        text=self.sentiment_input.get()
        result=self.apio.sentiment_analysis(text)
        #print(result)
        txt=''
        for item in result['scored_labels']:
            txt=txt+ item['label']+ '->' + str(item['score']) + '\n'
            #print(f"{item['label']} -> {item['score']}")
        self.sentiment_result['text']=txt

    def grammar_gui(self):
        self.clear()
        heading = Label(self.root, text='NLPAPP', bg='#333333', fg='red')
        heading.pack(pady=(30, 30))  # pack is a geometry manager
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='Grammar and Spelling Correction', bg='#333333', fg='white')
        heading2.pack(pady=(10, 20))  # pack is a geometry manager
        heading2.configure(font=('verdana', 20))

        label1 = Label(self.root, text='Enter the text for correction', bg='#333333', fg='white')
        label1.pack(pady=(10, 10))

        self.grammar_input = Entry(self.root, width=50)
        self.grammar_input.pack(pady=(5, 10), ipady=4)

        grammar_btn = Button(self.root, text='Correct',command=self.do_grammar_correction)  # when registernow is clicked register_gui function is called
        grammar_btn.pack(pady=(10, 10))

        self.grammar_result = Label(self.root, text='', bg='#333333', fg='white')
        self.grammar_result.pack(pady=(10, 10))
        self.grammar_result.configure(font=('verdana',16))

        goback_btn = Button(self.root, text='👈 Back',bg='red', fg='black',command=self.home_gui)  # when registernow is clicked register_gui function is called
        goback_btn.pack(pady=(10, 10))
    def do_grammar_correction(self):
        text=self.grammar_input.get()
        result=self.apio.grammar_correction(text)
        self.grammar_result['text']=result['correction']

    def headline_gui(self):
        self.clear()
        heading = Label(self.root, text='NLPAPP', bg='#333333', fg='red')
        heading.pack(pady=(30, 30))  # pack is a geometry manager
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='Headline Generation', bg='#333333', fg='white')
        heading2.pack(pady=(10, 20))  # pack is a geometry manager
        heading2.configure(font=('verdana', 20))

        label1 = Label(self.root, text='Enter the text', bg='#333333', fg='white')
        label1.pack(pady=(10, 10))

        self.headline_input = Entry(self.root, width=50)
        self.headline_input.pack(pady=(5, 10), ipady=4)

        headline_btn = Button(self.root, text='Generate Headline',command=self.do_headline_generation)  # when registernow is clicked register_gui function is called
        headline_btn.pack(pady=(10, 10))

        self.headline_result = Label(self.root, text='', bg='#333333', fg='white')
        self.headline_result.pack(pady=(10, 10))
        self.headline_result.configure(font=('verdana',16))

        goback_btn = Button(self.root, text='👈 Back',bg='red', fg='black',command=self.home_gui)  # when registernow is clicked register_gui function is called
        goback_btn.pack(pady=(10, 10))

    def do_headline_generation(self):
        text=self.headline_input.get()
        result=self.apio.headline_generation(text)
        #print(result)
        self.headline_result['text']=result['summary_text']

nlp=Nlpapp()


