# unmask.py

"""
Unmasking rules
===============

All utilities for unmasking the data provided by Farplas.

Most of the routines in this module are "u-functions", that is,
functions meant to be applied (via `apply`) to a whole pandas Series object.

Some other routines are intended to work on a column level.
When this is the case, it is indicated in the corresponding docstring.

API
---

"""

import pandas as pd
import numpy as np
# Application date

_MONTH_OFFSET_QUARTER = 3

# Rules 49, 51, 55, 57, 61, 63, 67, 69, 73, 75, 79, 81
# utils for Rules 10, 11
# unittested
def quarter_to_date(x:str) -> int:
    """Converts a single digit character `x` to a number representing a month.
    The single digit passed represents the quarter to which
    the resulting month lies in.
    Use the `_MONTH_OFFSET_QUARTER` constant to set which
    month of the quarter to use.

    Parameters
    ----------
    x : str
        Single digit representing a quarter of a year

    Returns
    -------
    int
        Number of the month that the quarter represents
    
    Examples
    --------
    >>> quarter_to_date('3') # with _MONTH_OFFSET_QUARTER = 3
    9 # Third month of the third quarter

    Notes
    -----
    This function implements Rules 49, 51, 55, 57, 61, 63, 67, 69,
    73, 75, 79 and 81. It is also used as a utility for Rules 10 and 11.
    """
    if x == '-':
        r = pd.NA
    else:
        r = int(x) * _MONTH_OFFSET_QUARTER
    return r

# Rules 10 and 11
# unittested
def applydate_to_date(x) -> pd.Timestamp:
    """
    Takes a string in the format ABC, where:
    - A is the quarter of the month (1-4)
    - BC is the last two digits of the year

    Parameters
    ----------
    x : string
        Masked date

    Returns
    -------
    pd.Timestamp
        A pandas object identifying the date.
        The day is set to 1st of the month, and the time is set to 00:00:00.
        The month is set to the last month of the corresponding quarter.
    
    Examples
    --------
    >>> applydate_to_date('420') # with _MONTH_OFFSET_QUARTER = 3
    pd.Timestamp('2020-12-01 00:00:00')

    Notes
    -----
    This function implements Rules 10 and 11.
    It uses the :func:`~.unmask.quater_to_date` as a utility.
    """
    if not isinstance(x, str):
        x = str(x)  # ensure x is a string
    month = quarter_to_date(x[0])
    year = int("20" + x[1:])
    r = pd.Timestamp(day=1, month=month, year=year)
    return r

# NOT NEEDED if group
# Rule 15
# unittested
def birthdate_to_period_str(x: str) -> str:
    """Removes unnecessary characters from a string representing a year period.

    Parameters
    ----------
    x : str
        A string representing a year period

    Returns
    -------
    str
        A string representing a year period with no strange characters
    
    Notes
    -----
    This function implements Rule 15.
    Although it returns a string, it removes the <= or >= characters in front,
    which were deemed as unnecessary since we get the same information
    by just looking at the year string.
    """
    if x == '<=1975':
        r = "1975"
    elif x == '1997<=':
        r = "1997"
    else:
        r = x
    return r

# Rule 16
# unittested
def gender_to_str(x: str) -> str | pd.NA:
    """
    Converts a string `x` into a more informative string
    representing the gender.

    Parameters
    ----------
    x : str
        A masked string representing gender

    Returns
    -------
    str | pd.NA
        A string representing the gender, or an empty value
    
    Notes
    -----
    This function implements Rule 16.
    It uses 'M' for _masculine_ and `F` for _femenine_, as those were the only
    genders included in the data.
    """
    if x == 'X':
        # masc
        r = "M"
    elif x == "Y":
        # fem
        r = "F"
    else:
        r = pd.NA
    return r

# Rule 19
# unittested
def citizen_to_bool(x: str) -> bool:
    """Converts the masked nationality string to a boolean value

    Parameters
    ----------
    x : str
        A string with either `A` or `B`

    Returns
    -------
    bool
        Returns true if the candidate is from Turkey, and false otherwise

    Notes
    -----
    This function implements Rule 19.
    """
    r = bool(x == "A")
    return r

# Rule 21
# unittested
def cityplate_to_float(x: float) -> float:
    """
    Converts a masked number to another number representing the driving plate code of a city

    Parameters
    ----------
    x : float
        A floating point number

    Returns
    -------
    float
        The resulting floating point number representing the driving plate
        code of a city
    
    Notes
    -----
    This function implements Rule 21.
    Floating point numbers are used in order to handle empty values.
    """
    r = x - 3
    return r

# Rule 22
# unittested
def employsituation_to_bool(x: str) -> bool:
    """
    Converts a masked string to a boolean value representing if the applicant
    was working at the moment or not.

    Parameters
    ----------
    x : str
        A string, either 'A' or 'B'

    Returns
    -------
    bool
        Returns true if the applicant was working at the time,
        and false otherwise

    Notes
    -----
    This function implements Rule 22.
    """
    r = bool(x == "A")
    return r

# NOT NEEDED if group
# Rule 23
# unittested
def exptime_to_str(x) -> str:
    if x == '<=2':
        r = "2"
    elif x == '15+':
        r = "15"
    else:
        r = x
    return r

# Using INT because we don't have the full rule
# Rule 24
# unittested
def education_to_int(x) -> int:
    if x == "M":
        r = 1
    else:
        r = int(x[0])
    return r

# Rule 25
# unittested
def graduation_to_str(x) -> str:
    if x == 0:
        r = "Graduated"
    elif x == -1:
        r = "Student"
    elif x == -2:
        r = "Dropped"
    else:
        r = pd.NA
    return r

# Illegal?
# Rule 26
# unittested
def disability_to_bool(x) -> bool:
    r = bool(x == 0) # Engelli = Disabled
    return r

# Rule 29
# FATAL: Missing information
def military_to_str(x) -> str:
    if x == 4:
        r = "Finished"
    elif x == 5:
        r = "Unfinished"
    elif x == 6:
        r = "Exempt"
    return r

# utils for Rules 34, 38, 42
# unittested
def rot24(x: str) -> str:
    _eng = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def rotation(k):
        return (_eng.find(k) + 24) % 26

    return ''.join([_eng[rotation(i)] for i in x])

# Rules 34, 38, 42
# unittested
def language_to_str(x) -> str:
    if x == '-':
        r = pd.NA
    else:
        r = rot24(x)
    return r

# Rules 35-37, 39-41, 43-45
# unittested
def langskill_to_str(x) -> int:
    lookup = dict(zip("ASDFGH", range(6)))
    if x in lookup.keys():
        r = lookup[x]
    else:
        r = pd.NA
    return r

# utils for Rules 48, 50, 54, 56, 60, 62, 66, 68, 72, 74, 78, 80
# unittested
def rev_caesar(x: str) -> int:
    _eng = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def match(k):
        return (_eng.find(k)) + 1

    return  int(''.join([str(match(i)) for i in x]))

# Rules 48, 50, 54, 56, 60, 62, 66, 68, 72, 74, 78, 80
# unittested
def expyears_to_date(x) -> pd.Timestamp:
    if x != "-":
        r = pd.Timestamp(str(2023 - rev_caesar(x)))
    else:
        r = pd.NA
    return r

# Rules 28, 30-33
# unittested
def slide_col(x, offset) -> pd.Series:
    r = pd.Series(np.roll(x.values, offset), index=x.index)
    return r
