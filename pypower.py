import _datetime
import customtkinter as _ctk
import pyperclip as _pyperclip
import time as _time
import webbrowser as _webbrowser
import os as _os
import subprocess as _subprocess
from turtle import Turtle as _Turtle
class Time:
    """convert time to type_output"""
    def convert_to_iterable_and_int(time_str, type_output=tuple):
        return type_output(map(int, time_str.split(':')))
    def how_many_hms_in_s(sec):
        """how many hours, minutes and seconds in seconds"""سن
        hours = sec // 3600
        minutes = (sec % 3600) // 60
        seconds = (sec % 3600) % 60
        return f"{hours:02}:{minutes:02}:{seconds:02}"
class Other:
    def sk_loop():
        while True:
            a = String(input('')).sk()
            _pyperclip.copy(a)
            print(a)
    def copy_pypower(path=_os.path.expanduser('~')+r'\AppData\Local\Programs\Python\Python314\pypower.py'):
        with open(path, 'r', encoding='utf-8') as f:
            _pyperclip.copy(f.read())
    def search_google(text):
        _webbrowser.open_new_tab(f"https://www.google.com/search?q={text}&oq=&gs_lcrp=EgZjaHJvbWUqCQgAECMYJxjqAjIJCAAQIxgnGOoCMgkIARAjGCcY6gIyCQgCEEUYOxjCAzIRCAMQABgDGEIYjwEYtAIY6gIyDwgEEC4YAxiPARi0AhjqAjIRCAUQABgDGEIYjwEYtAIY6gIyEQgGEAAYAxhCGI8BGLQCGOoCMg8IBxAuGAMYjwEYtAIY6gLSAQg0MDVqMGoxNagCCLACAfEF1j7Fc7lEloM&sourceid=chrome&ie=UTF-8")
    def in_bg(duration, action=None):
        import threading as _threading
        def v():
            _time.sleep(duration)
            if action:
                action()
        _threading.Thread(target=v, daemon=True).start()
class Apps:
    def create_app(path, icon=None):
        def mainloop():
            if not _os.path.exists(path):
                print('Error!')
            pj = _os.path.dirname(path)
            n_py = _os.path.basename(path)
            n_exe = _os.path.basename(path).replace('.py', '.exe')
            n_spec = _os.path.basename(path).replace('.py', '.spec')
            pro = ['pyinstaller', '--onefile', '--windowed', n_py]
            _os.chdir(pj)
            if icon:
                pro.append(f'--icon={icon}')
            p = _subprocess.Popen(pro, creationflags=_subprocess.CREATE_NO_WINDOW)
            p.wait()
            if _os.path.exists(_os.path.join('dist', n_exe)):
                _os.replace(_os.path.join('dist', n_exe), _os.path.join(pj, n_exe))
            if _os.path.exists(_os.path.join(pj, n_exe)):
                _os.system('rmdir /s /q dist')
                _os.system('rmdir /s /q build')
                _os.remove(n_spec)
            if _os.path.exists(path.replace('.py', '.exe')):
                print(f"App Created Successed in {path.replace('.py', '.exe')}")
        Other.in_bg(2, mainloop)
class Files:
    def make_if_not_exists(path, type=''):
        if not _os.path.exists(path):
            if type == '':
                _os.mkdir(path)
            else:
                with open(path, 'w', encoding='utf-8') as f:
                    pass
    def append_to_pypower(path=_os.path.expanduser('~')+r'\AppData\Local\Programs\Python\Python314\pypower.py', class_name, code):
        Files.append_to_file(path, f'\n#{class_name}'+code)
    def append_to_file(path, text):
        with open(path, 'r', encoding='utf-8') as a:
            old_text = a.read()
        with open(path, 'w', encoding='utf-8') as b:
            new_text = old_text + '\n' + text
            b.write(new_text.replace('\n\n', '\n'))
