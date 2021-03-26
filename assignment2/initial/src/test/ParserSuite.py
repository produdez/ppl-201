import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):

    
    
    # def test_expression(self):
    #     test_number = 999
    #     self.assertTrue(TestLexer.checkLexeme(ParserSuite.read_input_file(test_number),"No expected",test_number))

    
    # #...my helper functions..#
    # def read_input_file(file_number): #this is defined to read directly text from file instead of writing string testcases
    #     file = open("./test/testcases/my_test_input/" + str(file_number) + ".txt","r")
    #     string_file=file.read()
    #     file.close()
    #     return string_file

    #MY Parser
    
    #CODE
    def test_number_0(self):
        """Simple var dec"""
        self.assertTrue(TestParser.checkParser('Var: x;','successful',200))
    def test_number_1(self):
        """Multi var dec"""
        self.assertTrue(TestParser.checkParser('Var: x,y,z;','successful',201))
    def test_number_2(self):
        """Var dec with init value"""
        self.assertTrue(TestParser.checkParser('Var: x,y=10,   z=30, g, f;','successful',202))
    def test_number_3(self):
        """Array dec"""
        self.assertTrue(TestParser.checkParser('Var: array[5][6][7], a,c,c,   another[0];','successful',203))
    def test_number_4(self):
        """Array with init"""
        self.assertTrue(TestParser.checkParser('Var: a, array[5][3],c  = {1,2,3,{1,2},{1,2,{1},{3,4}}};','successful',204))
    def test_number_5(self):
        """Mixed declatation"""
        self.assertTrue(TestParser.checkParser('Var: a=6,c,y, arr[6][7]={1,2,{6}}, g="String", xx=12e7;','successful',205))
    def test_number_6(self):
        """Missing colon"""
        self.assertTrue(TestParser.checkParser('Var x;','Error on line 1 col 4: x',206))
    def test_number_7(self):
        """Missing semi"""
        self.assertTrue(TestParser.checkParser('Var: array[1][2] = {1}','Error on line 1 col 22: <EOF>',207))
    def test_number_8(self):
        """Init without init value"""
        self.assertTrue(TestParser.checkParser('Var: value=;','Error on line 1 col 11: ;',208))
    def test_number_9(self):
        """Miss match subscript"""
        self.assertTrue(TestParser.checkParser('Var: array[1][2 ;','Error on line 1 col 16: ;',209))
    def test_number_10(self):
        """Miss match array value"""
        self.assertTrue(TestParser.checkParser('Var: array[1][2] = {1,2,3,{4,5};','Error on line 1 col 31: ;',210))
    def test_number_11(self):
        """Variable list not separated"""
        self.assertTrue(TestParser.checkParser('Var: a,b,c d;','Error on line 1 col 11: d',211))
    def test_number_12(self):
        """Variable list separated but missing comma"""
        self.assertTrue(TestParser.checkParser('Var: a,b,c,;','Error on line 1 col 11: ;',212))
    def test_number_13(self):
        """Empty no param"""
        self.assertTrue(TestParser.checkParser('Function: empty \n Body: \n EndBody.','successful',213))
    def test_number_14(self):
        """Function no endline"""
        self.assertTrue(TestParser.checkParser('Function: empty Body: EndBody.','successful',214))
    def test_number_15(self):
        """Simple param"""
        self.assertTrue(TestParser.checkParser('Function: main \n Parameter: n,c,y Body: EndBody.','successful',215))
    def test_number_16(self):
        """Simple function no param"""
        self.assertTrue(TestParser.checkParser('Function: main \n Body: \n x = 10; fact(x); \n EndBody.','successful',216))
    def test_number_17(self):
        """Simple function param"""
        self.assertTrue(TestParser.checkParser('Function: main Parameter: n Body: assign = 10; EndBody.','successful',217))
    def test_number_18(self):
        """Funcition with var dec """
        self.assertTrue(TestParser.checkParser('Function: main Parameter: n Body: Var: i=0; assign = 10; EndBody.','successful',218))
    def test_number_19(self):
        """Function param has array element"""
        self.assertTrue(TestParser.checkParser('Function: main Parameter: n, a[2][3] Body: i =5; EndBody.','successful',219))
    def test_number_20(self):
        """Double function"""
        self.assertTrue(TestParser.checkParser('Function: main Parameter: n, a[2][3] Body: i =5; EndBody.Function: main Parameter: n, a[2][3] Body: i =5; EndBody.','successful',220))
    def test_number_21(self):
        """Param with init value"""
        self.assertTrue(TestParser.checkParser('Function: main Parameter: n=5','Error on line 1 col 27: =',221))
    def test_number_22(self):
        """Var dec after func dec"""
        self.assertTrue(TestParser.checkParser('Function: main Body: EndBody. Var: x,y,z;','Error on line 1 col 30: Var',222))
    def test_number_23(self):
        """Var dec after other statements in function"""
        self.assertTrue(TestParser.checkParser('Function: empty Body: a=c; Var: n;  EndBody.','Error on line 1 col 27: Var',223))
    def test_number_24(self):
        """Wrong function name"""
        self.assertTrue(TestParser.checkParser('Function: Func Body: EndBody.','F',224))
    def test_number_25(self):
        """Param but no thing"""
        self.assertTrue(TestParser.checkParser('Function: func Parameter: Body EndBody.','Error on line 1 col 26: Body',225))
    def test_number_26(self):
        """Param but not variables"""
        self.assertTrue(TestParser.checkParser('Function: func Parameter: 1,2,3 Body: EndBody.','Error on line 1 col 26: 1',226))
    def test_number_27(self):
        """Non-closed body"""
        self.assertTrue(TestParser.checkParser('Function: func Parameter: Body: int = 5; ','Error on line 1 col 26: Body',227))
    def test_number_28(self):
        """Missing colon after Parameter"""
        self.assertTrue(TestParser.checkParser('Function: func Parameter x,y,z Body EndBody.','Error on line 1 col 25: x',228))
    def test_number_29(self):
        """Missing dot after EndBody"""
        self.assertTrue(TestParser.checkParser('Function: main \n Parameter: n,c,y Body: EndBody','Error on line 2 col 31: <EOF>',229))
    def test_number_30(self):
        """just IF"""
        self.assertTrue(TestParser.checkParser('Function: main \n Body: \n If x>3 Then n=10;   EndIf. \n EndBody.','successful',230))
    def test_number_31(self):
        """one elseif no else"""
        self.assertTrue(TestParser.checkParser('Function: main Body: If a==b Then a=5; ElseIf a!=b Then Return; EndIf. EndBody.','successful',231))
    def test_number_32(self):
        """if elseif else"""
        self.assertTrue(TestParser.checkParser('Function: main Body: If  1+ 2 Then printf(); ElseIf !True Then Break; Else Return; EndIf. EndBody.','successful',232))
    def test_number_33(self):
        """else no elseif"""
        self.assertTrue(TestParser.checkParser('Function: main Body: If 7e3 *. "5" Then a=""; Else b(); EndIf. EndBody.','successful',233))
    def test_number_34(self):
        """multiple else if"""
        self.assertTrue(TestParser.checkParser('Function: main Body: If nothing Then x[3]=1; ElseIf 12.3 Then a[2]={1}; ElseIf "Nah\\n" Then sendError(); Else Return; EndIf. EndBody.','successful',234))
    def test_number_35(self):
        """two ifs"""
        self.assertTrue(TestParser.checkParser('Function: main Body: If (a||b) Then Return; Else Break; EndIf. If a>b+c Then Break; ElseIf nothing Then Return; Else Continue; EndIf. EndBody.','successful',235))
    def test_number_36(self):
        """if <nested if> elseif else"""
        self.assertTrue(TestParser.checkParser('Function: main Body: If null Then do(); If not Then Return True; EndIf. ElseIf 3.7+e7 Then gg=""; Else Break; EndIf. EndBody.','successful',236))
    def test_number_37(self):
        """if elseif <nested if> else"""
        self.assertTrue(TestParser.checkParser('Function: main Body: If 0xAFF Then a=x; ElseIf 0x1234 Then x=5; If another Then doit();  ElseIf nother Then  Break; EndIf. Else Break; EndIf. EndBody.','successful',237))
    def test_number_38(self):
        """if elseif else <nested if>"""
        self.assertTrue(TestParser.checkParser('Function: main Body: If a[3][6][7] Then Break; ElseIf "True" Then Return; Else Return null; If notThat3 Then asign=asi; Else Continue; EndIf. EndIf. EndBody.','successful',238))
    def test_number_39(self):
        """many nested if"""
        self.assertTrue(TestParser.checkParser('Function: main Body: If 1 Then Return 2; If 3 Then Return 4; Else Return "5";  If gg Then Break; ElseIf notgg6 Then Continue; EndIf. EndIf. ElseIf False Then Return True; Else Return 3e7; EndIf. EndBody.','successful',239))
    def test_number_40(self):
        """multi else"""
        self.assertTrue(TestParser.checkParser('Function: main Body: If (1) Then a=6==6; ElseIf 2 Then Break; Else Return; Else Return; Else Return; EndIf. EndBody.','Error on line 1 col 75: Else',240))
    def test_number_41(self):
        """elseif after else"""
        self.assertTrue(TestParser.checkParser('Function: main Body: If a+.6e7 Then Return; ElseIf True Then Return; Else Break; ElseIf null Then a=c+.8; EndIf. EndBody.','Error on line 1 col 81: ElseIf',241))
    def test_number_42(self):
        """empty expression"""
        self.assertTrue(TestParser.checkParser('Var: a=;','Error on line 1 col 7: ;',242))
    def test_number_43(self):
        """missing then"""
        self.assertTrue(TestParser.checkParser('Function: main Body: If (a==(5+6)) \n printf(); Else Return; EndIf. EndBody.','Error on line 2 col 1: printf',243))
    def test_number_44(self):
        """normal empty for"""
        self.assertTrue(TestParser.checkParser('Function: empty Body: For(var = !12>True, no, no ) Do EndFor. EndBody.','successful',244))
    def test_number_45(self):
        """for with some code"""
        self.assertTrue(TestParser.checkParser('Function: empty Body: For(i = 2, 1>2, True ) Do If a==!b Then Return "Pro\'"Inner\\n\'""; EndIf. EndFor. EndBody.','successful',245))
    def test_number_46(self):
        """nested for"""
        self.assertTrue(TestParser.checkParser('Function: empty Body: For(i = 2, i<=50, i+1 ) Do For(j=i, j < 100, j+5) Do printf(j);  EndFor. Continue; EndFor. EndBody.','successful',246))
    def test_number_47(self):
        """missing initExpr"""
        self.assertTrue(TestParser.checkParser('Function: empty Body: i = 15; For( , i<10 , i-1 ) Do EndFor. EndBody.','Error on line 1 col 35: ,',247))
    def test_number_48(self):
        """missing condition"""
        self.assertTrue(TestParser.checkParser('Function: empty Body: For(i = 2, 1>2,  ) Do EndFor. EndBody.','Error on line 1 col 39: )',248))
    def test_number_49(self):
        """for with initExpr but not assigned to a vairiable"""
        self.assertTrue(TestParser.checkParser('Function: empty Body: For(i , 1>2, True ) Do EndFor. EndBody.','Error on line 1 col 28: ,',249))
    def test_number_50(self):
        """variable is composite not scalaer"""
        self.assertTrue(TestParser.checkParser('Function: empty Body: For(i[5] = {1,2,3}, 1>2, True ) Do EndFor. EndBody.','Error on line 1 col 27: [',250))
    def test_number_51(self):
        """missing comma between expressions in for init"""
        self.assertTrue(TestParser.checkParser('Function: empty Body: For(i = 2 ; 1>2 ; True ) Do EndFor. EndBody.','Error on line 1 col 32: ;',251))
    def test_number_52(self):
        """no DO in for loop"""
        self.assertTrue(TestParser.checkParser('Function: empty Body: For(i = 2, 1>2, True ) print() EndFor. EndBody.','Error on line 1 col 45: print',252))
    def test_number_53(self):
        """statement as expression"""
        self.assertTrue(TestParser.checkParser('Function: empty Body: For(i = 2, 1>2, True ) Do i = i = 5; EndFor. EndBody.','Error on line 1 col 54: =',253))
    def test_number_54(self):
        """missing paren in for declaration"""
        self.assertTrue(TestParser.checkParser('Function: empty Body: For i=2,1>2, True Do \n \t Return; EndFor. EndBody.','Error on line 1 col 26: i',254))
    def test_number_55(self):
        """exess colon in for declaration"""
        self.assertTrue(TestParser.checkParser('Function: empty Body: For ( u=-10, may!=not, "Tru",) Do EndFor. EndBody.','Error on line 1 col 50: ,',255))
    def test_number_56(self):
        """empty while"""
        self.assertTrue(TestParser.checkParser('Function: empty Body: While nothing Do EndWhile. EndBody.','successful',256))
    def test_number_57(self):
        """some code while"""
        self.assertTrue(TestParser.checkParser('Function: empty Body: While a[10]!=100 Do printf(); EndWhile. EndBody.','successful',257))
    def test_number_58(self):
        """nested while"""
        self.assertTrue(TestParser.checkParser('Function: main3 Body: While n>10 Do While n<100 Do x=10e3; EndWhile. Continue; EndWhile. EndBody.','successful',258))
    def test_number_59(self):
        """commented while"""
        self.assertTrue(TestParser.checkParser('Function: empty Body: While x>2**,y>5** Do print(); EndWhile. EndBody.','successful',259))
    def test_number_60(self):
        """do while and while"""
        self.assertTrue(TestParser.checkParser('Function: empty Body: Do While x<100 Do EndDo. EndBody.','Error on line 1 col 40: EndDo',260))
    def test_number_61(self):
        """some code do while"""
        self.assertTrue(TestParser.checkParser('Function: empty Body: Do x=5.2; print(x); x=x+1; While x<100 EndDo. EndBody.','successful',261))
    def test_number_62(self):
        """nested do while"""
        self.assertTrue(TestParser.checkParser('Function: empty Body: Do Do x=-x; While x>50 EndDo. While x<100 EndDo. EndBody.','successful',262))
    def test_number_63(self):
        """do while with no do"""
        self.assertTrue(TestParser.checkParser('Function: empty Body: While x<100 Do Return; EndDo. EndBody.','Error on line 1 col 45: EndDo',263))
    def test_number_64(self):
        """empty do while"""
        self.assertTrue(TestParser.checkParser('Function: empty Body: Do While x<100 EndDo. EndBody.','successful',264))
    def test_number_65(self):
        """lots of var decl"""
        self.assertTrue(TestParser.checkParser('Var: a,b,c; Function: empty Body: Var: a,c,b; If a>b Then Var: a,b,c; Return; EndIf. EndBody.','successful',265))
    def test_number_66(self):
        """some call statements"""
        self.assertTrue(TestParser.checkParser('Function: empty Body: foo(1); foo(2); foo(3); EndBody.','successful',266))
    def test_number_67(self):
        """call statement empty param"""
        self.assertTrue(TestParser.checkParser('Function: empty Body: foo(); foo(); foo(); EndBody.','successful',267))
    def test_number_68(self):
        """Missing paren in param function call"""
        self.assertTrue(TestParser.checkParser('Function: empty Body: foo); foo(x); foo(y); EndBody.','Error on line 1 col 25: )',268))
    def test_number_69(self):
        """function expression as function call"""
        self.assertTrue(TestParser.checkParser('Function: empty Body: foo(); foo(foo() + foo(x) != foo("String")); foo(); EndBody.','successful',269))
    def test_number_70(self):
        """empty return"""
        self.assertTrue(TestParser.checkParser('Function: empty Body: Return; EndBody.','successful',270))
    def test_number_71(self):
        """return with expr"""
        self.assertTrue(TestParser.checkParser('Function: empty Body: Return(nothing); EndBody.','successful',271))
    def test_number_72(self):
        """statement outside function"""
        self.assertTrue(TestParser.checkParser('Function: main Body: Return; EndBody. printf();','Error on line 1 col 38: printf',272))
    def test_number_73(self):
        """just add minus int"""
        self.assertTrue(TestParser.checkParser('Function: main Body: If !!1+1+2+3e+5 --0xAFF Then ElseIf none Then Else EndIf. EndBody.','successful',273))
    def test_number_74(self):
        """just add minus float"""
        self.assertTrue(TestParser.checkParser('Function: main Body: If 3.5+3.0e-5-!!!1.2---0x123 Then ElseIf none Then Else EndIf. EndBody.','successful',274))
    def test_number_75(self):
        """just logical"""
        self.assertTrue(TestParser.checkParser('Function: main Body: If a||b&&c||b&&a Then ElseIf c&&a&&b||b||c Then Else EndIf. EndBody.','successful',275))
    def test_number_76(self):
        """nested negation"""
        self.assertTrue(TestParser.checkParser('Function: main Body: While !!!!!!!!!!!!a>!b Do Return; EndWhile. EndBody.','successful',276))
    def test_number_77(self):
        """nested index"""
        self.assertTrue(TestParser.checkParser('Function: main Body: While a[1][2][a[5][6]+b[foo("String") > fok()]] Do Return; EndWhile. EndBody.','successful',277))
    def test_number_78(self):
        """multi dimention array indexing"""
        self.assertTrue(TestParser.checkParser('Function: main Body: If x[1][2][2.5][3e+7] Then ElseIf nothing Then Else EndIf. EndBody.','successful',278))
    def test_number_79(self):
        """mixed precedence and assoc"""
        self.assertTrue(TestParser.checkParser('Function: empty Body: x = !-a + !b[0]\\5 -.( (x == y)*.(3e7 - 7 - gg)|| True || !False); EndBody.','successful',279))
    def test_number_80(self):
        """mixed precedence and assoc"""
        self.assertTrue(TestParser.checkParser('Function: empty Body: x = 2*-3+!True; EndBody.','successful',280))
    def test_number_81(self):
        """mixed precedence and assoc"""
        self.assertTrue(TestParser.checkParser('Function: empty Body: x = foo(1==2 * 1!=2) || foo(----1) && foo(-.-.1.2-1--2e3); EndBody.','Error on line 1 col 38: !=',281))
    def test_number_82(self):
        """mixed precedence and assoc"""
        self.assertTrue(TestParser.checkParser('Function: empty Body: x = --.!-!avalue[1]; EndBody.','Error on line 1 col 29: !',282))
    def test_number_83(self):
        """mixed precedence and assoc"""
        self.assertTrue(TestParser.checkParser('Function: empty Body: x = 3>.3<.5; EndBody.','Error on line 1 col 30: <.',283))
    def test_number_84(self):
        """mixed precedence and assoc"""
        self.assertTrue(TestParser.checkParser('Function: empty Body: x = function(function(a[2][function()])); EndBody.','successful',284))
    def test_number_85(self):
        """mixed precedence and assoc"""
        self.assertTrue(TestParser.checkParser('Function: empty Body: x = foo() foo(); EndBody.','Error on line 1 col 32: foo',285))
    def test_number_86(self):
        """mixed precedence and assoc"""
        self.assertTrue(TestParser.checkParser('Function: empty Body: x = 1&&2||3 % 5 %7.5 <= nothing; EndBody.','successful',286))
    def test_number_87(self):
        """mixed precedence and assoc"""
        self.assertTrue(TestParser.checkParser('Function: empty Body:  y=-fact(x+12345); EndBody.','successful',287))
    def test_number_88(self):
        """mixed precedence and assoc"""
        self.assertTrue(TestParser.checkParser('Function: empty Body: x = 2!; EndBody.','Error on line 1 col 27: !',288))
    def test_number_89(self):
        """mixed precedence and assoc"""
        self.assertTrue(TestParser.checkParser('Function: empty Body: func(!func()); EndBody.','successful',289))
    def test_number_90(self):
        """mixed precedence and assoc"""
        self.assertTrue(TestParser.checkParser('Function: empty Body: !func(); EndBody.','Error on line 1 col 22: !',290))
    def test_number_91(self):
        """mixed precedence and assoc"""
        self.assertTrue(TestParser.checkParser('Function: empty Body: func(-2+5++6); EndBody.','Error on line 1 col 32: +',291))
    def test_number_92(self):
        """mixed precedence and assoc"""
        self.assertTrue(TestParser.checkParser('Function: empty Body: x= --(6*7-5>7.7 == "String"); EndBody.','Error on line 1 col 38: ==',292))
    def test_number_93(self):
        """mixed precedence and assoc"""
        self.assertTrue(TestParser.checkParser('Function: empty Body: x= a[1==2] == b[6!=7] + a \\!b;  EndBody.','successful',293))
    def test_number_94(self):
        """mixed precedence and assoc"""
        self.assertTrue(TestParser.checkParser('Function: empty Body: a= (1==2)=/=5; EndBody.','successful',294))
    def test_number_95(self):
        """full program ex"""
        self.assertTrue(TestParser.checkParser('Var: a,b,c=5,d[5]["String"]={1}; Var: x,y; Function: count Parameter: n Body: While n>0 Do printf(n); n=n-1; EndWhile. Return n; EndBody. Function: main Body: count(5000); EndBody.','Error on line 1 col 18: "String"',295))
    def test_number_96(self):
        """full program ex"""
        self.assertTrue(TestParser.checkParser('Var: a,b,c=5,d[5][0x12]={1,{5.6,7}}; Var: x,y; Function: recur Parameter: n Body: If n==0 Then Return 0; EndIf. Return recur(n-1); EndBody. Function: main Body: recur(5000); EndBody.','successful',296))
    def test_number_97(self):
        """empty array"""
        self.assertTrue(TestParser.checkParser('Var: a; Function: main Body: array = {}; EndBody.','Error on line 1 col 38: }',297))
    def test_number_98(self):
        """nested empty array"""
        self.assertTrue(TestParser.checkParser('Var: arr[2][4]={{},{},{}};','Error on line 1 col 17: }',298))
    def test_number_99(self):
        """non-assoc with bracket"""
        self.assertTrue(TestParser.checkParser('Function: main Body: x=(1>2)>((3>4)>5); EndBody.','successful',299))

