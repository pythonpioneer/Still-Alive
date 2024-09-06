import datetime
import time
import pyautogui
import random
import argparse

def move_mouse_slightly():
    # Get the current mouse position
    x, y = pyautogui.position()

    # Generate small random offsets
    dx = random.randint(-1, 1)
    dy = random.randint(-1, 1)

    # Move the mouse to the new position
    pyautogui.moveTo(x + dx, y + dy)
    print('Executed!')


def recursive_function(end_time, interval):
    # Get the current time
    current_time = datetime.datetime.now().time()

    # Check if the current time has reached the end time
    if current_time >= end_time:
        print("Time reached! Exiting recursion.")
        return

    # Move the mouse slightly
    move_mouse_slightly()

    # Wait for the specified interval before the next call
    time.sleep(interval)

    # Call the function recursively
    recursive_function(end_time, interval)


def parse_time_arg(time_str):
    """Parse a time string in 'HH:MM' format into a time object."""
    try:
        return datetime.datetime.strptime(time_str, '%H:%M').time()
    except ValueError:
        raise argparse.ArgumentTypeError(f"Invalid time format: '{time_str}'. Expected HH:MM format.")


def main():
    # Create an argument parser
    parser = argparse.ArgumentParser(description="Move mouse slightly within a specified time range.")

    # Add arguments for start duration, end duration, start time, and end time
    parser.add_argument('-sd', '--start_duration', type=int, help="Start duration in minutes from now", default=0)
    parser.add_argument('-ed', '--end_duration', type=int, help="End duration in minutes from now")
    parser.add_argument('-st', '--start_time', type=parse_time_arg, help="Start time in 24-hour format (HH:MM)", required=False)
    parser.add_argument('-et', '--end_time', type=parse_time_arg, help="End time in 24-hour format (HH:MM)", required=False)

    # Add the interval argument (how often to move the mouse)
    parser.add_argument('-i', '--interval', type=int, default=50, help="Interval between movements in seconds (default: 50 seconds)")

    args = parser.parse_args()

    # Custom validation: either end_time (et) or end_duration (ed) is required
    if not args.end_time and not args.end_duration:
        parser.error("Either --end_time (-et) or --end_duration (-ed) is required.")

    # Calculate the start and end times based on the provided arguments
    current_time = datetime.datetime.now()

    if args.start_time:
        start_time = datetime.datetime.combine(current_time.date(), args.start_time)
    else:
        start_time = current_time + datetime.timedelta(minutes=args.start_duration)

    if args.end_time:
        end_time = datetime.datetime.combine(current_time.date(), args.end_time)
    elif args.end_duration:
        end_time = current_time + datetime.timedelta(minutes=args.end_duration)

    # Ensure that the start time is before the end time
    if start_time >= end_time:
        raise ValueError("Start time must be before end time.")

    # Wait until the start time if it's in the future
    time_diff = (start_time - current_time).total_seconds()
    if time_diff > 0:
        print(f"Waiting for {time_diff // 60} minutes to start...")
        time.sleep(time_diff)

    # Call the recursive function with the specified interval
    print(f"Starting mouse movement at {start_time.time()} until {end_time.time()} with {args.interval}-second intervals.")
    recursive_function(end_time.time(), args.interval)


if __name__ == "__main__":
    main()
