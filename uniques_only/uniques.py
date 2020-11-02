def uniques_only(list_for_dedupe):
    deduped_list = []
    for item in list_for_dedupe:
        if item not in deduped_list:
            deduped_list.append(item)
            yield item


if __name__ == "__main__":
    my_list = [1, 2, 2, 1, 1, 3, 2, 1]
    print(uniques_only(my_list))
