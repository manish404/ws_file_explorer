from .file import File
import os


class Folder():
    '''
    Working with a folder
    '''

    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.list = None  # stores everything inside folder as File() & Folder()
        # self.populate()

    def getName(self):
        '''
        returns name of the directory
        '''
        return self.name

    def getParent(self):
        '''
        returns parent directory of directory
        '''
        return self.parent

    def getDir(self):
        '''
        returns full-path: (parent + name) of directory
        '''
        return self.full_path()

    def getPath(self):
        '''
        returns full-path: (parent + name) of directory
        '''
        return self.full_path()

    def content(self):
        if self.list:
            return self.list

    def is_file(self):
        return os.path.isfile(self.full_path())

    def populate(self):
        # print(f'\t -> {self.full_path()}')
        '''
        scans directory and makes a tree of sub-files(File)-and-folders(Folder)
        '''
        if self.list:
            return self.list
        _list = self.readDir()
        self.list = []  #
        for e in _list:
            if e.is_file():
                f = File(self.full_path(), e.name)
                self.list.append(f)
            elif e.is_symlink():
                continue
            elif e.is_dir():
                f = Folder(e.name, self.getDir())
                self.list.append(f)
        # print(self.list)

    def full_path(self):
        '''
        builds a full (full-path: parent_dir+dir_name) and returns
        '''
        if self.parent:
            return self.parent + '\\' + self.name
        else:
            return self.name

    def readDir(self):
        '''
        Content of the directory: [files and folders]
        '''
        __list = os.scandir(self.full_path())
        '''
        scandir() is used for listing directory with properties
        properties are used inside populate function
        '''
        return __list


def makeTempDir(dir):
    '''
    makes temporary directory if not exists
    '''
    if os.path.exists(dir):
        return
    else:
        os.mkdir(dir)
