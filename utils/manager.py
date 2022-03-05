class Manager:
    def __init__(self):
        self.__dir = None  # main dir path
        self.__currDir = None

    def getDir(self):
        '''
        returns main directory (args[0])
        '''
        return self.__dir

    def setMainDir(self, dir):
        '''
        set args[0] from commandline as main directory
        '''
        self.__dir = dir

    def getCD(self):
        '''
        returns current directory
        '''
        return self.__currDir

    def setCD(self, dir):
        '''
        sets new directory as current directory
        '''
        self.__currDir = dir

    def extract(self):
        '''
        returns content & full-path of the directory
        '''
        return {
            'content': self.getCD().content(),
            'path': self.getCD().getPath()}
