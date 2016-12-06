## 2048 for the Command-Line

This is a command-line version of [2048](http://gabrielecirulli.github.io/2048/). 
There's a little more documentation [here on my site](http://www.johnloeber.com/docs/2048.html).

![screenshot](http://johnloeber.com/images/gamescreenshot.png)

## Details

- After cloning this repo, `cd` into it in your terminal, and type `python game2048.py` to run it.
- This is written in Python 2.7 using standard libraries only.
- The game tries to save your top score in a file in your home directory: `~/.2048.txt`.

The core logic is currently in `newboard`, an enormously ugly function in which I hardcoded a cascading fold.
[Geoff Shannon](http://github.com/RadicalZephyr) supplied a superior function, `use-later/fold.ml`, which I still need to incorporate
or replicate in the main script.
