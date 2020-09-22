# FYP
In this project, I am attempting to create a  GRAPHICAL USER AUTHENTICATION SYSTEM that will be resilient to different types of attacks.

## Installation
### Windows
1. Download from [Python](https://www.python.org/downloads/)

    a. Pick version 3.8.X (replace x with the highest number displayed)

    b. Be sure to check you're downloading the right python version for your system (64bit vs 32bit)

2. Open Python Installer (likely in Downloads):

   a. Tick/Select Add Python 3.8 to PATH

   b. Select Customize Installation (this is important) Tick/Select pip (others, leave as default) Hit next

   c. Tick/Select:

        - Install for all users
        - Add Python to environment variables
        - Create shortcuts for installed applications
        - Precomplie standard libary
        - Customize Install Location and use: C:\Python38 Hit Install

3. Verify Python Installed in Powershell

    a. Open Windows Powershell
    Type: ```python -V ```and hit enter.

   If typing python -V fails, try:
    * Restart Computer
    * Uninstall python and redo step 2 above.

5. Verify pip by entering:
```bash
    pip freeze
```

4. Update Powershell Settings:

You should only have to do this 1 time, if done correctly.

    - Search Windows Powershell

    - Right click, select Run as Administrator

    - Enter: Set-ExecutionPolicy Unrestricted

5. Create Dev Folder (directory):

    Open Windows Powershell
    Type:
```
    C:\ > cd ~/
    C:\ > mkdir Dev
```
6. Install [Pipenv](https://pypi.org/project/pipenv/):

   To install a Pipenv as our virtual environment manager:

   ``` python -m pip install pipenv```

### MacOS, you can install Pipenv easily with Homebrew:
```
$ brew install pipenv
```
### Debian Buster+
```
$ sudo apt install pipenv
```
### When none of the above is an option:
```
$ pip install pipenv
```

## Usage

```bash

cd FYP
pipenv shell
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[GNU General Public License v3.0](https://github.com/mahrous-amer/FYP/blob/master/LICENSE)
