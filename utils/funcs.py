import os


def free(path):
    '''
    frees files generated
    '''
    _list = os.listdir(path)
    for file in _list:
        os.remove(path+'\\'+file)
