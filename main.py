"""
A destop GUI app for running OpenModelica simulations.
Allows users to select an executable file,
set time constraints, and run simulations.
Displays real-time output from the simulation process.
Efficient error handling is provided for unexpected errors.
Simple and easy-to-use interface for running simulations.
"""

import os
import sys
import subprocess
from PyQt6.QtCore import Qt
from PyQt6.QtGui import (
    QIcon,
    QPixmap,
    QLinearGradient,
    QPalette,
    QColor,
    QBrush,
)
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
    QTextEdit,
)


class MainWindow(QWidget):
    """
    Main window class for the OpenModelica Simulation App.
    Includes the user interface and functionality to run simulations.
    Also, the window size is adjusted to accommodate the output area.
    """

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """
        Initializes the user interface.
        """
        layout = QVBoxLayout()
        self.setWindowTitle("OpenModelica Simulation App")
        self.setWindowIcon(QIcon("./assets/icons8-mechanical-64.png"))

        # gradient background
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0.0, QColor("#4FACFE"))  # Lighter at the top
        gradient.setColorAt(1.0, QColor("#1D2671"))  # Darker at the bottom

        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(gradient))
        self.setPalette(palette)

        # Banner section
        banner_layout = QHBoxLayout()
        banner_label = QLabel(self)
        banner_pixmap = QPixmap("./assets/banner.png")
        banner_label.setPixmap(banner_pixmap)
        banner_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        banner_layout.addWidget(banner_label)
        layout.addLayout(banner_layout)

        # Executable path input section
        layout.addLayout(self._create_executable_input())

        # Time input section
        layout.addLayout(self._create_time_inputs())

        # Run button
        self.run_button = QPushButton("Run", self)
        self.run_button.setFixedSize(100, 40)
        self.run_button.clicked.connect(self.run_app)
        layout.addWidget(
            self.run_button,
            alignment=Qt.AlignmentFlag.AlignCenter,
        )

        # Output display section
        self.output_display = QTextEdit(self)
        self.output_display.setReadOnly(True)
        self.output_display.setFixedHeight(200)
        layout.addWidget(self.output_display)

        # Main layout settings
        layout.setSpacing(5)
        layout.setContentsMargins(20, 20, 20, 20)
        self.setFixedSize(600, 520)
        self.setLayout(layout)

    def _create_executable_input(self):
        """
        Input layout for selecting an executable file.
        Default placeholder text is set to guide the user.
        Also only .exe files are allowed to be selected.
        """
        exe_layout = QHBoxLayout()
        exe_label = QLabel("Executable Path:")
        exe_label.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        exe_label.setFixedWidth(110)

        self.app_input = QLineEdit(self)
        self.app_input.setPlaceholderText("Browse executables to launch")

        browse_button = QPushButton("Browse", self)
        browse_button.setFixedSize(90, 30)
        browse_button.clicked.connect(self.browse_file)

        exe_layout.addWidget(exe_label)
        exe_layout.addWidget(self.app_input)
        exe_layout.addWidget(browse_button)

        return exe_layout

    def _create_time_inputs(self):
        """
        Layout for time input fields (start and stop time).
        Center Alignment is used for better visual appearance.
        Default value before selection is set to 0.
        """
        time_layout = QVBoxLayout()
        time_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        time_layout.setSpacing(10)
        time_layout.setContentsMargins(0, 2, 0, 0)

        # Start Time Layout (centered because it works better with UI)
        start_layout = QHBoxLayout()
        start_layout.setSpacing(0)
        start_label = QLabel("Start Time:")
        start_label.setAlignment(
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
        )
        start_label.setFixedWidth(70)
        self.start_time_input = QSpinBox(self)
        self.start_time_input.setRange(0, 5)
        self.start_time_input.setFixedSize(70, 30)

        start_layout.addWidget(start_label)
        start_layout.addWidget(self.start_time_input)

        # Stop Time Layout (centered because it works better with UI)
        stop_layout = QHBoxLayout()
        stop_layout.setSpacing(0)
        stop_label = QLabel("Stop Time:")
        stop_label.setAlignment(
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
        )
        stop_label.setFixedWidth(70)
        self.stop_time_input = QSpinBox(self)
        self.stop_time_input.setRange(0, 5)
        self.stop_time_input.setFixedSize(70, 30)

        stop_layout.addWidget(stop_label)
        stop_layout.addWidget(self.stop_time_input)

        time_layout.addLayout(start_layout)
        time_layout.addLayout(stop_layout)

        return time_layout

    def browse_file(self):
        """
        Opens a file dialog to select an executable file.
        Only .exe files are allowed to be selected.
        No other file types are allowed.
        """
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Open File", "", "Executable Files (*.exe)"
        )
        if file_path:
            self.app_input.setText(file_path)

    def run_app(self):
        """
        Runs the application with
        the provided executable path & time constraints.
        Streams real-time output to the display.
        Better error handling is provided for unexpected errors.
        """
        app_path = self.app_input.text().strip()
        start_time = self.start_time_input.value()
        stop_time = self.stop_time_input.value()

        # Validate inputs
        if not os.path.exists(app_path):
            QMessageBox.critical(
                self, "File Error", "The executable file path is invalid!"
            )
            return

        if not (0 <= start_time < stop_time <= 5):
            QMessageBox.critical(
                self,
                "Input Error",
                "Start time must be < stop time, with both in range [0,5].",
            )
            return

        working_dir = os.path.dirname(app_path)
        output_file = os.path.join(working_dir, "simulation_res.mat")

        command = [
            # Override default settings as per documentation
            # adjusted step-size to 0.002
            app_path,
            "-inputPath=" + working_dir,
            "-override",
            f"startTime={start_time},stopTime={stop_time},stepSize=0.002",
            "-r=" + output_file,
            "-lv=LOG_STDOUT,LOG_STATS",
        ]

        # Clear previous output and display status message
        self.output_display.clear()
        self.output_display.setText("Application is running...")

        try:
            # Run the subprocess and stream output
            process = subprocess.Popen(
                command,
                cwd=working_dir,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                env=os.environ.copy(),
            )

            # Read and display output in real-time
            if process.stdout:
                for line in iter(process.stdout.readline, ""):
                    self.output_display.append(line.strip())

            process.wait()

            # Check the return code and display the result
            if process.returncode == 0:
                self.output_display.append(
                    "\nSimulation completed successfully!"
                )  # noqa
                self.output_display.append(
                    f"Output file generated at: {output_file}"
                )  # noqa
            else:
                error_output = (
                    process.stderr.read()
                    if process.stderr
                    else "Unknown error occurred."
                )  # noqa
                self.output_display.append(
                    f"\nSimulation failed:\n{error_output}",
                )

        except Exception as e:
            QMessageBox.critical(
                self,
                "Execution Error",
                f"Unexpected error: {e}",
            )


# Main execution of the program
if __name__ == "__main__":
    app = QApplication([])
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
