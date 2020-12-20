import yaml, os


class Config:
    def __init__(self, token: str, clients: set[str]):
        self.token = token
        self.clients = clients


def load_config(
        config_dir: str = "../config/",
        config_file: str = "application.yaml",
        secrets_file: str = "secrets.yaml",
):
    dirname = os.path.join(os.path.dirname(__file__), config_dir)
    config = load_from_file(dirname + config_file)
    secrets = load_from_file(dirname + secrets_file)
    return Config(secrets["bot"]["token"], config["bot"]["allowed_clients"])


def load_from_file(file: str):
    with open(file) as f:
        return yaml.safe_load(f)
