
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
        logfileName = args.get("logFileName")
        #logfileName = logFilePath
        
        global logging
        logging = logging
        
        logging.basicConfig(
            # filename = logfileName, \
            handlers = [logging.FileHandler(logfileName, 'a', 'utf-8')], \
            
            # Will ignore levels lower than setting (e.g. set=info will ignore debug)
            level = logging.DEBUG, \
            format = '%(asctime)s | %(levelname)s | %(message)s'
            
            # Example: 2018-11-05 00:12:33,585 | INFO | -------Start of program-------
            # To parse timestamp in pandas:
            #        pd.to_datetime('2018-11-05 00:12:33,585', format="%Y-%m-%d %H:%M:%S,%f")
            # return: Timestamp('2018-11-05 00:12:33.586000')
            
            #datefmt = '%Y-%m-%d %H:%M:%S'
            # Example: 2018-11-05 00:12:33 | INFO | -------Start of program-------
        )
        self.start()
    
    def start(self):
        logging.info('Start of program'.center(30, '-'))
        
    def log_debug(self, msg=''):
        logging.debug(msg)
        
    def log_info(self, msg=''):
        logging.info(msg)
        
    def log_warning(self, msg=''):
        logging.warning(msg)
        
    def log_error(self, msg=''):
        logging.error(msg)
        
    def log_critical(self, msg=''):
        logging.critical(msg)
    
    def shutdown(self):
        logging.info('End of program'.center(30, '-'))
        logging.shutdown()


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
    
    config_log = {
        "logFileName" : path_helper.getOutputFileName(
                            path = __config__.LOG_DIR,
                            custom_name='log',
                            extension='.log'
                        )
    }
    
    logger_1 = logger(config_log)
    
    logger_1.log_debug('-----debug-----')
    logger_1.log_info('-----info-----')
    logger_1.log_warning('-----warning-----')
    logger_1.log_error('-----error-----')
    logger_1.log_critical('-----critical-----')
    
    logger_1.shutdown()
    
if __name__ == '__main__':
    _test()

