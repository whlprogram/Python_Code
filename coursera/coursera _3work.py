# template for "Stopwatch: The Game"
import simplegui
# define global variables
value = 0
x = 0
y = 0
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    if t <= 6000:
        A = t / 600
        B = (t % 600) / 100
        C = ((t % 600) / 10) % 10
        D = (t % 600) % 10
        return str(A) + ":" + str(B) + str(C) + "." + str(D)
    else:
        return "See You"                          
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    
def stop():
    timer.stop()
    global x , y
    y += 1
    if value % 10 == 0:
        x += 1
    
def reset():
    global value, x, y
    value = 0
    x = 0
    y = 0
    timer.stop()

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global value
    value += 1

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(value), [50, 150], 50, "White")
    canvas.draw_text(str(x) + "/" + str(y), [200, 50], 25, "Green")
    
# create frame
frame = simplegui.create_frame("Stopwatch", 250, 250)

# register event handlers
frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(100, timer_handler)
button1 = frame.add_button('Start', start, 150)
button2 = frame.add_button('Stop', stop, 150)
button3 = frame.add_button('Reset', reset, 150)

# start frame
frame.start()


# Please remember to review the grading rubric
