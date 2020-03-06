# Calculator
 That is a simple calculator made with Python 3.8
 
 ## Libraries
  These are the libraries required to run the program.
 #### PyQt5
  ```
  pip install pyqt5
  ```
  This is used to build the GUI.
  UI was designed using the PyQt Designer tool.
 #### Regex
  ```
  pip install regex
  ```
  Regular Expressions was used to separate number every operator and put it in a list by code bellow:
  ```python
  numbers = re.split(r'[- + * /]', numbers)
  ```

