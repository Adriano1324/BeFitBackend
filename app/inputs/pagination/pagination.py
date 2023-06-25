"""
This module contains Input for pagination
"""
import strawberry


@strawberry.input
class PaginationInput:
    """
    This is pagination input class
    """

    page: int
    size: int

    def get_page(self) -> int:
        """
        This method returns page number
        :return:  page number
        """
        if self.page <= 0:
            return 1
        return self.page

    def get_size(self) -> int:
        """
        This method returns page size
        :return: page size
        """
        if self.size < 0 or self.size > 100:
            return 10
        return self.size

    def get_offset(self) -> int:
        """
        This method calculate offset for database
        :return: Calculated offset
        """
        return (self.get_page() - 1) * self.get_size()
