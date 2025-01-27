# **OpenModelica GUI Application**

This project involves two parts:

1. **Compiling a model** using OpenModelica to create an executable program.
2. **Building a Python-based GUI application** to run the executable with specified parameters.

---

## **Features**

- **Intuitive and functional GUI**: Easy-to-use interface for running simulations.
- **Input fields for**:
  - **Executable File**: The compiled model.
  - **Start Time**: The simulation start time (integer).
  - **Stop Time**: The simulation stop time (integer).
- **User-specified time constraints**: Allows users to set `start time` and `stop time`.
- **Pythonic and PEP 8-compliant code**: Ensures readability and maintainability.
- **Well-structured and modular design**: Organized codebase for easy navigation and modification.
- **Proper input validation and meaningful error messages**: Ensures robust and user-friendly experience.

---

## **Technologies Used**

- **Python 3.12.6**
- **PyQt6 for GUI**:
  - `PyQt6==6.8.0`
  - `PyQt6-Qt6==6.8.1`
- **OpenModelica**: For compiling the model into an executable.

---

## **Installation**

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/OpenModelica-GUI.git
   cd OpenModelica-GUI
   ```

2. **Create a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

---

## **Usage**

1. **Run the GUI application**:

   ```bash
   python main.py
   ```

2. **Using the GUI**:
   - **Browse**: Select the compiled executable file.
   - **Set Start Time**: Enter the simulation start time.
   - **Set Stop Time**: Enter the simulation stop time.
   - **Run**: Click the "Run" button to start the simulation.

---

## **License**

This project is licensed under the MIT License. See the LICENSE file for details.

---

## **Acknowledgements**

- **OpenModelica**: For providing the tools to compile the model.
- **PyQt6**: For the GUI framework.

---
