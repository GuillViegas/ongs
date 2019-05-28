from enum import Enum


class EnumChoices(Enum):
    def as_tuple(self):
        return self.value, str(self)

    @classmethod
    def choices(cls):
        return[x.as_tuple() for x in list(cls)]