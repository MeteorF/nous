
# coding: utf-8

# In[1]:


# ../utilities/logger
# Last modify: 20181007


# In[2]:


import logging
import os
import __init__
import path_ops
import pathlib


# In[3]:


def init(logpath = None):
    print('===== logger/init =====')
    #------------
    # Log Level:
    #   debug (lowest)
    #   info
    #   warning
    #   error
    #   critical (highest)
    #-----------
    
    #logpath = 'C:\\Users\\alana\\AnacondaProjects\\nous\\logs'
    logfileName = path_ops.getOutputFileName(path = logpath, extension='.log', custom_name='log')
    
    global logging
    logging = logging
    
    logging.basicConfig(
        # filename = logfileName, \
        handlers=[logging.FileHandler(logfileName, 'a', 'utf-8')], \
        # Will ignore levels lower than setting (e.g. set=info will ignore debug)
        level = logging.DEBUG, \
        format = '%(asctime)s | %(levelname)s | %(message)s', \
        datefmt = '%Y-%m-%d %H:%M:%S'
    )


# In[4]:


def start():
    logging.info('Start of program'.center(30, '-'))


# In[5]:


def shutdown():
    logging.info('End of program'.center(30, '-'))
    logging.shutdown()


# In[6]:


if __name__ == '__main__':
    __init__.init()
    __config__ = __init__.config.__config__
    init(logpath=__config__.LOG_PATH)
    start()
    logging.debug('Try logging..')
    shutdown()

