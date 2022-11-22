import unittest
import pxc


class PxcTest(unittest.TestCase):

    def test_pxc(self):
        c = pxc.process("data.txt")
        self.assertEqual(len(c), 4)
        self.assertEqual(c, {
            'curiouser': 2,
            'and': 1,
            'cried': 1,
            'alice': 1
        })
