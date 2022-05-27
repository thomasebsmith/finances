"""A program for simulating personal finances."""

from argparse import ArgumentParser


def main():
    """Simulates personal finances."""
    parser = ArgumentParser(description="Simulate personal finances.")
    args = parser.parse_args()
    print("Hello from simulate!")
    print(args)


if __name__ == "__main__":
    main()
