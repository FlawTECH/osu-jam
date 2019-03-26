# osu! jam
osu! jam is a tool used to extract all songs from a given osu! installation and copies them over to a directory of your choice. It also tries to find the best suitable title for the audio files based on the parent directory and the file metadata.

[Requirements](#requirements)  
[Installation](#installation)  
[Usage](#usage)  
[Contributing](#contributing)

## Requirements
* Python 3.x

## Installation
'Installing' this is as simple as it gets :
```
git clone https://gitlab.com/FlawTECH/osu-jam.git
```

## Usage
```
osujam.py [-h] osu_src dest

Extracts songs from the game osu! and copies them over to your preferred
folder.

positional arguments:
  osu_src     root folder in which osu! is installed
  dest        folder in which the files will be copied into

optional arguments:
  -h, --help  show this help message and exit
```

### Example
```
osujam.py "C:\Games\osu!" "C:\Users\John\Music"
```
In this example, osu! is installed under `C:\Games\osu!` (the osu!.exe executable is inside this directory) and the songs will be copied to `C:\Users\John\Music`

## Contributing
Feel free to contribute to this project as it obviously lacks a lot of features. No guidelines at the moment.