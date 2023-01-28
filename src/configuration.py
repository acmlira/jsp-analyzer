"""
Configuration module
"""
import json

class Dict:
    """
    Config hold all configuration values
    """
    def __init__(self, dict_):
        self.__dict__.update(dict_)

class DefaultMetrics:
    """
    Helper class to parse configuration.json
    """
    def __init__(self, active: bool):
        self.active = active

class RegexMetrics:
    """
    Helper class to parse configuration.json
    """
    def __init__(self, label: str, regex: str, files: bool):
        self.label = label
        self.regex = regex
        self.files = files

class Configuration:
    """
    Hold all configuration values
    """
    def __init__(self,
                 default_metrics: DefaultMetrics,
                 regex_metrics: list[RegexMetrics]):
        self.default_metrics = default_metrics
        self.regex_metrics = regex_metrics

class ConfigurationFactory:
    """
    Factory class to produce Configuration objects
    """
    def __init__(self, path: str):
        file = open(path, encoding='UTF-8')
        file = file.read()
        self.dict_configuration = json.loads(file, object_hook=Dict)

    def __default_metrics(self) -> DefaultMetrics:
        return self.dict_configuration.default_metrics.active

    def __regex_metrics(self) -> list[RegexMetrics]:
        regex_metrics = []
        for regex_metric in self.dict_configuration.regex_metrics:
            regex_metrics.append(
                RegexMetrics(regex_metric.label, regex_metric.regex, regex_metric.files))
        return regex_metrics

    def new(self) -> Configuration:
        """
        Produce new Configuration object
        """
        return Configuration(self.__default_metrics(), self.__regex_metrics())
