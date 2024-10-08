#!/usr/bin/python
#encoding=utf-8

import unittest
import string

class SourceString(unittest.TestCase):
	def setUp(self):
		self.source = "HELLO"

class StringReplaceTestCase1(SourceString):
	"""测试空字符替换"""
	def runTest(self):
		expect = "HELLO"
		result = string.replace(self.source, "", "")
		self.assertEqual(expect, result)

class StringReplaceTestCase2(SourceString):
	"""测试空字符替换成常规字符"""
	def runTest(self):
		expect = "*H*E*L*L*O*"
		result = string.replace("HELLO", "", "*")
		self.assertEqual(expect, result)		

class StringReplaceTestCase3(SourceString):
	"""测试常规字符替换为空字符"""
	def runTest(self):
		expect = "HEO"
		result = string.replace("HELLO", "LL", "")
		self.assertEqual(expect, result)

class StringReplaceTestCase4(SourceString):
	"""测试常规字符换"""
	def runTest(self):
		expect = "HEMMO"
		result = string.replace("HELLO", "LL", "MM")
		self.assertEqual(expect, result)		
		
a = StringReplaceTestCase1()
		
if __name__ == "__main__":
	unittest.main()
