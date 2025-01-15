import sys
from PyQt6.QtWidgets import *
import subprocess

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.setWindowTitle("OpenModelica Simulation App")

        self.appInput = QLineEdit(self)
        self.appInput.setPlaceholderText('Search executables to launch')
        layout.addWidget(self.appInput)
        

        self.startTimeInput = QLineEdit(self)
        self.startTimeInput.setPlaceholderText('Start time of execution')
        layout.addWidget(self.startTimeInput)
        

        self.stopTimeInput = QLineEdit(self)
        self.stopTimeInput.setPlaceholderText('Stop time of execution')
        layout.addWidget(self.stopTimeInput)
        self.stopTimeInput.size()

        self.browseButton = QPushButton('Browse', self)
        self.browseButton.clicked.connect(self.browseFile)
        layout.addWidget(self.browseButton)
        self.browseButton.size()
        self.runButton = QPushButton('Run', self)
        self.runButton.clicked.connect(self.runApplication)
        layout.addWidget(self.runButton)

        #need to put this in a func
        self.setFixedSize(500, 250) 
        self.setMinimumSize(400, 200)
        self.setMaximumSize(1200, 600)

        self.setLayout(layout)
        self.setWindowTitle('OpenModelica GUI')
        self.show()

        

        

    #layout proper
    layout = QVBoxLayout()

    

    def browseFile(self): #needs to be placed properly
        fileName, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'Executable Files (*.exe)')
        if fileName:
         self.appInput.setText(fileName)
        
    

    

    def runApplication(self):
        appPath = self.appInput.text()
        startTime = self.startTimeInput.text()
        stopTime = self.stopTimeInput.text()
        if appPath and startTime and stopTime:
            
            try:
                startTimeInput = int(startTime)
                stopTimeInput = int(stopTime)
                if not (0<= startTimeInput < stopTimeInput < 5):
                    raise ValueError('oopsie daisy')
            except ValueError as e:
                QMessageBox.critical(self,"Input error", str(e))
                return

            try:
                result =subprocess.run([  #check the subprocess of open-modelica
                        appPath, 
                        f"-override=startTime={startTime}, 
                         stopTime={stopTime}"], #adding time contraints as mentioned in docs
                        capture_output=True, 
                        text=True,
                        check=True
                        )
                QMessageBox.information(self, f"Successful execution!\n\nOutput: \n{result.stdoutput}")
            except subprocess.CalledProcessError as e:
                QMessageBox.critical(self, "Execution error", f"Error during simulation:\n{e.stderr}")

            except Exception as e:
                print(f'Failed to run application: {e}')
        else:
            print('Please provide all inputs: application path, start time, and stop time')

if __name__ == '__main__':
    app = QApplication([])
    mainWindow = MainWindow()
    sys.exit(app.exec())
 #modify the run and start to be included as buttons
