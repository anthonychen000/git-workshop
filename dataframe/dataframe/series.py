class Series:
    """
    A class to represent a Series, a one-dimensional column (array) with a name.
    """

    def __init__(self, data: list[float], name: str):
        """
        Initialize the Series with data and a name.

        :param data: A list of numerical data.
        :param name: The name of the series (e.g., column name).
        """
        self.data = data
        self.name = name

    def __repr__(self) -> str:
        """Return a string representation of the Series."""
        return f"Series(name={self.name}, data={self.data})"

    def sum(self) -> float:
        """Return the sum of the data in the series."""
        return sum(self.data)

    def max(self) -> float:
        """Return the maximum value in the series."""
        return max(self.data)

    def min(self) -> float:
        """Return the minimum value in the series."""
        return min(self.data)

    def mean(self) -> float:
        """Return the mean of the data in the series."""
        return sum(self.data) / len(self.data) if self.data else float('nan')

    def mode(self) -> float:
        """Return the mode of the data in the series."""
        from collections import Counter
        count = Counter(self.data)
        mode = max(count, key=count.get)
        return mode

    def unique_val(self) -> list:
        """Return the unique values in the series."""
        return list(set(self.data))

    def contains(self, value: float) -> bool:
        """
        Return if the series contains the value.

        :param value: The specific value being checked.
        """
        return value in self.data

    def replace(self, current_val: float, new_val: float) -> 'Series':
        """Return a new Series with a specific current value replaced with a new value.

        :param current_val: The current value. 
        :param new_value: The new value that will replace current value.
        """
        new_data = [new_val if x == current_val else x for x in self.data]
        return Series(new_data, self.name)

    def apply(self, func) -> 'Series':
        """
        Apply a mapping function to each element in the series and return a new Series.

        :param func: A function to apply to each element.
        :return: A new Series with the function applied.
        """
        new_data = [func(x) for x in self.data]
        return Series(new_data, self.name)
