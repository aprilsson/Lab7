import re


class Problem1:
    """
    A class to find declared functions and their calls in a given file.
    """

    def __init__(self, file):
        """
        Initialize the class with the file path.
        """
        self.file = file
        self.code = self.read_file()

    def read_file(self):
        """
        Read the file and return its text.
        """
        file = open(self.file, "r")
        code = file.read()
        file.close()
        return code

    def find_declared_functions(self):
        """
        Find all declared functions in the file.
        """

        # Regular expression pattern to find function declaration
        pattern = re.compile(r"\bdef\s+([a-zA-Z_]\w*)\s*\(")
        functions = pattern.findall(self.code)
        return functions

    def find_function_calls(self, functions):
        """
        Find all function calls.
        """
        code_lines = self.code.splitlines()

        # Initialize a dictionary to store function calls
        calls = {func: [] for func in functions}
        line_number = 1

        # Iterate over each line in the code
        for line in code_lines:
            # Check each function if it is called in the current line
            for func in functions:
                call_pattern = re.compile(r"\b" + re.escape(func) + r"\s*\(")
                if call_pattern.search(line):
                    calls[func].append(line_number)

            line_number += 1

        return calls

    def output(self):
        """
        Print the declared functions and their calls.
        """
        declared_functions = self.find_declared_functions()
        function_calls = self.find_function_calls(declared_functions)

        # Print each function and the lines where it is called
        for func, call_lines in function_calls.items():
            print(f"{func}: def in {call_lines.pop(0)}, calls in {call_lines}")


file_path = "input_7_1.txt"

problem = Problem1(file_path)
problem.output()
