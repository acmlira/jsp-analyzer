"""
Arguments module
"""
import argparse

class Arguments():
    """
    Arguments class
    """

    def __parser(self) -> argparse.ArgumentParser:
        parser = argparse.ArgumentParser()
        parser.add_argument('--base_path', help='Base directory absolute path you want to analyze')
        parser.add_argument('--relative_path',
                            help='Child directory you want to analyze',
                            default="")
        parser.add_argument('--configuration_file',
                            help='Path to config.json that define the metrics',
                            default="configuration.json")
        parser.add_argument('--output_directory', help="Path to output directory", default=".")

        return parser

    def __init__(self):
        args = self.__parser().parse_args()

        self.base_path: str = args.base_path
        self.relative_path: str = args.relative_path
        self.configuration_file: str = args.configuration_file
        self.output_directory: str = args.output_directory
