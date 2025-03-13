import sys

def file_read_method():
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, 'r') as file:
            data = file.read()

            # Перевірка на наявність нового рядка в кінці файлу
            if not data.endswith("\n"):
                raise ValueError

            # Видаляємо зайві пробіли та розбиваємо рядок на числа
            parts = data.strip().split()

            if len(parts) != 3:
                raise ValueError

            a, b, c = map(float, parts)

            if a == 0:
                print("Error. a cannot be 0")
                sys.exit(1)

    except FileNotFoundError:
        print(f"file {filename} does not exist")
        sys.exit(1)
    except ValueError:
        print("invalid file format")
        sys.exit(1)

    print(f"Equation is: ({a}) x^2 + ({b}) x + ({c}) = 0")

    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        x1 = (-b - discriminant ** 0.5) / (2 * a)
        x2 = (-b + discriminant ** 0.5) / (2 * a)
        print("There are 2 roots")
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")
    elif discriminant == 0:
        x = -b / (2 * a)
        print("There are 1 roots")
        print(f"x1 = {abs(x)}")
    else:
        print("There are 0 roots")

file_read_method()
