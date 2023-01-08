from hypothesis import given
from hypothesis.strategies import from_regex
from location.postcodes import PostCode, PostCodeRegexes

"""
Property-based testing with the Hypothesis framework:
https://youtu.be/mkgd9iOiICc

Notes:
    - TDD: Arrange Act Assert   (describes what the test-code is doing)
    - BDD: Given When Then      (describes what a hypotheical user is doing with the feature under test)


    - Property-based testing is popular in functional programming (see Haskell "QuickCheck" framework)
"""

@given(from_regex(PostCodeRegexes.uk, fullmatch=True))
def test_uk_postcode_validation(test_postcode: str):
    print(test_postcode)
    assert PostCode(test_postcode)._raise_exception_if_postcode_invalid() is None

@given(from_regex(PostCodeRegexes.china, fullmatch=True))
def test_china_postcode_validation(test_postcode: str):
    print(test_postcode)
    assert PostCode(test_postcode)._raise_exception_if_postcode_invalid() is None
