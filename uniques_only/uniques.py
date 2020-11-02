from collections.abc import Hashable


def uniques_only(list_for_dedupe):
    deduped_list = []
    deduped_set = set()
    for item in list_for_dedupe:
        if isinstance(item, Hashable):
            if item not in deduped_set:
                yield item
                deduped_set.add(item)
        else:
            if item not in deduped_list:
                yield item
                deduped_list.append(item)


if __name__ == "__main__":
    my_list = [1, 2, 2, 1, 1, 3, 2, 1]
    print(uniques_only(my_list))
