#fucked up ones: 595,594,593,591,544,510,565,501
import unittest

from AST import *

from TestUtils import TestCodeGen


class CheckCodeGenSuite(unittest.TestCase):
    #CODE
    def test_number_0(self):
        """Global Var decl"""
        input = 'Var: a=5, b=11.2; Function: main Body: print(string_of_int(a)); EndBody.'
        expect = '5'
        self.assertTrue(TestCodeGen.test(input,expect,500))
    def test_number_1(self):
        """Global Var decl"""
        input = 'Var: a=5, b=0x12; Function: main Body: print(string_of_int(a+b)); EndBody.'
        expect = '23'
        self.assertTrue(TestCodeGen.test(input,expect,501))
    def test_number_2(self):
        """Float"""
        input = 'Var: a=5, b=11.2; Function: main Body: print(string_of_float(b)); EndBody.'
        expect = '11.2'
        self.assertTrue(TestCodeGen.test(input,expect,502))
    def test_number_3(self):
        """Local Var Decl"""
        input = 'Var: a=5;  Function: main Body: Var: b= "inner_string"; print(b); EndBody.'
        expect = 'inner_string'
        self.assertTrue(TestCodeGen.test(input,expect,503))
    def test_number_4(self):
        """Local Var Shadow"""
        input = 'Var: a=5,b="string";  Function: main Body: Var: b= "inner_string"; print(b); EndBody.'
        expect = 'inner_string'
        self.assertTrue(TestCodeGen.test(input,expect,504))
    def test_number_5(self):
        """Simple func decl"""
        input = 'Var: a=5,b="string";  Function: main Body: Var: b= "inner_string"; print(f1(b)); EndBody. Function: f1 Parameter: x Body: Return x; EndBody.'
        expect = 'inner_string'
        self.assertTrue(TestCodeGen.test(input,expect,505))
    def test_number_6(self):
        """Simple func decl"""
        input = 'Var: a=5,b="string";  Function: main Body: Var: b= "inner_string"; print(f1(a)); EndBody. Function: f1 Parameter: x Body: Return string_of_int(x); EndBody.'
        expect = '5'
        self.assertTrue(TestCodeGen.test(input,expect,506))
    def test_number_7(self):
        """Simple func decl"""
        input = 'Var: a=5,b="string";  Function: main Body: Var: x=7,y="x",z=1.5; print(f1(z)); EndBody. Function: f1 Parameter: x Body: Return "fixed string"; EndBody.'
        expect = 'fixed string'
        self.assertTrue(TestCodeGen.test(input,expect,507))
    def test_number_8(self):
        """Simple func decl"""
        input = 'Var: a=5,b="string";  Function: main Body: Var: x=7,y="x",z=1.5; print(f1(z)); EndBody. Function: f1 Parameter: x Body: Return string_of_float(x); EndBody.'
        expect = '1.5'
        self.assertTrue(TestCodeGen.test(input,expect,508))
    def test_number_9(self):
        """Simple func decl"""
        input = 'Var: a=5,b="string";  Function: main Body: Var: x=7,y="x",z=1.5; print(string_of_int(f1(x))); EndBody. Function: f1 Parameter: x Body: Return -x; EndBody.'
        expect = '-7'
        self.assertTrue(TestCodeGen.test(input,expect,509))
    def test_number_10(self):
        """Simple func decl"""
        input = 'Var: a=5,b="string";  Function: main Body: Var: x=7,y="x",z=1.5; print(string_of_int(f1(a,x))); EndBody. Function: f1 Parameter: x,y Body: Return x+y; EndBody.'
        expect = '12'
        self.assertTrue(TestCodeGen.test(input,expect,510))
    def test_number_11(self):
        """Simple func decl"""
        input = 'Var: a=5,b="string";  Function: main Body: Var: x=7,y="x",z=1.5; print(string_of_int(f1(x))); EndBody. Function: f1 Parameter: x Body: Return x+1--x; EndBody.'
        expect = '15'
        self.assertTrue(TestCodeGen.test(input,expect,511))
    def test_number_12(self):
        """Simple expressions"""
        input = 'Var: a=5,b="string",c=5.6;  Function: main Body: Var: x=7,y="x",z=2,k = 1.5; z = x + z -- z -- z\\2 +x*2 -1; print(string_of_int(z)); EndBody. '
        expect = '25'
        self.assertTrue(TestCodeGen.test(input,expect,512))
    def test_number_13(self):
        """Simple expressions"""
        input = 'Var: a=5,b="string",c=5.6;  Function: main Body: Var: x=7,y="x",z=2,k = 1.5; k = c +. k *.k -. float_to_int(z);  print(string_of_float(k)); EndBody. '
        expect = '5.85'
        self.assertTrue(TestCodeGen.test(input,expect,513))
    def test_number_14(self):
        """Simple expressions"""
        input = 'Var: a=5,b="string",c=5.6;  Function: main Body: Var: x=7,y="x",z=2,k = 1.5; z = x -1 + f1(k); print(string_of_int(z)); EndBody.  Function: f1 Parameter: x Body: Return int_of_float(x); EndBody.'
        expect = '7'
        self.assertTrue(TestCodeGen.test(input,expect,514))
    def test_number_15(self):
        """Simple expressions"""
        input = 'Var: a=5,b="string",c=5.6;  Function: main Body: Var: x=7,y="x",z=2,k = 1.5; b = "changed"; print(b); EndBody. '
        expect = 'changed'
        self.assertTrue(TestCodeGen.test(input,expect,515))
    def test_number_16(self):
        """Simple expressions"""
        input = 'Var: a=5,b="string",c=5.6;  Function: main Body: Var: x=7,y="x",z=2,k = 1.5; Var: temp = ""; temp = b; b=y; y= temp; print(b); print(y);  EndBody. '
        expect = 'xstring'
        self.assertTrue(TestCodeGen.test(input,expect,516))
    def test_number_17(self):
        """Float Rela"""
        input = 'Var: a=1.6, b= 0.4; Function: main Body: Var: t= True; f(a>.b);f(a<.b);f(a=/=b);f(a>=.b);f(a<=.b); EndBody. Function: f Parameter: x Body: print(string_of_bool(x)); Return; EndBody.'
        expect = 'truefalsetruetruefalse'
        self.assertTrue(TestCodeGen.test(input,expect,517))
    def test_number_18(self):
        """Int rela"""
        input = 'Var: a=4, b= 5; Function: main Body: Var: t= True; f(a>b);f(a<b);f(a==b);f(a!=b);f(a>=b);f(a<=b); EndBody. Function: f Parameter: x Body: print(string_of_bool(x)); Return; EndBody.'
        expect = 'falsetruefalsetruefalsetrue'
        self.assertTrue(TestCodeGen.test(input,expect,518))
    def test_number_19(self):
        """Simple expressions"""
        input = 'Var: a=5,b="string",c=5.6;  Function: main Body: Var: x=7,y="x",z=2,k = 1.5; print(f1(1,1.5,"2"));  EndBody. Function: f1 Parameter: a,b,c Body: Return string_of_int(a + int_of_float(b) + int_of_string( c)); EndBody. '
        expect = '4'
        self.assertTrue(TestCodeGen.test(input,expect,519))
    def test_number_20(self):
        """Global String"""
        input = 'Var: a=5,b="string",c=5.6;  Function: main Body: print(b);  EndBody.'
        expect = 'string'
        self.assertTrue(TestCodeGen.test(input,expect,520))
    def test_number_21(self):
        """Simple expressions"""
        input = 'Var: a=5,b="string",c=5.6;  Function: main Body: f1("random");  EndBody. Function: f1 Parameter: x Body: print("yea"); Return; EndBody.'
        expect = 'yea'
        self.assertTrue(TestCodeGen.test(input,expect,521))
    def test_number_22(self):
        """Ifs"""
        input = 'Var: a=5,b="string",c=5.6;  Function: main Body: If a == 5 Then print("a==5"); EndIf.  EndBody.'
        expect = 'a==5'
        self.assertTrue(TestCodeGen.test(input,expect,522))
    def test_number_23(self):
        """Ifs"""
        input = 'Var: a=5,b="string",c=5.6;  Function: main Body: If c =/= 6.0 Then print("not 6.0"); EndIf.  EndBody.'
        expect = 'not 6.0'
        self.assertTrue(TestCodeGen.test(input,expect,523))
    def test_number_24(self):
        """Ifs"""
        input = 'Var: a=5,b="string",c=5.6;  Function: main Body: If True Then print("True"); Else  print("false"); EndIf.  EndBody.'
        expect = 'True'
        self.assertTrue(TestCodeGen.test(input,expect,524))
    def test_number_25(self):
        """Ifs"""
        input = 'Var: a=5,b="string",c=5.6;  Function: main Body: If a==5 Then print("wow"); Else print("nan"); EndIf.  EndBody.'
        expect = 'wow'
        self.assertTrue(TestCodeGen.test(input,expect,525))
    def test_number_26(self):
        """Ifs"""
        input = 'Var: a=5,b="string",c=5.6;  Function: main Body:If (a>=5) && (a <= 10 )Then a = 6; ElseIf a ==7 Then a =7; Else a=10;EndIf. print(string_of_int(a)); EndBody.'
        expect = '6'
        self.assertTrue(TestCodeGen.test(input,expect,526))
    def test_number_27(self):
        """Ifs"""
        input = 'Var: a=5,b="string",c=5.6;  Function: main Body: If c >. 5.6 Then c = c+.1.0; EndIf. print(string_of_float(c)); If c <. 6e0 Then print("yes"); Else print("No"); EndIf.  EndBody.'
        expect = '5.6yes'
        self.assertTrue(TestCodeGen.test(input,expect,527))
    def test_number_28(self):
        """Ifs"""
        input = 'Function: main Body: Var: i = 7; If i == 1 Then print("1"); ElseIf i==2 Then print("2"); ElseIf i==3 Then print("3"); ElseIf i==4 Then print("4"); ElseIf i==7 Then print("7"); Else print("greater"); EndIf.  EndBody.'
        expect = '7'
        self.assertTrue(TestCodeGen.test(input,expect,528))
    def test_number_29(self):
        """Ifs"""
        input = 'Function: main Body: Var: i = 15; If i == 1 Then print("1"); ElseIf i==2 Then print("2"); ElseIf i==3 Then print("3"); ElseIf i==4 Then print("4"); ElseIf i==7 Then print("7"); Else print("greater"); EndIf.  EndBody.'
        expect = 'greater'
        self.assertTrue(TestCodeGen.test(input,expect,529))
    def test_number_30(self):
        """Ifs"""
        input = 'Function: main Body: Var: i = 1; If i == 1 Then print("1"); ElseIf i==2 Then print("2"); ElseIf i==3 Then print("3"); ElseIf i==4 Then print("4"); ElseIf i==7 Then print("7"); Else print("greater"); EndIf.  EndBody.'
        expect = '1'
        self.assertTrue(TestCodeGen.test(input,expect,530))
    def test_number_31(self):
        """Ifs"""
        input = 'Function: main Body: Var: a=1,b=2,c=3; If a +b +c > 3 Then If a+b>2 Then If a>1 Then print("a"); ElseIf b>1 Then print("b"); Else print("nei"); EndIf. EndIf. EndIf. EndBody.'
        expect = 'b'
        self.assertTrue(TestCodeGen.test(input,expect,531))
    def test_number_32(self):
        """Ifs"""
        input = 'Var:a=1,b=2,c=3; Function: main Body:  f1(b); EndBody. Function: f1 Parameter: a Body: If a>1 Then print("yes"); EndIf. Return; EndBody. '
        expect = 'yes'
        self.assertTrue(TestCodeGen.test(input,expect,532))
    def test_number_33(self):
        """Ifs"""
        input = 'Var:a=1,b=2,c=3; Function: main Body:  f1(a,b);  EndBody. Function: f1 Parameter: a,b Body: If a>b Then print("a"); Else print("b"); EndIf. Return; EndBody.'
        expect = 'b'
        self.assertTrue(TestCodeGen.test(input,expect,533))
    def test_number_34(self):
        """Ifs"""
        input = 'Var:a=1,b=2,c=3; Function: main Body: f1(1,1);  EndBody. Function: f1 Parameter: a,b Body: If a>b Then print("a"); Else print("b"); EndIf. Return; EndBody.'
        expect = 'b'
        self.assertTrue(TestCodeGen.test(input,expect,534))
    def test_number_35(self):
        """Ifs"""
        input = 'Var:a=1,b=2,c=3; Function: main  Body:f1(4,5); EndBody. Function: f1 Parameter: a,b Body: If a>b Then print(string_of_int(a)); Else print(string_of_int(b)); EndIf. Return; EndBody.'
        expect = '5'
        self.assertTrue(TestCodeGen.test(input,expect,535))
    def test_number_36(self):
        """Fors"""
        input = 'Var:a=1,b=2,c=3; Function: main Body:  For(a=1, a <5, 1) Do print(string_of_int(a)); EndFor. EndBody. '
        expect = '1234'
        self.assertTrue(TestCodeGen.test(input,expect,536))
    def test_number_37(self):
        """Fors"""
        input = 'Var:a=1,b=2,c=3; Function: main Body: Var: a = 15;  For(a=1, a <5, 1) Do print(string_of_int(a)); EndFor. EndBody. '
        expect = '1234'
        self.assertTrue(TestCodeGen.test(input,expect,537))
    def test_number_38(self):
        """Fors"""
        input = 'Var:a=1,b=2,c=3; Function: main Body: Var: a = 15; For(c=10,c>=0, -2) Do print(string_of_int(c)); EndFor. EndBody. '
        expect = '1086420'
        self.assertTrue(TestCodeGen.test(input,expect,538))
    def test_number_39(self):
        """Fors"""
        input = 'Var:a=1,b=2,c=3; Function: main Body: Var: a = 15; For(c=1,c<=5, 1) Do  print("start:"); print(string_of_int( c)); For(b=c-1,b>=-1,-1) Do print(string_of_int(b));EndFor. EndFor. EndBody. '
        expect = 'start:10-1start:210-1start:3210-1start:43210-1start:543210-1'
        self.assertTrue(TestCodeGen.test(input,expect,539))
    def test_number_40(self):
        """Fors"""
        input = 'Var:a=1,b=2,c=3; Function:  main Body: Var: a = 15; For (a=b, a<c, 1) Do print(string_of_int(a)); EndFor. EndBody. '
        expect = '2'
        self.assertTrue(TestCodeGen.test(input,expect,540))
    def test_number_41(self):
        """Fors"""
        input = 'Var:a=1,b=2,c=3; Function:  main Body: Var: a = 15,b=10,c=15; For(a=0,a<b,1) Do print(string_of_int(a)); EndFor.  For(b=0,b<c,1) Do print(string_of_int(b)); EndFor.  EndBody. '
        expect = '012345678901234567891011121314'
        self.assertTrue(TestCodeGen.test(input,expect,541))
    def test_number_42(self):
        """Fors"""
        input = 'Var:a=1,b=2,c=3; Function:main Body: Var: a = 15,b=10,c=15;   For(a=0,a<10,1)  Do EndFor. print(string_of_int(a)); EndBody. '
        expect = '10'
        self.assertTrue(TestCodeGen.test(input,expect,542))
    def test_number_43(self):
        """Fors"""
        input = 'Var:a=1,b=2,c=3; Function:main Body: Var: a = 15;   For(a=0,a<5,1) Do Var: i=0,j=0; i=b+a; j=c+a;  print(string_of_int(i+j));   EndFor. EndBody. '
        expect = '5791113'
        self.assertTrue(TestCodeGen.test(input,expect,543))
    def test_number_44(self):
        """Fors"""
        input = 'Var:a=1,b=2,c=3; Function:main Body: Var: a = 5,b=5,c=15;  Var: i=0,j=0; For(i=a-5, j<b, c-14) Do print(string_of_int(i)); j=j+2; EndFor. EndBody. '
        expect = '012'
        self.assertTrue(TestCodeGen.test(input,expect,544))
    def test_number_45(self):
        """While"""
        input = 'Var: a=1,b=2,c=3; Function: main Body: Var: x=5,y=6,z=7; While (z<0) Do print("yeas"); EndWhile. print("?"); EndBody.'
        expect = '?'
        self.assertTrue(TestCodeGen.test(input,expect,545))
    def test_number_46(self):
        """While"""
        input = 'Var: a=1,b=2,c=3; Function: main Body: Var: x=5,y=6,z=7; While (x>0) Do print("x"); x=x-b; EndWhile. print("?"); EndBody.'
        expect = 'xxx?'
        self.assertTrue(TestCodeGen.test(input,expect,546))
    def test_number_47(self):
        """While"""
        input = 'Var: a=1,b=2,c=3; Function: main Body: Var: x=5,y=6,z=7; While (y+z > x) Do print(string_of_int(y+z)); y=y-a; z=z-a; EndWhile. print("?"); EndBody.'
        expect = '131197?'
        self.assertTrue(TestCodeGen.test(input,expect,547))
    def test_number_48(self):
        """While"""
        input = 'Var: a=1,b=2,c=3; Function: main Body: Var: x=5,y=6,z=7; While (z>a) Do c= z; While (c>a) Do print(string_of_int(c)); c=c-1; EndWhile. z=z-1; EndWhile. print("?"); EndBody.'
        expect = '765432654325432432322?'
        self.assertTrue(TestCodeGen.test(input,expect,548))
    def test_number_49(self):
        """While"""
        input = 'Var: a=1,b=2,c=3; Function: main Body: Var: x=5,y=6,z=7; While (z>a) Do c= a; While (c<z) Do print(string_of_int(c)); c=c+1; EndWhile. z=z-1; EndWhile. print("?"); EndBody.'
        expect = '123456123451234123121?'
        self.assertTrue(TestCodeGen.test(input,expect,549))
    def test_number_50(self):
        """While"""
        input = 'Var: a=1,b=2,c=3; Function: main Body: Var: x=5,y=6,z=7; While (x>0) Do print(string_of_int(x)); x=x-b; EndWhile. While(x<5) Do print(string_of_int(x)); x=x+a; EndWhile. print(string_of_int(x));  EndBody.'
        expect = '531-1012345'
        self.assertTrue(TestCodeGen.test(input,expect,550))
    def test_number_51(self):
        """While"""
        input = 'Var: a=1,b=2,c=3; Function: main Body: Var: x=5,y=6,z=7; While (x>0) Do print(string_of_int(x)); x=x-b; EndWhile. While(x>0) Do print(string_of_int(x)); x=x+a; EndWhile. print(string_of_int(x));  EndBody.'
        expect = '531-1'
        self.assertTrue(TestCodeGen.test(input,expect,551))
    def test_number_52(self):
        """While"""
        input = 'Var: a=1,b=2,c=3; Function: main Body: Var: x=5,y=6,z=7; While (x>5) Do print(string_of_int(x)); x=x-1; EndWhile.  EndBody.'
        expect = ''
        self.assertTrue(TestCodeGen.test(input,expect,552))
    def test_number_53(self):
        """DoWhile"""
        input = 'Var: a=1,b=2,c=3; Function: main Body: Var: x=5,y=6,z=7; Do print(string_of_int(x)); x=x-1; While x>5 EndDo.  EndBody.'
        expect = '5'
        self.assertTrue(TestCodeGen.test(input,expect,553))
    def test_number_54(self):
        """DoWhile"""
        input = 'Var: a=1,b=2,c=3; Function: main Body: Var: x=5,y=6,z=7; Do print(string_of_int(z)); z=z-b; While z>a EndDo.  EndBody.'
        expect = '753'
        self.assertTrue(TestCodeGen.test(input,expect,554))
    def test_number_55(self):
        """DoWhile"""
        input = 'Var: a=1,b=2,c=3; Function: main Body: Var: x=5,y=6,z=7; Do print("x"); x=x-b; While (x>0) EndDo.print("?"); EndBody.'
        expect = 'xxx?'
        self.assertTrue(TestCodeGen.test(input,expect,555))
    def test_number_56(self):
        """Array Decl"""
        input = 'Var: a[1] = {1}; Function: main Body: print(string_of_int(a[0])); EndBody.'
        expect = '1'
        self.assertTrue(TestCodeGen.test(input,expect,556))
    def test_number_57(self):
        """Array Decl"""
        input = 'Var: a[1] = {1}; Function: main Body: Var: a[1] = {2}; print(string_of_int(a[0])); EndBody.'
        expect = '2'
        self.assertTrue(TestCodeGen.test(input,expect,557))
    def test_number_58(self):
        """Array Decl"""
        input = 'Var: a[2][1] = {{1},{2}}; Function: main Body: print(string_of_int(a[0][0])); EndBody.'
        expect = '1'
        self.assertTrue(TestCodeGen.test(input,expect,558))
    def test_number_59(self):
        """Array Decl"""
        input = 'Var: a[1] = {10}; Function: main Body: Var: a[2][1] = {{1},{2}}; print(string_of_int(a[0][0])); EndBody.'
        expect = '1'
        self.assertTrue(TestCodeGen.test(input,expect,559))
    def test_number_60(self):
        """Array Assignment"""
        input = 'Var: a[2][1] = {{1},{2}}; Function: main Body: a= {{99},{98}}; print(string_of_int(a[1][0])); EndBody.'
        expect = '98'
        self.assertTrue(TestCodeGen.test(input,expect,560))
    def test_number_61(self):
        """Array Assignment"""
        input = 'Var: a[1] = {1}; Function: main Body: a={78}; print(string_of_int(a[0])); EndBody.'
        expect = '78'
        self.assertTrue(TestCodeGen.test(input,expect,561))
    def test_number_62(self):
        """Array Assignment"""
        input = 'Var: a[1][1][1] = {{{5}}}; Function: main Body: a={{{78}}}; print(string_of_int(a[0][0][0])); EndBody.'
        expect = '78'
        self.assertTrue(TestCodeGen.test(input,expect,562))
    def test_number_63(self):
        """Array Assignment"""
        input = 'Var: a[3][2][1][1] = {{{{1}},{{2}}},{{{3}},{{4}}},{{{5}},{{6}}}}; Function: main Body: a={{{{7}},{{8}}},{{{9}},{{10}}},{{{11}},{{12}}}}; print(string_of_int(a[0][0][0][0])); print(string_of_int(a[2][1][0][0])); EndBody.'
        expect = '712'
        self.assertTrue(TestCodeGen.test(input,expect,563))
    def test_number_64(self):
        """Array cell use"""
        input = 'Function: main Body: Var: a [3][3] = {{1,2,3},{4,5,6},{7,8,9}}; a[0][0] = 10; print(string_of_int(a[0][0])); EndBody.'
        expect = '10'
        self.assertTrue(TestCodeGen.test(input,expect,564))
    def test_number_65(self):
        """Array cell use"""
        input = 'Function: main Body: Var: a [3][3] = {{1,2,3},{4,5,6},{7,8,9}}, b=100; b= a[0][0] + a[0][1] + a[0][2]; print(string_of_int(b)); EndBody. '
        expect = '6'
        self.assertTrue(TestCodeGen.test(input,expect,565))
    def test_number_66(self):
        """Array cell use"""
        input = 'Function: main Body: Var: a [3][3] = {{1,2,3},{4,5,6},{7,8,9}}, b=100;a[0][0] = a[0][1] + a[0][2]; print(string_of_int(a[0][0])); EndBody. '
        expect = '5'
        self.assertTrue(TestCodeGen.test(input,expect,566))
    def test_number_67(self):
        """Array cell use"""
        input = 'Function: main Body: Var: a [3][3] = {{1,2,3},{4,5,6},{7,8,9}}, b=100; If a[0][0] < a[0][1] Then print(string_of_int(a[0][0] + b));  EndIf. EndBody. '
        expect = '101'
        self.assertTrue(TestCodeGen.test(input,expect,567))
    def test_number_68(self):
        """Array cell use"""
        input = 'Function: main Body: Var: a [3][3] = {{1,2,3},{4,5,6},{7,8,9}}, b=100; If b< a[1][2] Then print(string_of_int(a[1][2])); ElseIf b<a[1][0] Then print("damm"); Else print("b"); EndIf.  EndBody. '
        expect = 'b'
        self.assertTrue(TestCodeGen.test(input,expect,568))
    def test_number_69(self):
        """Many Arrays"""
        input = 'Var: a[2][1] = {{42},{69}}, b[1] = {10}; Function: main Body: Var: c [3][3] = {{1,2,3},{4,5,6},{7,8,9}}, d[5] = {99,99,99,99,99},x=50;  print(string_of_int(x+d[2]+a[1][0]+ c[1][1] ));EndBody.'
        expect = '223'
        self.assertTrue(TestCodeGen.test(input,expect,569))
    def test_number_70(self):
        """Many Arrays"""
        input = 'Var: a[2][1] = {{42},{69}}, b[1] = {10}; Function: main Body: Var: c [3][3] = {{1,2,3},{4,5,6},{7,8,9}}, d[5] = {99,99,99,99,99},x=50; If a[0][0] > b[0] Then print("a>b"); Else print("b>a"); EndIf.  EndBody.'
        expect = 'a>b'
        self.assertTrue(TestCodeGen.test(input,expect,570))
    def test_number_71(self):
        """Many Arrays"""
        input = 'Var: a[2][1] = {{42},{69}}, b[1] = {10}; Function: main Body: Var: c [3][3] = {{1,2,3},{4,5,6},{7,8,9}}, d[5] = {99,99,99,99,99},x=50;  d[2] = a[1][0] - b[0] - c[0][0]; print(string_of_int(d[2] + x)); EndBody.'
        expect = '108'
        self.assertTrue(TestCodeGen.test(input,expect,571))
    def test_number_72(self):
        """return array"""
        input = 'Function: main Body: Var: a[3] = {1,2,3}; a = f(a); f1(a[0]); f1(a[1]); f1(a[2]); EndBody. Function: f Parameter: x[3] Body: x[0] = x[0] + 1; x[1] = x[1]+2; x[2] = x[2] + 3; Return x; EndBody. Function: f1 Parameter: temp Body: print(string_of_int(temp)); Return; EndBody.'
        expect = '246'
        self.assertTrue(TestCodeGen.test(input,expect,572))
    def test_number_73(self):
        """return array"""
        input = 'Function: main Body: Var: a[3] = {1,2,3}; a = f(); f1(a[0]); f1(a[1]); f1(a[2]); EndBody. Function: f Body:  Return {7,8,9}; EndBody. Function: f1 Parameter: temp Body: print(string_of_int(temp)); Return; EndBody.'
        expect = '789'
        self.assertTrue(TestCodeGen.test(input,expect,573))
    def test_number_74(self):
        """return array cell"""
        input = 'Function: main Body: Var: a[3] = {1,2,3}; a[1] = f(a); f1(a[0]); f1(a[1]); f1(a[2]); EndBody. Function: f Parameter: x[3] Body:  Return x[2] + 1; EndBody. Function: f1 Parameter: temp Body: print(string_of_int(temp)); Return; EndBody.'
        expect = '143'
        self.assertTrue(TestCodeGen.test(input,expect,574))
    def test_number_75(self):
        """return array cell"""
        input = 'Function: main Body: Var: a[3] = {1,2,3},b=0; b = f(a); f1(b); EndBody. Function: f Parameter: x[3] Body:  Return x[0]+ x[1] + x[2]; EndBody. Function: f1 Parameter: temp Body: print(string_of_int(temp)); Return; EndBody.'
        expect = '6'
        self.assertTrue(TestCodeGen.test(input,expect,575))
    def test_number_76(self):
        """Complex arith"""
        input = 'Function: main Body: Var: a=5,b=3,c=2; print(string_of_int(a*10 + b*100 + c*1000)); EndBody.'
        expect = '2350'
        self.assertTrue(TestCodeGen.test(input,expect,576))
    def test_number_77(self):
        """Complex arith"""
        input = 'Function: main Body: Var: a=5,b=3,c=2; print(string_of_float(float_to_int(a)\\. float_to_int(b)*. 100.0)); EndBody.'
        expect = '166.66666'
        self.assertTrue(TestCodeGen.test(input,expect,577))
    def test_number_78(self):
        """Complex arith"""
        input = 'Function: main Body: Var: a = 5,b=3,c=3; print(string_of_int(a\\b)); print(string_of_int(a%b)); EndBody.'
        expect = '12'
        self.assertTrue(TestCodeGen.test(input,expect,578))
    def test_number_79(self):
        """print all array"""
        input = 'Function: main Body: Var: a[3][3] = {{1,2,3},{4,5,6},{7,8,9}}; f(a); EndBody. Function: f Parameter: x[3][3] Body: Var: i=0, j=0; For(i=0, i<3,1) Do For (j=0,j<3,1) Do print(string_of_int(x[i][j])); EndFor. EndFor. Return; EndBody.'
        expect = '123456789'
        self.assertTrue(TestCodeGen.test(input,expect,579))
    def test_number_80(self):
        """for with array cell"""
        input = 'Var: a[3] = {"1","2","3"}, b[3] = {"","",""}; Function: main Body: Var: i =0; For (i=int_of_string(a[0])-1, i<int_of_string(a[2]), int_of_string(a[1])-1) Do b[i] = "changed"; EndFor. print(a[0]); print(a[1]); print(a[2]); print(b[0]); print(b[1]); print(b[2]); EndBody.'
        expect = '123changedchangedchanged'
        self.assertTrue(TestCodeGen.test(input,expect,580))
    def test_number_81(self):
        """while arraycell"""
        input = 'Var: a[4] = {1,0,0,1}; Function: main Body: Var:i =0; While (i<4) Do a[i] = 1; i=i+1; If i==4 Then Break; EndIf. EndWhile. For(i=0,i<4,1) Do print(string_of_int(a[i])); EndFor. EndBody.'
        expect = '1111'
        self.assertTrue(TestCodeGen.test(input,expect,581))
    def test_number_82(self):
        """string swapping"""
        input = 'Function: main Body: Var: a = "a", b = "b"; f1(a,b); print(a); print(b); EndBody. Function: f1 Parameter: x,y Body: Var: temp = ""; temp = x; x=y; y=temp; Return; EndBody.'
        expect = 'ab'
        self.assertTrue(TestCodeGen.test(input,expect,582))
    def test_number_83(self):
        """array swapping"""
        input = 'Function: main Body: Var: a[1] = {1}, b[1] ={2} ; f1(a,b); print(string_of_int(a[0])); print(string_of_int(b[0])); EndBody. Function: f1 Parameter: x[1],y[1] Body: Var: temp[1] = {0}; temp = x; x=y; y=temp; Return; EndBody.'
        expect = '12'
        self.assertTrue(TestCodeGen.test(input,expect,583))
    def test_number_84(self):
        """loop control cond"""
        input = 'Function: main Body: Var: i=10; For(i=0,i<10,1) Do If i ==5 Then Break;  EndIf. print(string_of_int(i)); EndFor. print("end"); EndBody.'
        expect = '01234end'
        self.assertTrue(TestCodeGen.test(input,expect,584))
    def test_number_85(self):
        """loop control cond"""
        input = 'Function: main Body: Var: i=10; For(i=0,i<10,1) Do  If i ==5 Then Continue;  EndIf. print(string_of_int(i)); EndFor. print("end"); EndBody.'
        expect = '012346789end'
        self.assertTrue(TestCodeGen.test(input,expect,585))
    def test_number_86(self):
        """loop control cond"""
        input = 'Function: main Body: Var: i=10; For(i=0,i<10,1) Do If i ==5 Then Return;  EndIf. print(string_of_int(i)); EndFor. print("end"); EndBody.'
        expect = '01234'
        self.assertTrue(TestCodeGen.test(input,expect,586))
    def test_number_87(self):
        """loop control cond"""
        input = 'Function: main Body: Var: i=10; f1(i); EndBody. Function: f1 Parameter: x Body: Var: i = 0; For (i=0 , i<=x, 1) Do Var: j = 0; For (j=x-i, j>=0, -1) Do If j==(x-i)\\2 Then Continue; EndIf. If j%2 ==0 Then print(string_of_int(j));  Else print(string_of_int(-j)); EndIf. EndFor. If i == x\\2 Then Break; EndIf. EndFor. Return; EndBody.'
        expect = '10-98-764-32-10-98-76-5-32-108-76-5-32-10-76-542-106-542-10-54-3-10'
        self.assertTrue(TestCodeGen.test(input,expect,587))
    def test_number_88(self):
        """loop control cond"""
        input = 'Function: main Body: Var: x = 10; While x>0 Do If x<3 Then Break; ElseIf x%2==0 Then x=x-1; Continue; EndIf. print(string_of_int(x)); x=x-1; EndWhile. EndBody.'
        expect = '9753'
        self.assertTrue(TestCodeGen.test(input,expect,588))
    def test_number_89(self):
        """loop control cond"""
        input = 'Function: main Body: Var: x = 10;  Do If x<3 Then Break; ElseIf x%2==0 Then x=x-1; Continue; EndIf. print(string_of_int(x)); x=x-1;While x>0 EndDo. EndBody.'
        expect = '9753'
        self.assertTrue(TestCodeGen.test(input,expect,589))
    def test_number_90(self):
        """recursive"""
        input = 'Function: main Body: Var: a=88, b = 76; print(string_of_int(gcd(a,b))); EndBody. Function: gcd Parameter: a,b Body: If a==0 Then Return b; EndIf. If b==0 Then Return a; EndIf. If a==b Then Return a ; EndIf. If a>b Then Return gcd(a-b,b); EndIf. Return gcd(a,b-a); EndBody.'
        expect = '4'
        self.assertTrue(TestCodeGen.test(input,expect,590))
    def test_number_91(self):
        """recursive"""
        input = 'Function: main Body: Var: a = 9; print(string_of_int(factorial(a))); EndBody. Function: factorial Parameter: x Body: If (x == 0) || (x ==1) Then Return 1; EndIf. Return x * factorial(x-1); EndBody.'
        expect = '362880'
        self.assertTrue(TestCodeGen.test(input,expect,591))
    def test_number_92(self):
        """nested func call"""
        input = 'Function: main Body: Var: x = 5; print(string_of_int(f(x))); EndBody. Function: f Parameter: x Body: Return f1(x); EndBody. Function: f1 Parameter: x Body: Return f2(x); EndBody. Function: f2 Parameter: x Body: Return f3(x); EndBody. Function: f3 Parameter: x Body: Return x+1; EndBody.'
        expect = '6'
        self.assertTrue(TestCodeGen.test(input,expect,592))
    def test_number_93(self):
        """If Return"""
        input = 'Function: main Body: Var: x = 3; print(f1(x)); EndBody. Function: f1 Parameter: z Body: If z==1 Then Return "1"; ElseIf z==2 Then Return "2"; ElseIf z==3 Then Return "3"; Else print("noshit"); Return ""; EndIf. Return "Done"; EndBody. '
        expect = '3'
        self.assertTrue(TestCodeGen.test(input,expect,593))
    def test_number_94(self):
        """nested func call"""
        input = 'Function: main Body: Var: x = 5; print(string_of_int(f(x))); EndBody. Function: f Parameter: x Body: Return f1(x)+1; EndBody. Function: f1 Parameter: x Body: Return f2(x)+1; EndBody. Function: f2 Parameter: x Body: Return f3(x)+1; EndBody. Function: f3 Parameter: x Body: Return x+1; EndBody.'
        expect = '9'
        self.assertTrue(TestCodeGen.test(input,expect,594))
    def test_number_95(self):
        """Float div"""
        input = 'Function: main Body: Var: x=12.5, y=3.4; print(string_of_float(f(x,y))); EndBody. Function: f Parameter: a,b Body: Return a\\.b; EndBody.'
        expect = '3.6764705'
        self.assertTrue(TestCodeGen.test(input,expect,595))
    def test_number_96(self):
        """bool arith"""
        input = 'Function: main Body: Var: t= True, f=False, x=15,y=3,z=12.5,k=4.3; t=(x>y) && !(k=/=z) || !!!f ||!t; print(string_of_bool(t)); EndBody.'
        expect = 'true'
        self.assertTrue(TestCodeGen.test(input,expect,596))
    def test_number_97(self):
        """float arith"""
        input = 'Function: main Body: Var: a=1.2, b=1.8, c= 5.0; c = c *.b \\.a -.a -.-.a +.c; print(string_of_float( c)); EndBody.'
        expect = '12.499999'
        self.assertTrue(TestCodeGen.test(input,expect,597))
    def test_number_98(self):
        """short circuit"""
        input = 'Function: main Body: If True || (1\\0>2) Then print("cir-ed"); EndIf. EndBody.'
        expect = 'cir-ed'
        self.assertTrue(TestCodeGen.test(input,expect,598))
    def test_number_99(self):
        """short circuit"""
        input = 'Function: main Body: If !(False && (1\\0>2)) Then print("cir-ed"); EndIf. EndBody.'
        expect = 'cir-ed'
        self.assertTrue(TestCodeGen.test(input,expect,599))
    def test_number_100(self):
        """indexing array returned from function call"""
        input = 'Function: f Body: Return {{1,2},{3,4}}; EndBody. Function: main Body: print(string_of_int(f()[1][0])); EndBody. '
        expect = '3'
        self.assertTrue(TestCodeGen.test(input,expect,600))
    def test_number_101(self):
        """indexing array returned from function call"""
        input = 'Function: f Parameter: a[2] Body: a[0] = 5; a[1]=6; Return a; EndBody. Function: main Body: Var: a[2] = {1,2}; f(a)[1]= 5; print(string_of_int(a[0])); print(string_of_int(a[1])); EndBody. '
        expect = '55'
        self.assertTrue(TestCodeGen.test(input,expect,601))
    def test_number_102(self):
        """indexing array returned from function call"""
        input = 'Function: f Parameter: a[6],n Body: a[n] = 888; Return a; EndBody. Function: main Body:Var: a[6] = {1,2,3,4,5,6}; f(a,(1+2+3\\2+101-a[3]*6)%6)[a[3]%6]= 999; print(string_of_int(a[0])); print(string_of_int(a[1]));print(string_of_int(a[2]));print(string_of_int(a[3]));print(string_of_int(a[4])); print(string_of_int(a[5])); EndBody. '
        expect = '9992388856'
        self.assertTrue(TestCodeGen.test(input,expect,602))
    def test_number_103(self):
        """Equal float cmp"""
        input = 'Var: a=1.6, b= 1.6; Function: main Body: Var: t= True; f(a>.b);f(a<.b);f(a=/=b);f(a>=.b);f(a<=.b); EndBody. Function: f Parameter: x Body: print(string_of_bool(x)); Return; EndBody.'
        expect = 'falsefalsefalsetruetrue'
        self.assertTrue(TestCodeGen.test(input,expect,603))
    def test_number_104(self):
        """pass by ref"""
        input = 'Function: main Body: Var: a[2][2] = {{1,2},{3,4}} ; f1(a); print(string_of_int(a[0][0])); print(string_of_int(a[0][1])); EndBody. Function: f1 Parameter: x[2][2] Body: x[0][0]= x[0][1];  Return; EndBody.'
        expect = '22'
        self.assertTrue(TestCodeGen.test(input,expect,604))
    def test_number_105(self):
        """pass by ref"""
        input = 'Function: main Body: Var: a[1] = {1}, b[1] ={2} ; f1(a,b); print(string_of_int(a[0])); print(string_of_int(b[0])); EndBody. Function: f1 Parameter: x[1],y[1] Body: Var: temp = 0; temp = x[0]; x[0]=y[0]; y[0]=temp; Return; EndBody.'
        expect = '21'
        self.assertTrue(TestCodeGen.test(input,expect,605))
    def test_number_106(self):
        """pass by val"""
        input = 'Function: main Body: Var: a =1, b =2; f(a,b); print(string_of_int(a)); print(string_of_int(b)); EndBody. Function: f Parameter: a,b Body: Var: temp = 0; temp = a; a=b; b= temp; Return; EndBody.'
        expect = '12'
        self.assertTrue(TestCodeGen.test(input,expect,606))
    def test_number_107(self):
        """local array string"""
        input = 'Function: main Body: Var: a[3] = {"1","2","3"}, b[3] = {"","",""}; Var: i =0; For (i=int_of_string(a[0])-1, i<int_of_string(a[2]), int_of_string(a[1])-1) Do b[i] = "changed"; EndFor. print(a[0]); print(a[1]); print(a[2]); print(b[0]); print(b[1]); print(b[2]); EndBody.'
        expect = '123changedchangedchanged'
        self.assertTrue(TestCodeGen.test(input,expect,607))
    def test_number_108(self):
        """nested string array"""
        input = 'Var: b[3][1][1] = {{{""}},{{""}},{{""}}}; Function: main Body: Var: a[3][1][1] = {{{"1"}},{{"2"}},{{"3"}}}; Var: i =0; For (i=int_of_string(a[0][0][0])-1, i<int_of_string(a[2][0][0]), int_of_string(a[1][0][0])-1) Do b[i][0][0] = "changed"; EndFor. print(a[0][0][0]); print(a[1][0][0]); print(a[2][0][0]); print(b[0][0][0]); print(b[1][0][0]); print(b[2][0][0]); EndBody.'
        expect = '123changedchangedchanged'
        self.assertTrue(TestCodeGen.test(input,expect,608))
    def test_number_109(self):
        """print all string array"""
        input = 'Function: main Body: Var: a[3][3] = {{"1","2","3"},{"4","5","6"},{"7","8","9"}}; f(a); EndBody. Function: f Parameter: x[3][3] Body: Var: i=0, j=0; For(i=0, i<3,1) Do For (j=0,j<3,1) Do print((x[i][j])); EndFor. EndFor. Return; EndBody.'
        expect = '123456789'
        self.assertTrue(TestCodeGen.test(input,expect,609))
    def test_number_110(self):
        """print all string array global"""
        input = 'Function: main Body: Var: a[3][3] = {{"1","2","3"},{"4","5","6"},{"7","8","9"}}; f(a); EndBody. Function: f Parameter: x[3][3] Body: Var: i=0, j=0; For(i=0, i<3,1) Do For (j=0,j<3,1) Do print((x[i][j])); EndFor. EndFor. Return; EndBody.'
        expect = '123456789'
        self.assertTrue(TestCodeGen.test(input,expect,610))


