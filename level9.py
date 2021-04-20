import turtle

t = turtle.Pen()

for i in range(4):
    t.forward(100)
    t.right(90)

colors = ['yellow', 'blue', 'red', 'green']


t.reset()
def figure(step,times):
    t.color('red')
    t.begin_fill()
    for i in range(0,times):
        t.forward(step)
        t.right(360/times)
    t.end_fill()

figure(99,15)
t.hideturtle()


turtle.mainloop()