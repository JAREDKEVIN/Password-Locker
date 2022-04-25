# Password-Locker
An application that will help users manage  passwords and even generate new passwords


## Table of Content

+ [Description](#description)
+ [Setup/Installation Requirements](#setup/installationrequirements)
+ [How To Access the Site](#howtoaccessthesite)
+ [BDD & TDD](#bdd&tdd)
+ [Technology & Tools](#technology&tools)
+ [Reference](#reference)
+ [Known-Bugs](#knownbugs)
+ [Licence](#licence)
+ [Authors Info](#authors-info)

**[Live-Link to site.](https://jaredkevin.github.io/Password-Locker/)**

## Setup/Installation Requirements

### You need to have the following installed
  * Python3.8
  * Pip
  * Pyfiglet
  * Pyperclip
```
 
1. Clone this [github repo] (https://github.com/JAREDKEVIN/Password-Locker)
2. Ensure python is installed on your machine
3. On the terminal for linux or command prompt for windows;
  * Open the containing folder.
  * Run $chmod +x run.py
  * Run ./run.py
4. Follow the instructions to add details.

```

## BDD
| Behaviour                          | Input                                | Output  |
| ---:                               | ---:                                 | ---:    |
| Run the Atarah Passaver App in terminal | chmod +x run.py followed by ./run.py | Runs|
| Asks to either create a account or login | Enter user name | Asks for password |
| Prompts password   | Enter password | Displays a welcome message |
| Lists an option for user interactions| select short code | prompts generated |
| Short code cc - create new credentials | Enter account name and password | user account and password displayed |
| Short code dc- displays accounts | - | Displays a list of accounts created and their passwords|| Short code dd - delete accounts | account and password of app to be deleted| deletes app | 


## TDD

> To test the app, run this command in the terminal;

`$ python3.8 password_test.py`

## Support and contact details

Primary Address: @JAREDKEVIN

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

### License
*MIT License* [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](license/MIT)

Copyright (c) 2022 **Kipkemoi Jared Kevin**


