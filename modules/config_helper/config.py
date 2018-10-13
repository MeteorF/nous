
# coding: utf-8

# In[1]:


# ../utilities/config
# Last modify: 20181007


# # Parse Config
# 
# Ref: https://hackernoon.com/4-ways-to-manage-the-configuration-in-python-4623049e841b

# In[2]:


import os
import json

from path_ops import dir_check
# import importlib
# spec = importlib.util.spec_from_file_location("main", "util_path_ops.py")
# util_path_ops = importlib.util.module_from_spec(spec)
# spec.loader.exec_module(util_path_ops)
# from util_path_ops import dir_check


# In[3]:


class global_config:

    def __init__(self, args):
        self.VERSION = args['VERSION']
        self.ENV = args['ENV']
        self.DEBUG = args['DEBUG']
        self.PROJ_PATH = args['PROJ_PATH']
        self.INPUT_PATH = args['INPUT_PATH']
        self.OUTPUT_PATH = args['OUTPUT_PATH']
        self.LOG_PATH = args['LOG_PATH']
        
    def show(self):
        print (f"VERSION = {self.VERSION} | type = {type(self.VERSION)}")
        print (f"ENV = {self.ENV} | type = {type(self.ENV)}")
        print (f"DEBUG = {self.DEBUG} | type = {type(self.DEBUG)}")
        print (f"PROJ_PATH = {self.PROJ_PATH} | type = {type(self.PROJ_PATH)}")
        print (f"INPUT_PATH = {self.INPUT_PATH} | type = {type(self.INPUT_PATH)}")
        print (f"OUTPUT_PATH = {self.OUTPUT_PATH} | type = {type(self.OUTPUT_PATH)}")
        print (f"LOG_PATH = {self.LOG_PATH} | type = {type(self.LOG_PATH)}")
        print ("\n")


# In[4]:


def get_config_val(config_key, ENV_specific = 'DEFAULT'):
    print('===== config/get_config_val =====')
    
    if DEBUG:
        print(f'Attempt to get: config_key = {config_key} | ENV_specific={ENV_specific}')
    
    if (config_key == None):
        raise ValueError(f'config_key is none.')
    else:
        
        value = __settings__[ENV_specific][config_key]
        if DEBUG:
            print (f'val={value} | type={type(value)} \n')
        
        return value


# In[5]:


def parse_config():
    print('===== config/parse_config =====')
    
    global DEBUG, __settings__, __config__
    
#     config_file = 'settings/config.json'
    config_file = 'C:\\Users\\alana\\AnacondaProjects\\nous\\settings\\config.json'
    
    config_file_path = dir_check(config_file, dir_create=False, return_type='Path')
    
    with open(config_file_path) as f:
        # Read json as dictionary
        __settings__ = json.load(f)
    
    VERSION = __settings__['DEFAULT']['VERSION']
    ENV = __settings__['DEFAULT']['ENV']
    DEBUG = str_to_bool(__settings__[ENV]['DEBUG'])
    
    config = {
        "VERSION": VERSION,
        "ENV": ENV,
        "DEBUG": DEBUG,
        "PROJ_PATH": dir_check(get_config_val('PROJ_DIR'), dir_create=False, return_type='Path'),
        "INPUT_PATH": dir_check(get_config_val('INPUT_DIR'), dir_create=True, return_type='Path'),
        "OUTPUT_PATH": dir_check(get_config_val('OUTPUT_DIR'), dir_create=True, return_type='Path'),
        "LOG_PATH": dir_check(get_config_val('LOG_DIR'), dir_create=True, return_type='Path')
    }
    
    __config__ = global_config(config)


# In[6]:


def str_to_bool(s):
    print('===== config/str_to_bool =====')
    
    s = s.upper()
    if s in ('TRUE', 'T', '0'):
         return True
    elif s in ('FALSE', 'F', '1'):
         return False
    else:
         raise ValueError(f'Boolean Value {s} cannot be evaluated.')


# In[7]:


def init():
    print('===== config/init =====')
    parse_config()
#     print(get_config_val(config_key='SETTINGS_DIR'))


# In[8]:


if __name__ == '__main__':
    init()

