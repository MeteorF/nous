
# coding: utf-8

# In[1]:


# logger_helper/class_logger
# Last modify: 20181104


# In[2]:


# from ../../modules

# from ext lib
import logging


# In[3]:


class logger():
    #------------
    # Log Level:
    #   debug (lowest)
    #   info
    #   warning
    #   error
    #   critical (highest)
    #-----------
    
    def __init__(self, args):
        self.logfileName = args.get("logFileName")
        #logfileName = logFilePath
        
        global logging
        logging = logging
        
        logging.basicConfig(
            # filename = logfileName, \
            handlers = [logging.FileHandler(self.logfileName, 'a', 'utf-8')], \
            
            # Will ignore levels lower than setting (e.g. set=info will ignore debug)
            level = logging.DEBUG, \
            format = '%(asctime)s | %(levelname)s | %(processName)s | %(module)s | %(funcName)s | %(lineno)s | %(message)s'
            
            # Example: 2018-11-05 19:53:36,275 | INFO | class_logger.py | start | 59 | -------Start of program-------
            # To parse timestamp in pandas:
            #        pd.to_datetime('2018-11-05 00:12:33,585', format="%Y-%m-%d %H:%M:%S,%f")
            # return: Timestamp('2018-11-05 00:12:33.586000')
            
            #datefmt = '%Y-%m-%d %H:%M:%S'
            # Example: 2018-11-05 19:53:36 | INFO | class_logger.py | start | 59 | -------Start of program-------
        )
        self.start()
    
    def getCaller(self):
        caller = str(logging.getLogger(__name__))
        return caller
    
    def start(self):
        logging.info(self.getCaller() + ' | ' + 'Start of program'.center(30, '-'))
        
    def log_debug(self, msg=''):
        logging.debug(self.getCaller() + ' | ' + msg)
        
    def log_info(self, msg=''):
        logging.info(self.getCaller() + ' | ' + msg)
        
    def log_warning(self, msg=''):
        logging.warning(self.getCaller() + ' | ' + msg)
        
    def log_error(self, msg=''):
        logging.error(self.getCaller() + ' | ' + msg)
        
    def log_critical(self, msg=''):
        logging.critical(self.getCaller() + ' | ' + msg)
    
    def shutdown(self):
        logging.info(self.getCaller() + ' | ' + 'End of program'.center(30, '-'))
        logging.shutdown()
        
    def printLogString(self):
        print (f'logFileName = {self.logfileName}')
        with open(self.logfileName, 'r') as f:
            print(f.read())


# In[4]:


# Test function for module  
def _test():
    # test loadconfig & change cwd
    
    import sys
    sys.path.append('../../modules')
    
    import json
    import path_helper
    import config_helper
    
    global __config__
    config_file = 'C:/Users/alana/AnacondaProjects/nous/settings/config.json'
    
    if path_helper.dir_check(dir_check=config_file) == True:
        config_file_path = path_helper.dir_check(config_file, dir_create=False, return_type='Path')
    
        with open(config_file_path) as f:
            # Read json as dictionary
            __config_string__ = json.load(f)

            __config__ = config_helper.global_config(__config_string__)
            
            path_helper.chdir(__config__.PROJ_DIR)
    
    # init logger and test log msg
    
    global logger_1
    logFileName = path_helper.getOutputFileName(path=__config__.LOG_DIR, custom_name='log', extension='.log')
    config_log = {
        "logFileName" : logFileName
    }
    
    logger_1 = logger(config_log)
    
    logger_1.log_debug('-----debug-----')
    logger_1.log_info('-----info-----')
    logger_1.log_warning('-----warning-----')
    logger_1.log_error('-----error-----')
    logger_1.log_critical('-----critical-----')
    
    logger_1.shutdown()
    
    
    #print (f'logFileName = {logFileName}')
    #with open(logFileName, 'r') as f:
    #    print(f.read())
    
    logger_1.printLogString()
    
if __name__ == '__main__':
    _test()