class GUI:
    class CustomTk:
        def tidy_up(widgets, per_row, distance_down=5, distance_across=5):
            columns = 0
            rows = 1
            for w in widgets:
                w.grid(column=columns, row=rows, padx=distance_down, pady=distance_across)
                columns += 1
                if columns in Math.number_multiplies(per_row, len(widgets)):
                    rows += 1
                    columns = 0
        def all_objects(master):
            result = []
            for i in master.winfo_children():
                if isinstance(i, list):
                    result.extend(all_objects(i))
                else:
                    result.append(i)
            return result
        def edit_all_widgets_texts(master, font='arial', size=20, text_color='lightblue', bg=''):
            for i in master.winfo_children():
                if bg:
                    i.configure(font=(font, size), text_color=text_color, fg_color=bg)
                else:
                    i.configure(font=(font, size), text_color=text_color, fg_color=None)
        def info(widget, information, font='arial', size=20, bg='', hide_after=5):
            if bg:
                inf = _ctk.CTkLabel(widget.master, text=information, font=(font, size), fg_color=bg)
            else:
                inf = _ctk.CTkLabel(widget.master, text=information, font=(font, size), fg_color=None)
            def show(e):
                x = widget.winfo_x()
                y = widget.winfo_y()
                inf.after(1000, lambda: inf.place(x=x, y=y+widget.winfo_height()))
                inf.after(hide_after*1000, inf.place_forget)
            widget.bind('<Enter>', show)
        def mouse_wheel_num(entry, start, end):
            try:
                def f(e):
                    a = entry.get()
                    b = range(start, end+1)
                    if a.isdigit():
                        entry.delete(0, 'end')
                        if e.delta >= 1:
                            entry.insert(0, (b.index(int(a)) + 1) % len(b))
                        else:
                            entry.insert(0, (b.index(int(a)) - 1) % len(b))
                entry.bind("<MouseWheel>", f)
            except Exception as e:
                pass
    class Turtle:
        def move(obj, distance, direction='forward'):
            if direction in ['backward', 'forward']:
                obj.penup()
                if direction == 'forward':
                    obj.fd(distance)
                elif direction == 'backward':
                    obj.bk(distance)
                obj.pendown()
            else:
                print('Invalid direction!')
        def write_text(text, font=('arial', 20), color='black', align='center'):
            result = _Turtle()
            result.color(color)
            result.penup()
            result.hideturtle()
            result.write(text, font=font, align=align)
            return result
