def convert(time_str):
    # Split the input time string by colon to separate hours and minutes
    hours, minutes = time_str.split(":")
    # Convert hours and minutes to integers
    hours = int(hours)
    minutes = int(minutes)
    # Calculate the total time in hours as a float
    total_hours = hours + minutes / 60
    return total_hours

def main():
    # Prompt the user for the time
    time_str = input("Enter the time (in 24-hour format as #:## or ##:##): ")

    # Convert the time to hours as a float
    time_in_hours = convert(time_str)

    # Determine if it's breakfast time, lunch time, or dinner time
    if 7 <= time_in_hours <= 8:
        print("breakfast time")
    elif 12 <= time_in_hours <= 13:
        print("lunch time")
    elif 18 <= time_in_hours <= 19:
        print("dinner time")

if __name__ == "__main__":
    main()