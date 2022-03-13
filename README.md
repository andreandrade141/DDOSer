# DDOSer

## Description

This program is designed as a testbed for Direct Denial of Service attacks(DDOS) studies. This idea came to me when i was developing a script for testing URLs for my job. The basic functioning of this script is: It´s input is a json of URLs, and the output is a log of the operation.
To see more about each module and it´s functioning, just enter the docs folder here [Docs](/src/docs).
The JSON structure have the key as the name of the website and the value as the URL.

## Project Structure

- /src -> Folder where all logic is stored.
- /src/docs -> Documentation for each module.
- /src/modules -> Where all the modules and working bits are installed.
- /log -> Output folder for the logs.
- /main.py -> Config/start file.
- /requirements.txt -> Pip install file.
- /README.md -> All info about this project.
- /LICENSE -> Information about project license.
- /gitignore -> Git ignore file.
- /list.json -> JSON where the url is located.

## Changelog

- Version 0.1.0
  First version. Only implements the basic functioning of the project.
