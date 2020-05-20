import os
import sys

import configparser


class Provider(object):
    @property
    def config(self):
        config = configparser.ConfigParser()
        config.read(os.path.join(os.getcwd(), '.credentials'))
        return config

    def get_credential(self, key):
        try:
            return self.config.get("credentials", key)
        except (configparser.NoSectionError, configparser.NoOptionError, KeyError):
            print('No credentials found!')
            raise