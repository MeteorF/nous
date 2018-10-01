
# coding: utf-8

# In[1]:


# ../utilities/parse_config
# Last modify: 20181001


# # Parse Config
# 
# Ref: https://hackernoon.com/4-ways-to-manage-the-configuration-in-python-4623049e841b

# In[2]:


import os
import json

# from util_path_ops import dir_check
import importlib
spec = importlib.util.spec_from_file_location("main", "util_path_ops.py")
util_path_ops = importlib.util.module_from_spec(spec)
spec.loader.exec_module(util_path_ops)
from util_path_ops import dir_check


# In[3]:


def get_config_val(config_key, ENV_specific = 'DEFAULT'):
    print('===== parse_config/get_config_val =====')
    
    if DEBUG:
        print(f'Attempt to get: config_key = {config_key} | ENV_specific={ENV_specific}')
    
    if (config_key == None):
        raise ValueError(f'config_key is none.')
    else:
        
        value = __settings__[ENV_specific][config_key]
        if DEBUG:
            print (f'val={value} | type={type(value)} \n')
        
        return value


# In[4]:


def parse_config():
    print('===== parse_config/parse_config =====')
    
    global VERSION, ENV, DEBUG, __settings__
    
    config_file = 'settings/config.json'
    
    config_file_path = dir_check(config_file, dir_create=False, return_type='Path')
    
    with open(config_file_path) as f:
        # Read json as dictionary
        __settings__ = json.load(f)
    
    VERSION = __settings__['DEFAULT']['VERSION']
    ENV = __settings__['DEFAULT']['ENV']
    DEBUG = str_to_bool(__settings__[ENV]['DEBUG'])
    INPUT = config_file_path = dir_check(get_config_val('INPUT_DIR'), dir_create=True, return_type='Path')
    OUTPUT = config_file_path = dir_check(get_config_val('OUTPUT_DIR'), dir_create=True, return_type='Path')
    
    print (f"VERSION = {VERSION} | type = {type(VERSION)}")
    print (f"ENV = {ENV} | type = {type(ENV)}")
    print (f"DEBUG = {DEBUG} | type = {type(DEBUG)}")
    print (f"INPUT = {INPUT} | type = {type(INPUT)}")
    print (f"OUTPUT = {OUTPUT} | type = {type(OUTPUT)} \n")


# In[5]:


def str_to_bool(s):
    print('===== parse_config/str_to_bool =====')
    
    s = s.upper()
    if s in ('TRUE', 'T', '0'):
         return True
    elif s in ('FALSE', 'F', '1'):
         return False
    else:
         raise ValueError(f'Boolean Value {s} cannot be evaluated.')


# In[6]:


def main():
    print('MAIN')
    parse_config()
#     print(get_config_val(config_key='SETTINGS_DIR'))


# In[7]:


if __name__ == '__main__':
    main()
else:
    parse_config()

