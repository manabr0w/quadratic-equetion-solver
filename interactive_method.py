def interactive_method_solution():
    def get_float(prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError as e:
                print(f"Error. Expected a valid real number, got {e.args[0].split(': ')[1]} instead")

    while True:
        a = get_float("a = ")
        if a != 0:
            break
        print("Error. Coefficient 'a' cannot be zero.")

    b = get_float("b = ")
    c = get_float("c = ")

    print(f"Equation is: ({a}) x^2 + ({b}) x + ({c}) = 0")

    discriminant = (b ** 2) - (4 * a * c)
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
