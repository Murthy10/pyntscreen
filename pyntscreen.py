import os
import uuid
import tkinter as tk
from tkinter import filedialog
import pyscreenshot as ImageGrab


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.bind('<Control_L>', self.trigger)
        self.active = False
        self._image_height = tk.StringVar()
        self._image_width = tk.StringVar()
        self._counter_text = tk.StringVar()
        self._save_directory = tk.StringVar()
        self._set_texts()
        self.create_widgets()
        self.images = []

        self.x_old, self.y_old = self.master.winfo_pointerxy()

    def _set_texts(self):
        self.counter_text = 0
        self.image_height = 50
        self.image_width = 50
        self.save_directory = os.path.dirname(os.path.realpath(__file__))

    def create_widgets(self):
        tk.Label(self.master, textvariable=self._save_directory).grid(row=0)
        tk.Label(self.master, text="Image height").grid(row=1)
        tk.Label(self.master, text="Image width").grid(row=2)
        tk.Label(self.master, textvariable=self._counter_text).grid(row=3)

        entry_height = tk.Entry(self.master, width=10, textvariable=self._image_height)
        entry_width = tk.Entry(self.master, width=10, textvariable=self._image_width)
        entry_height.grid(row=1, column=1)
        entry_width.grid(row=2, column=1)

        tk.Button(self.master, text='Change', command=self.askdirectory).grid(row=0, column=1)

        button_store = tk.Button(self.master)
        button_store["text"] = "Save images"
        button_store["command"] = self.save_images
        button_store.grid(row=3, column=1)

    def askdirectory(self):
        self.save_directory = str(filedialog.askdirectory())

    def trigger(self, _):
        self.active = not self.active
        if self.active:
            self.take_pictures()
            self.master.config(background="green")
        else:
            self.master.config(background="gainsboro")

    def save_images(self):
        destination = self.save_directory
        if not destination.endswith('/'):
            destination += '/'
        for image in self.images:
            if image.mode != "RGB":
                image = image.convert("RGB")
            image.save(destination + str(uuid.uuid4()) + '.jpg')
        self.images = []
        self.counter_text = len(self.images)

    def take_pictures(self):
        if self.active and self._has_mouse_moved_enough():
            image = ImageGrab.grab(bbox=self._build_bbox())
            if self._right_image_size(image):
                self.images.append(image)
                self.counter_text = len(self.images)
        self.master.after(100, self.take_pictures)

    def _right_image_size(self, image):
        current_width, current_height = image.size
        return current_height == self.image_height and current_width == self.image_width

    def _has_mouse_moved_enough(self):
        x, y = self.master.winfo_pointerxy()
        diff_x = abs(x - self.x_old)
        diff_y = abs(y - self.y_old)
        if diff_x > self.image_width or diff_y > self.image_height:
            self.x_old = x
            self.y_old = y
            return True
        return False

    def _build_bbox(self):
        x, y = self.master.winfo_pointerxy()
        half_height = self.image_height / 2
        half_width = self.image_width / 2
        left = x - half_width
        top = y - half_height
        right = x + half_width
        bottom = y + half_height
        return left, top, right, bottom

    @property
    def image_height(self):
        return int(self._image_height.get())

    @image_height.setter
    def image_height(self, value):
        self._image_height.set(str(value))

    @property
    def image_width(self):
        return int(self._image_width.get())

    @image_width.setter
    def image_width(self, value):
        self._image_width.set(str(value))

    @property
    def counter_text(self):
        return self._counter_text.get()

    @counter_text.setter
    def counter_text(self, number):
        self._counter_text.set('Count: ' + str(number))

    @property
    def save_directory(self):
        return self._save_directory.get()

    @save_directory.setter
    def save_directory(self, path):
        self._save_directory.set(path)

if __name__ == '__main__':
    root = tk.Tk()
    root.wm_title("pyntscreen")
    app = Application(master=root)
    app.mainloop()


