import requests
import configuration

config = configuration.load_config()

base_url = 'https://api.telegram.org/bot' + config.token

if __name__ == "__main__":
    response = requests.get(base_url + '/getMe')
    print(response.content)
