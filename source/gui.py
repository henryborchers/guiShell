import sys
from time import sleep

__author__ = 'California Audio Visual Preservation Project'


from PyQt4.QtCore import *
from PyQt4.QtGui import *
from gui import Ui_Form
from enum import Enum
from queue import Queue
# TODO set GUI variables
SOURCE_LABLE = ""
JOB_NAME = ""

class running_status(Enum):
    PENDING = 0
    RUNNING = 1
    ERROR = 2


class MainWidget(QWidget, Ui_Form):

    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(JOB_NAME)
        self.status = running_status.PENDING
        self.labelSource.setText(SOURCE_LABLE + ":")
        self.lineEditISource.textChanged.connect(self.is_source_valid)
        self.pushButton_start.clicked.connect(self.start_job)
        self.updater_function = UPDATER_FUNCTION

    def is_source_valid(self):
        if validator(self.lineEditISource.text()):
            self.pushButton_start.setEnabled(True)
        else:
            self.pushButton_start.setEnabled(False)

    def start_job(self):
        print("Starting")
        self.status = running_status.RUNNING
        queue = get_jobs(self.lineEditISource.text())
        assert isinstance(queue, Queue)
        worker = Worker()

        progress = QProgressDialog(JOB_NAME, "Abort", 0, queue.qsize())
        progress.setWindowModality(Qt.WindowModal)
        progress.show()
        i = 0
        job = None
        self.status = running_status.PENDING
        while queue.unfinished_tasks:
            if not worker.isRunning():
                job = queue.get()
                worker = Worker(job)
                worker.run()
                self.status = running_status.RUNNING
            progress.setValue(i)
            if progress.wasCanceled():
                break
            if not worker.isRunning():
                i += 1
                queue.task_done()
                continue
            sleep(.01)
        print("Done")
        pass


class Worker(QThread):

    def __init__(self, job=None):
        super(Worker, self).__init__()
        self.job = job

    def run(self):
        #TODO create worker run method
        pass


def validator(data):
    valid = True
    # TODO check if data is valid
    return valid


def get_jobs(source)->Queue:
    # TODO get jobs from source
    jobs = Queue()

    return jobs


def tester():
    print("Testing")
    app = QApplication(sys.argv)
    form = MainWidget()
    form.show()
    app.exec_()


if __name__ == '__main__':
    tester()


