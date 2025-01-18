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

        #executable path field
        #this field will be filled with path of the executable file upon browsing
        self.appInput = QLineEdit(self)
        self.appInput.setPlaceholderText('Browse executables to launch')
        layout.addWidget(self.appInput)

        #browse button to select the executable file
        #only searches for .exe files, no error handling needed therefore
        self.browseButton = QPushButton('Browse', self)
        self.browseButton.clicked.connect(self.browseFile)
        layout.addWidget(self.browseButton)
        
        #start time of the execution of executable to launch

        self.startTimeInput = QLineEdit(self)
        self.startTimeInput.setPlaceholderText('Start time of execution')
        layout.addWidget(self.startTimeInput)
        
        #stop time of the execution of executable to launch
        self.stopTimeInput = QLineEdit(self)
        self.stopTimeInput.setPlaceholderText('Stop time of execution')
        layout.addWidget(self.stopTimeInput)
        
        
        self.runButton = QPushButton('Run', self)
        self.runButton.clicked.connect(self.runApplication)
        layout.addWidget(self.runButton)

        #need to put this in a func 
        self.setMinimumSize(400, 200)
        self.setMaximumSize(1200, 600)
        self.setLayout(layout)
        self.show()

    #layout proper
    layout = QVBoxLayout()

    def browseFile(self): 
        fileName, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'Executable Files (*.exe)')
        if fileName:
         self.appInput.setText(fileName)


    def runApplication(self):
        appPath = self.appInput.text()
        startTime = self.startTimeInput.text()
        stopTime = self.stopTimeInput.text()
        
        #error handling and validation of inputs
        if not appPath:
            QMessageBox.critical(self, "Inout Error", "Please select an executable file.")
            return
            
        try:
            startTime = int(startTime)
            stopTime = int(stopTime)
            if not (0<= startTime < stopTime < 5):
                raise ValueError('Oopsie daisy, start time must be less than stop time, and both should be in the range of [0,5]')
        except ValueError as e:
            QMessageBox.critical(self,"Input error", str(e))
            return

        #running the executable with -override arg
        #this argument will override the current XML of the TwoConnectedTanks.exe file while running
        #allows the user to run the executable as desired
        try:
            result =subprocess.run([  #check the subprocess of open-modelica
                appPath, 
                f"-override=startTime={startTime},stopTime={stopTime}"], #adding time contraints as mentioned in docs
                capture_output=True, 
                text=True,
                check=True
            )
            QMessageBox.information(self, "SUCCESS", f"Successful execution!\n\nOutput: \n{result.stdout}")
        except subprocess.CalledProcessError as e:
            QMessageBox.critical(self, "Execution error", f"Error during simulation:\n{e.stderr}") #getting this error every run right now
        except Exception as e:
            QMessageBox.critical(self, "Unexpected Error" , f'Failed to run application: {str(e)}')
        else:
            print('Please provide all inputs: application path, start time, and stop time')

#main execution of program
#this runs the GUI application
if __name__ == '__main__':
    app = QApplication([]) #no CLI here, everything happens on the active window
    mainWindow = MainWindow()
    sys.exit(app.exec())
 
