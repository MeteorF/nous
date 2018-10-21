import sys
sys.path.append('modules')

if __name__ == '__main__':
    from class_global_config import global_config
else:
    from .class_global_config import global_config