from argparse import ArgumentParser


class InputHandler(ArgumentParser):
    '''Commandline input/arguments handler'''

    def __init__(self):
        super().__init__(description="Web Based File Explorer", add_help=False)

    def start(self):
        # required [<name>]
        self.add_argument(
            'directory',
            help="Folder's full-path : to be served!",  type=str)
        # optional [--<name>]
        self.add_argument(
            '--port',
            help="Port to run this app",
            type=int,
            default=5000
        )
        self.add_argument(
            '--serve',
            help="Serve via wifi network too?", type=str, default='n', choices=['y', 'n'])
        self.add_argument(
            '--help', '-h',
            action='help', help="See available commands")
        return self.parse_args()
