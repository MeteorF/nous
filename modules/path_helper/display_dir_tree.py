
# coding: utf-8

# In[1]:


# display_dir_tree


# In[2]:


import pathlib
import datetime


# In[3]:


def display_dir_tree(directory):
    print(f'===== path_ops/display_dir_tree =====')
    print(f'+ {directory}')
    
    directory = pathlib.Path(directory)
    
    for path in sorted(directory.rglob('*')):
        depth = len(path.relative_to(directory).parts)
        spacer = '    ' * depth
        print(f'{spacer}+ {path.name}')


# In[4]:


# Test function for module  
def _test():
    path = 'C:/Users/alana/AnacondaProjects/nous/modules/path_helper/'
    print(path)
    display_dir_tree(path)

if __name__ == '__main__':
    _test()

