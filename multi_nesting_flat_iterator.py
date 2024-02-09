class FlatIterator:
    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists

    def __iter__(self):
        self.res = []
        for item in self.list_of_lists:
            self.merge(item)
        self.res_iter = iter(self.res)
        return self

    def __next__(self):
        return next(self.res_iter)

    def merge(self, list_):
        for el in list_:
            self.merge(el) if isinstance(el, list) else self.res.append(el)


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]
    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item
    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e',
                                                   'f', 'h', False, 1, 2,
                                                   None, '!']


if __name__ == '__main__':
    test_3()
