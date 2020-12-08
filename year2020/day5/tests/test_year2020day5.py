import pytest

from year2020.day5.year2020day5 import Seat


@pytest.mark.parametrize(
    "seat_specifier,row,column,seat_id",
    [
        ("BFFFBBFRRR", 70, 7, 567),
        ("FFFBBBFRRR", 14, 7, 119),
        ("BBFFBBFRLL", 102, 4, 820),
    ],
)
def test_seat(seat_specifier, row, column, seat_id):

    seat = Seat.from_specifier(seat_specifier)
    assert seat.row == row
    assert seat.column == column
    assert seat.id == seat_id
