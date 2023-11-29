from typing import Self


class Distance:

    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return "Distance(km=" + str(self.km) + ")"

    def __add__(self, other: int | float | Self) -> Self:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        else:
            return Distance(self.km + other)

    def __iadd__(self, other: int | float | Self) -> Self:
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other: int | float | Self) -> Self:
        return Distance(self.km * other)

    def __truediv__(self, other: int | float | Self) -> Self:
        result = self.km / other
        return Distance(round(result, 2))

    def __lt__(self, other: int | float | Self) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        else:
            return self.km < other

    def __gt__(self, other: int | float | Self) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        else:
            return self.km > other

    def __eq__(self, other: int | float | Self) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        else:
            return self.km == other

    def __le__(self, other: int | float | Self) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        else:
            return self.km <= other

    def __ge__(self, other: int | float | Self) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        else:
            return self.km >= other
