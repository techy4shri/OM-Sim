import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QFileDialog
import subprocess

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.appInput = QLineEdit(self)
        self.appInput.setPlaceholderText('Application launching')
        layout.addWidget(self.appInput)

        self.startTimeInput = QLineEdit(self)
        self.startTimeInput.setPlaceholderText('Start time')
        layout.addWidget(self.startTimeInput)

        self.stopTimeInput = QLineEdit(self)
        self.stopTimeInput.setPlaceholderText('Stop time')
        layout.addWidget(self.stopTimeInput)

        self.browseButton = QPushButton('Browse', self)
        self.browseButton.clicked.connect(self.browseFile)
        layout.addWidget(self.browseButton)

        self.runButton = QPushButton('Run', self)
        self.runButton.clicked.connect(self.runApplication)
        layout.addWidget(self.runButton)

        self.setLayout(layout)
        self.setWindowTitle('OpenModelica GUI')
        self.show()
 
    def browseFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'Executable Files (*.exe)')
        if fileName:
            self.appInput.setText(fileName)

    def runApplication(self):
        appPath = self.appInput.text()
        startTime = self.startTimeInput.text()
        stopTime = self.stopTimeInput.text()
        if appPath and startTime and stopTime:
            try:
                subprocess.run([appPath, startTime, stopTime])
                print(f'Running {appPath} from {startTime} to {stopTime}')
            except Exception as e:
                print(f'Failed to run application: {e}')
        else:
            print('Please provide all inputs: application path, start time, and stop time')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())
