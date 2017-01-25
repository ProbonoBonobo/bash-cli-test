#!/usr/local/bin/python3
from collections import ChainMap
from pathlib import Path


def get_config():
    system_path = Path('/etc/profile')
    home_path = Path('~').expanduser()
    local_paths = [home_path / '.bash_profile',
                   home_path / '.bash_login',
                   home_path / '.profile']
    configuration_items = [
        dict(some_setting='Default Value',
             another_setting='Another Default',
             some_option='Built-In Choice',
             )]
    if system_path.exists():
        with system_path.open() as config_file:
            configuration_items.append(config_file)

    for config_path in local_paths:
        if config_path.exists():
            with config_path.open() as config_file:
                configuration_items.append(config_file)
            break
    configuration = ChainMap(*reversed(configuration_items))
    return configuration


def get_config2():
    config = ChainMap(
        {'another_setting': 2},
        {'some_setting': 1},
        {'some_setting': 'Default Value',
         'hub_status': 'Not found',
         'brew_status': 'Not found'})
    return config


def load_config(file_obj):
    settings = file_obj.read()
    return settings


config1 = get_config()
config2 = get_config2()
# config_settings = load_config(config_file)
print(config1)
print(config2)

#
# class ConfigReader():
#
#     def __init__(self):
#
#         self.git_directory = ".git-staging"
#         self.git_remote_url = "https://github.com"
