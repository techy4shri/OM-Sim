"""
This module provides a GUI application for running OpenModelica simulations.
The application allows users to select an executable file and specify time
constraints.
"""

import sys
import subprocess
from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QFileDialog,
    QMessageBox,
    QApplication,
)


class MainWindow(QWidget):
    """
    Main window class for the OpenModelica Simulation App.
    Provides the user interface for selecting an executable file
    and running it with specified time constraints.
    """

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """
        Initializes the user interface.
        Sets up the layout and widgets for the application.
        """
        layout = QVBoxLayout()
        self.setWindowTitle("OpenModelica Simulation App")

        '''
        executable path field
        this field will be filled with path of the executable
        file upon browsing
        '''
        self.app_input = QLineEdit(self)
        self.app_input.setPlaceholderText("Browse executables to launch")
        layout.addWidget(self.app_input)

        # browse button to select the executable file
        # only searches for .exe files, no error handling needed therefore
        self.browse_button = QPushButton("Browse", self)
        self.browse_button.clicked.connect(self.browse_file)
        layout.addWidget(self.browse_button)

        # start time of the execution of executable to launch

        self.start_time_input = QLineEdit(self)
        self.start_time_input.setPlaceholderText("Start time of execution")
        layout.addWidget(self.start_time_input)

        # stop time of the execution of executable to launch
        self.stop_time_input = QLineEdit(self)
        self.stop_time_input.setPlaceholderText("Stop time of execution")
        layout.addWidget(self.stop_time_input)

        self.run_button = QPushButton("Run", self)
        self.run_button.clicked.connect(self.run_app)
        layout.addWidget(self.run_button)

        # need to put this in a func
        self.setMinimumSize(400, 200)
        self.setMaximumSize(1200, 600)
        self.setLayout(layout)
        self.show()

    def browse_file(self):
        """
        Opens a file dialog to select an executable file.
        Sets the selected file path to the app_input field.
        """
        file_name, _ = QFileDialog()  # type: ignore
        file_path, _ = file_name.getOpenFileName(
            self, "Open File", "", "Executable Files (*.exe)"
        )
        if file_path:
            self.app_input.setText(file_name)

    def run_app(self):
        """
        Runs the application with the provided executable path
        and time constraints.
        Validates the inputs and handles errors appropriately.
        """
        app_path = self.app_input.text()
        start_time = self.start_time_input.text()
        stop_time = self.stop_time_input.text()

        # error handling and validation of inputs
        if not app_path:
            QMessageBox.critical(
                self, "Inout Error", "Please select an executable file."
            )
            return

        try:
            start_time = int(start_time)
            stop_time = int(stop_time)
            if not 0 <= start_time < stop_time < 5:
                raise ValueError(
                    "Oopsie daisy, start time must be < stop time,under [0,5]"
                )
        except ValueError as e:
            QMessageBox.critical(self, "Input error", str(e))
            return

        # running the executable with -override arg
        # to override the current XML while running
        # allows the user to run the executable as desired
        try:
            result = subprocess.run(
                [  # check the subprocess of open-modelica
                    app_path,
                    # adding time contraints as mentioned in docs
                    f"-override=start_time={start_time},stop_time={stop_time}",
                ],
                capture_output=True,
                text=True,
                check=True,
            )
            QMessageBox.information(
                self,
                "SUCCESS",
                f"Successful execution!\n\nOutput:\n{result.stdout}",  # ignore
            )
        except subprocess.CalledProcessError as e:
            QMessageBox.critical(
                self,
                "Execution error",
                f"Error during simulation:\n{e.stderr}",
            )  # getting this error every run right now
        except FileNotFoundError as e:
            QMessageBox.critical(
                self, "File Not Found", f"Executable not found: {str(e)}"
            )
        except OSError as e:
            QMessageBox.critical(
                self, "OS Error", f"OS error occurred: {str(e)}"
            )  # ignore
        else:
            print("Please provide all inputs first!")


# main execution of program
# this runs the GUI application
if __name__ == "__main__":
    # no CLI here, everything happens on the active window
    app = QApplication([])
    mainWindow = MainWindow()
    sys.exit(app.exec())
