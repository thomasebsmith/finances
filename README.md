# Finances
**Warning: This project may be out of date or inaccurate. It does not attempt
to provide financial advice. Use it at your own risk!**

This project provides a Python library that you can use for analyzing and
simulating finances. It is designed for dealing with United States financial
law. It includes tax estimation functionality and will be extended to include
financial simulation functionality in the future.

## Prerequisites
You will need:
- Python >= 3.8
- POSIX sh (to run testing/linting scripts)

## Quick Start
It is recommended to install and run this library in a virtual environment.
However, doing so is not required.

To run an example program that uses this library:
```sh
$ git clone https://github.com/thomasebsmith/finances.git
$ cd finances
$ python3 -m src.finances.__main__
```

To run this library's unit tests (this will automatically create a virtual
environment and install test dependencies in it):
```sh
$ git clone https://github.com/thomasebsmith/finances.git
$ cd finances
$ ./scripts/test.sh
```

## Roadmap
### v0.1 - In Progress
- General financial utility classes
- Basic tax computations

### v0.2
- Basic financial simulations

## License
This library is released under the MIT License. See [LICENSE](./LICENSE) for
details.

## Copyright
This project is copyright © 2022 Thomas Smith.
