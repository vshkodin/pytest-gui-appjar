from configparser import ConfigParser


configConfig = ConfigParser()
configPytest = ConfigParser()
configConfig.read('config.ini')
configPytest.read('pytest.ini')
