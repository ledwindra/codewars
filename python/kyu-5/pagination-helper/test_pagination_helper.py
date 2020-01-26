from pagination_helper import PaginationHelper

collection = range(1,25)
helper = PaginationHelper(collection, 10)

class TestPaginationHelper:

    def test_first(self):
        assert helper.page_count() == 3
    
    def test_second(self):
        assert helper.page_index(23) == 2

    def test_third(self):
        assert helper.item_count() == 24