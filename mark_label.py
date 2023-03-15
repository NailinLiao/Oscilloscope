# from UI.mark_label import Ui_MainWindow
from UI.untitled import Ui_MainWindow
from multiprocessing import Process, Queue
import sys
from PyQt5.QtWidgets import *
import os


class Marker:
    def __init__(self, video_path, save_path, q):
        print('-----')
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        file_name = str(os.path.split(video_path)[-1]).split('.')[0]
        end_save_path = os.path.join(save_path, file_name + '.json')
        self.read_video_Process = Process(target=self.show, args=(end_save_path, q,))
        self.read_video_Process.start()

    def show(self, end_save_path, q):
        app = QApplication(sys.argv)
        self.ui_main = Ui_MainWindow(end_save_path, q)
        self.ui_main.show()
        sys.exit(app.exec_())

    def kill(self):
        self.read_video_Process.kill()


if __name__ == '__main__':
    q = Queue()
    maker = Marker('./test/aaa.avi', './test', q)
    for i in range(10):
        print(i)
    import time

    time.sleep(5)
    a = {
        'a': r'123',
    }
    q.put(a)
    time.sleep(100)
    maker.kill()
