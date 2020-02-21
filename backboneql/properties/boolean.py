from pydantic.dataclasses import dataclass

from backboneql.base import BaseType


@dataclass
class Boolean(BaseType):
    value: bool

    def to_sql(self) -> str:
        return 'TRUE' if self.value else 'FALSE'