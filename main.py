from threading import Thread
from utils.explorer import Explorer
from utils.funcs import free
from utils.input_handler import InputHandler


if __name__ == "__main__":
    args = InputHandler().start()
    #
    exp = Explorer()
    # ---- cleaning temp dir / cached files
    cleanTh = Thread(target=free, args=(exp.tempDir(),))
    cleanTh.start()
    # ----
    exp.setDir(args.directory)
    exp.run(port=args.port, debug=True, threaded=True)
