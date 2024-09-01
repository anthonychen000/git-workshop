from .series import Series

class DataFrame:
    """
    A class to represent a DataFrame, which is a collection of Series.
    """

    def __init__(self, data: list[Series]):
        """
        Initialize the DataFrame with a list of Series.

        :param data: A list of Series objects.
        """
        self.data = data
        self.columns = [series.name for series in data]
        self._validate()


    def _validate(self):
        """
        Validate that the series names are unique and all series have the same length.
        """
        # Check if all series have the same length
        if len(set(len(series.data) for series in self.data)) != 1:
            raise ValueError("All Series in the DataFrame must have the same length.")
        # Check if column names are unique
        if len(self.columns) != len(set(self.columns)):
            raise ValueError("Column names must be unique.")


    def __repr__(self) -> str:
        """Return a string representation of the DataFrame."""
        column_str = " | ".join(self.columns)
        rows_str = "\n".join(" | ".join(map(str, row)) for row in zip(*[series.data for series in self.data]))
        return f"{column_str}\n{rows_str}"


    def shape(self) -> tuple[int, int]:
        """
        Return the shape of the DataFrame (rows, columns).
        """
        return (len(self.data[0].data), len(self.columns))


    def head(self, n: int = 5) -> DataFrame:
        """
        Returns a new DataFrame with the first n rows.

        :param n: Number of rows to return.
        :return: A new DataFrame with the first n rows.
        """
        # TODO: Person 1 - Implement this function
        return DataFrame(self.data[:n], columns=self.columns)


    def tail(self, n: int = 5) -> DataFrame:
        """
        Returns a new DataFrame with the last n rows.

        :param n: Number of rows to return.
        :return: A new DataFrame with the last n rows.
        """
        # TODO: Person 2 - Implement this function


    def add_column(self, series: Series) -> None:
        """
        Add a new Series (column) to the DataFrame.

        This operation is done in-place.

        :param series: The Series object to add as a new column.
        """
        # TODO: Person 1 - Implement this function
        # Ensure the length of the series matches the number of rows in the DataFrame
        if len(series) != len(self.data):
            raise ValueError("Length of the series must match the number of rows in the DataFrame.")

        # Append the new series to the existing data
        for i in range(len(self.data)):
            self.data[i].append(series[i])

        # Update the columns attribute with the new column name
        self.columns.append(series.name)


    def drop_column(self, column_name: str) -> None:
        """
        Drop a column from the DataFrame.

        This operation is done in-place.

        :param column_name: The name of the column to drop.
        """
        # TODO: Person 2 - Implement this function


    def get_column(self, column_name: str) -> Series:
        """
        Returns the Series for a specific column.

        :param column_name: The name of the column to retrieve.
        :return: The Series object for the specified column.
        """
        # TODO: Person 1 - Implement this function
        # Check if the column name exists
        if column_name not in self.columns:
            raise KeyError(f"Column '{column_name}' does not exist in the DataFrame.")

        # Find the index of the column
        col_index = self.columns.index(column_name)

        # Extract the column data
        col_data = [row[col_index] for row in self.data]

        # Return as a Series object
        return Series(col_data, name=column_name)


    def set_column(self, column_name: str, values: list[float]) -> None:
        """
        Set the data for a specific column.

        This operation is done in-place.

        :param column_name: The name of the column to set.
        :param values: A list of data to set for the specified column.
        """
        # TODO: Person 2 - Implement this function


    def remove_duplicates(self) -> None:
        """
        Removes duplicate rows from the DataFrame.

        This operation is done in-place.
        """
        # TODO: Person 1 & 2 - Implement this function
        # Either code together or have one person code and the other review
        # If coding together, use pair programming & co-author the commit (git commit -m "message" -m "Co-authored-by: name <email>")
        # If reviewing, leave comments on what you think can be improved


    def combine_columns(self, col1: str, col2: str, new_col: str, operation: callable) -> None:
        """
        Combines two columns in the DataFrame based on a specified operation.

        This operation is done in-place.

        :param col1: The name of the first column.
        :param col2: The name of the second column.
        :param new_col: The name of the new column to create.
        :param operation: A function that takes two arguments and returns a value (e.g., addition, multiplication).
        """
        # TODO: Person 1 & 2 - Implement this function
        # Either code together or have one person code and the other review
        # ...


    def concatenate_vertically(self, other: DataFrame) -> None:
        """
        Concatenates another DataFrame to the current DataFrame vertically (adding rows).

        This operation is done in-place.

        :param other: Another DataFrame object to concatenate vertically.
        """
        # TODO: Person 1 - Implement this function
        # Ensure the columns match between the two DataFrames
        if self.columns != other.columns:
            raise ValueError("The columns of the two DataFrames must match.")

        # Extend the data with the rows from the other DataFrame
        self.data.extend(other.data)


    def concatenate_horizontally(self, other: DataFrame) -> None:
        """
        Concatenates another DataFrame to the current DataFrame horizontally (adding columns).

        This operation is done in-place.

        :param other: Another DataFrame object to concatenate horizontally.
        """
        # TODO: Person 2 - Implement this function


    def remove_na(self) -> DataFrame:
        """Return DataFrame that has all rows containing NaN values removed.
        NaN means Not a Number and is when values are missing or undefined.

        This operation is NOT done in-place.
        """
        # TODO: Person 1 - Implement this function
        # Importing the necessary module to handle NaN values
        from math import isnan

        # Function to check if a value is NaN
        def is_nan(value):
            return value != value  # NaN is the only value in Python that is not equal to itself

        # Filter out rows that contain any NaN values
        filtered_data = [row for row in self.data if not any(is_nan(value) for value in row)]

        # Return a new DataFrame with the filtered data
        return DataFrame(filtered_data, columns=self.columns)

    def replace_na(self, value: float) -> DataFrame:
        """Return DataFrame that replaces NaN with the specific value.
        NaN means Not a Number and is when values are missing or undefined.

        This operation is NOT done in-place.

        :param value: New value that replaces NaN."""
        # TODO: Person 2 - Implement this function

    def apply(self, func, column: str = None) -> DataFrame:
        """
        Applies a function to a specific column or all elements in the DataFrame.

        This operation is NOT done in-place.

        :param func: A function to apply to each element.
        :param column: Name of the column to apply the function to (optional).
        """
        # TODO: Person 1 & 2 - Implement this function
        # Either code together or have one person code and the other review
        # ...
