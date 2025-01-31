# **OpenModelica Simulation Desktop App**
This project is designed to streamline the process of running simulations generated from OpenModelica models through a user-friendly **Python GUI** application built with **PyQt6**.
For detailed documentation, including model changes, code improvements, and troubleshooting, visit the [**Project Wiki**](https://github.com/techy4shri/OpenModelica-GUI/wiki).
</br>
The task involves:
1. **Compiling a model** (e.g., TwoConnectedTanks) using OpenModelica to create an executable.
2. **Building a GUI application** that runs the executable with adjustable parameters like start and stop times.

---
### **Table of Contents**
1. [OpenModelica Simulation Desktop App](#openmodelica-simulation-desktop-app)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Installation](#installation)
   - [Clone the Repository](#clone-the-repository)
   - [Set up a Virtual Environment](#set-up-a-virtual-environment)
   - [Install Dependencies](#install-the-required-packages)
   - [Install OpenModelica](#install-openmodelica-if-not-already-installed)
   - [Set Environment Variables](#set-environment-variables)
5. [Usage Instructions](#usage-instructions)
   - [Running the Application](#running-the-application)
   - [Using the GUI](#in-the-gui)
6. [Project Structure](#project-structure)
7. [Simulation Flags](#simulation-flags)
8. [Troubleshooting](#troubleshooting)
   - [Common Issues](#common-issues)
9. [Contributing](#contributing)
10. [License](#license)
11. [Acknowledgements](#acknowledgements)

---

## **Project Structure**
```
OpenModelica-GUI/
├── .github/                             # GitHub-related files (workflows, issue templates, etc.)
├── .venv/                               # Python virtual environment directory (optional)
├── .vscode/                             # VS Code configuration directory (settings, launch configurations, etc.)
├── assessts/
  └── banner.png                         # Banner image used in the GUI application
  └── icons8-mechanical-64.png           # Application logo displayed on the window
├── NonInteractingTanks/                 # Directory containing the Tank and Tank2 Modelica files
├── NonInteractingTanks.TwoConnectedTanks/  # Directory for the compiled executable and dependencies
├── main.py                              # Main Python script for running the GUI application
├── requirements.txt                     # Python dependencies for the project
├── pyproject.toml                       # Project configuration file (e.g., for linters and formatters)
├── .pylintrc                             # Pylint configuration file
├── .pre-commit-config.yaml              # Pre-commit hooks configuration
├── LICENSE                              # License information for the project
└── README.md                            # Project documentation (overview, features, usage)
```
---

## **Features**

- **Intuitive and functional GUI**: Simplifies simulation execution.
- **Input fields**:
  - **Executable File**: Browse and select the compiled model executable.
  - **Start Time**: Set the simulation start time (`0 ≤ start time < stop time ≤ 5`).
  - **Stop Time**: Set the simulation stop time.
- **Output Display**: Real-time streaming of logs and results.
- **Input validation**: Ensures time constraints and valid file selection.
- **Error Handling**: Displays simulation errors, missing file issues, and environment variable problems.
- **Pythonic and PEP8-compliant code**: Code follows best practices with linters and formatters.
- **Project Linters and Formatters**:
  - **flake8**: For static code analysis.
  - **black**: For automatic formatting.

---

## **Technologies Used**

- **Python 3.6+**
- **PyQt6** (for GUI)
  - `PyQt6==6.8.0`
  - `PyQt6-Qt6==6.8.1`
- **OpenModelica**: For generating and running simulations.
- **Windows OS** (10/11)

---

## **Installation**

   ### **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/OpenModelica-GUI.git
   cd OpenModelica-GUI
   ```

   ### **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

   ### **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

   ### **Install OpenModelica** (if not already installed):
   - [Download OpenModelica](https://openmodelica.org)

   ### **Set environment variables**:
   Ensure that OpenModelica is added to your `PATH`.

---

## **Usage Instructions**

### **Running the Application**

1. Launch the application:
   ```bash
   python main.py
   ```

### **In the GUI**:
   - Use the **Browse** button to select the OpenModelica executable.
   - Enter the **Start Time** and **Stop Time** values.
   - Click **Run** to start the simulation.
   - View the output in the real-time display area.

---

## **Simulation Flags**

The executable is run with the following flags:
- **-override**: Allows dynamic setting of `startTime` and `stopTime`.
- **-lv=LOG_STDOUT,LOG_STATS**: Enables streaming logs for monitoring simulation progress.

For detailed documentation on simulation flags, visit the [OpenModelica Documentation](https://openmodelica.org/doc/OpenModelicaUsersGuide/latest/simulationflags.html).

---

## **Troubleshooting**

### **Common Issues:**
- **Missing DLLs:** Ensure all dependencies are present in the working directory.
- **Environment Variable Errors:** Add OpenModelica to the `PATH` variable.
- **Simulation Errors:** Verify input parameters and check the output logs for details.

---

## **Contributing**

- Currently not accepting contributions unless from FOSSEE.
- Please ensure your code adheres to PEP8 standards. 
- Run **flake8** and **black** before submitting pull requests.

---

## **License**

This project is licensed under the **MIT License**. See the [LICENSE](./LICENSE) file for details.

---

## **Acknowledgements**

- **OpenModelica**: For providing the simulation tools.
- **PyQt6**: For the graphical user interface library.
- **FOSSEE**: For providing the models for simulation.
- **Icon**: <a target="_blank" href="https://icons8.com/icon/43191/services">Mechanical</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
