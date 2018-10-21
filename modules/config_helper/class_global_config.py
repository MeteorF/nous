
# coding: utf-8

# In[1]:


# obj_global_config


# In[2]:


class global_config:
        
    def __init__(self, args):
        self.config = args
    
    def show_config(self):
        for key, value in self.config.items():
                print (f"key = {key} | value = {value}")
        
    def exportConfig(self, display=False):
        config_dict = {}
        for key, value in self.config.items():
            config_dict.update({key: value})
        
        if display == True:
            for key, value in config_dict.items():
                print (f"key = {key} | value = {value}")
            
        return config_dict


# In[3]:


# Test function for module  
def _test():
    config = {
        "VERSION": "1.0",
        "ENV": "DEV",
        "DEBUG": True,
        "PROJ_PATH": "C:/Users/alana/AnacondaProjects/nous",
        "INPUT_PATH": "input",
        "OUTPUT_PATH": "output",
        "LOG_PATH": "logs"
    }
    
    global __config__
    global __exportConfig__
    __config__ = global_config(config)
    __exportConfig__ = __config__.exportConfig(display=True)
    
    assert (config == __exportConfig__)

if __name__ == '__main__':
    _test()

