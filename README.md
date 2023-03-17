# Game Night Bot

## Overview
This bot is designed to help make hosting a TTRPG server easier, with timestamped echoing of when the next session will be in a timezone agnostic fashion! Never be confused about when the next game will be!

## Usage
| Command     | Description                                                                                                                                                        | 
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| /whenisgame | Retrieves a list of the games currently stored, including their timezone converted date and interval                                                               |
| /add_game   | Adds a new game to the database, taking in basic datetime data, days before next repetition, and timezone you are adding this ***from***. eg, `Australia/Melbourne`. |
| /remove_game | Removes a game from the list based on the ID provided by whenisgame                                                                                                |

## Credits
Template provided by https://github.com/kkrypt0nn/Python-Discord-Bot-Template and is used in compliance with their requirements.
Use this bot wherever you want, I don't care. Just don't wholesale copy it and pretend it's yours. Creative Commons applies.