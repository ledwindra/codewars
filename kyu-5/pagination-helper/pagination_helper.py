class PaginationHelper:

    def __init__(self, collection, item_per_page):
        self.collection = collection
        self.item_per_page = item_per_page

    def item_count(self):

        return len(self.collection)

    def page_count(self):

        page = []
        constant = self.item_per_page
        for i in range(len(self.collection)):
            page.append(self.collection[self.item_per_page - constant : self.item_per_page])
            self.item_per_page += constant

        return len([x for x in page if len(x) > 0])

    def page_item_count(self, page_index):