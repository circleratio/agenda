#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import tkinter as tk
import tkinter.font as tkFont
import datetime
import agenda
import json
import os

class Menubar(tk.Menu):
    def __init__(self, master=None):
        super().__init__(master)
        menu_font = tkFont.Font(family='Meiryo UI', size=12)

        # ファイルメニューの作成
        filemenu = tk.Menu(self, tearoff=0, font=menu_font)
        filemenu.add_command(label='New', font=menu_font)
        filemenu.add_command(label='New', font=menu_font)
        filemenu.add_command(label='Open', font=menu_font)
        filemenu.add_command(label='Save', font=menu_font, command=self.save)
        filemenu.add_command(label='Export', font=menu_font)
        filemenu.add_separator()
        filemenu.add_command(label='Exit', font=menu_font, command=self.quit)
        self.add_cascade(label='File', menu=filemenu)

        # 編集メニューの作成
        editmenu = tk.Menu(self, tearoff=0)
        editmenu.add_command(label='Cut', font=menu_font)
        editmenu.add_command(label='Copy', font=menu_font)
        editmenu.add_command(label='Paste', font=menu_font)
        self.add_cascade(label='Edit', menu=editmenu)

    def save(self):
        print('save')
        
class DateFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        
        back_week_button = tk.Button(self,text='<<')
        back_week_button.grid(column=0, row=0, padx=10, pady=10)

        back_day_button = tk.Button(self,text='<')
        back_day_button.grid(column=1, row=0, padx=0, pady=10)
        
        dt = datetime.datetime.now()
        date_text = dt.strftime('%Y/%m/%d (%a)')
        
        label = tk.Label(self, text=date_text)
        label.grid(column=2, row=0, padx=10, pady=10)
        
        forward_day_button = tk.Button(self,text='>')
        forward_day_button.grid(column=3, row=0, padx=0, pady=10)
        
        forward_week_button = tk.Button(self,text='>>')
        forward_week_button.grid(column=4, row=0, padx=10, pady=10)
               
class App(tk.Tk):
    def __init__(self, **kwargs):
        if 'agenda_dict' in kwargs:
            self.agenda_dict = kwargs['agenda_dict']
        else:
            self.agenda_dict = {}
        
        super().__init__()
        self.title('worklog')
        self.geometry()

        menubar = Menubar(self)
        self.config(menu=menubar)
        
        dateframe = tk.Frame(self)
        dateframe.pack()
        d = DateFrame(dateframe)
        d.pack()

        agendaframe = tk.Frame(self)
        agendaframe.pack()
        af = agenda.Agenda(agendaframe)
        af.pack()

if __name__ == '__main__':
    db_file = 'worklog.json'
    agenda_dict = {}
    
    if os.path.isfile(db_file):
        agenda_dict = json.load(db_file)
    
        app = App(agenda_dict=agenda_dict)
    app = App()
    app.mainloop()
