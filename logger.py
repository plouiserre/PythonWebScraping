#Not perfect system log, but I prefer keep it simple for now 
import logging 

class Logger :
    def __init__(self, levelApp, formatApp, encodingApp, fileNameApp) :
        self.logging = logging
        logging.basicConfig(format =formatApp ,filename=fileNameApp, encoding=encodingApp, level=levelApp)
    
    
    def Log_Debug_Level(self, message) :
        self.logging.debug(message)


    def Log_Info_Level(self, message) :
        self.logging.info(message)


    def Log_Warning_Level(self, message) : 
        self.logging.warning(message)


    def Log_Error_Level(self, message) :
        self.logging.error(message)