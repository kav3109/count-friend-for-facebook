# count-friends-for-facebook
Project for counting your friends on your page of Facebook 
-------------
## Description of project

Essence of this small test is that when you open page with your friends you may see only no more 20 people. In duty of the test is sclolling page down and load all friends. Then it counting all block with loaded friends and compare with counter of Facebook.   

## Structure of project

`/core`  - folder with configiration file, tools and elements

`/tests` - folder with test steps and test cases

## Installation
* Windows 7 64 or 32-bit
* Python 3.6.5 - [https://www.python.org/downloads/]
* Selenium - Python 3.6 has pip available in the standard library. Start a command prompt using the cmd.exe program and run the pip command as given below: 

   `C:\Python35\Scripts\pip.exe install selenium`
* ChromeDriver - needs to be installed from [https://sites.google.com/a/chromium.org/chromedriver/downloads]. 
Make sure it’s in your PATH, e. g., place it in /usr/bin or /usr/local/bin.
* Chrome Browser version 65.0.3325.181 - [https://www.google.com/chrome/]
* Pytest framework - run the following command in your command line:
   
   `C:\Python35\Scripts\pip.exe install -U pytest`
* PyCharm community - needs to be installed from [https://www.jetbrains.com/pycharm/download/#section=windows]
* Git - install from [https://git-scm.com/downloads]

## Starting of the test
* Before launching test you must set parameters of Login and Password of your user in config of project
  `\count-friends-for-facebook\core\config.py`
  
* Launch file:
  `\count-friends-for-facebook\tests\test_count_friends.py`
