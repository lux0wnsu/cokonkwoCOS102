# Simple program to find the roots of quadratic, cubic, and quartic equations

def quadratic():
    print("\nSolving Quadratic: Ax² + Bx + C = 0")
    a = float(input("Enter A: "))
    b = float(input("Enter B: "))
    c = float(input("Enter C: "))

    disc = b**2 - 4*a*c
    root1 = (-b + (disc)**0.5) / (2*a)
    root2 = (-b - (disc)**0.5) / (2*a)

    print("The roots are:", root1, "and", root2)

def cubic():
    print("\nSolving Cubic: Ax³ + Bx² + Cx + D = 0")
    a = float(input("Enter A: "))
    b = float(input("Enter B: "))
    c = float(input("Enter C: "))
    d = float(input("Enter D: "))

    # Using numpy for solving
    import numpy as np
    roots = np.roots([a, b, c, d])
    print("The roots are:")
    for r in roots:
        print(r)

def quartic():
    print("\nSolving Quartic: Ax⁴ + Bx³ + Cx² + Dx + E = 0")
    a = float(input("Enter A: "))
    b = float(input("Enter B: "))
    c = float(input("Enter C: "))
    d = float(input("Enter D: "))
    e = float(input("Enter E: "))

    # Using numpy for solving
    import numpy as np
    roots = np.roots([a, b, c, d, e])
    print("The roots are:")
    for r in roots:
        print(r)

# Main program
print("Welcome! Choose the equation type:")
print("1. Quadratic")
print("2. Cubic")
print("3. Quartic")

choice = input("Enter 1, 2, or 3: ")

if choice == "1":
    quadratic()
elif choice == "2":
    cubic()
elif choice == "3":
    quartic()
else:
    print("Invalid choice.")
