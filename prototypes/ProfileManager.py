#!/usr/bin/python
'''
author: Christian M
'''
from os import walk
from os.path import basename, splitext

class ProfileManager(object):
    
    def __init__(self, serviceRunner, widgetRunner):
        self.servivceRunner = serviceRunner
        self.widgetRunner = widgetRunner
        self.current = "Default"

    def init(self):
        self.loadDefault()

    def load(self, profileName):
        fileName = profileName+".json"
        self.servivceRunner.stopServices()
        self.servivceRunner.configServices(fileName)
        self.servivceRunner.initServices(fileName)
        self.servivceRunner.startServices(fileName)

        self.widgetRunner.stopWidgets()
        self.widgetRunner.configWidgets(fileName)
        self.widgetRunner.initWidgets(fileName)
        self.widgetRunner.startWidgets(fileName)
        self.current = profileName

    def all(self):
        f = []
        for (dirpath, dirnames, filenames) in walk("."):
            for file in filenames:
                if file.endswith(".json"):
                    f.append(splitext(basename(file))[0])
            break
        return f

    def loadDefault(self):
        self.load("Default")