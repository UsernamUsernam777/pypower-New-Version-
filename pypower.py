import _datetime
import customtkinter as _ctk
import pyperclip as _pyperclip
import time as _time
import webbrowser as _webbrowser
import os as _os
import subprocess as _subprocess
from turtle import Turtle as _Turtle

class Time:
    def convert_to_iterable_and_int(time_str, type_output=tuple):
        """Converts a time string (e.g., '10:30') into an iterable of integers."""
        return type_output(map(int, time_str.split(':')))

    def how_many_hms_in_s(sec):
        """Calculates hours, minutes, and seconds from total seconds."""
        hours = sec // 3600
        minutes = (sec % 3600) // 60
        seconds = (sec % 3600) % 60
        return f"{hours:02}:{minutes:02}:{seconds:02}"

class Other:
    def sk_loop():
        """Runs an infinite loop to fix keyboard language (sk) and copy to clipboard."""
        while True:
            a = String(input('')).sk()
            _pyperclip.copy(a)
            print(a)

    def search_google(text):
        """Searches Google for the given text in a new browser tab."""
        _webbrowser.open_new_tab(f"https://www.google.com/search?q={text}")

    def in_bg(duration, action=None):
        """Executes an action in a background thread after a specific duration."""
        import threading as _threading
        def v():
            _time.sleep(duration)
            if action: action()
        _threading.Thread(target=v, daemon=True).start()

class Apps:
    def create_app(path, icon=None):
        """Automates PyInstaller to create an EXE and cleans up build files."""
        def mainloop():
            if not _os.path.exists(path): print('Error!')
            pj = _os.path.dirname(path); n_py = _os.path.basename(path)
            n_exe = n_py.replace('.py', '.exe'); n_spec = n_py.replace('.py', '.spec')
            pro = ['pyinstaller', '--onefile', '--windowed', n_py]
            _os.chdir(pj)
            if icon: pro.append(f'--icon={icon}')
            p = _subprocess.Popen(pro, creationflags=_subprocess.CREATE_NO_WINDOW)
            p.wait()
            if _os.path.exists(_os.path.join('dist', n_exe)):
                _os.replace(_os.path.join('dist', n_exe), _os.path.join(pj, n_exe))
            _os.system('rmdir /s /q dist'); _os.system('rmdir /s /q build'); _os.remove(n_spec)
        Other.in_bg(2, mainloop)

class Files:
    def copy_pypower(pypower_path):
        """Copies the entire pypower.py file content to the clipboard."""
        with open(pypower_path, 'r', encoding='utf-8') as f: _pyperclip.copy(f.read())

    def append_to_pypower(class_name, code):
        """Appends a new class or code snippet directly to the pypower library."""
        Files.append_to_file(r"C:\Users\power\AppData\Local\Programs\Python\Python314\pypower.py", f'\n#{class_name}'+code)

    def append_to_file(path, text):
        """Safely appends text to a file, maintaining existing content."""
        with open(path, 'r', encoding='utf-8') as a: old_text = a.read()
        with open(path, 'w', encoding='utf-8') as b: b.write((old_text + '\n' + text).replace('\n\n', '\n'))

class GUI:
    class CustomTk:
        def tidy_up(widgets, per_row):
            """Organizes a list of widgets into a grid layout with a set number per row."""
            columns = 0; rows = 1
            for i in widgets:
                columns += 1; i.grid(row=rows, column=columns, padx=3, pady=3)
                if columns in Math.number_multiplies(per_row, len(widgets)):
                    columns = 0; rows += 1

        def all_objects(master):
            """Retrieves a flat list of all children widgets within a master container."""
            result = []
            for i in master.winfo_children():
                if isinstance(i, list): result.extend(all_objects(i))
                else: result.append(i)
            return result

        def edit_all_widgets_texts(master, font='arial', size=20, text_color='lightblue', bg=''):
            """Batch updates text styles for all widgets in a container."""
            for i in master.winfo_children():
                i.configure(font=(font, size), text_color=text_color, fg_color=bg if bg else None)

        def info(widget, information, font='arial', size=20, bg='', hide_after=5):
            """Creates a hover-triggered tooltip label for a widget."""
            inf = _ctk.CTkLabel(widget.master, text=information, font=(font, size), fg_color=bg if bg else None)
            def show(e):
                x = widget.winfo_x(); y = widget.winfo_y()
                inf.after(1000, lambda: inf.place(x=x, y=y+widget.winfo_height()))
                inf.after(hide_after*1000, inf.place_forget)
            widget.bind('<Enter>', show)

        def mouse_wheel_num(entry, start, end):
            """Enables value increment/decrement using the mouse scroll wheel."""
            def f(e):
                a = entry.get(); b = range(start, end)
                if a.isdigit():
                    entry.delete(0, 'end')
                    idx = b.index(int(a))
                    entry.insert(0, (idx + 1 if e.delta >= 1 else idx - 1) % len(b))
            entry.bind("<MouseWheel>", f)

    class Turtle:
        def move(obj, distance, direction='forward'):
            """Moves a Turtle object forward or backward without drawing."""
            obj.penup()
            if direction == 'forward': obj.fd(distance)
            else: obj.bk(distance)
            obj.pendown()

        def write_text(text, font=('arial', 20), color='black', align='center'):
            """Writes colored and aligned text on the Turtle screen."""
            res = _Turtle(); res.color(color); res.penup(); res.hideturtle()
            res.write(text, font=font, align=align); return res

