import logging.config
import tomllib
from typing import Dict, Any

def configure_logging(file_path) -> Dict[str, Any]:
    """
    Configure logging using settings from a 'logging.toml' file.

    This function reads the 'logging.toml' file, which contains logging configuration
    settings in TOML format, and configures the Python logging system accordingly.

    If the file is not found or contains invalid TOML syntax, exceptions are raised.

    Returns:
        Dict[str, Any]: A dictionary representing the logging configuration.

    Raises:
        FileNotFoundError: If 'logging.toml' file is not found.
        ValueError: If 'logging.toml' file contains invalid TOML syntax.

    Example usage:
    ```
    try:
        log_config = configure_logging()
        # Start using the configured logging system
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    ```
    """
    try:
        with open(file_path, mode='rb') as config_file:
            log_conf_dict = tomllib.load(config_file)
            logging.config.dictConfig(log_conf_dict)
    except FileNotFoundError as e:
        msg = f"The {file_path} file does not exist!"
        raise FileNotFoundError(msg) from e
    except tomllib.TOMLDecodeError as e:
        msg = f"The {file_path} file contains invalid TOML syntax! Error: {e}"
        raise ValueError(msg) from e

    return log_conf_dict

