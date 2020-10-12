from collections import defaultdict, Counter
import unittest


from proxydict import ProxyDict


class ProxyDictTests(unittest.TestCase):

    """Tests for ProxyDict."""

    def test_can_access_keys(self):
        d = ProxyDict({'a': 'b', 'c': 'd'})
        self.assertEqual(d['a'], 'b')
        self.assertEqual(d['c'], 'd')
        with self.assertRaises(KeyError):
            d['b']
            d[0]

    def test_cannot_write_to_keys(self):
        d = ProxyDict({0: 'b', 1: 'd'})
        self.assertEqual(d[0], 'b')
        with self.assertRaises(Exception):
            d[0] = 'e'
        with self.assertRaises(Exception):
            d[3] = 'z'

    def test_cannot_update(self):
        d = ProxyDict({0: 'b', 1: 'd'})
        with self.assertRaises(Exception):
            d.update({3: 'z'})

    def test_cannot_set_default_values(self):
        d = ProxyDict({0: 'b', 1: 'd'})
        with self.assertRaises(Exception):
            d.setdefault(2, 'e')

    def test_cannot_pop_key(self):
        d = ProxyDict({0: 'b', 1: 'd'})
        with self.assertRaises(Exception):
            d.pop(0)
        self.assertEqual(d[0], 'b')

    def test_changes_when_underlying_mapping_changes(self):
        mapping = {'a': 'b', 'c': 'd'}
        d = ProxyDict(mapping)
        self.assertEqual(d['a'], 'b')
        mapping['a'] = 'z'
        self.assertEqual(d['a'], 'z')

    def test_has_keys(self):
        d = ProxyDict({'a': 'b', 'c': 'd'})
        self.assertEqual(set(d.keys()), {'a', 'c'})

    # To test the Bonus part of this exercise, comment out the following line
    @unittest.expectedFailure
    def test_items_len_values_items_and_get(self):
        d = ProxyDict({'a': 'b', 'c': 'd'})
        self.assertEqual(set(d.items()), {('a', 'b'), ('c', 'd')})
        self.assertEqual(set(d.values()), {'b', 'd'})
        self.assertEqual(len(d), 2)
        self.assertEqual(d.get('a'), 'b')
        self.assertEqual(d.get('a', 'z'), 'b')
        self.assertEqual(d.get('d'), None)
        self.assertEqual(d.get('d', 'z'), 'z')

    # To test the Bonus part of this exercise, comment out the following line
    @unittest.expectedFailure
    def test_iteration_and_repr(self):
        d = ProxyDict({1: 'a', 3: 'c'})
        e = ProxyDict({'a': 'b', 'c': 'd'})
        self.assertEqual(set(d), {1, 3})
        self.assertEqual(set(e), {'a', 'c'})
        self.assertEqual(
            str(d),
            "ProxyDict({1: 'a', 3: 'c'})",
        )
        self.assertEqual(
            str(e),
            "ProxyDict({'a': 'b', 'c': 'd'})",
        )

    # To test the Bonus part of this exercise, comment out the following line
    @unittest.expectedFailure
    def test_supports_equality(self):
        mapping1 = {'a': 1, 'b': 2}
        mapping2 = {'a': 1}
        a = ProxyDict(mapping1)
        b = ProxyDict(mapping2)
        c = ProxyDict(mapping1)
        self.assertEqual(a, mapping1)
        self.assertEqual(b, mapping2)
        self.assertEqual(a, c)
        self.assertNotEqual(a, b)
        self.assertIs(a != mapping1, False)
        self.assertIs(a == b, False)
        mapping2['b'] = 2
        self.assertEqual(b, mapping2)
        self.assertEqual(a, mapping1)
        self.assertEqual(a, b)
        self.assertNotEqual(a, ['a', 'b'])
        self.assertEqual(a, defaultdict(int, {'a': 1, 'b': 2}))
        self.assertEqual(a, Counter('abb'))


if __name__ == "__main__":
    unittest.main(verbosity=2)