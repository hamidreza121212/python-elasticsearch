import os


def create_directories(base_dir: str, directories: list[tuple[str]]) -> None:
    """
    Creates a series of directories based on the input parameters.

    Args:
    - base_dir (str): The base directory in which the subdirectories will be created.
    - directories (list of tuples): A list of tuples where each tuple represents a subdirectory to create. 
      The first element of each tuple is the name of the subdirectory, and the rest of the elements (if any) 
      represent subdirectories within the previous directory.

    Example:
    base_dir = '/path/to/base'
    directories = [('logs',), ('logs', 'auth'), ('logs', 'core')]
    create_directories(base_dir, directories)

    This will create the following directories:
    - /path/to/base/logs
    - /path/to/base/logs/auth
    - /path/to/base/logs/core
    """

    parent_directory_path = os.path.abspath(os.path.join(base_dir, os.pardir))
    for directory in directories:
        path = os.path.join(parent_directory_path, *directory)
        if not os.path.exists(path):
            os.makedirs(path)