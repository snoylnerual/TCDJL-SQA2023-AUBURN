import logging
from datetime import date


'''
def giveMeLoggingObject():
    format_str = '%(asctime)s %(message)s'
    file_name  = 'SIMPLE-LOGGER.log'
    logging.basicConfig(format=format_str, filename=file_name, level=logging.INFO)
    loggerObj = logging.getLogger('simple-logger')
    return loggerObj
'''

def createLoggerObj(): 
    fileName  = date.today().strftime('%Y-%m-%d') + '_Project.log' 
    formatStr = '%(asctime)s %(message)s'
    logging.basicConfig(format=formatStr, filename=fileName, level=logging.INFO)
    myLogObj = logging.getLogger('sqa2023-logger') 
    return myLogObj