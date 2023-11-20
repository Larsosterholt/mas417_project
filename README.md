# Project Setup Instructions


1. **Create and Activate a New Conda Environment**:
   - Open your command line interface and run:
     ```bash
     conda create --name myenv
     conda activate myenv
     ```

2. **Clone the Project Repository**:
   - Use the following commands to clone the project and navigate to the project directory:
     ```bash
     git clone https://github.com/Larsosterholt/mas417_project.git
     cd mas417_project
     ```

3. **Install Required Packages**:
   - Install the `nameTagLib` package using `pip`:
     ```bash
     pip install dist/nameTagLib-0.1.0.tar.gz
     ```

3. **Run the Name Tag Generator**:
   - Use the name tag generator from CLI by running `main.py`
     ```bash
     python3 main.py
     ```

     - Use the name tag generator from web-GUI by running `app.py`
     ```bash
     python3 app.py
     ```
     Then in a web browser open http://127.0.0.1:5000/ to use the model generator.
