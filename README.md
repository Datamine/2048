## 2048 for the Command-Line

This is a command-line version of [2048](http://gabrielecirulli.github.io/2048/). 

![screenshot](http://johnloeber.com/images/gamescreenshot.png)

Try to get to 2048. On every turn, a new number, either 2 or 4, spawns. It is marked in bold. 
If you're a vim-user, then you can also use `h, j, k, l` instead of the arrow keys.

## Details

- After cloning this repo, `cd` into it in your terminal, and type `python game2048.py` to run it.
- This is written in Python 2.7 using standard libraries only.
- The game tries to save your top score in a file in your home directory: `~/.2048.txt`.
