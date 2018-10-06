
# coding: utf-8

# In[1]:


# ../utilities/util_path_ops
# Last modify: 20181001


# ## Picking Out Components of a Path
# Ref: https://realpython.com/python-pathlib/ <br>
# The different parts of a path are conveniently available as properties. Basic examples include:
# <ul>
#     <li>.name: the file name without any directory</li>
#     <li>.parent: the directory containing the file, or the parent directory if path is a directory</li>
#     <li>.stem: the file name without the suffix</li>
#     <li>.suffix: the file extension</li>
#     <li>.anchor: the part of the path before the directories</li>
# </ul>

# In[2]:


from os import mkdir
import pathlib


# In[23]:


def dir_check_bak (dir_check = None, dir_create = True, return_type = 'Bool'):
    print(f'===== util_dir_check/util_path_ops =====')
    
    if dir_check == None:
        raise ValueError("No directory for checking.")
        
    else:
        current_dir = pathlib.Path.cwd()
        print(f'current_dir = {current_dir}')
        proj_dir = current_dir.relative_to('../nous')
        dir_to_check = proj_dir.joinpath(dir_check)
        dir_to_check_exist = False
        
        if dir_to_check.exists() :
            print (f'{dir_to_check} | exist, no action required.')
            dir_to_check_exist = True
        else:
            
            # Not contain extension, is a directory
            if len(dir_to_check.suffix) == 0 and dir_create == True:
                print (f'{dir_to_check} | exist, dir created.')
                mkdir(dir_to_check)
                dir_to_check_exist = True
            
            elif len(dir_to_check.suffix) == 0 and dir_create == False :
                print (f'{dir_to_check} | exist, dir not created according to config.')
                
            # Contains extension, Not a directory
            elif len(dir_to_check.suffix) != 0:
                raise ValueError(f'{dir_to_check} | file not exist.')
        
        if return_type == 'Bool':
            return dir_to_check_exist
        elif return_type == 'Path':
            return str(dir_to_check)


# In[49]:


def dir_check (dir_check = None, dir_create = True, return_type = 'Exist'):
    print(f'===== util_dir_check/util_path_ops =====')
    
    if dir_check == None:
        raise ValueError("No directory for checking.")
        
    else:
        current_dir = pathlib.Path.cwd()
        proj_dir = pathlib.Path('..')
        dir_query = proj_dir / dir_check
        dir_to_check = dir_query.resolve()
        dir_to_check_exist = dir_query.exists()
        
        print(f'current_dir = {current_dir}')
        print(f'proj_dir = {proj_dir.resolve()}')
        print(f'dir_to_check = {dir_to_check} | exist = {dir_query.exists()} | is_dir = {dir_query.is_dir()} | is_file = {dir_query.is_file()}')
        
        if dir_to_check_exist == True :
            print (f'{dir_to_check} | exist, no action required.')
        else:
            # Not contain extension, is a directory
            if len(dir_to_check.suffix) == 0 and dir_create == True:
                print (f'{dir_to_check} | exist, dir created.')
                mkdir(dir_to_check)
            
            if len(dir_to_check.suffix) == 0 and dir_create == False :
                print (f'{dir_to_check} | exist, dir not created according to config.')
                
            # Contains extension, Not a directory
            elif len(dir_to_check.suffix) != 0:
                raise ValueError(f'{dir_to_check} | file not exist.')
        
        if return_type == 'Exist':
            return dir_to_check_exist
        elif return_type == 'Path':
            return str(dir_to_check)


# In[4]:


def display_dir_tree(directory):
    print(f'===== util_dir_check/display_dir_tree =====')
    print(f'+ {directory}')
    
    for path in sorted(directory.rglob('*')):
        depth = len(path.relative_to(directory).parts)
        spacer = '    ' * depth
        print(f'{spacer}+ {path.name}')


# In[54]:


def main():
    print(f"dir_check(Path option) = {dir_check('settings/abcccc', dir_create = False, return_type='Path')}")
    print(f"dir_check(Exist option) = {dir_check('settings/abcccc', dir_create = False, return_type='Exist')}")
    display_dir_tree(pathlib.Path.cwd().parent)


# In[55]:


if __name__ == '__main__':
    main()
