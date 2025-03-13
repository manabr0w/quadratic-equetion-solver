import sys

def solve_quadratic_from_file():
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    try:
        with open(filename, 'r') as file:
            data = file.read().strip()
            parts = data.split()
            if len(parts) != 3:
                print("invalid file format")
                sys.exit(1)

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
        print(f"x1 = {x}")
    else:
        print("There are 0 roots")

if __name__ == "__main__":
    solve_quadratic_from_file()
