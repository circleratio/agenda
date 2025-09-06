#!/usr/bin/python3
# -*- coding:utf-8 -*-

import tkinter as tk
import tkinter.ttk as ttk
from tkinter import simpledialog
from tkinter import scrolledtext
import re
import datetime

class AgendaItemDialog(simpledialog.Dialog):
    def __init__(self, master, **kwargs):
        dt = datetime.datetime.today()
        
        self.start_time_hour = dt.hour
        self.start_time_minute = dt.minute
        if 'start_time' in kwargs:
            print(kwargs['start_time'])
            m = re.match(r' *([0-9]+):([0-9]+)', kwargs['start_time'])
            if m:
                self.start_time_hour = int(m.group(1))
                self.start_time_minute = m.group(2)
                
        self.end_time_hour = dt.hour
        self.end_time_minute = dt.minute
        if 'end_time' in kwargs:
            m = re.match(r' *([0-9]+):([0-9]+)', kwargs['end_time'])
            if m:
                self.end_time_hour = int(m.group(1))
                self.end_time_minute = m.group(2)

        self.categories = ()
        if 'categories' in kwargs:
            self.categories = kwargs['categories']
                
        self.subject = ()
        if 'subject' in kwargs:
            self.subject = kwargs['subject']
            
        self.note = ()
        if 'note' in kwargs:
            self.note = kwargs['note']
            
        super(AgendaItemDialog, self).__init__(parent=master, title='Agenda Details')
        
    def body(self, master):
        hours_list = (7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
        minute_list = ('00', '15', '30', '45')
        
        # 開始時間
        label_start = tk.Label(master, text='開始時間')
        label_start.grid(column=0, row=0)

        frame_start_time = tk.Frame(master)
        frame_start_time.grid(column=1, row=0, padx=5, pady=5, sticky=tk.W)
        
        self.start_hour = ttk.Combobox(frame_start_time, values=hours_list, width=3)
        self.start_hour.set(self.start_time_hour)
        self.start_hour.pack(side=tk.LEFT)
        
        sp_start_time = tk.Label(frame_start_time, text=':')
        sp_start_time.pack(side=tk.LEFT)
        
        self.start_minute = ttk.Combobox(frame_start_time, values=minute_list, width=3)
        self.start_minute.set(self.start_time_minute)
        self.start_minute.pack(side=tk.LEFT)

        # 終了時間
        label_end = tk.Label(master, text='終了時間')
        label_end.grid(column=0, row=1)
        
        frame_end_time = tk.Frame(master)
        frame_end_time.grid(column=1, row=1, padx=5, pady=5, sticky=tk.W)
        
        self.end_hour = ttk.Combobox(frame_end_time, values=hours_list, width=3)
        self.end_hour.set(self.end_time_hour)
        self.end_hour.pack(side=tk.LEFT)
        
        sp_end_time = tk.Label(frame_end_time, text=':')
        sp_end_time.pack(side=tk.LEFT)
        
        self.end_minute = ttk.Combobox(frame_end_time, values=minute_list, width=3)
        self.end_minute.set(self.end_time_minute)
        self.end_minute.pack(side=tk.LEFT)

        # 分類
        label_category = tk.Label(master, text='分類')
        label_category.grid(column=0, row=2, padx=5, pady=5)
        
        self.category = ttk.Combobox(master, values=self.categories, width=12)
        self.category.grid(column=1, row=2, padx=5, pady=5, sticky=tk.W)

        # 項目
        label_subject = tk.Label(master, text='項目')
        label_subject.grid(column=0, row=3, padx=5, pady=5)
        
        self.subject = ttk.Entry(master, width=16)
        self.subject.grid(column=1, row=3, padx=5, pady=5, sticky=tk.W)

        # 備考
        label_note = tk.Label(master, text='備考')
        label_note.grid(column=0, row=4, padx=5, pady=5)
        
        self.note = scrolledtext.ScrolledText(master, width=16, height=4, wrap=tk.WORD)
        self.note.grid(column=1, row=4, padx=5, pady=5, sticky=tk.W)

        # エラー表示
        self.label_error = tk.Label(master, text='', fg='red')
        self.label_error.grid(column=1, row=5, padx=5, pady=5, sticky=tk.W)

        # フォーカスを当てるウィジェットを返す
        return self.start_hour
    
    def apply(self):
        result = {}

        result['start_time'] = '{:0>2}:{}'.format(self.start_hour.get(), self.start_minute.get())
        result['end_time'] = '{:0>2}:{}'.format(self.end_hour.get(), self.end_minute.get())
        result['category'] = self.category.get()
        result['subject'] = self.subject.get()
        result['note'] = self.note.get('1.0', 'end -1c')
        
        self.result = result

    def validate(self):
        start_time = '{:0>2}:{}'.format(self.start_hour.get(), self.start_minute.get())
        end_time = '{:0>2}:{}'.format(self.end_hour.get(), self.end_minute.get())

        if end_time <= start_time:
            self.label_error.config(text='終了時間は開始時間より後でなければなりません')
            return(False)
        
        if self.category.get() == '':
            self.label_error.config(text='分類は必須です')
            return(False)
        
        if self.subject.get() == '':
            self.label_error.config(text='項目は必須です')
            return(False)

        return(True)

if __name__ == '__main__':
    category_list = ('category a', 'category b', 'category c')

    root = tk.Tk()
    root.withdraw()

    dialog = AgendaItemDialog(root, categories=category_list)
    if dialog.result:
        print(f'入力された値: {dialog.result}')
    else:
        print('Canceled')
    
    root.destroy()
