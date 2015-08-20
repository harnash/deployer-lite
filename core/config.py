# -*- coding: utf-8 -*-

import lya
import os


def read(app_name, module_path, custom=None):
    # first we try to load defaults from the package
    config_path = os.path.normpath(module_path + '/config/defaults.yml')
    config = lya.AttrDict.from_yaml(config_path)

    # now we try to load system specifics
    config_path = os.path.normpath('/etc/deployer-lite/{}.yml'.format(app_name))
    if os.path.exists(config_path):
        config.update_yaml(config_path)

    # and user specifics
    config_path = os.path.normpath('~/.deployer-lite.{}.yml'.format(app_name))
    if os.path.exists(config_path):
        config.update_yaml(config_path)

    # and finally custom one if provided
    if custom is not None:
        config_path = os.path.normpath(custom).lstrip('/')
        if os.path.exists(config_path):
            config.update_yaml(config_path)

    return config
