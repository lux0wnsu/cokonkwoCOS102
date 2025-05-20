#The formula given is not
# CORRECT so i did another one 
# using the correct formula .Thank you 
def simple_interest(P, R, T):
    return P * (1 + (R / 100) * T)

def compound_interest(P, R, n, t):
    return P * (1 + R / (n * 100))**(n * t)

def annuity_plan(PMT, R, n, t):
    r = R / (n * 100)
    return PMT * (((1 + r)**(n * t) - 1) / r)

def main():
    print("Choose calculation:")
    print("1. Simple Interest")
    print("2. Compound Interest")
    print("3. Annuity Plan")
    choice = int(input("Enter choice (1/2/3): "))
    
    if choice == 1:
        P = float(input("Enter principal amount (P): "))
        R = float(input("Enter annual interest rate (R in %): "))
        T = float(input("Enter time period (T in years): "))
        A = simple_interest(P, R, T)
    
    elif choice == 2:
        P = float(input("Enter principal amount (P): "))
        R = float(input("Enter annual interest rate (R in %): "))
        n = int(input("Enter number of times interest is compounded per year (n): "))
        t = float(input("Enter time period (t in years): "))
        A = compound_interest(P, R, n, t)
    
    elif choice == 3:
        PMT = float(input("Enter periodic payment amount (PMT): "))
        R = float(input("Enter annual interest rate (R in %): "))
        n = int(input("Enter number of payments per year (n): "))
        t = float(input("Enter time period (t in years): "))
        A = annuity_plan(PMT, R, n, t)
    
    else:
        print("Invalid choice!")
        return
    
    print(f"The calculated amount (A) is: {A:.2f}")

if __name__ == "__main__":
    main()
