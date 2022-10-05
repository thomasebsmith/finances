# Finances
**Warning: This project may be out of date or inaccurate. It does not attempt
to provide financial advice. Use it at your own risk!**

This project provides a Python library and CLI that you can use for analyzing
and simulating finances. It is designed for dealing with United States financial
law. It includes tax estimation functionality and is being extended to include
financial simulation functionality.

## Prerequisites
You will need:
- Git (to clone this repository)
- Python >= 3.8 (to use this library)
- Python support for virtual environments (to run scripts)
- POSIX-compatible sh (to run scripts)

## Quick Start
It is recommended to install and run this library in a virtual environment.
However, doing so is not required.

To run an example program that uses this library (this will automatically
create and use a virtual environment):
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
By v1.0, this project will contain a complete financial utilities and
simulation library and CLI.

### v0.1 (released 2022-07-17)
- General financial utility classes
- Basic tax computations
- Placeholder simulation utility
- Basic testing and linting

### v0.2 (in progress)
- Basic financial simulations (inflation, investment returns, etc.)
- Variable distributions
- Confidence intervals based on variable distributions over time
- Account abstraction (with ability to transfer among accounts and ability to
  store variable distributions)

### v0.3 (in planning stages)
- Detailed historical tax calculations
- Financial simulations based on historical market and inflation data
- Simulation performance optimizations

### v0.4
- Simulated financial predictions
- Historical prediction accuracy analysis and adjustments

## Future Ideas
In the future, this project could include:
- A tax calculation GUI
- A simulation GUI

## License
This library is released under the MIT License. See [LICENSE](./LICENSE) for
details.

## Copyright
This project is copyright © 2022 Thomas Smith.
