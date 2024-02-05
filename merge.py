from pyglet.window import Window
from pyglet.app import run
from pyglet.shapes import Rectangle
from pyglet.graphics import Batch
from pyglet import clock
import math

def hex_to_rgb(hex_color):
    return int(hex_color[1:3], 16), int(hex_color[3:5], 16), int(hex_color[5:7], 16), 255

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        lh = arr[:mid]
        rh = arr[mid:]

        merge_sort(lh)
        merge_sort(rh)

        i = j = k = 0

        while i < len(lh) and j < len(rh):
            if lh[i] < rh[j]:
                arr[k] = lh[i]
                i += 1
            else:
                arr[k] = rh[j]
                j += 1
            k += 1

        while i < len(lh):
            arr[k] = lh[i]
            i += 1
            k += 1

        while j < len(rh):
            arr[k] = rh[j]
            j += 1
            k += 1

class Renderer(Window):
    def __init__(self, array):
        super().__init__(750, 900, "Merge Sort")
        self.batch = Batch()
        self.array = array
        self.rectangles = []

        for i, e in enumerate(self.array):
            self.rectangles.append(Rectangle(i * 100, 70, 55, e * 10, batch=self.batch))

    def on_update(self, deltatime):
        merge_sort(self.array)

        for i, rect in enumerate(self.rectangles):
            rect.height = self.array[i] * 10

        if all(self.array[i] <= self.array[i + 1] for i in range(len(self.array) - 1)):
            clock.unschedule(self.on_update)
            return

    def on_draw(self):
        self.clear()
        self.batch.draw()

input = [80,56,62,40,49,43,58]
renderer = Renderer(input)
clock.schedule_interval(renderer.on_update, 3)
run()
