import sys
sys.path.append('modules')

if __name__ == '__main__':
    from class_logger import logger
else:
    from .class_logger import logger