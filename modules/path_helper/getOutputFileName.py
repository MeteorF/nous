
# coding: utf-8

# In[1]:


# getOutputFileName


# In[2]:


import pathlib
import datetime

print(f'__name__ = {__name__}')

if __name__ == '__main__':
    from dir_check import dir_check
else:
    from .dir_check import dir_check


# In[3]:


def getOutputFileName(extension='.txt', path=None, custom_name=None):
    ## Output file name setting
    print(f'===== path_ops/getOutputFileName =====')
    
    if (path == None):
        raise ValueError("No path is received")
    else:
        # Parse string to path object
        path = dir_check(path, dir_create=False, return_type='Path')
        path = pathlib.PurePath(path)
        
    now = datetime.datetime.now()
    # print(now.strftime("%Y%m%d_%H%M%S"))
    timeStampStr = str(now.strftime("%Y%m%d_%H%M%S%f"))
    
    if (custom_name == None):
        output_filename = 'output_' + timeStampStr + extension
    elif (len(custom_name) > 0):
        output_filename = custom_name[:20] + '_' + timeStampStr + extension
    elif (len(custom_name) == 0):
        output_filename = timeStampStr + extension
    
    ## output_filename = os.path.join(output_folder, output_filename) + extension
    path = path.joinpath(output_filename)
    
    print(f'path = {path}')
    print ("\n")
    return str(path)


# In[4]:


# Test function for module  
def _test():
    path = getOutputFileName(path='.')
    assert(pathlib.Path(path).suffix == '.txt')

if __name__ == '__main__':
    _test()

