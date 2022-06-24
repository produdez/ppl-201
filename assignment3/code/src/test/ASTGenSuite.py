import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_number_141(self):
        """declare inside use outside"""
        self.assertTrue(TestAST.checkASTGen("""Function: main Body: If True Then Var: x =5; EndIf. Return x+.5.5; EndBody.""","""""",541))
    def test_number_142(self):
        """var decl as main and no real main func"""
        self.assertTrue(TestAST.checkASTGen("""Var: a,c,b,d,main,foo,fuc,pung; Function: f2 Body: EndBody.""","""""",542))
    def test_number_143(self):
        """func with same name as global var"""
        self.assertTrue(TestAST.checkASTGen("""Var: main; Function: main Body: EndBody.""","""""",543))





