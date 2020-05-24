import os
import sys

import configparser


class Provider(object):
    @property
    def config(self):
        config = configparser.ConfigParser()
        config.read(os.path.join(os.getcwd(), '.properties'))
        return config

    def get_properties(self, key):
        try:
            return self.config.get('default', key)
        except (configparser.NoSectionError, configparser.NoOptionError, KeyError):
            print('No config properties found!')
            raise