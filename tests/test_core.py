# -*- coding: utf-8 -*-
import unittest

import lora

class test_core(unittest.TestCase):

    def test_hello(self):

      res = lora.hello("World") 
      self.assertEqual(res, "Hello, World!\n")

    def test_math_square(self):

      m = lora.math()
      res = m.square(10)
      self.assertEqual(res, 100)

    def test_callback(self):

      def foo(x):
        return x * x

      m = lora.invoke(foo, 10)

    def test_handle(self):

      c = lora.callee

      res = lora.caller(c, 2)

      self.assertEqual(res, 9)

if __name__ == '__main__':
    unittest.main()