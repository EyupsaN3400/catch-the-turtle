import time
import turtle
import random
import math

countdown_turtle = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
screen.title('Catch the Turtle')
score = 0
game_over = False

t = turtle.Turtle(visible=False)

def draw_circle_random():
    global game_over
    
    if not game_over:
        new_x = random.randint(-200, 200)
        new_y = random.randint(-200, 200)
        color = 'green'
        
        t.clear()
        t.penup()
        t.goto(new_x, new_y)
        t.dot(50, color) 

def check_click_in_circle(x, y):
    global score
    
    if not game_over:
        circle_x, circle_y = t.position()
        circle_radius = 25
        distance = math.sqrt((x - circle_x) ** 2 + (y - circle_y) ** 2)

        if distance <= circle_radius:
            score += 1
            draw_circle_random()
            update_score()

def countdown(time):
    global game_over
    
    countdown_turtle.hideturtle()
    countdown_turtle.color("white")
    countdown_turtle.penup()
    
    top_height = screen.window_height() / 2
    y = top_height * 0.9
    countdown_turtle.setposition(0, y - 30)

    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg="Time: {}".format(time), move=False, align="center")
        screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        game_over = True
        countdown_turtle.clear()
        countdown_turtle.write(arg="Time's up! Final Score: {}".format(score), move=False, align="center")

def update_score():
    global score
    
    score_turtle.clear()
    score_turtle.write(arg="Score: {}".format(score), move=False, align="center")

score_turtle = turtle.Turtle()
score_turtle.hideturtle()
score_turtle.color("white")
score_turtle.penup()
score_turtle.setposition(0, screen.window_height() / 2 - 50)
score_turtle.write(arg="Score: 0", move=False, align="center")



draw_circle_random()
countdown(10)
turtle.onscreenclick(check_click_in_circle)

turtle.done()
