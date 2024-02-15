import os
from os import environ



class Utils:
    @staticmethod
    def addToPathIfNotExists(envVariable):
        if environ.get(envVariable) is not None:
            # print(os.pathsep)
            os.environ["PATH"] += os.pathsep + os.path.abspath(envVariable)


