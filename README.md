# <img width="40" height="40" alt="image" src="https://github.com/user-attachments/assets/bed0a9e9-8b69-4ce2-8d3c-bff94b4954bc" />  Password Telegram Bot


Telegram bot that allows you to generate, manage, associate passwords and save your associations. 
Passwords are stored in the database in encrypted form
> [!NOTE]
> [Link to the bot](https://t.me/pws_generator_bot)

<br>

## Commands
>[!TIP]
> **/start** - start bot
>
> **/help** - display the list of available commands
>
> **/generate** - start generating a new password
>
> **/associate** - associate word with your password
>
> **/change** - change password to your association
>
> **/del** - delete your association
>
> **/del_all** - delete all your associations
>
> **/my** - print your associations

<br>

## How it works?

### Generate and Associate
<img width="600" height="276" alt="Screenshot from 2025-10-11 23-44-10" src="https://github.com/user-attachments/assets/17b290cb-8679-4c5b-973b-4cd7b7560a51" />

 <br>
 <br>
 
### Change Association
<img width="600" height="276" alt="image" src="https://github.com/user-attachments/assets/d68aaa1c-f01e-443d-b8bc-1589fce8520c" />

<br>
<br>

### Delete Association
<img width="600" height="276" alt="image" src="https://github.com/user-attachments/assets/97b8df32-5959-4e54-8e43-31bd412c3df1" />

<br>

## Used Technologies
- Python
  - aiogram 3.22
  - pytest
  - aiosqlite
  - cryptography
- SQLite

<br>

## Architecture
Bot is written using a ***clean architecture***

- Handlers
- Commands and Messages
- Repo

<img width="400" height="400" alt="architecture" src="https://github.com/user-attachments/assets/2241f031-ee50-4e28-ad1e-1c297831ac61" />

<br>

## Structure
<details> <summary>Tree of Dirs/Files</summary>

```  
├── app
│   ├── app.py
│   ├── commands
│   │   ├── association
│   │   │   ├── adder.py
│   │   │   ├── association.py
│   │   │   ├── changer.py
│   │   │   ├── deleter.py
│   │   │   ├── __init__.py
│   │   │   └── printer.py
│   │   ├── commands.py
│   │   ├── default
│   │   │   ├── helper.py
│   │   │   ├── __init__.py
│   │   │   └── starter.py
│   │   ├── __init__.py
│   │   └── password
│   │       ├── __init__.py
│   │       └── password.py
│   ├── errors
│   │   ├── errors.py
│   │   └── __init__.py
│   ├── handlers
│   │   ├── association
│   │   │   ├── adder.py
│   │   │   ├── association.py
│   │   │   ├── changer.py
│   │   │   ├── deleter.py
│   │   │   ├── __init__.py
│   │   │   └── printer.py
│   │   ├── default
│   │   │   ├── help.py
│   │   │   ├── __init__.py
│   │   │   └── start.py
│   │   ├── handler.py
│   │   ├── __init__.py
│   │   ├── message
│   │   │   ├── __init__.py
│   │   │   └── message.py
│   │   ├── password
│   │   │   ├── __init__.py
│   │   │   └── password.py
│   │   └── registrator
│   │       ├── association
│   │       │   ├── adder.py
│   │       │   ├── association.py
│   │       │   ├── changer.py
│   │       │   ├── deleter.py
│   │       │   ├── __init__.py
│   │       │   └── printer.py
│   │       ├── default
│   │       │   ├── default.py
│   │       │   └── __init__.py
│   │       ├── __init__.py
│   │       ├── message
│   │       │   ├── __init__.py
│   │       │   └── message.py
│   │       ├── password
│   │       │   ├── __init__.py
│   │       │   └── password.py
│   │       └── registrator.py
│   ├── __init__.py
│   ├── message
│   │   ├── __init__.py
│   │   └── message.py
│   ├── password
│   │   ├── generator.py
│   │   └── __init__.py
│   ├── repo
│   │   ├── __init__.py
│   │   ├── query
│   │   │   ├── common
│   │   │   │   ├── common.py
│   │   │   │   └── __init__.py
│   │   │   ├── __init__.py
│   │   │   ├── password
│   │   │   │   ├── __init__.py
│   │   │   │   └── password.py
│   │   │   └── user
│   │   │       ├── __init__.py
│   │   │       └── user.py
│   │   ├── repo.py
│   │   └── tables.py
│   └── state
│       ├── __init__.py
│       └── state.py
├── config
│   ├── config.py
│   └── __init__.py
├── Dockerfile
├── LICENSE
├── logger
│   ├── __init__.py
│   └── logger.py
├── main.py
├── migrations
│   ├── 1_create_tables.up.sql
│   ├── 1_drop_tables.down.sql
│   ├── __init__.py
│   └── migrator.py
├── passwords.db
├── README.md
├── requirements.txt
├── test.db
├── tests
│   ├── converter
│   │   ├── fixture.py
│   │   ├── __init__.py
│   │   └── test_converter.py
│   ├── encrypter
│   │   ├── fixture.py
│   │   ├── __init__.py
│   │   └── test_encrypter.py
│   ├── generator
│   │   ├── fixture.py
│   │   ├── __init__.py
│   │   └── test_generator.py
│   ├── __init__.py
│   ├── parser
│   │   ├── fixture.py
│   │   ├── __init__.py
│   │   └── test_parser.py
│   ├── repo
│   │   ├── fixture.py
│   │   ├── __init__.py
│   │   └── test_repo.py
│   └── respondent
│       ├── fixture.py
│       ├── __init__.py
│       └── test_respondent.py
└── utils
    ├── converter.py
    ├── encrypter.py
    ├── __init__.py
    ├── parser.py
    └── respondent.py
```

</details>
