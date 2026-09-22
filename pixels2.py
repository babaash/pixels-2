import turtle as t, math as m, time 

s = t.Screen()
s.setup(700, 700)
s.bgcolor("black")
s.tracer(0)

p = t.Turtle()
p.hideturtle()
p.pencolor("white")
p.width(1)

areas = 11
steps = 75

for i in range(steps):
    t_val = i / steps
    r_width = 30 + 225 * (t_val ** 0.9)
    cr = 22 * ((1 - t_val) ** 0.85) + 1.8

    for i in range(areas):
        a0 = 2 * m.pi * i / areas
        angle = a0 + 1.8 * (t_val ** 1.2) - 0.4 * m.pi * t_val
        x = r_width * m.cos(angle)
        y = r_width * m.sin(angle)

        p.penup()
        p.goto(x, y - cr)
        p.pendown()
        p.circle(cr)

    s.update()
    time.sleep(0.025)

t.done()