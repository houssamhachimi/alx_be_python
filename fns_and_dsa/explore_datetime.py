# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in 'YYYY-MM-DD HH:MM:SS' format.
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date(days_to_add):
    """
    Calculates the future date after adding the given number of days to the current date.
    
    Parameters:
        days_to_add (int): Number of days to add to the current date.
    
    Returns:
        None
    """
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_to_add)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

def main():
    display_current_datetime()
    
    try:
        days_input = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days_input)
    except ValueError:
        print("Please enter a valid integer for the number of days.")

if __name__ == "__main__":
    main()
