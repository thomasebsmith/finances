# Finances
**Warning: This project may be out of date or inaccurate. It does not attempt
to provide financial advice. Use it at your own risk!**

This project provides a Python library and CLI that you can use for analyzing
and simulating finances. It is designed for dealing with United States financial
simulation and law. It includes tax estimation functionality and is being
extended to include financial simulation functionality.

## Prerequisites
You will need:
- Git (to clone this repository)
- Python >= 3.8 (to use this library and CLI)
- Python support for virtual environments (to run the provided scripts)
- POSIX-compatible sh (to run the provided scripts)

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
- Correct use of tax terminology (AGI vs MAGI vs taxable income, deductions vs
  adjustments) in API
- Basic financial simulations (inflation, investment returns, etc.)
- Probabilistic variable ranges and distributions
- Confidence intervals based on variable distributions over time
- Account abstraction (with ability to transfer among accounts and ability to
  store variable distributions)
- Thorough unit testing of basic types and simulations

### v0.3 (in planning stages)
- Detailed historical tax calculations (United States only)
- Alternative minimum tax support (United States only)
- Financial simulations based on historical market and inflation data (United
  States only)
- Deduction and adjustment eligibility checking (United States only)

### v0.4
- Simulated financial predictions
- Simulation performance optimizations
- Historical prediction accuracy analysis and adjustments

## Future Ideas
In future versions after v0.4, this project could include:
- A tax calculation GUI (with interactive explanations)
- A simulation GUI (including visualizations of possible outcomes, confidence
  intervals, etc.)
- An optimizer for desired financial outcomes
- Simulation data and tax calculations for locations outside the United States
- Data about other types of investment assets (commodities, real estate,
  derivatives, etc.) integrated into the predictor and optimizer

## Contributing
To contribute to this project, please open an issue if one does not exist for
your desired feature or bug fix. Then, feel free to comment that you are working
on that issue and create a corresponding PR. Your PR will be reviewed and
hopefully approved for merge when it is ready.

## License
This project is licensed as open source software under the MIT License. See
[LICENSE](./LICENSE) for details.

## Copyright
This project was originally created by Thomas Smith and is copyright © 2022-2023
Thomas Smith.
