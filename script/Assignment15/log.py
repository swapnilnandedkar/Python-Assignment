"""
    Logger class with static method to log data inside 'Log.txt'
"""

class Logger:
    logFileName = 'Log.txt'
    fileDescripter = None
    
    @staticmethod
    def openLogFile():
        Logger.fileDescripter = open(Logger.logFileName,'w')

    @staticmethod
    def writeLog(data):
        Logger.fileDescripter.write(data+'\n')
    
    @staticmethod
    def closeLogFile():
        Logger.fileDescripter.close()
