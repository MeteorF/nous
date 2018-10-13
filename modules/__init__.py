
# coding: utf-8

# In[1]:


# ../utilities/__init__
# Last modify: 20181007


# In[2]:


import config
import path_ops
import logger
from os import chdir


# In[3]:


def init():
    # Get config
    global __config__
    config.init()
    __config__ = config.__config__
    
    # Change Current Working Directory to __config__.PROJ_PATH
    chdir(path_ops.dir_check(dir_check=__config__.PROJ_PATH, dir_create=False, return_type='Path'))
    
#     logger.init(logpath = __config__.LOG_PATH)
#     logger.start()


# In[4]:


if __name__ == '__main__':
    init()

