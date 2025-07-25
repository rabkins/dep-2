import click
import sys


def main():
    print(f"Hello from dep-2 with click={click.__version__}")


if __name__ == "__main__":
    sys.exit(main())
