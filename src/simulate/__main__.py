"""A program for simulating personal finances."""

from argparse import ArgumentParser


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
    print("Hello from simulate!")
    print(f"Starting in {args.start}")
    print(f"Ending in {args.end}")


if __name__ == "__main__":
    main()
