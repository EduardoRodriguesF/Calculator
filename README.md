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
 
 ## Setting up
  Assuming you already have Python and `pip` installed, to run the program you will need to get the following packages:
  * PyQt5
  * Regex
  * Math
  For that, you just need to use the commands bellow in your Command prompt:
  ```
  > pip install pyqt5 regex math
  ```
Now you should be able to use it by running `script.py`
