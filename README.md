# Still Alive

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/pythonpioneer/Still-Alive)
[![PyPI](https://img.shields.io/badge/PyPI-StillAlive-orange?logo=pypi)](https://pypi.org/project/still-alive/)

`Still Alive` is a Python package and **command-line tool** designed to keep your system from going idle by simulating mouse movements at specified intervals. Whether you're giving a presentation, monitoring long-running tasks, or simply want to prevent your screen from locking, `Still Alive` can automate mouse movements and ensure your system stays active.

With `Still Alive`, you can customize when the mouse movements begin and end, as well as the frequency of those movements. The tool is command-line friendly and offers flexible configuration options to suit different scenarios.


## Features

- **Simulates Mouse Movements:** The tool makes slight, random mouse movements to prevent system idle.
- **Customizable Timeframes:** Choose specific start and end times, or define durations (in minutes) to control how long the tool runs.
- **Flexible Interval Control:** Specify how often the mouse moves during the active period.
- **Command-Line Interface:** Easily run and configure the tool from the command line, making it simple to automate.

## Installation

To install the package via `pip`, use the following command:

```bash
pip install still-alive
```

This will install the still-alive package, making it available as a command-line tool on your system.

## Usage

The tool provides flexible options to control the start and end times of the mouse movements, as well as the interval between movements.

### Command-Line Arguments:

`Still Alive` offers several command-line arguments to configure its behavior:

- **`--start-duration / -sd:`** Start time in minutes from the current time. Defaults to `0`, meaning it starts immediately unless otherwise specified.
- **`--end-duration / -ed:`** The end time is specified in minutes from the current time. If not provided, it defaults to `60 minutes`, meaning the execution will run for 1 hour.
- **`--start-time / -st:`** Start time in `HH:MM` (24-hour format). If not provided, the tool will either start immediately or after the specified start duration.
- **`--end-time / -et:`** End time in HH:MM (24-hour format). If `--end-duration` is not provided, the execution will default to 1 hour.
- **`--interval / -i:`** Interval between mouse movements, in seconds. The default is `50 seconds`, but you can set any interval that fits your needs.

### How It Works

Once executed, `Still Alive` begins simulating small mouse movements. The movements are very subtle, with slight, random shifts in the mouse’s position. The tool continues these movements at regular intervals (specified by `--interval`), until the defined end time or duration is reached.

### Example Usage

- Move mouse for 2 hours, starting immediately with a 30-second interval between movements:

    ```bash
    still-alive -ed=120 -i=30
    ```

- Start moving the mouse at 2:00 PM and stop at 6:30 PM:

    ```bash
    still-alive -st=14:00 -et=18:30
    ```

- Start after 10 minutes, run for 1 hour, with default intervals (50 seconds):

    ```bash
    still-alive -sd=10 -ed=60
    ```

- Start after 20 minutes, run unitl 4:40 PM, with 2 minutes interval

    ```bash
    still-alive -sd=20 -et=18:40 -i=120
    ```

- Start moving the mouse for 1 hour, with default interval

    ```bash
    still-alive
    ```

### Important Notes

- You should specify either the `end-time` (`-et`) or `end-duration` (`-ed`). If neither is provided, it will execute for **1 hour**.
- If `start-time` (`-st`) is not provided, the script will **start immediately** or after the duration specified by `start-duration` (`-sd`).
- If you provide both `start-time` (`-st`) and `start-duration` (`-sd`), then `start-time` (`-st`) takes precedence.
- If you provide both `end-time` (`-et`) and `end-duration` (`-ed`), then `end-time` (`-et`) takes precedence.


## Running in the Background

To ensure that the tool continues running even if the terminal is closed, you can run it in the background using `nohup` (`no hang-up`). This is particularly useful if you want to keep your system active while performing long-running tasks:

```bash
nohup still-alive -et=18:00 --interval=60 &
```

This command will run `Still Alive` until 6:00 PM with an interval of 60 seconds between mouse movements. The process will keep running even if you close the terminal.

### Killing the Process

If you've started `Still Alive` as a background process and want to stop it, follow these steps:

1. Find the process ID (PID):

    ```bash
    ps -aux | grep still-alive
    ```

    This will list the active processes, including `still-alive`. Look for the corresponding PID.

2. Use the PID to kill the process:

    ```bash
    kill <PID>
    ```

    Replace `<PID>` with the process ID of `still-alive`.


## LICENSE

This project is licensed under the `MIT License`, allowing for free use, modification, and distribution under permissive terms.

