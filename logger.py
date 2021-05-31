from datetime import datetime
import os
import time
import logging

class Logger:
    currentlyLogging = False
    def createLogsDirectory(self):
        logsDirExists = os.path.isdir('./logs')
        print(str(datetime.now()) + " Logs directory exists: " + str(logsDirExists))
        if logsDirExists == False:
            print(str(datetime.now()) + " Running createLogsDirectory Fxn")
            newDir = './logs'
            os.mkdir(newDir)
            print(str(datetime.now()) + " Logs directory created")

    def createNewLogFile(self):
        print(str(datetime.now()) + " Running createNewLogFile Fxn")
        currentDateTime = datetime.now()
        formattedDT = currentDateTime.strftime("%m-%d-%y_%H-%M-%S")
        print('Formatted datetime: ' + formattedDT)
        directoryForFile = './logs'
        fileName = formattedDT + '.txt'
        with open(os.path.join(directoryForFile, fileName), 'w') as fp:
            pass
            # fp.write("testing")
        return directoryForFile + '/' + fileName

    def startLogging(self, fileToLogTo):
        print(str(datetime.now()) + " Running startLogging Fxn")
        if self.currentlyLogging == False:
            logging.basicConfig(filename=fileToLogTo, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
            self.currentlyLogging = True
            print(str(datetime.now()) + " Logging has been enabled")

    def stopLogging(self):
        print(str(datetime.now()) + " Running stopLogging Fxn")
        if self.currentlyLogging == True:
            logging.disable(logging.CRITICAL)
            self.currentlyLogging = False
            print(str(datetime.now()) + " Logging has been disabled")

    def writeLine(self, lineToWrite):
        if self.currentlyLogging == True:
            logging.debug(lineToWrite)
        print(str(datetime.now()) + " " + lineToWrite)

logger = Logger()