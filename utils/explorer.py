from flask import Flask, request, render_template, url_for
from .configs import *
from .manager import Manager
from .file import File
from .folder import Folder, makeTempDir


class Explorer(Flask):
    '''
    Web-based File Explorer \\
        with different file support
    '''

    def __init__(self):
        super().__init__(__name__,
                         template_folder=template_dir,
                         static_folder=static_dir)
        self.man = Manager()
        self.configure()
        self.makeRoutes()
        self.__tempDir = './web/static/temp/'

    def configure(self):
        '''
        basic app configuration
        '''
        self.config['UPLOAD_FOLDER'] = upload_dir
        self.config['MAX_CONTENT_LENGTH'] = max_content_length

    def makeRoutes(self):
        '''
        url routing rules
        '''
        self.add_url_rule('/', 'folder_view', self.folderView)
        self.add_url_rule('/fo/<folder_name>',
                          'folder_view_w_name', self.folderView)
        self.add_url_rule('/dir', 'get_curr_working_dir',
                          self.cwd, methods=['POST'])
        self.add_url_rule('/fi/<file_name>', 'serve_file', self.serveFile)

    def folderView(self, folder_name=None):
        '''
        serves folder and it's content : is also a homepage;
        '''
        # print(f'\t\t\t\t Path ---> {path}')
        if folder_name and self.path:
            self.man.setCD(
                Folder(folder_name, self.path))
        else:
            self.man.setCD(
                Folder(self.path))
        self.man.getCD().populate()
        content, _path = self.man.extract().values()
        return render_template('index.html', DIR=_path, content=content)

    def cwd(self):
        '''
        route to get working-directory
        '''
        # print(f'\t\t\t\t Path ---> {path}')
        if request.method == 'POST':
            inc = request.get_json()
            self.path = inc['path']
        return {}

    def serveFile(self, file_name):
        '''
        route to serve file to user \\
        default : plain text file / code file ✔ \\
        Image : (png, jpg, jpeg, svg) ✔ \\
        AV : (mp3, mp4) \\
        Pdf: pdf ✔ \\
        Office : (word, excel)
        '''
        file = File(self.path, file_name)
        f_type = file.file_type()
        if f_type == 'TEXT':
            return render_template('/file/text.html',
                                   FILENAME=file_name, content=file.readContent())
        elif f_type == 'IMAGE':
            f_path = file.duplicate()
            return render_template('/file/image.html',
                                   FILENAME=file_name,  PATH=f_path)
        elif f_type == 'PDF':
            f_path = file.duplicate()
            return render_template('/file/pdf.html',
                                   FILENAME=file_name, PATH=f_path)
        elif f_type == 'MD':
            return render_template('/file/markdown.html',
                                   FILENAME=file_name, content=file.readContent())
        # for audio & video, use buffering
        # after these twos are implemented, run render_template at last
        elif f_type == 'AUDIO':
            pass
        elif f_type == 'VIDEO':
            pass
        else:
            return "ERROR"

    def setDir(self, dir):
        self.path = dir  # this will change
        # man.mainDir will not change
        self.man.setMainDir(dir)

    def tempDir(self):
        '''
        returns if temporary directory exists
        else makes one
        '''
        makeTempDir(self.__tempDir)
        return self.__tempDir
