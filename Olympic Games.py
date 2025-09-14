#Display three messages
print ("Hello World!!!")
print ("Olympics 2024")
print ("Let's Gooooo!!!")

#Display mathematical code
import datetime
x = datetime.date(2024, 8, 26)
print (x)

#OlympicSymbol.py
import turtle
turtle.speed(10) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest
turtle.bgcolor("lightblue")
turtle.hideturtle()
turtle.pensize(6)
turtle.color("blue")
turtle.penup()
turtle.goto(-110, -25)
turtle.pendown()
turtle.circle(50)
turtle.color("black")
turtle.penup()
turtle.goto(0, -25)
turtle.pendown()
turtle.circle(50)
turtle.color("red")
turtle.penup()
turtle.goto(110, -25)
turtle.pendown()
turtle.circle(50)
turtle.color("yellow")
turtle.penup()
turtle.goto(-55, -75)
turtle.pendown()
turtle.circle(50)
turtle.color("green")
turtle.penup()
turtle.goto(55, -75)
turtle.pendown()
turtle.circle(50)
turtle.color("black")
turtle.penup()

import turtle
pen = turtle.Turtle()
pen.speed(1) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest
pen.hideturtle()
def draw_text_with_border(text, font, border_color, text_color):
    pen.color(border_color)
    pen.penup()
    
    for offset in range(-2, 3, 2):
        pen.goto(0 + offset, -10 + offset)
        pen.write(text, font=font, align="center")
        pen.color(text_color)
    pen.write(text, font=font, align="center")

draw_text_with_border("OLYMPIC GAMES", ("Arial", 40, "bold"), "black", "white")

def draw_text_with_border(text, font, border_color, text_color):
    pen.color(border_color)
    pen.penup()
  
    for offset in range(-2, 3, 2):
        pen.goto(0 + offset, -51 + offset)
        pen.write(text, font=font, align="center")
        pen.color(text_color)
    pen.write(text, font=font, align="center")
   
draw_text_with_border("2024", ("Arial", 38, "bold"), "black", "white")
    


turtle.done()