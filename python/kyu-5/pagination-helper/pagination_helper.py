class PaginationHelper:

    def __init__(self, collection, item_per_page):

        self.collection = collection
        self.item_per_page = item_per_page

    def item_count(self):

        return len(self.collection)

    def page_count(self):

        i = 0
        collection = self.collection
        item_per_page = self.item_per_page

        if len(collection) == item_per_page:
            return 1
        else:
            while len(collection[(item_per_page * i) : (item_per_page * (i + 1))]) > 0:
                i += 1

        return i
    
    def page_item_count(self, page_index):

        page_count = self.page_count()
        item_per_page = self.item_per_page
        collection = self.collection
        
        if page_index >= page_count:
            return -1
        elif page_index == 0:
            return item_per_page
        else:
            return len(collection[item_per_page * page_index : item_per_page * (page_index + 1)])

    def page_index(self, item_index):

        collection = self.collection
        item_per_page = self.item_per_page
        item_count = self.item_count()

        try:            
            i = 0
            if item_index < 0 or item_index > item_count:
                return -1
            elif collection[item_index] in collection[ : item_per_page]:
                return 0
            else:
                while not collection[item_index] in collection[(item_per_page * i) : item_per_page * (i + 1)]:
                    i += 1
                return i
        except IndexError:
            return -1