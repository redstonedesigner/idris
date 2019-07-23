from yaml import load, dump

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

def getConfig():
    with open("../config.yml","r") as file:
        config = file.read()
        file.close()
    return config
