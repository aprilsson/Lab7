class not2DError(Exception):
    # Error for 1D list
    def __str__(self):
        return "[ERROR]: list is not 2D."


class unevenListError(Exception):
    # Error for uneven list
    def __str__(self):
        return "[ERROR]: inner lists are not same in length."


class improperMatrixError(Exception):
    # Error for incompatible matmul pair
    def __str__(self):
        return "[ERROR]: [a][b]*[c][d] not b==c."


def mul1d(arr1, arr2):
    # arr1 * arr2
    # [1,2,3] * [4,5,6]
    # return  1*4 + 2*5 + 3*6
    sum = 0
    for i in range(len(arr1)):
        sum += arr1[i] * arr2[i]
    return sum


class list_D2(list):
    def __init__(self, arr):
        """
        Initialize the objects with a 2D list.
        """

        # Check if arr is a 2D list
        for item in arr:
            if not isinstance(item, list):
                raise not2DError()

            # Check if there are no nested lists
            for subitem in item:
                if isinstance(subitem, list):
                    raise not2DError()

        # Check if all rows have the same length
        for item in arr:
            if len(item) != len(arr[0]):
                raise unevenListError()

        # Initialize the object with the 2D list if all checks pass
        self.extend(arr)

    def __str__(self):
        """
        Return a formatted string representation.
        """

        # Get the number of rows and columns in the 2D list
        rows = len(self)
        columns = len(self[0]) if rows > 0 else 0

        # Return a formatted string
        return f"list_2D: {rows}*{columns}"

    def transpose(self):
        """
        Returns new list_D2 instance which is transpose of itself.
        """

        # Create an empty list to store the transposed list
        trans_list = []

        # Iterate over columns in the list
        for i in range(len(self[0])):
            n_row = [self[j][i] for j in range(len(self))]
            trans_list.append(n_row)

        return list_D2(trans_list)

    def __matmul__(self, others):
        """
        Multiply the 2D list with another matrix and return the result.
        """

        # Check if the number of columns in the first matrix matches the number of rows in the second matrix
        if len(self[0]) != len(others):
            raise improperMatrixError()

        # Initialize a result list with zeros
        result = [[0] * len(others[0]) for _ in range(len(self))]

        for i in range(len(self)):
            for j in range(len(others[0])):
                # Calculate the dot product of the ith row of the first matrix and the jth column of the second matrix
                result[i][j] = mul1d(self[i], [row[j] for row in others])

        return list_D2(result)

    def avg(self):
        """
        Returns average value of itself.
        """

        # Calculate the total sum of all elements
        tot_sum = sum(sum(row) for row in self)

        # Calculate the total number of elements
        num_elements = sum(len(row) for row in self)

        # Calculate the average
        return tot_sum / num_elements if num_elements != 0 else 0.0
