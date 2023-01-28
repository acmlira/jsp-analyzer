"""
JSP Analyzer entrypoint module
"""
from arguments import Arguments
from analyzer import Analyzer

if __name__ == '__main__':
    args = Arguments()

    analyzer = Analyzer(args.base_path, args.relative_path, args.configuration_file)
    analyzer.analyze()
    analyzer.save(args.output_directory)
