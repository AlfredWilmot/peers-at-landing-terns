from ..weather import is_postcode_format_valid
from hypothesis import given
import hypothesis.strategies as st

"""
Property-based testing with the Hypothesis framework:
https://youtu.be/mkgd9iOiICc

Notes:
    - TDD: Arrange Act Assert   (describes what the test-code is doing)
    - BDD: Given When Then      (describes what a hypotheical user is doing with the feature under test)


    - Property-based testing is popular in functional programming (see Haskell "QuickCheck" framework)
"""

