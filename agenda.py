#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import tkinter as tk
import agenda_item_dialog

class Agenda(tk.Frame):
    def __init__(self, master=None):
        global last_x, last_y
        last_x, last_y = 0, 0
        
        self.TOP_OFFSET = 4
        self.STEP = 12
        self.START_HOUR = 7
        self.TIME_RANGE = 13

        self.categories = ('category a', 'category b', 'category c')
    
        super().__init__(master)

        self.canvas = tk.Canvas(self, width=480, height=640)
        self.canvas.pack(padx=5, pady=3)

        self.canvas.bind('<Button-1>', self.start_draw) # 左クリック時
        self.canvas.bind('<Motion>', self.draw)         # マウス移動時
        self.canvas.bind('<ButtonRelease-1>', self.stop_draw) # 左ボタンを離した時

        self.refresh()

    def refresh(self):
        self.canvas.create_rectangle(0, 0, 480, 640, fill='#eeeeee', outline='#eeeeee')
        self.draw_timetable(self.canvas)
        self.draw_ruler(self.canvas, 0, self.TIME_RANGE * 4)

    def start_draw(self, event):
        global last_x, last_y, min_y, max_y
        last_x, last_y, min_y, max_y = event.x, event.y, event.y, event.y

    def draw(self, event):
        global last_x, last_y, min_y, max_y
        global min_point, current_point

        if last_x and last_y: # 前回の位置があれば描画
            last_x, last_y = event.x, event.y # マウスの現在位置を更新

            y_bottom = self.TOP_OFFSET + self.STEP * self.TIME_RANGE * 4
            if last_y > y_bottom:
                last_y = y_bottom
                
            if last_y > max_y:
                max_y = last_y

            if last_y < min_y:
                last_y = min_y

            min_point = (min_y - self.TOP_OFFSET) // self.STEP
            current_point = (last_y - self.TOP_OFFSET) // self.STEP
            max_point = (max_y - self.TOP_OFFSET) // self.STEP
            
            rect_y_top = self.TOP_OFFSET + min_point * self.STEP
            rect_y_mid = self.TOP_OFFSET + current_point * self.STEP
            rect_y_bottom = self.TOP_OFFSET + max_point * self.STEP

            if rect_y_mid > rect_y_top:
                self.canvas.create_rectangle(90, rect_y_top, 470, rect_y_mid, fill='#888888', outline='#888888', width=1)
            if rect_y_bottom > rect_y_mid:
                self.canvas.create_rectangle(90, rect_y_mid + 1, 470, rect_y_bottom, fill='#eeeeee', outline='#eeeeee', width=1)
            self.draw_ruler(self.canvas, min_point, max_point)
            
    def stop_draw(self, event):
        global last_x, last_y, min_y, max_y
        last_x, last_y, min_y, max_y = None, None, None, None
        global min_point, current_point

        t_start = self.conv_index_time(min_point)
        t_end = self.conv_index_time(current_point)

        dialog = agenda_item_dialog.AgendaItemDialog(self, start_time=t_start, end_time=t_end, categories=self.categories)
        if dialog.result:
            print(f'入力された値: {dialog.result}')
        else:
            print('Canceled')

        self.refresh()

    def draw_ruler(self, canvas, start_index, end_index):
        for i in range(start_index, end_index + 1):
            y = self.TOP_OFFSET + i * self.STEP
            if i % 4 == 0:
                self.canvas.create_line(90, y, 470, y, fill='#888888', width=1)
            elif i % 4 == 2:
                self.canvas.create_line(90, y, 470, y, fill='#888888', width=1, dash=(1, 1))
            else:
                self.canvas.create_line(90, y, 470, y, fill='#eeeeee', width=1)

        y_bottom = self.TOP_OFFSET + self.STEP * self.TIME_RANGE * 4
        self.canvas.create_line(90, self.TOP_OFFSET, 90, y_bottom, fill='#888888', width=1)
        self.canvas.create_line(470, self.TOP_OFFSET, 470, y_bottom, fill='#888888', width=1)

    def draw_timetable(self, canvas):
        for i in range(0, self.TIME_RANGE * 4 + 1):
            y = self.TOP_OFFSET + i * self.STEP
            if i % 4 == 0:
                self.canvas.create_line(10, y, 90, y, fill='#888888', width=1)
            elif i % 4 == 2:
                self.canvas.create_line(10, y, 90, y, fill='#888888', width=1, dash=(1, 1))
            else:
                self.canvas.create_line(10, y, 90, y, fill='#eeeeee', width=1)

        for i in range(0, self.TIME_RANGE * 4):
            y = self.TOP_OFFSET + i * self.STEP
            if i % 4 == 0:
                t = self.conv_index_time(i)
                canvas.create_text(50, y + 12, text=t, font=('Arial', 12))
                
        y_bottom = self.TOP_OFFSET + self.STEP * self.TIME_RANGE * 4
        self.canvas.create_line(10, self.TOP_OFFSET, 10, y_bottom, fill='#888888', width=1)
        self.canvas.create_line(90, self.TOP_OFFSET, 90, y_bottom, fill='#888888', width=1)
        
    def conv_index_time(self, idx, **kwargs):
        h = idx // 4 + self.START_HOUR
        m = (idx % 4) * 15

        if 'end' in kwargs:
            if kwargs['end']:
                m += 15
        if m == 60:
            h += 1
            m = 0
        
        t = f'{h}:{m:02}'.rjust(5, ' ')
        return(t)
