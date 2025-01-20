# **OpenModelica GUI Application**

This project involves two parts:  
1. **Compiling a model** using OpenModelica to create an executable program.  
2. **Building a Python-based GUI application** to run the executable with specified parameters.

---

## **Features**
- Intuitive and functional GUI.
- Input fields for:
  - **Executable File**: The compiled model.
  - **Start Time**: The simulation start time (integer).
  - **Stop Time**: The simulation stop time (integer).
- User specified `start time` and `stop time`.
- Pythonic and PEP 8-compliant code.
- Well-structured and modular design.
- Proper input validation and meaningful error messages.
---

## **Technologies Used**
Python 3.12.6
- `PyQt6 for GUI`
    - `PyQt6==6.8.0`
    - `PyQt6-Qt6==6.8.1`
    - `PyQt6_sip==13.9.1`

- Testing and Linting Tools
    - `black==24.10.0`
    - `flake8==7.1.1`
    - `pylint==3.3.3`

---

## **Installation Guide**

### **1. Prerequisites**
- **Install Python 3.6+**: Download and install from [Python.org](https://www.python.org/).
- **Install PyQt6**:
  ```bash
  pip install PyQt6
  ```
- **Install OpenModelica**: Download and install from [OpenModelica.org](https://www.openmodelica.org/).

---

### **2. Steps to Compile the Model**
1. **Download OpenModelica** and install it on a Windows 10/11 machine.  
2. Open the **OMEdit (OpenModelica Connection Editor)**.  
3. Download the **TwoConnectedTanks** model package from the provided link.  
4. **Load the model** in OMEdit:
   - Go to `File > Open Model/Library File` and select the model file.  
5. **Build (Compile) the Model**:
   - Select the `TwoConnectedTanks` model and click the **Simulate** button.
   - The compiled executable and its dependent files will be saved in the working directory.

---

### **3. Run the Python GUI**
1. Fork the repo.
2. Clone this repository:
   ```bash
   git clone https://github.com/user_name/OpenModelica-GUI
   cd OpenModelica-GUI
   ``` 
3. Run the Python application:
   ```bash
   python main.py
   ```

---

## **Usage**
1. Launch the GUI application.  
2. Use the **Browse** button to select the compiled executable.  
3. Enter valid `start time` and `stop time` (integer values, ensuring `0 <= start time < stop time < 5`).  
4. Click the **Run** button.

---
Here’s the **Testing** section in Markdown format:

---

## **Testing the Code**

This project uses **Flake8**, **Black**, and **Pylint** to ensure high code quality, proper formatting, and adherence to PEP 8 guidelines.

### **1. Install Linters and Formatters**
First, ensure all necessary testing dependencies are installed:
```bash
pip install -r requirements_test.txt
```

### **2. Testing Tools**

#### **a. Code Formatting with Black**
Run Black to format your code automatically:
```bash
black .
```

#### **b. Code Linting with Flake8**
Use Flake8 to check for PEP 8 violations and other linting issues:
```bash
flake8 .
```

#### **c. Static Analysis with Pylint**
Run Pylint for an in-depth code analysis and suggestions:
```bash
pylint main.py
```

---
## **Adherence to Requirements**:
   - Handles `0 <= start time < stop time < 5` validation correctly.
   - Successfully executes the model via the GUI.

---

## **References**
- [OpenModelica User's Guide](https://openmodelica.org/doc/OpenModelicaUsersGuide/latest/simulationflags.html#simflag-override)  
- [Python PEP 8 Guidelines](https://peps.python.org/pep-0008/)  

---

Made by [Garima](https://github.com/techy4shri)👩‍💻
