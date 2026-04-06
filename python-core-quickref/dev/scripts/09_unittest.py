"""对应 09-unittest.md：TestCase、TextTestRunner"""

from __future__ import annotations

import sys
import unittest

from _io_util import utf8_stdout


def section(title: str) -> None:
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)


def add(a: int, b: int) -> int:
    return a + b


class TestAdd(unittest.TestCase):
    def setUp(self) -> None:
        self.left = 2

    def tearDown(self) -> None:
        pass

    def test_add(self) -> None:
        self.assertEqual(add(self.left, 3), 5)

    def test_raises(self) -> None:
        with self.assertRaises(TypeError):
            add(1, "x")  # type: ignore[arg-type]


def main() -> None:
    utf8_stdout()
    section("unittest：TextTestRunner 运行 Sample")
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestAdd)
    runner = unittest.TextTestRunner(verbosity=2, stream=sys.stdout)
    result = runner.run(suite)
    print("wasSuccessful:", result.wasSuccessful())


if __name__ == "__main__":
    main()
