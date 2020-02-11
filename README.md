# EPGP discord bot

The goal of this project is to create a discord bot to visualise and query EPGP standings.

## MVP Design

* The bot will read the `.csv` file uploads from a specified channel (hardcoded to `#epgp-standings-log` for now) and store that as a source of truth
    ** How/where will we store the csv? Should it be parsed and stored into a db? Should we just query the file directly?
* The bot will respond to a single command, `!epgp`. This command will output (with a formatted embed), the current guild EPGP standings sorted by descending PR.

## Installation

`pip install -U discord.py`
`pip install python-dotenv`

## Usage

Create a `.env` file (copy from `.env.template`) and populate it with a discord token.
`python bot.py`