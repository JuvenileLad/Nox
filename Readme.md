# Nox Project

## Installation and Setup

- First, create a virtual environment using the following command.
- Activate the virtual environment in a terminal window inside the Nox folder.
- Venv activation is crucial and cannot be skipped.

- If you are not using VSCode, manually install all the requirements listed in the `requirements.txt` file.

OR

- If you are using VSCode, press `Ctrl+Shift+P` and type "create environment" to select the first result. Choose the interpreter and allow installation of requirements from the `.txt` file. Wait for a few seconds until the process is completed.



## Running the Application

Due to limitations with Gunicorn on non-Linux systems, the project utilizes Waitress as the server. To run the application:

1. Ensure the virtual environment is active.

2. In the terminal, use the following command:
    ```
    python waitress_serve.py
    ```

3. The terminal should output 'Working!' without any further output unless an exception occurs.

## Customization

To customize the application behavior, modify the code within the `main.py` file.

## About

Chat-GPT helped create this readme.
