## CSC500 Module 5 - Critical Thinking, Part One
## Sonya Bourgeois
## 06/16/2024

def main():
    """This program will calculate average rainfall over a specified number of years."""

    total_rainfall = 0.0  # Baseline for rainfall calculations.
    num_months = 0

    # Prompt user for number of years.
    while True:
        try:
            num_years = int(input("Enter number of years to be averaged: "))
            if num_years > 0:
                break
            else:
                print("Please enter a POSITIVE non-zero number of years.")
        except ValueError:
            print("Invalid input. Please enter a WHOLE number.")

    # Outer loop - iterates once for each year.
    for year in range(1, num_years + 1):
        print(f"\nYear # {year}:")

        # Inner loop - iterates twelve times, once for each month.
        for month in range(1, 13):
            while True:
                try:
                    rainfall = float(input(f"Enter rainfall for month {month} (in inches): "))
                    if rainfall >= 0:  # Confirm rainfall is not negative.
                        total_rainfall += rainfall
                        num_months += 1
                        break  # Exit inner loop if valid.
                    else:
                        print("Oopsie! Rainfall can't have negative value. Please re-enter.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

    # Calculate and display total # of months, total inches rainfall and
    # average rainfall per month.
    if num_months > 0:  
        average_rainfall = total_rainfall / num_months
        print(f"\nTotal # of months: {num_months}")
        print(f"Total rainfall: {total_rainfall:.2f} inches")
        print(f"Average rainfall per month: {average_rainfall:.2f} inches")
    else:
        print("\nNo rainfall data entered.")


if __name__ == "__main__":
    main()
