#!/usr/bin/python
#encoding=utf-8

import unittest
import string

class StringStripTestCase(unittest.TestCase):
	def testBlank(self):
		expect = "HELLO"
		result = string.strip("HELLO     ")
		self.assertEqual(expect, result)

	def testStr(self):
		expect = "HELLO"
		result = string.strip("xxHELLOxx", "xx")
		self.assertEqual(expect, result)

class StringReplaceTestCase(unittest.TestCase):
	def setUp(self):
		self.source = "HELLO"	
	
	"""测试空字符替换"""
	def testBlank(self):
		expect = "HELLO"
		result = string.replace(self.source, "", "")
		self.assertEqual(expect, result)

	"""测试空字符替换成常规字符"""
	def testBlankOrd(self):
		expect = "*H*E*L*L*O*"
		result = string.replace(self.source, "", "*")
		self.assertEqual(expect, result)		

	"""测试常规字符替换为空字符"""
	def testOrdBlank(self):
		expect = "HEO"
		result = string.replace(self.source, "LL", "")
		self.assertEqual(expect, result)

	"""测试常规字符换"""
	def testOrd(self):
		expect = "HEMMO"
		result = string.replace(self.source, "LL", "MM")
		self.assertEqual(expect, result)		

def suite():
	suite = unittest.TestSuite()
		
	suite.addTest(StringReplaceTestCase("testBlank"))
	
	suite.addTest(StringReplaceTestCase("testOrd"))
	
	suite.addTest(StringStripTestCase("testBlank"))
	
	StringStripTestSuite = unittest.makeSuite(StringStripTestCase,'test')
	
	StringReplaceTestSuite = unittest.makeSuite(StringReplaceTestCase,'test')
	
	alltests = unittest.TestSuite((StringStripTestSuite, StringReplaceTestSuite))


	return suite
		
if __name__ == "__main__":
	runner = unittest.TextTestRunner()

	runner.run(suite())
