## CSC500 Module 5 - Critical Thinking, Part Two
## Sonya Bourgeois
## 06/16/2024

def main():
    """This program calculates # of book club points based on book purchase count."""

    while True:
        try:
            num_books_purchased = int(input("How many books did you purchase this month?"))

            if num_books_purchased < 0:
                print("Returns are not a factor. Please enter a non-negative number.")
                continue  # Ask for input again

            points = 0

            if num_books_purchased >= 8:
                points = 60
            elif num_books_purchased >= 6:
                points = 30
            elif num_books_purchased >= 4:
                points = 15
            elif num_books_purchased >= 2:
                points = 5

            print(f"Congrats - you've earned {points} points this month!")
            break  # Exit the loop after a valid input

        except ValueError:
            print("Partial book purchases are not a thing. Please enter a whole number.")

if __name__ == "__main__":
    main()
