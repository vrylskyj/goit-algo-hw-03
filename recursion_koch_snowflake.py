import turtle

def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order-1, size/3)
            t.left(angle)

def main():
    # Запитуємо в користувача рівень рекурсії
    order = int(input("Введіть рівень рекурсії (ціле число >= 0): "))
    
    # Створюємо вікно та налаштовуємо туртл
    window = turtle.Screen()
    window.bgcolor("white")
    window.title("Сніжинка Коха")
    t = turtle.Turtle()
    t.speed(0)  # Налаштовуємо максимальну швидкість для швидкої відобразки

    # Переміщуємо туртл до відповідного місця перед малюванням
    t.penup()
    t.goto(-150, 90)
    t.pendown()

    # Малюємо сніжинку Коха
    for _ in range(3):
        koch_snowflake(t, order, 300)
        t.right(120)

    # Закриваємо вікно при кліку на нього
    window.mainloop()

if __name__ == "__main__":
    main()
