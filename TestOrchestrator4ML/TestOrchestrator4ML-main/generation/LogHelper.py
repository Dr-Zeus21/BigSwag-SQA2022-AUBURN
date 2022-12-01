import logging

def getSQALogger():
    logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
    loggerOBJ = logging.getLogger('SQA-Logger')
    return loggerOBJ