"""A program for simulating personal finances."""

from argparse import ArgumentParser
from typing import cast

from finances import Money

from .simulation import Simulation


def main() -> None:
    """Simulates personal finances."""
    parser = ArgumentParser(description="Simulate personal finances.")
    parser.add_argument(
        "--start",
        metavar="YEAR",
        type=int,
        required=True,
        help="The year in which to start the simulation",
    )
    parser.add_argument(
        "--end",
        metavar="YEAR",
        type=int,
        required=True,
        help="The year in which to end the simulation",
    )
    parser.add_argument(
        "--starting-balance",
        metavar="MONEY",
        type=Money.parse,
        required=True,
        help="The balance to start the simulation with, in USD",
    )
    args = parser.parse_args()

    simulation = Simulation(
        cast(int, args.start),
        cast(int, args.end),
        cast(Money, args.starting_balance),
    )

    simulation.run()


if __name__ == "__main__":
    main()
