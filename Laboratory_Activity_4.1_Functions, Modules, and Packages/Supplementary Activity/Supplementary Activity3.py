import math

def solve_quadratic(a, b, c):
    # Calculate the discriminant
    d = b**2 - 4*a*c

    if d > 0:
        root1 = (-b + math.sqrt(d)) / (2*a)
        root2 = (-b - math.sqrt(d)) / (2*a)
        result = f"Two real roots: {root1} and {root2}"
    elif d == 0:
        root = -b / (2*a)
        result = f"One real root: {root}"
    else:
        real = -b / (2*a)
        imag = math.sqrt(-d) / (2*a)
        result = f"Complex roots: {real}+{imag}i and {real}-{imag}i"

    return result


def save_to_file(a, b, c, result):
    # Save input
    with open("input.txt", "w") as f:
        f.write(f"a = {a}\n")
        f.write(f"b = {b}\n")
        f.write(f"c = {c}\n")

    # Save output
    with open("output.txt", "w") as f:
        f.write(result)


def main():
    print("Quadratic Equation Solver (ax^2 + bx + c = 0)")

    try:
        a = float(input("Enter value for a: "))
        b = float(input("Enter value for b: "))
        c = float(input("Enter value for c: "))

        if a == 0:
            print("This is not a quadratic equation.")
            return

        result = solve_quadratic(a, b, c)

        print("\nResult:")
        print(result)

        save_to_file(a, b, c, result)
        print("\nInput and output saved to files.")

    except ValueError:
        print("Invalid input. Please enter numbers only.")


if __name__ == "__main__":
    main()