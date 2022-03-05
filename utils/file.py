import os


class File():
    '''
    Working with a file
    '''

    def __init__(self, _dir, name):
        self.dir = _dir
        self.name = name
        self.path = self.dir + '\\' + self.name
        # print(f'\t\t -> {self.path}')

    def file_type(self):
        if self.name.endswith('.mp3'):
            return 'AUDIO'
        elif self.name.endswith('.mp4'):
            return 'VIDEO'
        elif self.name.endswith('.pdf'):
            return 'PDF'
        elif (self.name.endswith('.png')
              or self.name.endswith('.jpg')
              or self.name.endswith('.jpeg')
              or self.name.endswith('.svg')):
            return 'IMAGE'
        elif self.name.endswith('.md'):
            return 'MD'
        else:
            return 'TEXT'

    def getPath(self):
        '''
        returns full file-path: dir + name
        '''
        return self.path

    def getName(self):
        '''
        returns name of the file
        '''
        return self.name

    def getParent(self):
        '''
        No use
        '''
        return ""

    def readContent(self):
        '''
        read file content and returns
        '''
        try:
            with open(self.path, 'r') as f:
                content = f.read()
        except Exception as e:
            return "Can't open file!"
        return content

    def readBinary(self):
        '''
        '''
        try:
            with open(self.path, 'rb') as f:
                content = f.read()
        except Exception as e:
            return "Can't open file!"
        return content

    def duplicate(self) -> str or None:
        '''
        make a duplicate+temporary file and uses it as static asset \\
        returns duplicate file path
        '''
        path = f'/static/temp/{self.name}'
        if os.path.exists(path):
            return path
        with open(f'./web{path}', 'wb') as f:
            f.write(self.readBinary())
        return path or None

    def is_file(self):
        return os.path.isfile(self.path)
