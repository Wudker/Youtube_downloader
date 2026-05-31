# Vivaldi – YouTube Downloader GUI

## Description

Vivaldi is a simple Python desktop application created for downloading YouTube videos through a graphical user interface.

The application allows the user to paste a YouTube link, select the desired output format and choose where the downloaded file should be saved. The main goal of the project was to create a small and convenient downloader with a simple interface instead of using command-line tools.

The program was developed as a practical Python utility using GUI libraries, file handling and external media tools.

## Features

* YouTube link input
* Graphical user interface
* MP3 download option
* MP4 download option
* Custom output folder selection
* Quick save to Desktop
* Automatic USB folder search
* Basic filename sanitization
* Download status messages
* Dark mode interface

## Software

* Python
* Tkinter
* CustomTkinter
* pytube
* unidecode
* FFmpeg support for media conversion
* pathlib and os for file path handling

## Application operation

The user pastes a YouTube link into the input field, selects the preferred file type and chooses the output directory.

The application can save files to a manually selected folder, directly to the Desktop or to a detected USB drive containing a folder named `muzyka`.

Before downloading, the program checks whether the link, output type and save location were selected correctly.

## Main functions

* Downloading YouTube content
* Selecting output format
* Selecting destination folder
* Detecting external drive folder
* Cleaning video titles before saving
* Displaying basic download feedback in the GUI

## Challenges

Main development challenges:

* creating a simple and readable GUI,
* handling different save locations,
* detecting folders on external drives,
* preparing filenames safe for saving,
* connecting the GUI with downloading logic,
* adding support for media conversion.

## Current status

Working prototype built and tested.

Future improvements:

* improved error handling,
* progress bar during download,
* better MP3 conversion workflow,
* more portable icon path,
* option to select audio quality,
* preventing duplicate downloads when multiple formats are selected,
* packaging the application as an executable file.

## About

Simple Python GUI YouTube downloader built with CustomTkinter, supporting MP3/MP4 download options, filename sanitization and selectable output folders.

## Note

This project is intended for educational and personal use. Downloading media should be done only when the user has the right to access and save the content.
