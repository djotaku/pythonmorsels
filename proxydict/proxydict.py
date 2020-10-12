from collections.abc import Mapping


class ProxyDict(Mapping):

    def __init__(self, dictionary):
        self.proxy_dictionary = dictionary
        super().__init__()

    def __getitem__(self, item):
        return self.proxy_dictionary[item]

    def __iter__(self):
        return (key for key in self.proxy_dictionary.keys())

    def __len__(self):
        return len(self.proxy_dictionary)

    def __repr__(self):
        # center_list = [f"{key}: '{value}'" for key, value in self.proxy_dictionary.items()]
        # center = (', '.join(center_list))
        center_list = []
        for key, value in self.proxy_dictionary.items():
            if isinstance(key, int):
                center_list.append(f"{key}: '{value}'")
            else:
                center_list.append(f"'{key}': '{value}'")
        center = (', '.join(center_list))
        return "ProxyDict({"+center+"})"
