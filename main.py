"""
This module provides a GUI application for running OpenModelica simulations.
The application allows users to select an executable file and specify time
constraints.
"""

import sys
import subprocess
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QFileDialog,
    QMessageBox,
    QApplication,
    QSpinBox,
    QSizePolicy,
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
        self.setWindowIcon(QIcon("path_to_logo/logo.png"))

        banner_layout = QHBoxLayout()
        banner_label = QLabel(self)
        banner_pixmap = QPixmap("./banner.png")
        banner_label.setPixmap(banner_pixmap)
        banner_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        banner_layout.addWidget(banner_label)
        layout.addLayout(banner_layout)

        '''
        executable path field
        this field will be filled with path of the executable
        file upon browsing
        '''

        exe_layout = QHBoxLayout()
        exe_label = QLabel("Executable Path:")
        exe_label.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        exe_label.setFixedWidth(90)

        self.app_input = QLineEdit(self)
        self.app_input.setPlaceholderText("Browse executables to launch")
        self.app_input.setFixedSize(250, 30)
        self.app_input.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed
        )

        browse_button = QPushButton("Browse", self)
        browse_button.setFixedSize(90, 30)
        browse_button.clicked.connect(self.browse_file)

        # layout widgets for exe
        exe_layout.addWidget(exe_label)
        exe_layout.addWidget(self.app_input)
        exe_layout.addWidget(browse_button)
        exe_layout.setSpacing(5)
        exe_layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        layout.addLayout(exe_layout)

        start_layout = QHBoxLayout()
        start_label = QLabel("Start Time:")
        start_label.setFixedWidth(60)

        self.start_time_input = QSpinBox(self)
        self.start_time_input.setRange(0, 5)  # Range: [0, 5]
        self.start_time_input.setValue(0)  # Default value
        self.start_time_input.setFixedSize(70, 40)

        start_layout.addWidget(start_label)
        start_layout.addWidget(self.start_time_input)
        start_layout.addStretch()
        layout.addLayout(start_layout)

        stop_layout = QHBoxLayout()
        stop_label = QLabel("Stop Time:")
        stop_label.setFixedWidth(60)

        self.stop_time_input = QSpinBox(self)
        self.stop_time_input.setRange(0, 5)
        self.stop_time_input.setValue(0)
        self.stop_time_input.setFixedSize(70, 40)

        stop_layout.addWidget(stop_label)
        stop_layout.addWidget(self.stop_time_input)
        stop_layout.addStretch()
        layout.addLayout(stop_layout)

        # Run button
        self.run_button = QPushButton("Run", self)
        self.run_button.setFixedSize(100, 40)
        layout.addWidget(
            self.run_button,
            alignment=Qt.AlignmentFlag.AlignCenter,
        )
        self.run_button.clicked.connect(self.run_app)

        # Main Window Layout
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)
        self.setFixedSize(600, 400)
        self.setLayout(layout)
        self.show()

    def browse_file(self):
        """
        Opens a file dialog to select an executable file.
        Sets the selected file path to the app_input field.
        """
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Open File", "", "Executable Files (*.exe)"
        )
        if file_path:
            self.app_input.setText(file_path)

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
                self, "Input Error", "Please select an executable file."
            )
            return

        try:
            start_time = int(start_time)
            stop_time = int(stop_time)
            if not 0 <= start_time < stop_time < 5:
                raise ValueError(
                    "Oopsie daisy, start time must be less than stop time, "
                    "and both should be in the range of [0,5]"
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
                    "-override",
                    f"startTime={start_time},stopTime={stop_time}",
                ],
                capture_output=True,
                text=True,
                check=True,
            )
            QMessageBox.information(
                self,
                "SUCCESS",
                f"Successful execution!\n\nOutput:\n{result.stdout}",
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
                self,
                "OS Error",
                f"OS error occurred: {str(e)}",
            )
        # Debugging information
        except Exception as e:
            QMessageBox.critical(
                self, "Unexpected Error", f"Failed to run application:{str(e)}"
            )
            print(f"Exception: {e}")
            print(f"app_path: {app_path}")
            print(f"start_time: {start_time}")
            print(f"stop_time: {stop_time}")


# main execution of program
# this runs the GUI application
if __name__ == "__main__":
    # no CLI here, everything happens on the active window
    app = QApplication([])
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