class String:
    def __init__(self, text):
        self.text = text
    def en_nums_to_ar(self):
        dist = {'0': '۰', '1': '۱', '2': '۲', '3': '۳', '4': '٤', '5': '٥', '6': '٦', '7': '٧', '8': '۸', '9': '۹'}
        result = ''
        for i in self.text:
            if i in dist:
                result += dist[i]
            else:
                result += i
        return result
    def there_is_a_number(self , start=0, end=9):
        a = ''
        for i in self.text:
            if i.isdigit():
                if int(i) in range(start, end+1):
                    a += i
        return bool(a)
    def super_join(self, sep, after_how_many_letters, with_spaces=True):
        value = 0
        new = ''
        ran = Math.number_multiplies(after_how_many_letters, len(self.text)-1)
        for i in self.text:
            new += i
            value += 1
            if value in ran:
                new += sep
        if not with_spaces:
            new = new.replace(sep+' '+sep, sep+' ')
        return new
    def sk(self, copy=False):
        if self.text:
            s = ''
            eng_ara = {'`': 'ذ', 'q': 'ض', 'w': 'ص', 'e': 'ث', 'r': 'ق', 't': 'ف', 'y': 'غ', 'u': 'ع', 'i': 'ه', 'o': 'خ', 'p': 'ح', '[': 'ج', ']': 'د', 'a': 'ش', 's': 'س', 'd': 'ي', 'f': 'ب', 'g': 'ل', 'h': 'ا',
                       'j': 'ت', 'k': 'ن', 'l': 'م', ';': 'ك', "'": 'ط', 'z': 'ئ', 'x': 'ء', 'c': 'ؤ', 'v': 'ر', 'b': 'لا', 'n': 'ى', 'm': 'ة', ',': 'و', '.': 'ز', '/': 'ظ'}
            eng_ara_shift = {'~': 'ّ', 'Q': 'َ', 'W': 'ً', 'E': 'ُ', 'R': 'ٌ', 'T': 'لإ', 'Y': 'إ', 'U': '‘', 'I': '÷', 'O': '×', 'P': '؛', '{': '<', '}': '>', 'A': 'ِ', 'S': 'ٍ',
                             'D': ']', 'F': '[', 'G': 'لأ', 'H': 'أ', 'J': 'ـ', 'K': '،', 'L': '/', ':': ':', '"': '"', 'Z': '~', 'X': 'ْ', 'C': '}', 'V': '{', 'B': 'لآ', 'N': 'آ', 'M': '’', '<': ',', '>': '.', '?': '؟'}
            swap_eng_ara = {v: k for k, v in eng_ara.items()}
            swap_eng_ara_shift = {v: k for k, v in eng_ara_shift.items()}
            for i in self.text:
                if i in eng_ara:
                    s += eng_ara[i]
                elif i in swap_eng_ara:
                    s += swap_eng_ara[i]
            #shift
                elif i in eng_ara_shift:
                    s += eng_ara_shift[i]
                elif i in swap_eng_ara_shift:
                    s += swap_eng_ara_shift[i]
                else:
                    s += i
            if s and copy:
                _pyperclip.copy(s)
            return s
        else:
            return ''
    def reverse(self, sep):
        return f'{sep}'.join(self.text.split(sep)[::-1])
    def replace_objects_with_one(self, iterable, new_obj=''):
        result = ''
        for i in self.text:
            if i not in iterable:
                s += i
            else:
                s += new_obj
        return s
    def replace_many(self, old_iterable, new_iterable):
        result = ''
        for i in self.text:
            if i in old_iterable:
                result += new_iterable[old_iterable.index(i)]
            else:
                result += i
        return result
class Iterable:
    def numred(iterable):
        """numred the objects in an iterable ex: if you want to create numred tasks
            numred(['visiting my uncle', 'water the plants']) ➡ 1.visiting my uncle"""
        result = ''
        for i in range(len(iterable)):
            result += f"{i+1}. {iterable[i]}\n"
        return result.strip()
    def return_brakets():
        """return the brakets in a dict"""
        return {'list': ('[', ']'), 'tuple':('(', ')'), 'curley': ('{', '}')}
    def replace(iterable, index, new_obj):
        """replace an object by it's index with new_obj ex:    replace(['mike', 'mark'], 1, 'Olivia')
result = ['Olivia', 'mark']"""
        co = lst[:]
        co[index-1] = new_obj
        return co
    class Dict:
        def swap_dict(dic):
            """k: v ➡ v, k"""
            result = {}
            for k, v in dic.items():
                if isinstance(v, (list, tuple, set, dict)):
                    v = str(v)
                result[v] = k
            return result
    def return_dict_in_lines(dec):
        result = ''
        for i in dec:
            result += f"{i}: {dec[i]}\n"
        return result.strip()
class Math:
    def iter_num(iterable):
        return {'sum': sum(iterable), 'average': sum(iterable) / len(iterable), 'max': max(iterable), 'min': min(iterable)}
    def number_multiplies(num, end, type=list):
        return type(range(num, end+1, num))
    def arrays(array, step, show='lists'):
        result = []
        for i in range(step, array, step):
            result.append([i, i+step])
        if show != 'lists':
            result2 = ''
            for i, e in result:
                result2 += str((i, e)).replace('(', '').replace(')', '').replace(', ', ' - ')+'\n'
            return result2.strip()
        return result
