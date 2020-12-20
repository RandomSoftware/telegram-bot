import unittest
import src.configuration as configuration


class ConfigurationTest(unittest.TestCase):

    def setUp(self):
        self.config = configuration.load_config(config_dir="../tests/fixtures/config/")

    def test_load_token(self):
        self.assertEqual(self.config.token, "secret_bot_token")

    def test_load_clients(self):
        self.assertCountEqual(self.config.clients, ["foo", "bar"])


if __name__ == '__main__':
    unittest.main()
