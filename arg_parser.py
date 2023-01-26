import argparse


def arg_parser():
    parser = argparse.ArgumentParser(description="Argument Parser Example")
    parser.add_argument(
        "-n", "--name",
        type=str,
        dest="name",
        help="Name argument"
    )
    parser.add_argument(
        "-a", "--age",
        type=int,
        dest="age",
        help="Age argument"
    )
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = arg_parser()
    print(f"Name: {args.name}")
    print(f"Age:  {args.age}")
