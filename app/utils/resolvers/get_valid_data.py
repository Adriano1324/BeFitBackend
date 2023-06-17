"""
This method returns valid data from db obj
"""
import logging


def get_valid_data(model_data_object, model_class) -> dict:  # type: ignore
    """
    This function returns dict of valid fields
    """
    data_dict = {}
    for column in model_class.__table__.columns:
        try:
            data_dict[column.name] = getattr(model_data_object, column.name)
        except Exception as error:  # pylint: disable=W0718
            logging.error(error.__class__)
    return data_dict
