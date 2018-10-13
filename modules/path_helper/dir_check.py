
# coding: utf-8

# In[1]:


# dir_check


# In[2]:


import pathlib
from os import mkdir


# In[3]:


def dir_check (dir_check = None, dir_create = True, return_type = 'Exist'):
    print(f'===== path_helper/dir_check =====')
    
    if dir_check == None:
        raise ValueError("No directory for checking.")
        
    else:
        current_dir = pathlib.Path.cwd()
        # proj_dir = pathlib.Path(root_dir)
        dir_query = pathlib.Path(dir_check)
        dir_to_check = dir_query.resolve()
        dir_to_check_exist = dir_to_check.exists()
        
        print(f'current_dir = {current_dir}')
        # print(f'proj_dir = {proj_dir.resolve()}')
        print(f'dir_to_check = {dir_to_check} | exist = {dir_query.exists()} | is_dir = {dir_query.is_dir()} | is_file = {dir_query.is_file()}')
        
        if dir_to_check_exist == True :
            print (f'{dir_to_check} | exist, no action required.')
        else:
            # Not contain extension, is a directory
            if len(dir_to_check.suffix) == 0 and dir_create == True:
                print (f'{dir_to_check} | not exist, dir created.')
                mkdir(dir_to_check)
            
            if len(dir_to_check.suffix) == 0 and dir_create == False :
                print (f'{dir_to_check} | not exist, dir not created according to config.')
                
            # Contains extension, Not a directory
            elif len(dir_to_check.suffix) != 0:
                raise ValueError(f'{dir_to_check} | file not exist.')
        
            print ("\n")
        
        if return_type == 'Exist':
            return dir_to_check_exist
        elif return_type == 'Path':
            return str(dir_to_check)


# In[4]:


# Test function for module  
def _test():
    assert dir_check(dir_check='abc', dir_create=False, return_type='Exist') == False
    assert dir_check(dir_check='def', dir_create=False, return_type='Path') == 'def'

if __name__ == '__main__':
    _test()

