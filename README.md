### About
Python utility to automatically accepts League of Legends matches.

### Dependencies
You need Python 3.x.x\
Then you need to download the repository and then update the dependencies
```bash
git clone https://github.com/Santti4go/lobby-finder.git
pip install -r requirements.txt
```

### How to
Just launch the program while League of Legends is looking for a game and press the 'Search for lobby' button. \
Leave the game in foreground and once a match is found, the program will accept it.
If you want to stop the program before a game has been found, press 'Stop searching lobby'.


### Program layout
<p align="center">
  <image src="assets/main_window.png" alt="Program layout"
  caption="Program layout">
</p>


### To build the app
This is only necessary if you want to generate an `.exe` file.
The easiest way to build the entire app into a single executable is using `pyinstaller`.

pyinstaller --add-data 'assets;assets' lobby_finder.py --onefile -y
