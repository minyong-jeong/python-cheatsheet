'''
- config.ini

[LOG]
path = /path/to/test.log
'''

import configparser


class App:
    __conf = None

    @staticmethod
    def config():
        if App.__conf is None:
            App.__conf = configparser.ConfigParser()
            App.__conf.read('config.ini')
        return App.__conf


if __name__ == "__main__":
    c = App.config()
    print(c['LOG']['path'])
