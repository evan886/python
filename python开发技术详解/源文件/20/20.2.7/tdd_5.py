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
		
	def checkequal(self, result, object, methodname, *args):
		realresult = getattr(object, methodname)(*args)
		self.assertEqual(
            result,
            realresult
        )
	
	"""测试空字符替换"""
	def testBlank(self):
		self.checkequal("HELLO", self.source, "replace", "", "")


	"""测试空字符替换成常规字符"""
	def testBlankOrd(self):
		self.checkequal("*H*E*L*L*O*", self.source, "replace", "", "*")
		
	"""测试常规字符替换为空字符"""
	def testOrdBlank(self):
		self.checkequal("HE*O", self.source, "replace", "LL", "*")

	"""测试常规字符换"""
	def testOrd(self):
		self.checkequal("HEMMO", self.source, "replace", "LL", "MM")
			

def suite():
	StringStripTestSuite = unittest.makeSuite(StringStripTestCase,'test')	
	StringReplaceTestSuite = unittest.makeSuite(StringReplaceTestCase,'test')
	
	alltests = unittest.TestSuite((StringStripTestSuite, StringReplaceTestSuite))
	return alltests

if __name__ == "__main__":
	#runner = unittest.TextTestRunner()

	#runner.run(suite())
	
	unittest.main()







