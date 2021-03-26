import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    # def test_lower_identifier(self):
    #     """test identifiers"""
    #     self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))

    # def test_lower_upper_id(self):
    #     self.assertTrue(TestLexer.checkLexeme("Var","Var,<EOF>",102))

    # def test_wrong_token(self):
    #     self.assertTrue(TestLexer.checkLexeme("ab?svn","ab,Error Token ?",103))

    # def test_integer(self):
    #     """test integers"""
    #     self.assertTrue(TestLexer.checkLexeme("Var x;","Var,x,;,<EOF>",104))

    # def test_illegal_escape(self):
    #     """test illegal escape"""
    #     self.assertTrue(TestLexer.checkLexeme(""" "abc\\h def"  ""","""Illegal Escape In String: abc\\h""",105))

    # def test_unterminated_string(self):
    #     """test unclosed string"""
    #     self.assertTrue(TestLexer.checkLexeme(""" "abc def  ""","""Unclosed String: abc def  """,106))

    # def test_normal_string_with_escape(self):
    #     """test normal string with escape"""
    #     self.assertTrue(TestLexer.checkLexeme(""" "ab'"c\\n def"  ""","""ab'"c\\n def,<EOF>""",107))

    def test_id_1(self):
        test_id = 101
        self.assertTrue(TestLexer.checkLexeme("a" , "a,<EOF>" ,test_id));
    def test_id_2(self):
        test_id = 102
        self.assertTrue(TestLexer.checkLexeme("b1" , "b1,<EOF>" ,test_id));
    def test_id_3(self):
        test_id = 103
        self.assertTrue(TestLexer.checkLexeme("bkit" , "bkit,<EOF>" ,test_id));
    def test_id_4(self):
        test_id = 104
        self.assertTrue(TestLexer.checkLexeme("Hello" , "Error Token H" ,test_id));
    def test_id_5(self):
        test_id = 105
        self.assertTrue(TestLexer.checkLexeme("123413" , "Error Token 1" ,test_id))  
    def test_id_6(self):
        test_id = 106
        self.assertTrue(TestLexer.checkLexeme("lkf12baf" , "lkf12baf,<EOF>" ,test_id));
    def test_id_7(self):
        test_id = 107
        self.assertTrue(TestLexer.checkLexeme("ooooo" , "ooooo,<EOF>" ,test_id));
    def test_id_8(self):
        test_id = 108
        self.assertTrue(TestLexer.checkLexeme("AAA" , "Error Token A" ,test_id));
    def test_id_9(self):
        test_id = 109
        self.assertTrue(TestLexer.checkLexeme("aafJJ" , "aaf,Error Token J" ,test_id));
    def test_id_10(self):
        test_id = 100
        self.assertTrue(TestLexer.checkLexeme("" , "<EOF>" ,test_id));


    #test float
    def test_float_1(self):
        test_id = 110;
        self.assertTrue(TestLexer.checkLexeme("123e+10" , "123e+10,<EOF>" ,test_id));
    def test_float_2(self):
        test_id = 111;
        self.assertTrue(TestLexer.checkLexeme("23.05e-10" , "23.05e-10,<EOF>" ,test_id));
    def test_float_3(self):
        test_id = 112;
        self.assertTrue(TestLexer.checkLexeme(".66e10" , ".66e10,<EOF>" ,test_id));
    def test_float_4(self):
        test_id = 113;
        self.assertTrue(TestLexer.checkLexeme("27.000" , "27.000,<EOF>" ,test_id));
    def test_float_5(self):
        test_id = 114;
        self.assertTrue(TestLexer.checkLexeme(".0000" , ".0000,<EOF>" ,test_id));
    def test_float_6(self):
        test_id = 115;
        self.assertTrue(TestLexer.checkLexeme("12345" , "Error Token 1" ,test_id));
    def test_float_7(self):
        test_id = 116;
        self.assertTrue(TestLexer.checkLexeme("56.65x190" , "56.65,Error Token x" ,test_id));
    def test_float_8(self):
        test_id = 117;
        self.assertTrue(TestLexer.checkLexeme("00..00" , "00.,.00,<EOF>" ,test_id));
    def test_float_9(self):
        test_id = 118;
        self.assertTrue(TestLexer.checkLexeme("0" , "Error Token 0" ,test_id));
    def test_float_10(self):
        test_id = 119;
        self.assertTrue(TestLexer.checkLexeme("e45" , "Error Token e" ,test_id));
    

    def test_string_1(self):
        test_id = 120;
        self.assertTrue(TestLexer.checkLexeme("\'Hello\'" , "" ,test_id));
    def test_string_2(self):
        test_id = 121;
        self.assertTrue(TestLexer.checkLexeme("\'123\'" , "" ,test_id));
    def test_string_3(self):
        test_id = 122;
        self.assertTrue(TestLexer.checkLexeme("\'\\\'" , "" ,test_id));
    def test_string_4(self):
        test_id = 123;
        self.assertTrue(TestLexer.checkLexeme("\'\n\'" , "" ,test_id));
    def test_string_5(self):
        test_id = 124;
        self.assertTrue(TestLexer.checkLexeme("\'  \'" , "" ,test_id));
    def test_string_6(self):
        test_id = 125;
        self.assertTrue(TestLexer.checkLexeme("\'fasdf\'" , "" ,test_id));
    def test_string_7(self):
        test_id = 126;
        self.assertTrue(TestLexer.checkLexeme("\"" , "" ,test_id));
    def test_string_8(self):
        test_id = 127;
        self.assertTrue(TestLexer.checkLexeme("3241234" , "" ,test_id));
    def test_string_9(self):
        test_id = 128;
        self.assertTrue(TestLexer.checkLexeme("asdfadsf" , "" ,test_id));
    def test_string_10(self):
        test_id = 129;
        self.assertTrue(TestLexer.checkLexeme("" , "" ,test_id));

