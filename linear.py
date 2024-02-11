import pyglet
import random

window = pyglet.window.Window(width=1500, height=200, caption='Linear Search Visualization')
batch = pyglet.graphics.Batch()

numbers = random.sample(range(1, 100), 35) + [82]
random.shuffle(numbers)

current_index = 0
found_index = -1
search_complete = False

def linear_search():
    global current_index, found_index, search_complete
    if current_index < len(numbers):
        if numbers[current_index] == 82:
            found_index = current_index
            search_complete = True
        current_index += 1
    else:
        search_complete = True

pyglet.clock.schedule_interval(lambda dt: linear_search(), 1)

@window.event
def on_draw():
    window.clear()
    for i, number in enumerate(numbers):
        
        x = i * 40 + 10
        y = window.height // 2
        width = 30
        height = 30

        if i == current_index and not search_complete:
            color = (173, 216, 230)  
        elif i == found_index:
            color = (255, 160, 122)  
        else:
            color = (200, 200, 200)  
        
        pyglet.shapes.Rectangle(x, y, width, height, color=color, batch=batch).draw()
        
        label = pyglet.text.Label(str(number), x=x+width//2, y=y+height//2, anchor_x='center', anchor_y='center', color=(0, 0, 0, 255), batch=batch)
        label.draw()

pyglet.app.run()