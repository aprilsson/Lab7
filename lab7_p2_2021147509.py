class Problem2:
    """
    A class to count the occurrences of alphabets in a given file.
    """

    def __init__(self, file_path):
        """
        Initialize the class with the file path.
        """
        self.file_path = file_path
        self.occurrences = {}
        self.text = self.read_file()

    def read_file(self):
        """
        Read the fil and return its content.
        """
        file = open(self.file_path, "r")
        text = file.read()
        file.close()
        return text

    def count_alphabet(self):
        """
        Count the occurrences of each alphabet in the text.
        """
        for char in self.text:
            if char.isalpha():
                char_lower = char.lower()
                # Increase the count of the current character
                self.occurrences[char_lower] = self.occurrences.get(char_lower, 0) + 1

    def print_sorted_counts(self):
        """
        Print the counts of each alphabet in descending order.
        """
        # Sort the counts in descending order
        sorted_counts = sorted(
            self.occurrences.items(), key=lambda x: x[1], reverse=True
        )

        # Convert the alphabet to upper case
        list = [alphabet.upper() for alphabet, _ in sorted_counts]
        print(list)


file_path = "input_7_2.txt"

problem2 = Problem2(file_path)
problem2.count_alphabet()
problem2.print_sorted_counts()
