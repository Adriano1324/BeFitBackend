"""
This module contains function to get only selected fields
"""
from typing import Any

from sqlalchemy.inspection import inspect

from app.security.context import Info

from .convert_camel_case import convert_camel_case


def get_only_selected_fields(db_baseclass_name: Any, info: Info) -> list[Any]:
    """
    This function is used to load only selected fields
    """
    selections = []
    for field in list(info.selected_fields[0].selections):
        if field.name != "pageMeta":  # type: ignore
            selections.extend(field.selections)
    db_relations_fields = inspect(db_baseclass_name).relationships.keys()
    db_columns = db_baseclass_name.__table__.columns.keys()
    selected_fields = [
        getattr(db_baseclass_name, convert_camel_case(field.name))  # type: ignore
        for field in selections
        if (
            convert_camel_case(field.name) not in db_relations_fields  # type: ignore
            and convert_camel_case(field.name) in db_columns  # type: ignore
        )
    ]
    return selected_fields
