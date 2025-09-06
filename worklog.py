#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import tkinter as tk
import tkinter.font as tkFont
import datetime
import agenda
import json
import os

app_icon = '''R0lGODlhAAEAAfcAAAAAAAAAMwAAZgAAmQAAzAAA/wArAAArMwArZgArmQArzAAr
/wBVAABVMwBVZgBVmQBVzABV/wCAAACAMwCAZgCAmQCAzACA/wCqAACqMwCqZgCq
mQCqzACq/wDVAADVMwDVZgDVmQDVzADV/wD/AAD/MwD/ZgD/mQD/zAD//zMAADMA
MzMAZjMAmTMAzDMA/zMrADMrMzMrZjMrmTMrzDMr/zNVADNVMzNVZjNVmTNVzDNV
/zOAADOAMzOAZjOAmTOAzDOA/zOqADOqMzOqZjOqmTOqzDOq/zPVADPVMzPVZjPV
mTPVzDPV/zP/ADP/MzP/ZjP/mTP/zDP//2YAAGYAM2YAZmYAmWYAzGYA/2YrAGYr
M2YrZmYrmWYrzGYr/2ZVAGZVM2ZVZmZVmWZVzGZV/2aAAGaAM2aAZmaAmWaAzGaA
/2aqAGaqM2aqZmaqmWaqzGaq/2bVAGbVM2bVZmbVmWbVzGbV/2b/AGb/M2b/Zmb/
mWb/zGb//5kAAJkAM5kAZpkAmZkAzJkA/5krAJkrM5krZpkrmZkrzJkr/5lVAJlV
M5lVZplVmZlVzJlV/5mAAJmAM5mAZpmAmZmAzJmA/5mqAJmqM5mqZpmqmZmqzJmq
/5nVAJnVM5nVZpnVmZnVzJnV/5n/AJn/M5n/Zpn/mZn/zJn//8wAAMwAM8wAZswA
mcwAzMwA/8wrAMwrM8wrZswrmcwrzMwr/8xVAMxVM8xVZsxVmcxVzMxV/8yAAMyA
M8yAZsyAmcyAzMyA/8yqAMyqM8yqZsyqmcyqzMyq/8zVAMzVM8zVZszVmczVzMzV
/8z/AMz/M8z/Zsz/mcz/zMz///8AAP8AM/8AZv8Amf8AzP8A//8rAP8rM/8rZv8r
mf8rzP8r//9VAP9VM/9VZv9Vmf9VzP9V//+AAP+AM/+AZv+Amf+AzP+A//+qAP+q
M/+qZv+qmf+qzP+q///VAP/VM//VZv/Vmf/VzP/V////AP//M///Zv//mf//zP//
/wAAAAAAAAAAAAAAACH5BAEAAPwALAAAAAAAAQABAAj/APcJHEiwoMGDCBMqXEgw
0yQxYm5ARENMGcOLGDNq3KhQ2SQ0ECFmIsaxpMmTKFNiVAbyhsuIMCWisaiypk2N
xEDGeMlT4iSaN4MKHaqxXiYxMZBC3MnlRlOYP4lKransaMynSZ2+zAR0qtevKj1K
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
LuQl2jDuYbWNWp+aBKsEYYwICAA7'''

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

        self.tk.call('wm', 'iconphoto', self._w, tk.PhotoImage(data=app_icon))
            
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
