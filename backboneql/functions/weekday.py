from typing import Union

from typing_extensions import Literal

from backboneql.functions.base import BaseFunction
from backboneql.properties.property import Property
from backboneql.properties.constant import Constant


class Weekday(BaseFunction):
    obj: Literal['weekday'] = 'weekday'
    property: Union[Property, BaseFunction, Constant]
    alias: str = None

    def to_sql(self) -> str:
        # TODO: postgresql
        sql = f"WEEKDAY({self.property})"

        if self.alias is not None:
            sql = f"{sql} AS {self.alias}"

        return sql
