# -*- coding: utf-8 -*-
"""Module 5: Critical Thinking - Colin Tenaglia

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hNlg0SIIS5EFCyH9uktTdmQdZ5O1IJR4

###**Pseudo-Code**
**Start**
- **Define** function: average_rainfall
- **Prompt** the user to enter the number of years
- **Initialize** total_inches to 0
- **Calculate** total_months as years multiplied by 12

- For each year from 1 to years
  - **Print** the current year number
- For each month from 1 to 12
   - **Prompt** the user to enter the rainfall in inches for the current month
   - **Add** the rainfall to total_inches
   - **Calculate** average_rainfall as total_inches divided by total_months

- **Print** total_months
- **Print** total_inches
- **Print** average_rainfall

**End**

###**Source Code**
"""

def average_rainfall():
    # Ask for the number of years
    years = int(input("Enter the number of years: "))

    total_inches = 0
    total_months = years * 12  # Total months

    # Loop through each year
    for year in range(1, years + 1):
        print(f"\nYear {year}")
        # Loop through each month of the current year
        for month in range(1, 13):
            # Get the rainfall for the month
            rainfall = float(input(f"Enter the inches of rainfall for month {month}: "))
            total_inches += rainfall

    # Calculate the average rainfall per month
    average_rainfall = total_inches / total_months

    # Display results
    print("\nRainfall Statistics:")
    print(f"Total number of months: {total_months}")
    print(f"Total inches of rainfall: {total_inches:.2f}")
    print(f"Average rainfall per month: {average_rainfall:.2f} inches")

# Call the function to execute
average_rainfall()

"""### **Pseudo-Code**
**Start**
- **Define** function: **book_club_points_accumulator**
- **Prompt** the user to enter the number of months to record purchases
- **Initialize** total_points to 0

  - **For** each month from 1 to number_of_months
    - **Prompt** the user to enter the number of books purchased in month {month}
    - **Initialize** points to 0

    - **If** books_purchased >= 8
      - **Set** points to 60
    - **Else if** books_purchased >= 6
      - **Set** points to 30
    - **Else if** books_purchased >= 4
      - **Set** points to 15
    - **Else if** books_purchased >= 2
      - **Set** points to 5
    - **Else**
      - **Set** points to 0

    - **Add** points to total_points
    - **Print** "Month {month}: Points awarded = {points}"

- **Print** "Total points for {number_of_months} months: {total_points}"

**End**

"""

def book_club_points_accumulator():
    # Prompt the user for the number of months
    number_of_months = int(input("Enter the number of months to record purchases: "))
    total_points = 0  # Initialize total points

    # Process each month
    for month in range(1, number_of_months + 1):
        # Ask for the number of books purchased this month
        books_purchased = int(input(f"Enter the number of books purchased in month {month}: "))
        points = 0  # Initialize points for the current month

        # Calculate points based on the number of books purchased
        if books_purchased >= 8:
            points = 60
        elif books_purchased >= 6:
            points = 30
        elif books_purchased >= 4:
            points = 15
        elif books_purchased >= 2:
            points = 5
        else:
            points = 0

        # Add the points for this month to the total points
        total_points += points

        # Print the points for this month
        print(f"Month {month}: Points awarded = {points}")

    # Print the total points after all months have been processed
    print(f"Total points for {number_of_months} months: {total_points}")

# Call the function to execute
book_club_points_accumulator()

