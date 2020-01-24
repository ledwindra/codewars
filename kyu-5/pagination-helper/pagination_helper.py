class PaginationHelper:

    def __init__(self, collection, item_per_page):

        self.collection = collection
        self.item_per_page = item_per_page

    def item_count(self):

        return len(self.collection)

    def page_count(self):

        i = 0
        array = self.collection
        item_per_page = self.item_per_page

        if len(self.collection) == self.item_per_page:
            return 1
        else:
            while len(array[(item_per_page * i) : (item_per_page * (i + 1))]) > 0:
                i += 1

        return i
    
    def page_item_count(self, page_index):

        
        if page_index >= self.page_count():
            return -1
        elif page_index == 0:
            return self.item_per_page
        else:
            return len(self.collection[self.item_per_page - (page_index - 1) : self.item_per_page * (page_index + 1)])

    def page_index(self, item_index):

        array = self.collection
        item_per_page = self.item_per_page
        item_count = self.item_count()

        i = 0
        if item_index < 0 or item_index > item_count:
            return -1
        elif array[item_index] in array[ : item_per_page]:
            return 0
        else:
            while not array[item_index] in array[(item_per_page * i) : item_per_page * (i + 1)]:
                i += 1
            return i