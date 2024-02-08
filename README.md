### About
Python utility to automatically accept League of Legends matches.
Useful when you want to go for a glass of water while on queue :wink:

https://github.com/Santti4go/lobby-finder/assets/95138114/c33da9dd-6de1-443e-93a8-85532fad7fc8

### Installation
If you just want to go ahead and use it, feel free to download the [`lobby_finder.exe`](dist/lobby_finder.exe) and jump right into [how to use it](#How-to-use-it). If you will like to inspect the code then go to [dependencies](#Dependencies) section first.

Languages supported:
* English.
* Spanish

### Dependencies
You need Python 3.x.x\
Then you need to download the repository and then update the dependencies
```bash
git clone https://github.com/Santti4go/lobby-finder.git
pip install -r requirements.txt
```

### How to use it
Just launch the program while League of Legends is looking for a game and press the 'Search for lobby' button. \
Leave the game in foreground and once a match is found, the program will accept it.
If you want to stop the program before a game has been found, press 'Stop searching lobby'.


### Program layout
<p align="center">
  <image src="doc/main_window.png" alt="Program layout"
  caption="Program layout">
</p>


### To build the app
This is only necessary if you want to generate an `.exe` file.
The easiest way to build the entire app into a single executable is using `pyinstaller`.

```bash
pyinstaller --add-data 'assets;assets' lobby_finder.py --onefile -y
```
