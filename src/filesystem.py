"""
Filesystem module
"""
import os

class File:
    """
    File class is responsible to handle file I/O
    """
    def __init__(self, absolute_path: str):
        self.absolute_path = absolute_path

    def get_data(self) -> str:
        """
        Return all file content
        """
        with open(self.absolute_path, 'r', encoding='UTF-8') as file:
            return file.read()

    def get_lines(self) -> list[str]:
        """
        Return all lines in list
        """
        return self.get_data().split("\n")

class Directory:
    """
    Directory class is responsible to handle workdir metadata +
    files in tree
    """
    def __init__(self, base_path: str, relative_path = ""):
        self.base_path = base_path
        self.relative_path = relative_path

    def files(self) -> list[File]:
        """
        Return the list of files in directory tree
        """
        file_list: list[File] = []
        for directory, _, files in os.walk(self.base_path + self.relative_path):
            if len(files) > 0:
                for file in files:
                    if file.endswith(".jsp"):
                        _, tail = os.path.split(file)
                        if tail[0].isupper():
                            file_list.append(File(f'{directory}/{file}'))

        return file_list
