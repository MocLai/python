import turtle

# Khởi tạo màn hình đồ họa
screen = turtle.Screen()
screen.setup(500, 500)  # Thiết lập kích thước màn hình

# Khởi tạo con rùa
heart = turtle.Turtle()
heart.shape("turtle")
heart.color("red")
heart.fillcolor("red")
heart.pensize(3)

# Đặt vị trí ban đầu cho con rùa
heart.penup()
heart.goto(0, -150)
heart.pendown()

# Vẽ hình trái tim
heart.begin_fill()
heart.left(140)
heart.forward(224)
for i in range(200):
    heart.right(1)
    heart.forward(2)
heart.left(120)
for i in range(200):
    heart.right(1)
    heart.forward(2)
heart.forward(224)
heart.end_fill()

# Ẩn con rùa sau khi vẽ xong
heart.hideturtle()

# Đóng cửa sổ đồ họa khi nhấn chuột vào cửa sổ
turtle.done()