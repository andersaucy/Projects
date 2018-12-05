import math

#Enter a number generate Pi up to n decimal places

def piToTheNth(n):
    pi_Nth = round(math.pi, n)
    pi = str(pi_Nth)
    return pi;

def main():
    digits = int(input("How many decimal places?\n"))
    print piToTheNth(digits);

if __name__ == "__main__":
    main()
