https://teclado.com/30-days-of-python/python-30-day-24-exceptions-advanced/

| Exception Name          | Description                                            | Example Code                                 |
|-------------------------|--------------------------------------------------------|----------------------------------------------|
| `ZeroDivisionError`     | Raised when division or modulo by zero is attempted.  | ```python result = 10 / 0```                |
| `ValueError`            | Raised when an invalid conversion is attempted.       | ```python num = int("abc")```               |
| `TypeError`            | Raised when an operation is performed on an incompatible data type. | ```python result = "5" + 10```  |
| `IndexError`            | Raised when an index is out of range in a sequence.   | ```python my_list = [1, 2, 3]```<br>```value = my_list[4]``` |
| `KeyError`              | Raised when trying to access a non-existent key in a dictionary. | ```python my_dict = {"name": "Alice"}```<br>```value = my_dict["age"]``` |
| `FileNotFoundError`     | Raised when attempting to open a non-existent file.   | ```python with open("non_existent_file.txt", "r") as file:```<br>```content = file.read()``` |
| `IOError`               | Raised for various I/O-related errors.                | ```python with open("/dev/full", "w") as file:```<br>```file.write("This will raise an IOError.")``` |
| `NameError`             | Raised when a local or global name is not found.     | ```python print(variable_that_does_not_exist)``` |
| `AttributeError`        | Raised when an attribute reference or assignment fails. | ```python obj.my_method()``` (when `obj` does not have `my_method()`) |


## All exceptions

- `BaseException`
  - `SystemExit`
  - `KeyboardInterrupt`
  - `GeneratorExit`
  - `Exception`
    - `StopIteration`
    - `StopAsyncIteration`
    - `ArithmeticError`
      - `FloatingPointError`
      - `OverflowError`
      - `ZeroDivisionError`
    - `AssertionError`
    - `AttributeError`
    - `BufferError`
    - `EOFError`
    - `ImportError`
      - `ModuleNotFoundError`
    - `LookupError`
      - `IndexError`
      - `KeyError`
    - `MemoryError`
    - `NameError`
      - `UnboundLocalError`
    - `OSError`
      - `BlockingIOError`
      - `ChildProcessError`
      - `ConnectionError`
        - `BrokenPipeError`
        - `ConnectionAbortedError`
        - `ConnectionRefusedError`
        - `ConnectionResetError`
      - `FileExistsError`
      - `FileNotFoundError`
      - `InterruptedError`
      - `IsADirectoryError`
      - `NotADirectoryError`
      - `PermissionError`
      - `ProcessLookupError`
      - `TimeoutError`
    - `ReferenceError`
    - `RuntimeError`
      - `NotImplementedError`
      - `RecursionError`
    - `SyntaxError`
      - `IndentationError`
        - `TabError`
    - `SystemError`
    - `TypeError`
    - `ValueError`
      - `UnicodeError`
        - `UnicodeDecodeError`
        - `UnicodeEncodeError`
        - `UnicodeTranslateError`
    - `Warning`
      - `DeprecationWarning`
      - `PendingDeprecationWarning`
      - `RuntimeWarning`
      - `SyntaxWarning`
      - `UserWarning`
      - `FutureWarning`
      - `ImportWarning`
      - `UnicodeWarning`
      - `BytesWarning`
      - `ResourceWarning`
