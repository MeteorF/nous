
# coding: utf-8

# In[1]:


# chdir


# In[2]:


import pathlib
from os import chdir as os_chdir

print(f'__name__ = {__name__}')

if __name__ == '__main__':
    from dir_check import dir_check
else:
    from .dir_check import dir_check


# In[3]:


def chdir(path=None):
    print(f'===== path_ops/chdir =====')
    
    if (path == None):
        raise ValueError("No path is received")
    else:
        # Parse string to path object
        path = dir_check(path, dir_create=False, return_type='Path')
        print (f'target_dir = {path}')
        path = pathlib.PurePath(path)
        
        os_chdir(path)
        cwd = pathlib.Path.cwd()
        print (f'cwd = {cwd}')


# In[4]:


# Test function for module  
def _test():
    path = 'C:/Users/alana/AnacondaProjects/nous'
    chdir(path)
    
    cwd = pathlib.Path.cwd()
    path = pathlib.PurePath(path)
    assert(cwd == path)

if __name__ == '__main__':
    _test()

