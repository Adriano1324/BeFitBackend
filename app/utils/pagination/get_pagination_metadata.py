"""
This module contains function to get pagination metadata based on request pagination and model
"""
from sqlalchemy import func, select

from app.db.async_session import get_session
from app.db.base_class import Base
from app.inputs.pagination.pagination import PaginationInput
from app.scalars.pagination.pagination_metadata import PaginationMetadata


# TODO Specify type of data inside of list
async def get_pagination_meta(
    pagination: PaginationInput, model: Base, filters: list
) -> PaginationMetadata:
    """
    :param pagination: This is pagination input from user
    :param model: DB model from which data are returned
    :param filters: Filters used to get data
    :return: PaginationMetadata instance
    """
    async with get_session() as s:
        result: int = (
            await s.execute(select(func.count()).select_from(model).filter(*filters))
        ).scalar() or 0
    if result % pagination.get_size() == 0:
        pages = int(result / pagination.get_size())
    else:
        pages = int(result / pagination.get_size()) + 1

    return PaginationMetadata(
        total=result,
        page=pagination.get_page(),
        size=pagination.get_size(),
        pages=pages,
    )
