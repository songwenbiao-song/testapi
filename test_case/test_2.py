from turtle import *

color('black', 'red')
begin_fill()

penup()
goto(50, 50)
pendown()

right(45)
goto(100, 0)
left(90)
fd(120)
circle(50, 225)

penup()
goto(0, 0)
pendown()

left(135)
fd(120)
circle(50, 225)
seth(90)
circle(50, 225)

fd(121)
end_fill()
left(56)

penup()
goto(-210, 40)
pendown()
goto(0, 80)
penup()
goto(160, 110)
pendown()
goto(320, 140)

done()
