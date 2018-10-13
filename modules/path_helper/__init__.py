
# coding: utf-8

# In[1]:


# init


# In[2]:


import sys
sys.path.append('modules')

from os import mkdir
from os import chdir
import pathlib
import datetime

if __name__ == '__main__':
    from dir_check import dir_check
    from display_dir_tree import display_dir_tree
    from getOutputFileName import getOutputFileName
    from chdir import chdir
else:
    from .dir_check import dir_check
    from .display_dir_tree import display_dir_tree
    from .getOutputFileName import getOutputFileName
    from .chdir import chdir

