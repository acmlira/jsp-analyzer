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
        files: list[File] = []
        for directory, _, file in os.walk(self.base_path + self.relative_path):
            files.append(File(f'{directory}/{file[0]}'))
        return files
