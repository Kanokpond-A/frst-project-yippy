import pyglet
import random

window = pyglet.window.Window(width=1500, height=200, caption='Binary Search Visualization')
batch = pyglet.graphics.Batch()

numbers = sorted(random.sample(range(1, 100), 35) + [82])

left, right = 0, len(numbers) - 1
mid = (left + right) // 2
found = False
search_complete = False

def binary_search():
    global left, right, mid, found, search_complete
    if left <= right and not found:
        mid = (left + right) // 2
        if numbers[mid] == 82:
            found = True
        elif numbers[mid] < 82:
            left = mid + 1
        else:
            right = mid - 1
    else:
        search_complete = True

pyglet.clock.schedule_interval(lambda dt: binary_search(), 1)

@window.event
def on_draw():
    window.clear()
    for i, number in enumerate(numbers):
        
        x = i * 40 + 10
        y = window.height // 2
        width = 30
        height = 30

        if left <= i <= right and not search_complete:
            color = (173, 216, 230)  
        elif i == mid and not search_complete:
            color = (255, 160, 122)  
        elif found and i == mid:
            color = (144, 238, 144)  
        else:
            color = (200, 200, 200)  
        
        pyglet.shapes.Rectangle(x, y, width, height, color=color, batch=batch).draw()
        
        label = pyglet.text.Label(str(number), x=x+width//2, y=y+height//2, anchor_x='center', anchor_y='center', color=(0, 0, 0, 255), batch=batch)
        label.draw()

pyglet.app.run()