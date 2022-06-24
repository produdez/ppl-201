import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      

    #MYPART: testing a random test (to know how this all works)
    
    # def test_comment(self):
    #     test_number=300
    #     """simple comment test"""
    #     self.assertTrue(TestLexer.checkLexeme("**thies thise **\n Key **2**","No expected",test_number))

    #special tests read from file

    # def test_order(self):
    #     """test string and multiline comment and multiline string (error)"""
    #     test_number = 301
    #     self.assertTrue(TestLexer.checkLexeme(LexerSuite.read_input_file(test_number),"No expected",test_number))
    
    #...my helper functions..#

    # def read_input_file(file_number): #this is defined to read directly text from file instead of writing string testcases
    #     file = open("./test/testcases/my_test_input/" + str(file_number) + ".txt","r")
    #     string_file=file.read()
    #     file.close()
    #     return string_file


    #MY LEXER SUITE

    def test_number_0(self):
        """single line comment"""
        self.assertTrue(TestLexer.checkLexeme('**this is a comment**','<EOF>',100))
    def test_number_1(self):
        """multi-line comment"""
        self.assertTrue(TestLexer.checkLexeme('**this is a \n multiline \n comment**','<EOF>',101))
    def test_number_2(self):
        """non-terminated one line comment"""
        self.assertTrue(TestLexer.checkLexeme('** not finished ......','Unterminated Comment',102))
    def test_number_3(self):
        """non terminated multiline comment"""
        self.assertTrue(TestLexer.checkLexeme('** multi not finished .. \n and ... \n more','Unterminated Comment',103))
    def test_number_4(self):
        """just lower"""
        self.assertTrue(TestLexer.checkLexeme('identifier','identifier,<EOF>',104))
    def test_number_5(self):
        """id lower upper"""
        self.assertTrue(TestLexer.checkLexeme('fOOlzZZ','fOOlzZZ,<EOF>',105))
    def test_number_6(self):
        """id lower underscore"""
        self.assertTrue(TestLexer.checkLexeme('under__score','under__score,<EOF>',106))
    def test_number_7(self):
        """id lower digit"""
        self.assertTrue(TestLexer.checkLexeme('the1andon1y','the1andon1y,<EOF>',107))
    def test_number_8(self):
        """id lower upper under"""
        self.assertTrue(TestLexer.checkLexeme('parser_RULE','parser_RULE,<EOF>',108))
    def test_number_9(self):
        """id lower upper digit"""
        self.assertTrue(TestLexer.checkLexeme('vaRIAb1e567','vaRIAb1e567,<EOF>',109))
    def test_number_10(self):
        """id lower under digit"""
        self.assertTrue(TestLexer.checkLexeme('x__221','x__221,<EOF>',110))
    def test_number_11(self):
        """all char id"""
        self.assertTrue(TestLexer.checkLexeme('mIxed13_andYoUxx__','mIxed13_andYoUxx__,<EOF>',111))
    def test_number_12(self):
        """all chars id"""
        self.assertTrue(TestLexer.checkLexeme('lOVrE_99_YOUr3000','lOVrE_99_YOUr3000,<EOF>',112))
    def test_number_13(self):
        """all chars id"""
        self.assertTrue(TestLexer.checkLexeme('aBBBBBx999rr0','aBBBBBx999rr0,<EOF>',113))
    def test_number_14(self):
        """id with upper start"""
        self.assertTrue(TestLexer.checkLexeme('Aa','Error Token A',114))
    def test_number_15(self):
        """error char"""
        self.assertTrue(TestLexer.checkLexeme('aaaaa?bbbbb','aaaaa,Error Token ?',115))
    def test_number_16(self):
        """escape after id"""
        self.assertTrue(TestLexer.checkLexeme('abc\n','abc,<EOF>',116))
    def test_number_17(self):
        """id with number start"""
        self.assertTrue(TestLexer.checkLexeme('1233what','1233,what,<EOF>',117))
    def test_number_18(self):
        """some key words"""
        self.assertTrue(TestLexer.checkLexeme('Body Break Continue Do Else ElseIf EndBody EndIf','Body,Break,Continue,Do,Else,ElseIf,EndBody,EndIf,<EOF>',118))
    def test_number_19(self):
        """more key words"""
        self.assertTrue(TestLexer.checkLexeme('EndFor EndWhile For Function If Parameter Return Then','EndFor,EndWhile,For,Function,If,Parameter,Return,Then,<EOF>',119))
    def test_number_20(self):
        """rest of key words"""
        self.assertTrue(TestLexer.checkLexeme('Var While True False EndDo','Var,While,True,False,EndDo,<EOF>',120))
    def test_number_21(self):
        """mix keyword and identifier"""
        self.assertTrue(TestLexer.checkLexeme('If if Else else','If,if,Else,else,<EOF>',121))
    def test_number_22(self):
        """mix keyword and identifier"""
        self.assertTrue(TestLexer.checkLexeme('Do a whiLe b Return','Do,a,whiLe,b,Return,<EOF>',122))
    def test_number_23(self):
        """upper + something that's not keyword"""
        self.assertTrue(TestLexer.checkLexeme('DoNothing','Do,Error Token N',123))
    def test_number_24(self):
        """upper + unknown char"""
        self.assertTrue(TestLexer.checkLexeme('Do?While','Do,Error Token ?',124))
    def test_number_25(self):
        """int operators"""
        self.assertTrue(TestLexer.checkLexeme('+-*\\==!=><>=<=','+,-,*,\,==,!=,>,<,>=,<=,<EOF>',125))
    def test_number_26(self):
        """float operators"""
        self.assertTrue(TestLexer.checkLexeme('+.-.*.\\.=/=<.>.<=.>=.','+.,-.,*.,\.,=/=,<.,>.,<=.,>=.,<EOF>',126))
    def test_number_27(self):
        """bool operators"""
        self.assertTrue(TestLexer.checkLexeme('!&&||','!,&&,||,<EOF>',127))
    def test_number_28(self):
        """Full line with op, keyword and identifier"""
        self.assertTrue(TestLexer.checkLexeme('If a+b==c Then exit();','If,a,+,b,==,c,Then,exit,(,),;,<EOF>',128))
    def test_number_29(self):
        """Full line with op, keyword and identifier"""
        self.assertTrue(TestLexer.checkLexeme('Function: x\n Body:\n me = 2 + 2e3;  \nBody.','Function,:,x,Body,:,me,=,2,+,2e3,;,Body,.,<EOF>',129))
    def test_number_30(self):
        """Some non-operator symbols"""
        self.assertTrue(TestLexer.checkLexeme(' a+b>0? Return;','a,+,b,>,0,Error Token ?',130))
    def test_number_31(self):
        """Non-operator symbols"""
        self.assertTrue(TestLexer.checkLexeme('Var: a<> = \'yea;','Var,:,a,<,>,=,Error Token \'',131))
    def test_number_32(self):
        """Normal and non operator"""
        self.assertTrue(TestLexer.checkLexeme('&& &','&&,Error Token &',132))
    def test_number_33(self):
        """Some separators"""
        self.assertTrue(TestLexer.checkLexeme('Var: array ={ [1,2,(5.6.7)];}','Var,:,array,=,{,[,1,,,2,,,(,5.6,.,7,),],;,},<EOF>',133))
    def test_number_34(self):
        """int zero and decimals (separator)"""
        self.assertTrue(TestLexer.checkLexeme('0 7685','0,7685,<EOF>',134))
    def test_number_35(self):
        """ hexa x and X"""
        self.assertTrue(TestLexer.checkLexeme('0x000 0X67ABF50 0xEEEE','0,x000,0X67ABF50,0xEEEE,<EOF>',135))
    def test_number_36(self):
        """octo o and O"""
        self.assertTrue(TestLexer.checkLexeme('0o034 0O555','0,o034,0O555,<EOF>',136))
    def test_number_37(self):
        """all types"""
        self.assertTrue(TestLexer.checkLexeme('0O123 99 0x76','0O123,99,0x76,<EOF>',137))
    def test_number_38(self):
        """hex, oct and identifier"""
        self.assertTrue(TestLexer.checkLexeme('0x123 x123 123','0x123,x123,123,<EOF>',138))
    def test_number_39(self):
        """wrong format hex"""
        self.assertTrue(TestLexer.checkLexeme('1x45AB','1,x45AB,<EOF>',139))
    def test_number_40(self):
        """wrong format oct"""
        self.assertTrue(TestLexer.checkLexeme('0p43','0,p43,<EOF>',140))
    def test_number_41(self):
        """many zeros"""
        self.assertTrue(TestLexer.checkLexeme('0000','0,0,0,0,<EOF>',141))
    def test_number_42(self):
        """out of bound octo"""
        self.assertTrue(TestLexer.checkLexeme('0o9999','0,o9999,<EOF>',142))
    def test_number_43(self):
        """out of bound hexa"""
        self.assertTrue(TestLexer.checkLexeme('0xGG123','0,xGG123,<EOF>',143))
    def test_number_44(self):
        """float no dot: int exp"""
        self.assertTrue(TestLexer.checkLexeme('55e007','55e007,<EOF>',144))
    def test_number_45(self):
        """float no dot: int +Exp"""
        self.assertTrue(TestLexer.checkLexeme('123E+3','123E+3,<EOF>',145))
    def test_number_46(self):
        """float dot no exp: int.int"""
        self.assertTrue(TestLexer.checkLexeme('567.789','567.789,<EOF>',146))
    def test_number_47(self):
        """float dot no exp: int."""
        self.assertTrue(TestLexer.checkLexeme('12.','12.,<EOF>',147))
    def test_number_48(self):
        """float full: int.(nothing)+exp"""
        self.assertTrue(TestLexer.checkLexeme('69.e+420','69.e+420,<EOF>',148))
    def test_number_49(self):
        """float full: int.intExp"""
        self.assertTrue(TestLexer.checkLexeme('345.543E678','345.543E678,<EOF>',149))
    def test_number_50(self):
        """float all zero """
        self.assertTrue(TestLexer.checkLexeme('000.00e-000','000.00e-000,<EOF>',150))
    def test_number_51(self):
        """many floats"""
        self.assertTrue(TestLexer.checkLexeme('03.5e-10 0.e1 9e+6 3.123','03.5e-10,0.e1,9e+6,3.123,<EOF>',151))
    def test_number_52(self):
        """float exp with no number"""
        self.assertTrue(TestLexer.checkLexeme('7e','7,e,<EOF>',152))
    def test_number_53(self):
        """float two dot"""
        self.assertTrue(TestLexer.checkLexeme('44..44e123','44.,.,44e123,<EOF>',153))
    def test_number_54(self):
        """float no int part just exp and deci"""
        self.assertTrue(TestLexer.checkLexeme('.34-E98','.,34,-,Error Token E',154))
    def test_number_55(self):
        """float wrong e letter"""
        self.assertTrue(TestLexer.checkLexeme('99.76G44','99.76,Error Token G',155))
    def test_number_56(self):
        """float change dot into other separator"""
        self.assertTrue(TestLexer.checkLexeme('12,12e43','12,,,12e43,<EOF>',156))
    def test_number_57(self):
        """int float iden keyword operator"""
        self.assertTrue(TestLexer.checkLexeme('Var: a_B=0E90, do = 0X90;','Var,:,a_B,=,0E90,,,do,=,0X90,;,<EOF>',157))
    def test_number_58(self):
        """int float iden keyword operator"""
        self.assertTrue(TestLexer.checkLexeme('hh + 0000 >= 12.E00 - True;','hh,+,0,0,0,0,>=,12.E00,-,True,;,<EOF>',158))
    def test_number_59(self):
        """some kind of boolean"""
        self.assertTrue(TestLexer.checkLexeme('True False true false TRUE FALSE ','True,False,true,false,Error Token T',159))
    def test_number_60(self):
        """single line string"""
        self.assertTrue(TestLexer.checkLexeme('" just a normal string"',' just a normal string,<EOF>',160))
    def test_number_61(self):
        """escape string"""
        self.assertTrue(TestLexer.checkLexeme('" \\n Hello \\n \\f \\t"',' \\n Hello \\n \\f \\t,<EOF>',161))
    def test_number_62(self):
        """nested string"""
        self.assertTrue(TestLexer.checkLexeme('" Outside \'" inside \'"  and just a quote\'"  "',' Outside \'" inside \'"  and just a quote\'"  ,<EOF>',162))
    def test_number_63(self):
        """empty string"""
        self.assertTrue(TestLexer.checkLexeme('""',',<EOF>',163))
    def test_number_64(self):
        """fake error string"""
        self.assertTrue(TestLexer.checkLexeme('"""oh no"',',oh no,<EOF>',164))
    def test_number_65(self):
        """string combine with other types"""
        self.assertTrue(TestLexer.checkLexeme('{"","yea",2134}','{,,,,yea,,,2134,},<EOF>',165))
    def test_number_66(self):
        """string combine with other types"""
        self.assertTrue(TestLexer.checkLexeme('"123", 123 **diferent types** "str**i**ng"','123,,,123,str**i**ng,<EOF>',166))
    def test_number_67(self):
        """single non closed"""
        self.assertTrue(TestLexer.checkLexeme('" never closing \\t yea!!','Unclosed String:  never closing \\t yea!!',167))
    def test_number_68(self):
        """nested non-closed"""
        self.assertTrue(TestLexer.checkLexeme('"""Hello im not done""',',Hello im not done,Unclosed String: ',168))
    def test_number_69(self):
        """multi-line  string"""
        self.assertTrue(TestLexer.checkLexeme('"Multiline \n String";','Unclosed String: Multiline ',169))
    def test_number_70(self):
        """wrong excape"""
        self.assertTrue(TestLexer.checkLexeme('"Using wrong escape: \\x";','Illegal Escape In String: Using wrong escape: \\x',170))
    def test_number_71(self):
        """normal and wrong escape"""
        self.assertTrue(TestLexer.checkLexeme('"Many escapes: \\b \\t \\g \\"','Illegal Escape In String: Many escapes: \\b \\t \\g',171))
    def test_number_72(self):
        """comment inside string"""
        self.assertTrue(TestLexer.checkLexeme('"str **i** ng"','str **i** ng,<EOF>',172))
    def test_number_73(self):
        """string in comment"""
        self.assertTrue(TestLexer.checkLexeme('**str "i" ng**','<EOF>',173))
    def test_number_74(self):
        """escaping a double quote in tring"""
        self.assertTrue(TestLexer.checkLexeme('"What if I escape like this: \\"','Illegal Escape In String: What if I escape like this: \\"',174))
    def test_number_75(self):
        """no input"""
        self.assertTrue(TestLexer.checkLexeme('','<EOF>',175))
    def test_number_76(self):
        """error char"""
        self.assertTrue(TestLexer.checkLexeme('aa$#@','aa,Error Token $',176))
    def test_number_77(self):
        """all types"""
        self.assertTrue(TestLexer.checkLexeme('Var: a=1234,"sslsls",0x54,True,3.25e1;','Var,:,a,=,1234,,,sslsls,,,0x54,,,True,,,3.25e1,;,<EOF>',177))
    def test_number_78(self):
        """negative number"""
        self.assertTrue(TestLexer.checkLexeme('-3,-6.77,+0x000','-,3,,,-,6.77,,,+,0,x000,<EOF>',178))
    def test_number_79(self):
        """print"""
        self.assertTrue(TestLexer.checkLexeme('print("Okay lets go \n");','print,(,Unclosed String: Okay lets go ',179))
    def test_number_80(self):
        """print string line with conversion"""
        self.assertTrue(TestLexer.checkLexeme('printStrLn(string_of_float(12.e-5));','printStrLn,(,string_of_float,(,12.e-5,),),;,<EOF>',180))
    def test_number_81(self):
        """some random code"""
        self.assertTrue(TestLexer.checkLexeme(' def f ( x ) : { y = x * x ; e = ( m * c * c ) ;','def,f,(,x,),:,{,y,=,x,*,x,;,e,=,(,m,*,c,*,c,),;,<EOF>',181))
    def test_number_82(self):
        """c pre-processor """
        self.assertTrue(TestLexer.checkLexeme('#include <assert.h>','Error Token #',182))
    def test_number_83(self):
        """function call as expression"""
        self.assertTrue(TestLexer.checkLexeme('foo(2 + x, 4. \n y) + bar("A string \t") == float_of_int(0O7777);','foo,(,2,+,x,,,4.,y,),+,bar,(,A string \t,),==,float_of_int,(,0O7777,),;,<EOF>',183))
    def test_number_84(self):
        """variable assignment"""
        self.assertTrue(TestLexer.checkLexeme('v = (4. \. 3.) *. 3.14 *. r *. r *. r;','v,=,(,4.,\.,3.,),*.,3.14,*.,r,*.,r,*.,r,;,<EOF>',184))
    def test_number_85(self):
        """for loop"""
        self.assertTrue(TestLexer.checkLexeme('For (i=0, i<10,2) Do \n writeln(i); \n EndFor.','For,(,i,=,0,,,i,<,10,,,2,),Do,writeln,(,i,),;,EndFor,.,<EOF>',185))
    def test_number_86(self):
        """array subscript"""
        self.assertTrue(TestLexer.checkLexeme('a[3+ foo(2)] = a [b[2][3]] + 4;','a,[,3,+,foo,(,2,),],=,a,[,b,[,2,],[,3,],],+,4,;,<EOF>',186))
    def test_number_87(self):
        """full function"""
        self.assertTrue(TestLexer.checkLexeme('Function: foo \n Parameter: a[5], b \n Body: \n Var: i = 0;\n While(i<5) \n a[i] = b +. 1.0; \n i = i+1; \n EndWhile. \n EndBody.','Function,:,foo,Parameter,:,a,[,5,],,,b,Body,:,Var,:,i,=,0,;,While,(,i,<,5,),a,[,i,],=,b,+.,1.0,;,i,=,i,+,1,;,EndWhile,.,EndBody,.,<EOF>',187))
    def test_number_88(self):
        """Variable declaration"""
        self.assertTrue(TestLexer.checkLexeme('Var: c, d = 6,e,f;','Var,:,c,,,d,=,6,,,e,,,f,;,<EOF>',188))
    def test_number_89(self):
        """escape sequence outside string"""
        self.assertTrue(TestLexer.checkLexeme('Var x = 12\\n;','Var,x,=,12,\\,n,;,<EOF>',189))
    def test_number_90(self):
        """just useless spaces"""
        self.assertTrue(TestLexer.checkLexeme('       \t    \t  \n \n ','<EOF>',190))
    def test_number_91(self):
        """random numberlike sequence"""
        self.assertTrue(TestLexer.checkLexeme('0e31xAFab__1234','0e31,xAFab__1234,<EOF>',191))
    def test_number_92(self):
        """random numberlike sequence"""
        self.assertTrue(TestLexer.checkLexeme('54e30x21AGG','54e30,x21AGG,<EOF>',192))
    def test_number_93(self):
        """wrong format of literal"""
        self.assertTrue(TestLexer.checkLexeme('1. x= 1xab;','1.,x,=,1,xab,;,<EOF>',193))
    def test_number_94(self):
        """float wrong format"""
        self.assertTrue(TestLexer.checkLexeme('1.0.0.0..0','1.0,.,0.0,.,.,0,<EOF>',194))
    def test_number_95(self):
        """multi dimention"""
        self.assertTrue(TestLexer.checkLexeme('[1][3][6][7][]','[,1,],[,3,],[,6,],[,7,],[,],<EOF>',195))
    def test_number_96(self):
        """cool comment"""
        self.assertTrue(TestLexer.checkLexeme('*** ** ','<EOF>',196))
    def test_number_97(self):
        """cool comment"""
        self.assertTrue(TestLexer.checkLexeme(' ** ***','*,<EOF>',197))
    def test_number_98(self):
        """single qoute in strig"""
        self.assertTrue(TestLexer.checkLexeme('"Who\'s this?"','Unclosed String: Who',198))
    def test_number_99(self):
        """cool comment"""
        self.assertTrue(TestLexer.checkLexeme('*****','*,<EOF>',199))

