# telegram-bot

## Prerequisites
* [pyenv](https://github.com/pyenv/pyenv#installation) — for managing Python versions
* [pipenv](https://pipenv.pypa.io/en/latest/#install-pipenv-today) — for managing dependencies

## Usage
* `make shell` — installs dependencies and runs virtual environment
* `make test` — runs tests
* `make run` — runs the application

## Configuration
The application expects file `secrets.yaml` inside the configuration folder with the following structure:
```
bot:
  token: <telegram_bot_token>
```
where `<telegram_bot_token>` is an access token of your Telegram bot