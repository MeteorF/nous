
# coding: utf-8

# In[1]:


# ../utilities/__init__
# Last modify: 20181007


# In[2]:


import config
import path_ops
import logger


# In[3]:


def init():
    config.init()
    __config__ = config.__config__
#     logger.init(logpath = __config__.LOG_PATH)
#     logger.start()


# In[4]:


if __name__ == '__main__':
    init()

