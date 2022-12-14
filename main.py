from argparse import ArgumentParser

from ad_manager import AdManager


def main():
    parser = ArgumentParser()
    parser.add_argument("command", choices=['upload', 'print'], help="Command: one of [upload, print]")
    parser.add_argument("path", help="Path to csv file to be parsed")
    parser.add_argument("--entity_type", choices=['campaign', 'ad_group', 'ad'], required=False,
                        help="Entity type")
    parser.add_argument("--entity_id", type=int, required=False, help="Entity id")
    args = parser.parse_args()

    ads_manager = AdManager()
    if args.command == 'upload':
        ads_manager.upload(args.path)

    if args.command == 'print':
        ads_manager.print(args.path, args.entity_type, args.entity_id)


if __name__ == "__main__":
    main()
