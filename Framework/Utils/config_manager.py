import json
import pathlib


class ConfigManager:

    @staticmethod
    def get_driver_conf():
        with open(pathlib.Path(__file__).parent.joinpath('config.json'), 'r', encoding='utf-8') as conf:
            browser_config = {k: v.lower().strip() if isinstance(v, str) else v for k, v in json.load(conf).items()}

        return browser_config

    @staticmethod
    def get_test_data():
        with open(pathlib.Path(__file__).parent.joinpath('test_data.json'), 'r', encoding='utf-8') as data:
            test_data = json.load(data)

        return test_data
