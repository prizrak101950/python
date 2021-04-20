import turtle
t = turtle.Pen()
turtle.mainloop()
t = turtle.Pen()
t.forvard(100)
t.right(90)
t.forvard(100)
t.right(90)
t.forvard(100)
t.right(90)
t.forvard(100)
t.right(90)

t.reset()
for i in range(4):
    t.forvard(100)
    t.right(90)
    t.color("green")
    for i in range(4):
        t.forvard(100)
        t.right(90)
turtle.mainloop()
