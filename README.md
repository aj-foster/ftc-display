# FTC Scoring Display Setup

_Automatically launch an FTC Live field timer display on a Raspberry Pi._

---

It may seem silly, but manually walking over and plugging in a keyboard/mouse to a Raspberry Pi in order to set up a field timer display is a hassle.
We have better things to do during setup.
So for the handful of people in the world that use a Raspberry Pi as their field timers for _FIRST_ Tech Challenge competitions, here's a solution.

## Usage

This repository comes with a few assumptions:

1. You use a Raspberry Pi as a field timer
2. You have a consistent IP address for your FTC Live scoring computer
3. You know ahead of time which field (1 or 2) the Pi will be on
4. Your Pi automatically logs in to a default user named `pi`

Given all of this, you can run `setup.sh` to get all of the files arranged correctly.
(Change all mentions of the path `/home/pi` if your user is named differently.)

The setup script installs two files:

1. `/home/pi/ftc-scoring-display.py`, the script that does the actual work.
  **Note**: There are required changes in this file!
2. `/home/pi/.config/autostart/ftc-scoring-display.desktop`, the configuration that runs the script once the user logs in.

By their powers combined, Chromium will start automatically on login and show a field display for the currently-active event in FTC Live.

Be sure to change the `SCORING_ADDRESS` and `FIELD_NUMBER` constants at the top of the python script.

Happy hosting!

## Acknowledgments

_FIRST®_ and _FIRST_ Tech Challenge (formerly also known as FTC®) are trademarks of For Inspiration and Recognition of Science and Technology (_FIRST_).
This project is not affiliated with _FIRST_ and _FIRST_ provides no warranty or support.
