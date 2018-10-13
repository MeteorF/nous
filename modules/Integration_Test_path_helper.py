
# coding: utf-8

# In[1]:


import path_helper


# In[2]:


# Unit Test: path_helper.dir_check
def _test_dir_check():
    print (f'===== Unit Test: path_ops/dir_check =====')
    path_helper.dir_check(dir_check='efg', dir_create=False, return_type='Exist')


# In[3]:


# Unit Test: path_helper.getOutputFileName
def _test_getOutputFileName():
    print (f'===== Unit Test: path_ops/getOutputFileName =====')
    path_helper.getOutputFileName(path='.')


# In[4]:


# Unit Test: path_helper.chdir
def _test_chdir():
    print (f'===== Unit Test: path_ops/chdir =====')
    import pathlib

    print (f'cwd_as_is = {pathlib.Path.cwd()}')
    path_helper.chdir('C:/Users/alana/AnacondaProjects/nous')
    print (f'cwd_to_be = {pathlib.Path.cwd()}')


# In[5]:


# Unit Test: path_helper.display_dir_tree
def _test_display_dir_tree():
    print (f'===== Unit Test: path_ops/display_dir_tree =====')
    path_helper.display_dir_tree('C:/Users/alana/AnacondaProjects/nous/modules/path_helper/')


# In[6]:


# Test function for module  
def _test():
    _test_display_dir_tree()
    _test_dir_check()
    _test_getOutputFileName()
    _test_chdir()

if __name__ == '__main__':
    _test()

