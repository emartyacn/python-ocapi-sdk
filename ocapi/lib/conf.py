import os
import sys

import configparser

import logging


class Provider(object):

    @property
    def config(self):
        config = configparser.ConfigParser()
        if len (config.read(os.path.join(os.getcwd(), '.properties'))) == 0:
            return None
        else:
            return config

    def get_properties(self, key):
        if self.config == None:
            return
        else:
            try:
                return self.config.get('default', key)
            #except (configparser.NoSectionError, configparser.NoOptionError, KeyError):
            except:
                logging.exception('\n\nProperties file found however configs could not be determined\n\n')