# tlog

`tlog` is a logging library for Python that formats log messages with ISO 8601 timestamps.

## Installation

You can install `tlog` using pip:

`

## Usage

```python
from tlog import setup_logger

# Initialize the logger with the path where logs will be kept
log_path = 'path/to/your/logfile.log'
logger = setup_logger(log_path)

# Log some messages
logger.info("This is an info message.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")
`
```
