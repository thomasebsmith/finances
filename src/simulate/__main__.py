"""A program for simulating personal finances."""

from argparse import ArgumentParser

from .simulation import Simulation


def main():
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
    args = parser.parse_args()

    simulation = Simulation(args.start, args.end)
    simulation.run()


if __name__ == "__main__":
    main()
