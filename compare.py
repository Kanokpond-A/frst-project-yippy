import pyglet
import random

window = pyglet.window.Window(width=1500, height=800, caption='Search Algorithms Comparison')
batch = pyglet.graphics.Batch()

def reset_searches():
    global numbers, linear_index, linear_found, binary_left, binary_right, binary_mid, binary_found
    
    numbers = random.sample(range(1, 100), 35) + [82]
    random.shuffle(numbers)  
    numbers.sort()  

    linear_index = 0
    linear_found = False
    binary_left, binary_right = 0, len(numbers) - 1
    binary_mid = (binary_left + binary_right) // 2
    binary_found = False

reset_searches()  

def update_searches(dt):
    global linear_index, linear_found, binary_left, binary_right, binary_mid, binary_found

    if not linear_found and linear_index < len(numbers):
        if numbers[linear_index] == 82:
            linear_found = True
        linear_index += 1

    if not binary_found and binary_left <= binary_right:
        binary_mid = (binary_left + binary_right) // 2
        if numbers[binary_mid] == 82:
            binary_found = True
        elif numbers[binary_mid] < 82:
            binary_left = binary_mid + 1
        else:
            binary_right = binary_mid - 1

@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.R:
        reset_searches()

pyglet.clock.schedule_interval(update_searches, 1)

@window.event
def on_draw():
    window.clear()
    margin = 5  
    box_size = (window.width - margin * (len(numbers) + 1)) // len(numbers)  
    for i, number in enumerate(numbers):
        x = i * (box_size + margin) + margin  
        
        y_linear = window.height * 3/4 - box_size / 2
        color_linear = (255, 160, 122) if linear_found and i == linear_index - 1 else (173, 216, 230) if i == linear_index else (200, 200, 200)
        pyglet.shapes.Rectangle(x, y_linear, box_size, box_size, color=color_linear, batch=batch).draw()

        y_binary = window.height / 4 - box_size / 2
        color_binary = (255, 160, 122) if binary_found and i == binary_mid else (173, 216, 230) if binary_left <= i <= binary_right else (200, 200, 200)
        pyglet.shapes.Rectangle(x, y_binary, box_size, box_size, color=color_binary, batch=batch).draw()

        label = pyglet.text.Label(str(number), x=x + box_size/2, y=y_linear + box_size/2, anchor_x='center', anchor_y='center', color=(0, 0, 0, 255), batch=batch)
        label.draw()
        label = pyglet.text.Label(str(number), x=x + box_size/2, y=y_binary + box_size/2, anchor_x='center', anchor_y='center', color=(0, 0, 0, 255), batch=batch)
        label.draw()

pyglet.app.run()