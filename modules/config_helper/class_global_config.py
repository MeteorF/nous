
# coding: utf-8

# In[1]:


# class_global_config
#
# Usage:
# 1.Parse config file (format see settings/config.json) to variables
# 2.Display converted keys and values
# 3.Export keys and values as dictionary


# In[2]:


class global_config:
        
    def __init__(self, args):
        key = "DEFAULT"    
        self.__dict__.update(args.get(key))
        current_env = self.ENV
        self.__dict__.update(args.get(current_env))
    
    def show_config(self):
        for key, value in self.__dict__.items():
                print (f"key = {key} | value = {value}")
        
    def exportConfig(self, display=False):
        config_dict = {}
        for key, value in self.__dict__.items():
            config_dict.update({key: value})
        
        if display == True:
            for key, value in self.__dict__.items():
                print (f"key = {key} | value = {value}")
            
        return config_dict


# In[3]:


# Test function for module  
def _test():
    config = {
        "DEFAULT": {
            "ADMIN_NAME": "...",
            "AWS_DEFAULT_REGION": "...",
            "MAX_IMAGE_SIZE": 5242880,
            "PROJ_DIR": "C:/Users/alana/AnacondaProjects/nous",
            "INPUT_DIR": "input",
            "OUTPUT_DIR": "output",
            "SETTINGS_DIR": "settings",
            "LOG_DIR": "logs",
            "ENV": "DEV"
        },
        "DEV": {
            "VERSION": "0.0.1",
            "SECRET_KEY": "",
            "DEBUG": "T",
            "TEST_TMP_DIR": "tests",
            "TEST_TIMEOUT": 20
        },
        "PRD": {
            "VERSION": "0.0.1",
            "SECRET_KEY": "",
            "DEBUG": "F",
            "SERVICE": "travis-ci",
            "HOOK_URL": "..."
        }
    }
    
    global __config__
    global __exportConfig__
    __config__ = global_config(config)
    __exportConfig__ = __config__.exportConfig(display=True)
    
    assert (config.get("DEFAULT").get("ENV") == __exportConfig__.get("ENV"))

if __name__ == '__main__':
    _test()

