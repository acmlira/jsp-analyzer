"""
JSP Analyzer business logic module
"""
import time
import re
import pandas

from filesystem import Directory
from configuration import ConfigurationFactory

class Analyzer:
    """
    JSP Analyzer business logic module
    """
    def __init__(self, base_path: str, relative_path: str, configuration_file: str):
        self.directory = Directory(base_path, relative_path)
        self.configuration = ConfigurationFactory(configuration_file).new()
        self.data = pandas.DataFrame(
            data=[file.absolute_path for file in self.directory.files()],
            columns=['File names'])

    def __number_of_lines(self) -> int:
        number_of_lines = []
        for file in self.directory.files():
            number_of_lines.append(len(file.get_lines()))
        return number_of_lines

    def __number_of_characters(self) -> int:
        number_of_characters = []
        for file in self.directory.files():
            number_of_characters.append(len(file.get_data()))
        return number_of_characters

    def __regex_values(self, regex: str) -> list[int]:
        def __matches(regex: str, content: str):
            """
            Return regex matches on content
            """
            return re.finditer(regex, content)

        values = []
        for file in self.directory.files():
            matches = __matches(regex, file.get_data())
            values.append(sum(1 for match in matches))
        return values

    def __regex_files(self, regex: str) -> list[int]:
        def __matches(regex: str, content: str):
            """
            Return regex matches on content
            """
            return re.finditer(regex, content)

        values = []
        for file in self.directory.files():
            matches = __matches(regex, file.get_data())
            values.append([match.group(0).replace('"', '') for match in matches])
        return values

    def analyze(self):
        """
        Run main procedure
        """
        if self.configuration.default_metrics:
            self.data['Number of lines'] = self.__number_of_lines()
            self.data['Number of characters'] = self.__number_of_characters()
        for regex_metrics in self.configuration.regex_metrics:
            self.data[regex_metrics.label] = self.__regex_values(regex_metrics.regex)

            if regex_metrics.files:
                self.data[f'{regex_metrics.label} files'] = self.__regex_files(regex_metrics.regex)

    def save(self, output_directory = "."):
        """
        Export data to .csv
        """
        return self.data.to_csv(
            f'{output_directory + "/"}jsp-analyzer-{int(round(time.time()))}.csv')
