import types

class FlatIterator:

    def __init__(self, list_of_list):
        self.a = list_of_list
        

    def __iter__(self):
        self.cur_row = 0
        self.cur_col = 0
        self.column = len(self.a)-1
        self.row = len(self.a[self.cur_row])-1

        return self

    def __next__(self):
        if  self.cur_col <= self.column:
            self.row = len(self.a[self.cur_col])-1
            if self.cur_row <= self.row:
                item = self.a[self.cur_col][self.cur_row]
                self.cur_row += 1
                return item
            else:
                self.cur_col += 1
                self.cur_row = 0
                if  self.cur_col <= self.column:
                    item = self.a[self.cur_col][self.cur_row]
                    self.cur_row += 1
                    return item
                else: raise StopIteration 
        else: raise StopIteration 
        
    

list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


def flat_generator(list_of_lists):

  for item in list_of_lists:
    sub_list = item
    for element in sub_list:
      yield element
    


def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)

if __name__ == '__main__':
    test_1()
    test_2()

