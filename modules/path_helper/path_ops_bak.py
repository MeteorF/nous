
# coding: utf-8

# In[1]:


# ../utilities/path_ops
# Last modify: 20181007


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
from os import chdir
import pathlib
import datetime


# In[3]:


def dir_check (dir_check = None, dir_create = True, return_type = 'Exist'):
    print(f'===== path_ops/dir_check =====')
    
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


# In[5]:


def display_dir_tree(directory):
    print(f'===== path_ops/display_dir_tree =====')
    print(f'+ {directory}')
    
    for path in sorted(directory.rglob('*')):
        depth = len(path.relative_to(directory).parts)
        spacer = '    ' * depth
        print(f'{spacer}+ {path.name}')


# In[6]:


def main():
    print(f"dir_check(Path option) = {dir_check('settings/abcccc', dir_create = False, return_type='Path')} \n")
    print(f"dir_check(Exist option) = {dir_check('settings/abcccc', dir_create = False, return_type='Exist')} \n")
    # display_dir_tree(pathlib.Path.cwd().parent)


# In[7]:


if __name__ == '__main__':
    main()

