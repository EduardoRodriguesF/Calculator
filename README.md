# Calculator
 That is a simple calculator made with Python 3.8
 
 ## What have I learned with the project?
 #### GUI Design
 While using the PyQt5 Designer tool, I was able to learn about the software's workplace and how to use it in code to display whatever I want.
 #### Counting, separating and controlling strings
My calculator software was made in such a way that everytime you press a button, it adds it to a string displayed on top of the window, or it manipulates the string to involve certain numbers within functions.
```python
count = count[:index] + 'sqr(' + count[index:] + ')'
# the code above puts latest numbers after an operator (+, -, * or /) in between square function
# 'index' represents those numbers 
```

Once you press `=` the program uses `eval()`
 
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
 #### Math
  This library was needed to make the square root function
  ```python
  math.sqrt(x)
  ```

