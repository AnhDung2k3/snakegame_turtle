from turtle import Turtle, Screen
import time
from random import randint

init_pos = [(0, 0), (-20, 0), (-40, 0)]

class Snake():
    def __init__(self):
        self.nodes_snake = []
        self.init_snake()
        self.snake_speed = 0.2
    
    def init_snake(self):
        for pos in init_pos:
            self.add_node(pos)

    def add_node(self, pos):
        node_snake = Turtle()
        node_snake.color("white")
        node_snake.shape("square")
        node_snake.penup()
        node_snake.goto(pos)
        self.nodes_snake.append(node_snake)

    def snake_eat(self):
        #"position" method is used to find the turtle’s current location (x, y), as a Vec2D-vector.
        self.add_node(self.nodes_snake[-1].position())

    def move_snake(self):
        for i in range(len(self.nodes_snake) - 1, 0, -1):
            pos_x = self.nodes_snake[i - 1].xcor()
            pos_y = self.nodes_snake[i - 1].ycor()
            self.nodes_snake[i].goto(pos_x, pos_y)
        
        self.nodes_snake[0].forward(20)

    def go_up(self):
        if self.nodes_snake[0].heading() != 270:
            self.nodes_snake[0].setheading(90)
    
    def go_down(self):
        if self.nodes_snake[0].heading() != 90:
            self.nodes_snake[0].setheading(270)

    def go_right(self):
        if self.nodes_snake[0].heading() != 180:
            self.nodes_snake[0].setheading(0)

    def go_left(self):
        if self.nodes_snake[0].heading() != 0:
            self.nodes_snake[0].setheading(180)

    def increase_speed(self):
        self.snake_speed *= 0.5

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.6, 0.6)
        self.penup()
        self.color("red")
        x_pos = randint(-280, 280)
        y_pos = randint(-280, 280)
        self.goto(x_pos, y_pos)
    
    def init_food(self):
        x_pos = randint(-280, 280)
        y_pos = randint(-280, 280)
        self.goto(x_pos, y_pos)

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.grade = 0
        self.color("yellow")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_grade()

    def update_grade(self):
        self.write(f"Your score: {self.grade}", align = "center", font = ("sans", 20, "normal"))

    def increase_point(self):
        self.grade += 1
        self.clear()
        self.update_grade()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align = "center", font = ("sans", 20, "normal"))
        self.goto(0, -30)
        self.write("Press SPACE to continue", align = "center", font = ("sans", 20, "normal"))

display = Screen()
display.setup(600, 600)
display.bgcolor("black")
display.title("Snake game")
display.tracer(0)

display.listen()

def start_game():
    snake = Snake()
    food = Food()
    score = Score()

    display.onkey(snake.go_up, "Up")
    display.onkey(snake.go_down, "Down")
    display.onkey(snake.go_left, "Left")
    display.onkey(snake.go_right, "Right")

    start_game = True
    while start_game:
        time.sleep(snake.snake_speed)
        display.update()
        snake.move_snake()
        
        if snake.nodes_snake[0].distance(food) < 16:
            food.init_food()
            score.increase_point()
            snake.snake_eat()
            if score.grade % 5 == 0:
                snake.increase_speed()

        if snake.nodes_snake[0].xcor() > 280 or snake.nodes_snake[0].xcor() < -280 or snake.nodes_snake[0].ycor() > 280 or snake.nodes_snake[0].ycor() < -280:
            start_game = False
            score.game_over()
        
        for node in snake.nodes_snake[1:]:
            if snake.nodes_snake[0].distance(node) < 10:
                start_game = False
                score.game_over()

def game_continue():
    display.reset()
    start_game()

game_continue()
display.onkey(game_continue, "space")

display.exitonclick()