class String:
    def __init__(self, text): self.text = text

    def en_nums_to_ar(self):
        """Translates English digits to Arabic/Eastern numerals."""
        dist = {'0': '۰', '1': '۱', '2': '۲', '3': '۳', '4': '٤', '5': '٥', '6': '٦', '7': '٧', '8': '۸', '9': '۹'}
        return ''.join([dist[i] if i in dist else i for i in self.text])

    def there_is_a_number(self, start=0, end=9):
        """Checks if the string contains digits within a specific range."""
        return any(i.isdigit() and int(i) in range(start, end+1) for i in self.text)

    def super_join(self, sep, after_how_many_letters, with_spaces=True):
        """Inserts a separator every N characters in the string."""
        new = ''; ran = Math.number_multiplies(after_how_many_letters, len(self.text)-1)
        for idx, char in enumerate(self.text):
            new += char
            if idx + 1 in ran: new += sep
        return new if with_spaces else new.replace(sep+' '+sep, sep+' ')

    def sk(self, copy=False):
        """Corrects text typed with the wrong keyboard layout."""
        if not self.text: return ''
        eng_ara = {'`': 'ذ', 'q': 'ض', 'w': 'ص', 'e': 'ث', 'r': 'ق', 't': 'ف', 'y': 'غ', 'u': 'ع', 'i': 'ه', 'o': 'خ', 'p': 'ح', '[': 'ج', ']': 'د', 'a': 'ش', 's': 'س', 'd': 'ي', 'f': 'ب', 'g': 'ل', 'h': 'ا', 'j': 'ت', 'k': 'ن', 'l': 'م', ';': 'ك', "'": 'ط', 'z': 'ئ', 'x': 'ء', 'c': 'ؤ', 'v': 'ر', 'b': 'لا', 'n': 'ى', 'm': 'ة', ',': 'و', '.': 'ز', '/': 'ظ'}
        swap_eng_ara = {v: k for k, v in eng_ara.items()}
        s = ''.join([eng_ara[i] if i in eng_ara else swap_eng_ara[i] if i in swap_eng_ara else i for i in self.text])
        if s and copy: _pyperclip.copy(s)
        return s

    def reverse(self, sep):
        """Reverses string segments based on a delimiter (e.g., reversing dates)."""
        return sep.join(self.text.split(sep)[::-1])

    def replace_objects_with_one(self, iterable, new_obj=''):
        """Replaces all specified characters in a string with a single new object."""
        return ''.join([new_obj if i in iterable else i for i in self.text])

    def replace_many(self, old_iterable, new_iterable):
        """Replaces multiple characters based on mapping lists."""
        res = ''
        for i in self.text:
            if i in old_iterable: res += new_iterable[old_iterable.index(i)]
            else: res += i
        return res

class Iterable:
    def numred(iterable):
        """Formats an iterable into a numbered string list."""
        return "\n".join([f"{i+1}. {item}" for i, item in enumerate(iterable)])

    def return_brakets():
        """Returns a dictionary of common bracket types."""
        return {'list': ('[', ']'), 'tuple':('(', ')'), 'curley': ('{', '}')}

    def replace(iterable, index, new_obj):
        """Replaces an item in a list by its index (1-based)."""
        co = iterable[:]
        co[index-1] = new_obj
        return co

    def return_dict_in_lines(dec):
        """Converts a dictionary to a formatted multi-line string."""
        return "\n".join([f"{k}: {v}" for k, v in dec.items()])

    class Dict:
        def swap_dict(dic):
            """Swaps dictionary keys and values."""
            return {str(v): k for k, v in dic.items()}

class Math:
    def iter_num(iterable):
        """Returns statistical analysis (sum, average, max, min) of a numeric list."""
        return {'sum': sum(iterable), 'average': sum(iterable) / len(iterable), 'max': max(iterable), 'min': min(iterable)}

    def number_multiplies(num, end, type=list):
        """Generates a list of multiples of a number up to a limit."""
        return type(range(num, end+1, num))

    def arrays(array_end, step, show='lists'):
        """Creates stepped range pairs as lists or formatted strings."""
        result = [[i, i+step] for i in range(step, array_end, step)]
        if show != 'lists':
            return "\n".join([f"{i} - {e}" for i, e in result])
        return result
