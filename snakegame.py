import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("blue")
wn.setup(width=600, height=600)
wn.tracer(0)

# Başlıqın forması və rəngi
head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# Yemənin forması, rəngi və yeri
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Qazanç və xalın forması, rəngi və yeri
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score : 0  High Score : 0", align="center", font=("candara", 24, "bold"))

# Qrupun yönünü dəyişmək üçün funksiyalar
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

# İstənilən funksiyanı uyğun klavişə tətbiq etmək
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

segments = []

while True:
    wn.update()

    # Xüsusi hadisə: əgər baş özünü oxunun sərhədinə çatdırsa
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"

        # Kölgəni və rəngi təyin et
        colors = random.choice(['red', 'blue', 'green'])
        shapes = random.choice(['square', 'circle'])

        # Qurtun bütün segmentlərini göndər
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()

        # Yeni oyun başlayanda xüsusiyyətləri sıfırlayın
        score = 0
        delay = 0.1

        # Xal və qazanın təyin olunması
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("candara", 24, "bold"))

    # Xüsusi hadisə: əgər qurt yemi təmas edərsə
    if head.distance(food) < 20:
        # Yeməni yeni bir yerdə yerləşdir
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

        # Yeni bir qurt segmenti əlavə et
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("orange")
        new_segment.penup()
        segments.append(new_segment)

        # Xalı və gediş xalını artır
        delay -= 0.001
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("candara", 24, "bold"))

    # Qurtun vəziyyətini yenilə
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Qurtun başını başın yerinə gətirin
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    # Qurtun hərəkət etməsi
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    elif head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    elif head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    elif head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


    # Qurtun özünə çarpması yoxlanılır
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "Stop"

            # Kölgəni və rəngi təyin et
            colors = random.choice(['red', 'blue', 'green'])
            shapes = random.choice(['square', 'circle'])

            # Qurtun bütün segmentlərini göndər
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

            # Yeni oyun başlayanda xüsusiyyətləri sıfırlayın
            score = 0
            delay = 0.1

            # Xal və qazanın təyin olunması
            pen.clear()
            pen.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("candara", 24, "bold"))

    # Yeniləmə gecikməsi
    time.sleep(delay)

wn.mainloop()