import re
from dataclasses import dataclass

"""
Different methods of postcode validation:
https://ideal-postcodes.co.uk/guides/postcode-validation
"""

class InvalidPostCode(Exception):
    pass

@dataclass(frozen=True)
class PostCode(str):
    """
    A postcode class with some bulit-in validation.
    Behaves like a string that throws an Exception
    when an invalid postcode is passed as input.
    """
    postcode: str

    @property
    def _list_of_valid_postcode_regexes(self) -> list[str]:
        """ Add all postcode regexes to this list so they can be called internally. """

        return [

            # https://ideal-postcodes.co.uk/guides/postcode-validation
            # (UK)
            r"^[a-zA-Z]{1,2}\d[a-zA-Z\d]?\s*\d[a-zA-Z]{2}$",

            # https://gist.github.com/jamesbar2/1c677c22df8f21e869cca7e439fc3f5b
            # (China)
            r"^\d{6}$",
        ]

    def _raise_exception_if_postcode_invalid(self) -> None:
        """ Does not guarantee the postcode is real, only that it matches a valid format. """

        if type(self.postcode) is not str:
            raise ValueError("postcode must be of type str")
        for regex in self._list_of_valid_postcode_regexes:
            if type(re.search(regex, self.postcode)) is re.Match:
                return None
        raise InvalidPostCode(
            f"'{self.postcode}'did not match any of the valid postcode regexes:\n"
            f"{self._list_of_valid_postcode_regexes}"
        )

    def __post_init__(self):
        self._raise_exception_if_postcode_invalid()
