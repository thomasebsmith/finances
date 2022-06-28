# Finances
**Warning: This project may be out of date or inaccurate. It does not attempt
to provide financial advice. Use it at your own risk!**

This project provides a Python library and CLI that you can use for analyzing
and simulating finances. It is designed for dealing with United States financial
law. It includes tax estimation functionality and will be extended to include
financial simulation functionality in the future.

## Prerequisites
You will need:
- Git (to clone this repository)
- Python >= 3.8 (to use this library)
- POSIX sh (to run the testing and linting scripts)

## Quick Start
It is recommended to install and run this library in a virtual environment.
However, doing so is not required.

To run an example program that uses this library (this will automatically
create a virtual environment):
```sh
$ git clone https://github.com/thomasebsmith/finances.git
$ cd finances
$ . ./scripts/venv.sh
$ pip install .
$ finances
```

To run this library's unit tests (this will automatically create a virtual
environment and install test dependencies in it):
```sh
$ git clone https://github.com/thomasebsmith/finances.git
$ cd finances
$ ./scripts/test.sh
```

To lint this repository's code (this will automatically create a virtual
environment and install linting dependencies in it):
```sh
$ git clone https://github.com/thomasebsmith/finances.git
$ cd finances
$ ./scripts/lint.sh
```

## Roadmap
### v0.1 - In Progress
- General financial utility classes
- Basic tax computations

### v0.2
- Basic financial simulations

### v0.3
- Financial simulations based on historical data

## License
This library is released under the MIT License. See [LICENSE](./LICENSE) for
details.

## Copyright
This project is copyright © 2022 Thomas Smith.
