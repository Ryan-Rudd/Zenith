import os
import inspect

def getDotZenith(path):
    calling_file = inspect.stack()[1].filename
    module_dir = os.path.dirname(os.path.abspath(calling_file))
    absolute_path = os.path.abspath(os.path.join(module_dir, path))

    try:
        with open(absolute_path, 'r') as file:
            contents = ""
            for line in file:
                contents += line
        return contents
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Error: File '{path}' not found.") from e
    except PermissionError as e:
        raise PermissionError(f"Error: Permission denied to read file '{path}'.") from e
    except IsADirectoryError as e:
        raise IsADirectoryError(f"Error: '{path}' is a directory, not a file.") from e
    except IOError as e:
        raise IOError(f"Error: Could not read file '{path}'.") from e
