import os

try:
    import configparser
except ImportError:
    import ConfigParser as configparser


def create_config(path):
    config = configparser.ConfigParser()
    config.add_section('Tickpanel')
    config.set('Tickpanel', 'sumticks_period', '777')

    with open(path, 'w') as config_file:
        config.write(config_file)


def get_config(path):
    if not os.path.exists(path):
        create_config(path)

    config = configparser.ConfigParser()
    config.read(path)
    return config


def get_setting(path, section, setting):
    config = get_config(path)
    value = config.get(section, setting)
    return value


def update_setting(path, section, setting, value):
    config = get_config(path)
    config.set(section, setting, value)
    with open(path, 'w') as config_file:
        config.write(config_file)


def delete_setting(path, section, setting, value):
    config = get_config(path)
    config.remove_option(section, setting)
    with open(path, 'w') as config_file:
        config.write(config_file)
