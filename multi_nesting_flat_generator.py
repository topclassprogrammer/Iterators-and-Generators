import types

res = []


def flat_generator(list_):
    if not res:
        merge(list_)
    else:
        for el in res:
            yield el


def merge(list_):
    for el in list_:
        merge(el) if isinstance(el, list) else res.append(el)


def test_4():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]
    list(flat_generator(list_of_lists_2))
    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item
    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e',
                                                     'f', 'h', False, 1, 2,
                                                     None, '!']
    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()
