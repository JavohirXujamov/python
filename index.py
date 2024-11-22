import turtle

# Ekranda turtle oynasini yaratish
screen = turtle.Screen()
screen.bgcolor("black")  # Orqa fonni qora qilish

# Yurak chizish uchun turtle obyektini yaratish
pen = turtle.Turtle()
pen.shape("turtle")
pen.color("red")
pen.speed(3)

# Yurak shaklini chizish funktsiyasi
def draw_heart():
    pen.begin_fill()
    pen.left(50)
    pen.forward(133)
    pen.circle(50, 200)
    pen.right(140)
    pen.circle(50, 200)
    pen.forward(133)
    pen.end_fill()

# Yurakni chizish va animatsiya qilish
for _ in range(10):  # Yurakni 10 marta chizish
    draw_heart()
    pen.penup()
    pen.forward(200)  # Har safar bir oz oldinga harakatlanish
    pen.pendown()

# Ekranda turtle oynasini yopmaslik uchun
turtle.done()