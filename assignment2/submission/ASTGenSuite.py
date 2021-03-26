import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    # def test_simple_program(self):
    #     """Simple program: int main() {} """
    #     input = """Var:x;"""
    #     expect = Program([VarDecl(Id("x"),[],None)])
    #     self.assertTrue(TestAST.checkASTGen(input,expect,300))

   #MY CODE
    def test_number_0(self):
        """Simple var dec"""
        self.assertTrue(TestAST.checkASTGen('Var: x;','Program([VarDecl(Id(x))])',300))
    def test_number_1(self):
        """Multi var dec"""
        self.assertTrue(TestAST.checkASTGen('Var: x,y,z;','Program([VarDecl(Id(x)),VarDecl(Id(y)),VarDecl(Id(z))])',301))
    def test_number_2(self):
        """Var dec with init value"""
        self.assertTrue(TestAST.checkASTGen('Var: x,y=10,   z=30, g, f;','Program([VarDecl(Id(x)),VarDecl(Id(y),IntLiteral(10)),VarDecl(Id(z),IntLiteral(30)),VarDecl(Id(g)),VarDecl(Id(f))])',302))
    def test_number_3(self):
        """Array dec"""
        self.assertTrue(TestAST.checkASTGen('Var: array[5][6][7], a,c,c,   another[0];','Program([VarDecl(Id(array),[5,6,7]),VarDecl(Id(a)),VarDecl(Id(c)),VarDecl(Id(c)),VarDecl(Id(another),[0])])',303))
    def test_number_4(self):
        """Array with init"""
        self.assertTrue(TestAST.checkASTGen('Var: a, array[5][3],c  = {1,2,3,{1,2},{1,2,{1},{3,4}}};','Program([VarDecl(Id(a)),VarDecl(Id(array),[5,3]),VarDecl(Id(c),ArrayLiteral(IntLiteral(1),IntLiteral(2),IntLiteral(3),ArrayLiteral(IntLiteral(1),IntLiteral(2)),ArrayLiteral(IntLiteral(1),IntLiteral(2),ArrayLiteral(IntLiteral(1)),ArrayLiteral(IntLiteral(3),IntLiteral(4)))))])',304))
    def test_number_5(self):
        """Mixed declatation"""
        self.assertTrue(TestAST.checkASTGen('Var: a=6,c,y, arr[6][7]={1,2,{6}}, g="String", xx=12e7;','Program([VarDecl(Id(a),IntLiteral(6)),VarDecl(Id(c)),VarDecl(Id(y)),VarDecl(Id(arr),[6,7],ArrayLiteral(IntLiteral(1),IntLiteral(2),ArrayLiteral(IntLiteral(6)))),VarDecl(Id(g),StringLiteral(String)),VarDecl(Id(xx),FloatLiteral(120000000.0))])',305))
    def test_number_6(self):
        """Function no endline"""
        self.assertTrue(TestAST.checkASTGen('Function: empty Body: EndBody.','Program([FuncDecl(Id(empty)[],([][]))])',306))
    def test_number_7(self):
        """Simple param"""
        self.assertTrue(TestAST.checkASTGen('Function: main \n Parameter: n,c,y Body: EndBody.','Program([FuncDecl(Id(main)[VarDecl(Id(n)),VarDecl(Id(c)),VarDecl(Id(y))],([][]))])',307))
    def test_number_8(self):
        """Simple function no param"""
        self.assertTrue(TestAST.checkASTGen('Function: main \n Body: \n x = 10; fact(x); \n EndBody.','Program([FuncDecl(Id(main)[],([][Assign(Id(x),IntLiteral(10)),CallStmt(Id(fact),[Id(x)])]))])',308))
    def test_number_9(self):
        """Simple function param"""
        self.assertTrue(TestAST.checkASTGen('Function: main Parameter: n Body: assign = 10; EndBody.','Program([FuncDecl(Id(main)[VarDecl(Id(n))],([][Assign(Id(assign),IntLiteral(10))]))])',309))
    def test_number_10(self):
        """Funcition with var dec """
        self.assertTrue(TestAST.checkASTGen('Function: main Parameter: n Body: Var: i=0; assign = 10; EndBody.','Program([FuncDecl(Id(main)[VarDecl(Id(n))],([VarDecl(Id(i),IntLiteral(0))][Assign(Id(assign),IntLiteral(10))]))])',310))
    def test_number_11(self):
        """Function param has array element"""
        self.assertTrue(TestAST.checkASTGen('Function: main Parameter: n, a[2][3] Body: i =5; EndBody.','Program([FuncDecl(Id(main)[VarDecl(Id(n)),VarDecl(Id(a),[2,3])],([][Assign(Id(i),IntLiteral(5))]))])',311))
    def test_number_12(self):
        """Double function"""
        self.assertTrue(TestAST.checkASTGen('Function: main Parameter: n, a[2][3] Body: i =5; EndBody.Function: main Parameter: n, a[2][3] Body: i =5; EndBody.','Program([FuncDecl(Id(main)[VarDecl(Id(n)),VarDecl(Id(a),[2,3])],([][Assign(Id(i),IntLiteral(5))])),FuncDecl(Id(main)[VarDecl(Id(n)),VarDecl(Id(a),[2,3])],([][Assign(Id(i),IntLiteral(5))]))])',312))
    def test_number_13(self):
        """just IF"""
        self.assertTrue(TestAST.checkASTGen('Function: main \n Body: \n If x>3 Then n=10;   EndIf. \n EndBody.','Program([FuncDecl(Id(main)[],([][If(BinaryOp(>,Id(x),IntLiteral(3)),[],[Assign(Id(n),IntLiteral(10))])Else([],[])]))])',313))
    def test_number_14(self):
        """one elseif no else"""
        self.assertTrue(TestAST.checkASTGen('Function: main Body: If a==b Then a=5; ElseIf a!=b Then Return; EndIf. EndBody.','Program([FuncDecl(Id(main)[],([][If(BinaryOp(==,Id(a),Id(b)),[],[Assign(Id(a),IntLiteral(5))])ElseIf(BinaryOp(!=,Id(a),Id(b)),[],[Return()])Else([],[])]))])',314))
    def test_number_15(self):
        """if elseif else"""
        self.assertTrue(TestAST.checkASTGen('Function: main Body: If  1+ 2 Then printf(); ElseIf !True Then Break; Else Return; EndIf. EndBody.','Program([FuncDecl(Id(main)[],([][If(BinaryOp(+,IntLiteral(1),IntLiteral(2)),[],[CallStmt(Id(printf),[])])ElseIf(UnaryOp(!,BooleanLiteral(true)),[],[Break()])Else([],[Return()])]))])',315))
    def test_number_16(self):
        """else no elseif"""
        self.assertTrue(TestAST.checkASTGen('Function: main Body: If 7e3 *. "5" Then a=""; Else b(); EndIf. EndBody.','Program([FuncDecl(Id(main)[],([][If(BinaryOp(*.,FloatLiteral(7000.0),StringLiteral(5)),[],[Assign(Id(a),StringLiteral())])Else([],[CallStmt(Id(b),[])])]))])',316))
    def test_number_17(self):
        """multiple else if"""
        self.assertTrue(TestAST.checkASTGen('Function: main Body: If nothing Then x[3]=1; ElseIf 12.3 Then a[2]={1}; ElseIf "Nah\\n" Then sendError(); Else Return; EndIf. EndBody.','Program([FuncDecl(Id(main)[],([][If(Id(nothing),[],[Assign(ArrayCell(Id(x),[IntLiteral(3)]),IntLiteral(1))])ElseIf(FloatLiteral(12.3),[],[Assign(ArrayCell(Id(a),[IntLiteral(2)]),ArrayLiteral(IntLiteral(1)))])ElseIf(StringLiteral(Nah\\n),[],[CallStmt(Id(sendError),[])])Else([],[Return()])]))])',317))
    def test_number_18(self):
        """two ifs"""
        self.assertTrue(TestAST.checkASTGen('Function: main Body: If (a||b) Then Return; Else Break; EndIf. If a>b+c Then Break; ElseIf nothing Then Return; Else Continue; EndIf. EndBody.','Program([FuncDecl(Id(main)[],([][If(BinaryOp(||,Id(a),Id(b)),[],[Return()])Else([],[Break()]),If(BinaryOp(>,Id(a),BinaryOp(+,Id(b),Id(c))),[],[Break()])ElseIf(Id(nothing),[],[Return()])Else([],[Continue()])]))])',318))
    def test_number_19(self):
        """if <nested if> elseif else"""
        self.assertTrue(TestAST.checkASTGen('Function: main Body: If null Then do(); If not Then Return True; EndIf. ElseIf 3.7+e7 Then gg=""; Else Break; EndIf. EndBody.','Program([FuncDecl(Id(main)[],([][If(Id(null),[],[CallStmt(Id(do),[]),If(Id(not),[],[Return(BooleanLiteral(true))])Else([],[])])ElseIf(BinaryOp(+,FloatLiteral(3.7),Id(e7)),[],[Assign(Id(gg),StringLiteral())])Else([],[Break()])]))])',319))
    def test_number_20(self):
        """if elseif <nested if> else"""
        self.assertTrue(TestAST.checkASTGen('Function: main Body: If 0xAFF Then a=x; ElseIf 0x1234 Then x=5; If another Then doit();  ElseIf nother Then  Break; EndIf. Else Break; EndIf. EndBody.','Program([FuncDecl(Id(main)[],([][If(IntLiteral(2815),[],[Assign(Id(a),Id(x))])ElseIf(IntLiteral(4660),[],[Assign(Id(x),IntLiteral(5)),If(Id(another),[],[CallStmt(Id(doit),[])])ElseIf(Id(nother),[],[Break()])Else([],[])])Else([],[Break()])]))])',320))
    def test_number_21(self):
        """if elseif else <nested if>"""
        self.assertTrue(TestAST.checkASTGen('Function: main Body: If a[3][6][7] Then Break; ElseIf "True" Then Return; Else Return null; If notThat3 Then asign=asi; Else Continue; EndIf. EndIf. EndBody.','Program([FuncDecl(Id(main)[],([][If(ArrayCell(Id(a),[IntLiteral(3),IntLiteral(6),IntLiteral(7)]),[],[Break()])ElseIf(StringLiteral(True),[],[Return()])Else([],[Return(Id(null)),If(Id(notThat3),[],[Assign(Id(asign),Id(asi))])Else([],[Continue()])])]))])',321))
    def test_number_22(self):
        """many nested if"""
        self.assertTrue(TestAST.checkASTGen('Function: main Body: If 1 Then Return 2; If 3 Then Return 4; Else Return "5";  If gg Then Break; ElseIf notgg6 Then Continue; EndIf. EndIf. ElseIf False Then Return True; Else Return 3e7; EndIf. EndBody.','Program([FuncDecl(Id(main)[],([][If(IntLiteral(1),[],[Return(IntLiteral(2)),If(IntLiteral(3),[],[Return(IntLiteral(4))])Else([],[Return(StringLiteral(5)),If(Id(gg),[],[Break()])ElseIf(Id(notgg6),[],[Continue()])Else([],[])])])ElseIf(BooleanLiteral(false),[],[Return(BooleanLiteral(true))])Else([],[Return(FloatLiteral(30000000.0))])]))])',322))
    def test_number_23(self):
        """normal empty for"""
        self.assertTrue(TestAST.checkASTGen('Function: empty Body: For(var = !12>True, no, no ) Do EndFor. EndBody.','Program([FuncDecl(Id(empty)[],([][For(Id(var),BinaryOp(>,UnaryOp(!,IntLiteral(12)),BooleanLiteral(true)),Id(no),Id(no),[],[])]))])',323))
    def test_number_24(self):
        """for with some code"""
        self.assertTrue(TestAST.checkASTGen('Function: empty Body: For(i = 2, 1>2, True ) Do If a==!b Then Return "Pro\'"Inner\\n\'""; EndIf. EndFor. EndBody.','Program([FuncDecl(Id(empty)[],([][For(Id(i),IntLiteral(2),BinaryOp(>,IntLiteral(1),IntLiteral(2)),BooleanLiteral(true),[],[If(BinaryOp(==,Id(a),UnaryOp(!,Id(b))),[],[Return(StringLiteral(Pro\'"Inner\\n\'))])Else([],[])])]))])',324))
    def test_number_25(self):
        """nested for"""
        self.assertTrue(TestAST.checkASTGen('Function: empty Body: For(i = 2, i<=50, i+1 ) Do For(j=i, j < 100, j+5) Do printf(j);  EndFor. Continue; EndFor. EndBody.','Program([FuncDecl(Id(empty)[],([][For(Id(i),IntLiteral(2),BinaryOp(<=,Id(i),IntLiteral(50)),BinaryOp(+,Id(i),IntLiteral(1)),[],[For(Id(j),Id(i),BinaryOp(<,Id(j),IntLiteral(100)),BinaryOp(+,Id(j),IntLiteral(5)),[],[CallStmt(Id(printf),[Id(j)])]),Continue()])]))])',325))
    def test_number_26(self):
        """empty while"""
        self.assertTrue(TestAST.checkASTGen('Function: empty Body: While nothing Do EndWhile. EndBody.','Program([FuncDecl(Id(empty)[],([][While(Id(nothing),[],[])]))])',326))
    def test_number_27(self):
        """some code while"""
        self.assertTrue(TestAST.checkASTGen('Function: empty Body: While a[10]!=100 Do printf(); EndWhile. EndBody.','Program([FuncDecl(Id(empty)[],([][While(BinaryOp(!=,ArrayCell(Id(a),[IntLiteral(10)]),IntLiteral(100)),[],[CallStmt(Id(printf),[])])]))])',327))
    def test_number_28(self):
        """nested while"""
        self.assertTrue(TestAST.checkASTGen('Function: main3 Body: While n>10 Do While n<100 Do x=10e3; EndWhile. Continue; EndWhile. EndBody.','Program([FuncDecl(Id(main3)[],([][While(BinaryOp(>,Id(n),IntLiteral(10)),[],[While(BinaryOp(<,Id(n),IntLiteral(100)),[],[Assign(Id(x),FloatLiteral(10000.0))]),Continue()])]))])',328))
    def test_number_29(self):
        """commented while"""
        self.assertTrue(TestAST.checkASTGen('Function: empty Body: While x>2**,y>5** Do print(); EndWhile. EndBody.','Program([FuncDecl(Id(empty)[],([][While(BinaryOp(>,Id(x),IntLiteral(2)),[],[CallStmt(Id(print),[])])]))])',329))
    def test_number_30(self):
        """some code do while"""
        self.assertTrue(TestAST.checkASTGen('Function: empty Body: Do x=5.2; print(x); x=x+1; While x<100 EndDo. EndBody.','Program([FuncDecl(Id(empty)[],([][Dowhile([],[Assign(Id(x),FloatLiteral(5.2)),CallStmt(Id(print),[Id(x)]),Assign(Id(x),BinaryOp(+,Id(x),IntLiteral(1)))],BinaryOp(<,Id(x),IntLiteral(100)))]))])',330))
    def test_number_31(self):
        """nested do while"""
        self.assertTrue(TestAST.checkASTGen('Function: empty Body: Do Do x=-x; While x>50 EndDo. While x<100 EndDo. EndBody.','Program([FuncDecl(Id(empty)[],([][Dowhile([],[Dowhile([],[Assign(Id(x),UnaryOp(-,Id(x)))],BinaryOp(>,Id(x),IntLiteral(50)))],BinaryOp(<,Id(x),IntLiteral(100)))]))])',331))
    def test_number_32(self):
        """empty do while"""
        self.assertTrue(TestAST.checkASTGen('Function: empty Body: Do While x<100 EndDo. EndBody.','Program([FuncDecl(Id(empty)[],([][Dowhile([],[],BinaryOp(<,Id(x),IntLiteral(100)))]))])',332))
    def test_number_33(self):
        """lots of var decl"""
        self.assertTrue(TestAST.checkASTGen('Var: a,b,c; Function: empty Body: Var: a,c,b; If a>b Then Var: a,b,c; Return; EndIf. EndBody.','Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(empty)[],([VarDecl(Id(a)),VarDecl(Id(c)),VarDecl(Id(b))][If(BinaryOp(>,Id(a),Id(b)),[VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c))],[Return()])Else([],[])]))])',333))
    def test_number_34(self):
        """some call statements"""
        self.assertTrue(TestAST.checkASTGen('Function: empty Body: foo(1); foo(2); foo(3); EndBody.','Program([FuncDecl(Id(empty)[],([][CallStmt(Id(foo),[IntLiteral(1)]),CallStmt(Id(foo),[IntLiteral(2)]),CallStmt(Id(foo),[IntLiteral(3)])]))])',334))
    def test_number_35(self):
        """call statement empty param"""
        self.assertTrue(TestAST.checkASTGen('Function: empty Body: foo(); foo(); foo(); EndBody.','Program([FuncDecl(Id(empty)[],([][CallStmt(Id(foo),[]),CallStmt(Id(foo),[]),CallStmt(Id(foo),[])]))])',335))
    def test_number_36(self):
        """function expression as function call"""
        self.assertTrue(TestAST.checkASTGen('Function: empty Body: foo(); foo(foo() + foo(x) != foo("String")); foo(); EndBody.','Program([FuncDecl(Id(empty)[],([][CallStmt(Id(foo),[]),CallStmt(Id(foo),[BinaryOp(!=,BinaryOp(+,CallExpr(Id(foo),[]),CallExpr(Id(foo),[Id(x)])),CallExpr(Id(foo),[StringLiteral(String)]))]),CallStmt(Id(foo),[])]))])',336))
    def test_number_37(self):
        """empty return"""
        self.assertTrue(TestAST.checkASTGen('Function: empty Body: Return; EndBody.','Program([FuncDecl(Id(empty)[],([][Return()]))])',337))
    def test_number_38(self):
        """return with expr"""
        self.assertTrue(TestAST.checkASTGen('Function: empty Body: Return(nothing); EndBody.','Program([FuncDecl(Id(empty)[],([][Return(Id(nothing))]))])',338))
    def test_number_39(self):
        """just add minus int"""
        self.assertTrue(TestAST.checkASTGen('Function: main Body: If !!1+1+2+3e+5 --0xAFF Then ElseIf none Then Else EndIf. EndBody.','Program([FuncDecl(Id(main)[],([][If(BinaryOp(-,BinaryOp(+,BinaryOp(+,BinaryOp(+,UnaryOp(!,UnaryOp(!,IntLiteral(1))),IntLiteral(1)),IntLiteral(2)),FloatLiteral(300000.0)),UnaryOp(-,IntLiteral(2815))),[],[])ElseIf(Id(none),[],[])Else([],[])]))])',339))
    def test_number_40(self):
        """just add minus float"""
        self.assertTrue(TestAST.checkASTGen('Function: main Body: If 3.5+3.0e-5-!!!1.2---0x123 Then ElseIf none Then Else EndIf. EndBody.','Program([FuncDecl(Id(main)[],([][If(BinaryOp(-,BinaryOp(-,BinaryOp(+,FloatLiteral(3.5),FloatLiteral(3e-05)),UnaryOp(!,UnaryOp(!,UnaryOp(!,FloatLiteral(1.2))))),UnaryOp(-,UnaryOp(-,IntLiteral(291)))),[],[])ElseIf(Id(none),[],[])Else([],[])]))])',340))
    def test_number_41(self):
        """just logical"""
        self.assertTrue(TestAST.checkASTGen('Function: main Body: If a||b&&c||b&&a Then ElseIf c&&a&&b||b||c Then Else EndIf. EndBody.','Program([FuncDecl(Id(main)[],([][If(BinaryOp(&&,BinaryOp(||,BinaryOp(&&,BinaryOp(||,Id(a),Id(b)),Id(c)),Id(b)),Id(a)),[],[])ElseIf(BinaryOp(||,BinaryOp(||,BinaryOp(&&,BinaryOp(&&,Id(c),Id(a)),Id(b)),Id(b)),Id(c)),[],[])Else([],[])]))])',341))
    def test_number_42(self):
        """nested negation"""
        self.assertTrue(TestAST.checkASTGen('Function: main Body: While !!!!!!!!!!!!a>!b Do Return; EndWhile. EndBody.','Program([FuncDecl(Id(main)[],([][While(BinaryOp(>,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,Id(a))))))))))))),UnaryOp(!,Id(b))),[],[Return()])]))])',342))
    def test_number_43(self):
        """nested index"""
        self.assertTrue(TestAST.checkASTGen('Function: main Body: While a[1][2][a[5][6]+b[foo("String") > fok()]] Do Return; EndWhile. EndBody.','Program([FuncDecl(Id(main)[],([][While(ArrayCell(Id(a),[IntLiteral(1),IntLiteral(2),BinaryOp(+,ArrayCell(Id(a),[IntLiteral(5),IntLiteral(6)]),ArrayCell(Id(b),[BinaryOp(>,CallExpr(Id(foo),[StringLiteral(String)]),CallExpr(Id(fok),[]))]))]),[],[Return()])]))])',343))
    def test_number_44(self):
        """multi dimention array indexing"""
        self.assertTrue(TestAST.checkASTGen('Function: main Body: If x[1][2][2.5][3e+7] Then ElseIf nothing Then Else EndIf. EndBody.','Program([FuncDecl(Id(main)[],([][If(ArrayCell(Id(x),[IntLiteral(1),IntLiteral(2),FloatLiteral(2.5),FloatLiteral(30000000.0)]),[],[])ElseIf(Id(nothing),[],[])Else([],[])]))])',344))
    def test_number_45(self):
        """mixed precedence and assoc"""
        self.assertTrue(TestAST.checkASTGen('Function: empty Body: x = !-a + !b[0]\\5 -.( (x == y)*.(3e7 - 7 - gg)|| True || !False); EndBody.','Program([FuncDecl(Id(empty)[],([][Assign(Id(x),BinaryOp(-.,BinaryOp(+,UnaryOp(!,UnaryOp(-,Id(a))),BinaryOp(\,UnaryOp(!,ArrayCell(Id(b),[IntLiteral(0)])),IntLiteral(5))),BinaryOp(||,BinaryOp(||,BinaryOp(*.,BinaryOp(==,Id(x),Id(y)),BinaryOp(-,BinaryOp(-,FloatLiteral(30000000.0),IntLiteral(7)),Id(gg))),BooleanLiteral(true)),UnaryOp(!,BooleanLiteral(false)))))]))])',345))
    def test_number_46(self):
        """mixed precedence and assoc"""
        self.assertTrue(TestAST.checkASTGen('Function: empty Body: x = 2*-3+!True; EndBody.','Program([FuncDecl(Id(empty)[],([][Assign(Id(x),BinaryOp(+,BinaryOp(*,IntLiteral(2),UnaryOp(-,IntLiteral(3))),UnaryOp(!,BooleanLiteral(true))))]))])',346))
    def test_number_47(self):
        """mixed precedence and assoc"""
        self.assertTrue(TestAST.checkASTGen('Function: empty Body: x = function(function(a[2][function()])); EndBody.','Program([FuncDecl(Id(empty)[],([][Assign(Id(x),CallExpr(Id(function),[CallExpr(Id(function),[ArrayCell(Id(a),[IntLiteral(2),CallExpr(Id(function),[])])])]))]))])',347))
    def test_number_48(self):
        """mixed precedence and assoc"""
        self.assertTrue(TestAST.checkASTGen('Function: empty Body: x = 1&&2||3 % 5 %7.5 <= nothing; EndBody.','Program([FuncDecl(Id(empty)[],([][Assign(Id(x),BinaryOp(<=,BinaryOp(||,BinaryOp(&&,IntLiteral(1),IntLiteral(2)),BinaryOp(%,BinaryOp(%,IntLiteral(3),IntLiteral(5)),FloatLiteral(7.5))),Id(nothing)))]))])',348))
    def test_number_49(self):
        """mixed precedence and assoc"""
        self.assertTrue(TestAST.checkASTGen('Function: empty Body:  y=-fact(x+12345); EndBody.','Program([FuncDecl(Id(empty)[],([][Assign(Id(y),UnaryOp(-,CallExpr(Id(fact),[BinaryOp(+,Id(x),IntLiteral(12345))])))]))])',349))
    def test_number_50(self):
        """mixed precedence and assoc"""
        self.assertTrue(TestAST.checkASTGen('Function: empty Body: func(!func()); EndBody.','Program([FuncDecl(Id(empty)[],([][CallStmt(Id(func),[UnaryOp(!,CallExpr(Id(func),[]))])]))])',350))
    def test_number_51(self):
        """mixed precedence and assoc"""
        self.assertTrue(TestAST.checkASTGen('Function: empty Body: x= a[1==2] == b[6!=7] + a \\!b;  EndBody.','Program([FuncDecl(Id(empty)[],([][Assign(Id(x),BinaryOp(==,ArrayCell(Id(a),[BinaryOp(==,IntLiteral(1),IntLiteral(2))]),BinaryOp(+,ArrayCell(Id(b),[BinaryOp(!=,IntLiteral(6),IntLiteral(7))]),BinaryOp(\,Id(a),UnaryOp(!,Id(b))))))]))])',351))
    def test_number_52(self):
        """mixed precedence and assoc"""
        self.assertTrue(TestAST.checkASTGen('Function: empty Body: a= (1==2)=/=5; EndBody.','Program([FuncDecl(Id(empty)[],([][Assign(Id(a),BinaryOp(=/=,BinaryOp(==,IntLiteral(1),IntLiteral(2)),IntLiteral(5)))]))])',352))
    def test_number_53(self):
        """full program ex"""
        self.assertTrue(TestAST.checkASTGen('Var: a,b,c=5,d[5][0x12]={1,{5.6,7}}; Var: x,y; Function: recur Parameter: n Body: If n==0 Then Return 0; EndIf. Return recur(n-1); EndBody. Function: main Body: recur(5000); EndBody.','Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c),IntLiteral(5)),VarDecl(Id(d),[5,18],ArrayLiteral(IntLiteral(1),ArrayLiteral(FloatLiteral(5.6),IntLiteral(7)))),VarDecl(Id(x)),VarDecl(Id(y)),FuncDecl(Id(recur)[VarDecl(Id(n))],([][If(BinaryOp(==,Id(n),IntLiteral(0)),[],[Return(IntLiteral(0))])Else([],[]),Return(CallExpr(Id(recur),[BinaryOp(-,Id(n),IntLiteral(1))]))])),FuncDecl(Id(main)[],([][CallStmt(Id(recur),[IntLiteral(5000)])]))])',353))
    def test_number_54(self):
        """non-assoc with bracket"""
        self.assertTrue(TestAST.checkASTGen('Function: main Body: x=(1>2)>((3>4)>5); EndBody.','Program([FuncDecl(Id(main)[],([][Assign(Id(x),BinaryOp(>,BinaryOp(>,IntLiteral(1),IntLiteral(2)),BinaryOp(>,BinaryOp(>,IntLiteral(3),IntLiteral(4)),IntLiteral(5))))]))])',354))
    def test_number_55(self):
        """array with func as ID"""
        self.assertTrue(TestAST.checkASTGen('Function: empty \n Body: a_neme(1,2,a[2][-True])[5+6] = a_neme[1][!!2]; EndBody.','Program([FuncDecl(Id(empty)[],([][Assign(ArrayCell(CallExpr(Id(a_neme),[IntLiteral(1),IntLiteral(2),ArrayCell(Id(a),[IntLiteral(2),UnaryOp(-,BooleanLiteral(true))])]),[BinaryOp(+,IntLiteral(5),IntLiteral(6))]),ArrayCell(Id(a_neme),[IntLiteral(1),UnaryOp(!,UnaryOp(!,IntLiteral(2)))]))]))])',355))
    def test_number_56(self):
        """mixed of array_element and ID"""
        self.assertTrue(TestAST.checkASTGen('Var: a[1], b[9][10]={1,{2}}; Function: main \n Body: func(a[6], func[6][7], {2})[2] = func(null)[True] + func[True] + func(True) || !func(True, f(),f(true)[0]); EndBody.','Program([VarDecl(Id(a),[1]),VarDecl(Id(b),[9,10],ArrayLiteral(IntLiteral(1),ArrayLiteral(IntLiteral(2)))),FuncDecl(Id(main)[],([][Assign(ArrayCell(CallExpr(Id(func),[ArrayCell(Id(a),[IntLiteral(6)]),ArrayCell(Id(func),[IntLiteral(6),IntLiteral(7)]),ArrayLiteral(IntLiteral(2))]),[IntLiteral(2)]),BinaryOp(||,BinaryOp(+,BinaryOp(+,ArrayCell(CallExpr(Id(func),[Id(null)]),[BooleanLiteral(true)]),ArrayCell(Id(func),[BooleanLiteral(true)])),CallExpr(Id(func),[BooleanLiteral(true)])),UnaryOp(!,CallExpr(Id(func),[BooleanLiteral(true),CallExpr(Id(f),[]),ArrayCell(CallExpr(Id(f),[Id(true)]),[IntLiteral(0)])]))))]))])',356))
    def test_number_57(self):
        """normal array with init decl"""
        self.assertTrue(TestAST.checkASTGen('Var: array[1][2] = {1,2,3,{4,5}};','Program([VarDecl(Id(array),[1,2],ArrayLiteral(IntLiteral(1),IntLiteral(2),IntLiteral(3),ArrayLiteral(IntLiteral(4),IntLiteral(5))))])',357))
    def test_number_58(self):
        """mixed precedence and assoc"""
        self.assertTrue(TestAST.checkASTGen('Function: empty Body: x = 3>.(3<.5); EndBody.','Program([FuncDecl(Id(empty)[],([][Assign(Id(x),BinaryOp(>.,IntLiteral(3),BinaryOp(<.,IntLiteral(3),IntLiteral(5))))]))])',358))
    def test_number_59(self):
        """mixed precedence and assoc"""
        self.assertTrue(TestAST.checkASTGen('Function: empty Body: x = foo() *. foo(); EndBody.','Program([FuncDecl(Id(empty)[],([][Assign(Id(x),BinaryOp(*.,CallExpr(Id(foo),[]),CallExpr(Id(foo),[])))]))])',359))
    def test_number_60(self):
        """mixed precedence and assoc"""
        self.assertTrue(TestAST.checkASTGen('Function: empty Body: x = x[7] - (True >= !func(2)[5]); EndBody.','Program([FuncDecl(Id(empty)[],([][Assign(Id(x),BinaryOp(-,ArrayCell(Id(x),[IntLiteral(7)]),BinaryOp(>=,BooleanLiteral(true),UnaryOp(!,ArrayCell(CallExpr(Id(func),[IntLiteral(2)]),[IntLiteral(5)])))))]))])',360))
    def test_number_61(self):
        """mixed precedence and assoc"""
        self.assertTrue(TestAST.checkASTGen('Function: empty Body: func(!False); EndBody.','Program([FuncDecl(Id(empty)[],([][CallStmt(Id(func),[UnaryOp(!,BooleanLiteral(false))])]))])',361))
    def test_number_62(self):
        """mixed precedence and assoc"""
        self.assertTrue(TestAST.checkASTGen('Function: empty Body: func(-0xEE123+(0-0X12)+6.6*7e-7); EndBody.','Program([FuncDecl(Id(empty)[],([][CallStmt(Id(func),[BinaryOp(+,BinaryOp(+,UnaryOp(-,IntLiteral(975139)),BinaryOp(-,IntLiteral(0),IntLiteral(18))),BinaryOp(*,FloatLiteral(6.6),FloatLiteral(7e-07)))])]))])',362))
    def test_number_63(self):
        """mixed precedence and assoc"""
        self.assertTrue(TestAST.checkASTGen('Function: empty Body: x= --(6*(7-5>7.7) == "String"); EndBody.','Program([FuncDecl(Id(empty)[],([][Assign(Id(x),UnaryOp(-,UnaryOp(-,BinaryOp(==,BinaryOp(*,IntLiteral(6),BinaryOp(>,BinaryOp(-,IntLiteral(7),IntLiteral(5)),FloatLiteral(7.7))),StringLiteral(String)))))]))])',363))
    def test_number_64(self):
        """test all ints"""
        self.assertTrue(TestAST.checkASTGen('Var: a= {1,0,0x1,0x12A, 0o123,0O2227};','Program([VarDecl(Id(a),ArrayLiteral(IntLiteral(1),IntLiteral(0),IntLiteral(1),IntLiteral(298),IntLiteral(83),IntLiteral(1175)))])',364))
    def test_number_65(self):
        """test all bools"""
        self.assertTrue(TestAST.checkASTGen('Var: a= {True,False};','Program([VarDecl(Id(a),ArrayLiteral(BooleanLiteral(true),BooleanLiteral(false)))])',365))
    def test_number_66(self):
        """test all float"""
        self.assertTrue(TestAST.checkASTGen('Var: a ={0., 1.2, 0.0, 2e+3,2e-3,3E+4,3E-4,5e6,5E6,0.e3,5.6E-6} ;','Program([VarDecl(Id(a),ArrayLiteral(FloatLiteral(0.0),FloatLiteral(1.2),FloatLiteral(0.0),FloatLiteral(2000.0),FloatLiteral(0.002),FloatLiteral(30000.0),FloatLiteral(0.0003),FloatLiteral(5000000.0),FloatLiteral(5000000.0),FloatLiteral(0.0),FloatLiteral(5.6e-06)))])',366))
    def test_number_67(self):
        """lots of var and func"""
        self.assertTrue(TestAST.checkASTGen('Var: a,b,c; Var: d,e,f; Function: f1 Parameter: a,b,c,d Body: Var: a,b,c; Var: d,e,f; EndBody. Function: f2 Parameter: e,f,g,h Body: Var: a,b,c; Var: d,e,f; EndBody.','Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),VarDecl(Id(d)),VarDecl(Id(e)),VarDecl(Id(f)),FuncDecl(Id(f1)[VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),VarDecl(Id(d))],([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),VarDecl(Id(d)),VarDecl(Id(e)),VarDecl(Id(f))][])),FuncDecl(Id(f2)[VarDecl(Id(e)),VarDecl(Id(f)),VarDecl(Id(g)),VarDecl(Id(h))],([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),VarDecl(Id(d)),VarDecl(Id(e)),VarDecl(Id(f))][]))])',367))
    def test_number_68(self):
        """full if with var decl"""
        self.assertTrue(TestAST.checkASTGen('Function: main Parameter: a,b Body: Var: car,di,lak; If a>b Then Var: a,b; a=b; ElseIf c>d Then Var: c,d; c=d; Else Var: x,y; x=y; EndIf. EndBody.','Program([FuncDecl(Id(main)[VarDecl(Id(a)),VarDecl(Id(b))],([VarDecl(Id(car)),VarDecl(Id(di)),VarDecl(Id(lak))][If(BinaryOp(>,Id(a),Id(b)),[VarDecl(Id(a)),VarDecl(Id(b))],[Assign(Id(a),Id(b))])ElseIf(BinaryOp(>,Id(c),Id(d)),[VarDecl(Id(c)),VarDecl(Id(d))],[Assign(Id(c),Id(d))])Else([VarDecl(Id(x)),VarDecl(Id(y))],[Assign(Id(x),Id(y))])]))])',368))
    def test_number_69(self):
        """full for with var decl"""
        self.assertTrue(TestAST.checkASTGen('Function: main Parameter: a,b Body: Var: car,di,lak; For (a = b, c>5, x + True) Do Var: a,b,c; a = c*!-b; EndFor. Break; EndBody.','Program([FuncDecl(Id(main)[VarDecl(Id(a)),VarDecl(Id(b))],([VarDecl(Id(car)),VarDecl(Id(di)),VarDecl(Id(lak))][For(Id(a),Id(b),BinaryOp(>,Id(c),IntLiteral(5)),BinaryOp(+,Id(x),BooleanLiteral(true)),[VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c))],[Assign(Id(a),BinaryOp(*,Id(c),UnaryOp(!,UnaryOp(-,Id(b)))))]),Break()]))])',369))
    def test_number_70(self):
        """full while with var decl"""
        self.assertTrue(TestAST.checkASTGen('Function: main Parameter: a,b Body: Var: car,di,lak;  While x =/= y Do Var: a,b,c; a()[6][7][b()] = c; EndWhile. EndBody.','Program([FuncDecl(Id(main)[VarDecl(Id(a)),VarDecl(Id(b))],([VarDecl(Id(car)),VarDecl(Id(di)),VarDecl(Id(lak))][While(BinaryOp(=/=,Id(x),Id(y)),[VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c))],[Assign(ArrayCell(CallExpr(Id(a),[]),[IntLiteral(6),IntLiteral(7),CallExpr(Id(b),[])]),Id(c))])]))])',370))
    def test_number_71(self):
        """full dowhile with var decl"""
        self.assertTrue(TestAST.checkASTGen('Function: main Parameter: a,b Body: Var: car,di,lak; Do Var: x,y,g; x[1] = y[7.5] \\. g["True"]; While nothing EndDo.  EndBody.','Program([FuncDecl(Id(main)[VarDecl(Id(a)),VarDecl(Id(b))],([VarDecl(Id(car)),VarDecl(Id(di)),VarDecl(Id(lak))][Dowhile([VarDecl(Id(x)),VarDecl(Id(y)),VarDecl(Id(g))],[Assign(ArrayCell(Id(x),[IntLiteral(1)]),BinaryOp(\.,ArrayCell(Id(y),[FloatLiteral(7.5)]),ArrayCell(Id(g),[StringLiteral(True)])))],Id(nothing))]))])',371))
    def test_number_72(self):
        """full counting program"""
        self.assertTrue(TestAST.checkASTGen('Var: a,b,c=5,d[5][0o12]={1}; Var: x,y; Function: count Parameter: n Body: While n>0 Do printf(n); n=n-1; EndWhile. Return n; EndBody. Function: main Body: count(5000); EndBody.','Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c),IntLiteral(5)),VarDecl(Id(d),[5,10],ArrayLiteral(IntLiteral(1))),VarDecl(Id(x)),VarDecl(Id(y)),FuncDecl(Id(count)[VarDecl(Id(n))],([][While(BinaryOp(>,Id(n),IntLiteral(0)),[],[CallStmt(Id(printf),[Id(n)]),Assign(Id(n),BinaryOp(-,Id(n),IntLiteral(1)))]),Return(Id(n))])),FuncDecl(Id(main)[],([][CallStmt(Id(count),[IntLiteral(5000)])]))])',372))
    def test_number_73(self):
        """diverse and full program"""
        self.assertTrue(TestAST.checkASTGen('Var: a={5,6}, arr[1][2]=7.5; Var: str="String"; Function: all_full Parameter: n, n[2][3], n[0] Body: Var: str = "a long \\n string"; n = len(str); While n > 0 Do Var: a = 1, b=2; println(n+a, n-b,n[1][6*0.5>True\\0e0]); Continue; EndWhile. EndBody. ','Program([VarDecl(Id(a),ArrayLiteral(IntLiteral(5),IntLiteral(6))),VarDecl(Id(arr),[1,2],FloatLiteral(7.5)),VarDecl(Id(str),StringLiteral(String)),FuncDecl(Id(all_full)[VarDecl(Id(n)),VarDecl(Id(n),[2,3]),VarDecl(Id(n),[0])],([VarDecl(Id(str),StringLiteral(a long \\n string))][Assign(Id(n),CallExpr(Id(len),[Id(str)])),While(BinaryOp(>,Id(n),IntLiteral(0)),[VarDecl(Id(a),IntLiteral(1)),VarDecl(Id(b),IntLiteral(2))],[CallStmt(Id(println),[BinaryOp(+,Id(n),Id(a)),BinaryOp(-,Id(n),Id(b)),ArrayCell(Id(n),[IntLiteral(1),BinaryOp(>,BinaryOp(*,IntLiteral(6),FloatLiteral(0.5)),BinaryOp(\,BooleanLiteral(true),FloatLiteral(0.0)))])]),Continue()])]))])',373))
    def test_number_74(self):
        """simple add func"""
        self.assertTrue(TestAST.checkASTGen('Function: add Parameter: a,b Body: Return a+b; EndBody. ','Program([FuncDecl(Id(add)[VarDecl(Id(a)),VarDecl(Id(b))],([][Return(BinaryOp(+,Id(a),Id(b)))]))])',374))
    def test_number_75(self):
        """functional prog?"""
        self.assertTrue(TestAST.checkASTGen('Function: main Body: Var: add_f,a,b; add_f = add; a= cin(); b=cin(); printf(add_f(a,b)); EndBody. ','Program([FuncDecl(Id(main)[],([VarDecl(Id(add_f)),VarDecl(Id(a)),VarDecl(Id(b))][Assign(Id(add_f),Id(add)),Assign(Id(a),CallExpr(Id(cin),[])),Assign(Id(b),CallExpr(Id(cin),[])),CallStmt(Id(printf),[CallExpr(Id(add_f),[Id(a),Id(b)])])]))])',375))
    def test_number_76(self):
        """mixed precedence and assoc"""
        self.assertTrue(TestAST.checkASTGen('Function: main Body: f()[a[b(f( c\\ f(a) ))]] = {1,2,{3},{4,5}}; EndBody.','Program([FuncDecl(Id(main)[],([][Assign(ArrayCell(CallExpr(Id(f),[]),[ArrayCell(Id(a),[CallExpr(Id(b),[CallExpr(Id(f),[BinaryOp(\\,Id(c),CallExpr(Id(f),[Id(a)]))])])])]),ArrayLiteral(IntLiteral(1),IntLiteral(2),ArrayLiteral(IntLiteral(3)),ArrayLiteral(IntLiteral(4),IntLiteral(5))))]))])',376))
    def test_number_77(self):
        """many assignments"""
        self.assertTrue(TestAST.checkASTGen('Function: assign Parameter: a,b,c Body: a[5] = 1+5*7>9\\5 || (True == False); f(2)[1] = f(6); f[g]= 1 =/= 2; d = 0x12 % you; EndBody.','Program([FuncDecl(Id(assign)[VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c))],([][Assign(ArrayCell(Id(a),[IntLiteral(5)]),BinaryOp(>,BinaryOp(+,IntLiteral(1),BinaryOp(*,IntLiteral(5),IntLiteral(7))),BinaryOp(||,BinaryOp(\,IntLiteral(9),IntLiteral(5)),BinaryOp(==,BooleanLiteral(true),BooleanLiteral(false))))),Assign(ArrayCell(CallExpr(Id(f),[IntLiteral(2)]),[IntLiteral(1)]),CallExpr(Id(f),[IntLiteral(6)])),Assign(ArrayCell(Id(f),[Id(g)]),BinaryOp(=/=,IntLiteral(1),IntLiteral(2))),Assign(Id(d),BinaryOp(%,IntLiteral(18),Id(you)))]))])',377))
    def test_number_78(self):
        """complex for expression"""
        self.assertTrue(TestAST.checkASTGen('Function: for Parameter: x,y Body: For (a= 1+ 5<=5  || (2\\3)*4%5, a =/=5 || b \\. 5 *. !!!-6 , True - "String" && False >= !!!a) Do nothing(); EndFor. EndBody.','Program([FuncDecl(Id(for)[VarDecl(Id(x)),VarDecl(Id(y))],([][For(Id(a),BinaryOp(<=,BinaryOp(+,IntLiteral(1),IntLiteral(5)),BinaryOp(||,IntLiteral(5),BinaryOp(%,BinaryOp(*,BinaryOp(\,IntLiteral(2),IntLiteral(3)),IntLiteral(4)),IntLiteral(5)))),BinaryOp(=/=,Id(a),BinaryOp(||,IntLiteral(5),BinaryOp(*.,BinaryOp(\.,Id(b),IntLiteral(5)),UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(-,IntLiteral(6)))))))),BinaryOp(>=,BinaryOp(&&,BinaryOp(-,BooleanLiteral(true),StringLiteral(String)),BooleanLiteral(false)),UnaryOp(!,UnaryOp(!,UnaryOp(!,Id(a))))),[],[CallStmt(Id(nothing),[])])]))])',378))
    def test_number_79(self):
        """do while in while"""
        self.assertTrue(TestAST.checkASTGen('Function: dowhileinwhile Body: While a>b Do Do a=5; While a<b EndDo. EndWhile. EndBody.','Program([FuncDecl(Id(dowhileinwhile)[],([][While(BinaryOp(>,Id(a),Id(b)),[],[Dowhile([],[Assign(Id(a),IntLiteral(5))],BinaryOp(<,Id(a),Id(b)))])]))])',379))
    def test_number_80(self):
        """while in do while"""
        self.assertTrue(TestAST.checkASTGen('Function: whileindowhile Body: Do While a>b Do nothing(); EndWhile. While b<a EndDo. EndBody.','Program([FuncDecl(Id(whileindowhile)[],([][Dowhile([],[While(BinaryOp(>,Id(a),Id(b)),[],[CallStmt(Id(nothing),[])])],BinaryOp(<,Id(b),Id(a)))]))])',380))
    def test_number_81(self):
        """some comment in stupid places"""
        self.assertTrue(TestAST.checkASTGen('Function: main **main** Body**:**: If a**==** == b Then a=5**or = 6**; ElseIf a!=b Then **Return;** Continue; EndIf. EndBody. **Var: x;** **\n\n\n\n**','Program([FuncDecl(Id(main)[],([][If(BinaryOp(==,Id(a),Id(b)),[],[Assign(Id(a),IntLiteral(5))])ElseIf(BinaryOp(!=,Id(a),Id(b)),[],[Continue()])Else([],[])]))])',381))
    def test_number_82(self):
        """all relation op"""
        self.assertTrue(TestAST.checkASTGen('Function: comp Body: a= (a==b) != (c<(d>e)+(1<=2 + (1>=2))) \\ (1 =/= 2 * (2<.5 * (6>.7))) - (a <=. (b >=. c)); EndBody.','Program([FuncDecl(Id(comp)[],([][Assign(Id(a),BinaryOp(!=,BinaryOp(==,Id(a),Id(b)),BinaryOp(-,BinaryOp(\\,BinaryOp(<,Id(c),BinaryOp(+,BinaryOp(>,Id(d),Id(e)),BinaryOp(<=,IntLiteral(1),BinaryOp(+,IntLiteral(2),BinaryOp(>=,IntLiteral(1),IntLiteral(2)))))),BinaryOp(=/=,IntLiteral(1),BinaryOp(*,IntLiteral(2),BinaryOp(<.,IntLiteral(2),BinaryOp(*,IntLiteral(5),BinaryOp(>.,IntLiteral(6),IntLiteral(7))))))),BinaryOp(<=.,Id(a),BinaryOp(>=.,Id(b),Id(c))))))]))])',382))
    def test_number_83(self):
        """all plus minus op"""
        self.assertTrue(TestAST.checkASTGen('Function: comp Body: a = 1 + 2 +. 3 - 4 -. 5; EndBody.','Program([FuncDecl(Id(comp)[],([][Assign(Id(a),BinaryOp(-.,BinaryOp(-,BinaryOp(+.,BinaryOp(+,IntLiteral(1),IntLiteral(2)),IntLiteral(3)),IntLiteral(4)),IntLiteral(5)))]))])',383))
    def test_number_84(self):
        """all mul op"""
        self.assertTrue(TestAST.checkASTGen('Function: comp Body: a = 1 * 2 *. 3 \\ 4 \\. 5 % 6; EndBody.','Program([FuncDecl(Id(comp)[],([][Assign(Id(a),BinaryOp(%,BinaryOp(\\.,BinaryOp(\\,BinaryOp(*.,BinaryOp(*,IntLiteral(1),IntLiteral(2)),IntLiteral(3)),IntLiteral(4)),IntLiteral(5)),IntLiteral(6)))]))])',384))
    def test_number_85(self):
        """logic sign and nega op"""
        self.assertTrue(TestAST.checkASTGen('Function: comp Body: a = !!-False && (!True || - notFalse ---5 - !!!6); EndBody.','Program([FuncDecl(Id(comp)[],([][Assign(Id(a),BinaryOp(&&,UnaryOp(!,UnaryOp(!,UnaryOp(-,BooleanLiteral(false)))),BinaryOp(||,UnaryOp(!,BooleanLiteral(true)),BinaryOp(-,BinaryOp(-,UnaryOp(-,Id(notFalse)),UnaryOp(-,UnaryOp(-,IntLiteral(5)))),UnaryOp(!,UnaryOp(!,UnaryOp(!,IntLiteral(6))))))))]))])',385))
    def test_number_86(self):
        """lots of nested function call"""
        self.assertTrue(TestAST.checkASTGen('Function: comp Body: a = f(f(f(f(f(f()))))) + g(g(g(),g(),g(g(1,2,3,{5})))); EndBody.','Program([FuncDecl(Id(comp)[],([][Assign(Id(a),BinaryOp(+,CallExpr(Id(f),[CallExpr(Id(f),[CallExpr(Id(f),[CallExpr(Id(f),[CallExpr(Id(f),[CallExpr(Id(f),[])])])])])]),CallExpr(Id(g),[CallExpr(Id(g),[CallExpr(Id(g),[]),CallExpr(Id(g),[]),CallExpr(Id(g),[CallExpr(Id(g),[IntLiteral(1),IntLiteral(2),IntLiteral(3),ArrayLiteral(IntLiteral(5))])])])])))]))])',386))
    def test_number_87(self):
        """func with call assign conti break return"""
        self.assertTrue(TestAST.checkASTGen('Function: bunchofs Body: funtion(); a=b; f()[2] = {6}; Continue; Break; Return s; Return; EndBody.','Program([FuncDecl(Id(bunchofs)[],([][CallStmt(Id(funtion),[]),Assign(Id(a),Id(b)),Assign(ArrayCell(CallExpr(Id(f),[]),[IntLiteral(2)]),ArrayLiteral(IntLiteral(6))),Continue(),Break(),Return(Id(s)),Return()]))])',387))
    def test_number_88(self):
        """simple gcd function"""
        self.assertTrue(TestAST.checkASTGen('Function: gcd Parameter: a,b Body: If b == 0 Then Return a; Else Return gcd(b, a%b); EndIf. EndBody.','Program([FuncDecl(Id(gcd)[VarDecl(Id(a)),VarDecl(Id(b))],([][If(BinaryOp(==,Id(b),IntLiteral(0)),[],[Return(Id(a))])Else([],[Return(CallExpr(Id(gcd),[Id(b),BinaryOp(%,Id(a),Id(b))]))])]))])',388))
    def test_number_89(self):
        """rap viet"""
        self.assertTrue(TestAST.checkASTGen('Var: use_less_var; Function: rapviet Parameter: longlanh,laplanh, kieusa, money Body: If longlanh &&laplanh &&kieusa Then print("DC"); ElseIf money Then print("Gducky"); Else print("Meh"); EndIf. EndBody.','Program([VarDecl(Id(use_less_var)),FuncDecl(Id(rapviet)[VarDecl(Id(longlanh)),VarDecl(Id(laplanh)),VarDecl(Id(kieusa)),VarDecl(Id(money))],([][If(BinaryOp(&&,BinaryOp(&&,Id(longlanh),Id(laplanh)),Id(kieusa)),[],[CallStmt(Id(print),[StringLiteral(DC)])])ElseIf(Id(money),[],[CallStmt(Id(print),[StringLiteral(Gducky)])])Else([],[CallStmt(Id(print),[StringLiteral(Meh)])])]))])',389))
    def test_number_90(self):
        """second conv"""
        self.assertTrue(TestAST.checkASTGen('Function: second_converter Parameter: day,hour,minute,second Body: hour = 24*day + hour; minute = hour*60+minute; second = minute * 60 + second; Return second; EndBody.','Program([FuncDecl(Id(second_converter)[VarDecl(Id(day)),VarDecl(Id(hour)),VarDecl(Id(minute)),VarDecl(Id(second))],([][Assign(Id(hour),BinaryOp(+,BinaryOp(*,IntLiteral(24),Id(day)),Id(hour))),Assign(Id(minute),BinaryOp(+,BinaryOp(*,Id(hour),IntLiteral(60)),Id(minute))),Assign(Id(second),BinaryOp(+,BinaryOp(*,Id(minute),IntLiteral(60)),Id(second))),Return(Id(second))]))])',390))
    def test_number_91(self):
        """day conv"""
        self.assertTrue(TestAST.checkASTGen('Function: day_converter Parameter: day,hour,minute,second Body: day = hour\\.24+ minute \\.(60*24) + second \\. (60*60*24) + day; Return day \\ 1; EndBody. ','Program([FuncDecl(Id(day_converter)[VarDecl(Id(day)),VarDecl(Id(hour)),VarDecl(Id(minute)),VarDecl(Id(second))],([][Assign(Id(day),BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(\\.,Id(hour),IntLiteral(24)),BinaryOp(\\.,Id(minute),BinaryOp(*,IntLiteral(60),IntLiteral(24)))),BinaryOp(\\.,Id(second),BinaryOp(*,BinaryOp(*,IntLiteral(60),IntLiteral(60)),IntLiteral(24)))),Id(day))),Return(BinaryOp(\\,Id(day),IntLiteral(1)))]))])',391))
    def test_number_92(self):
        """prefix priting"""
        self.assertTrue(TestAST.checkASTGen('Function: print_prefix Parameter: root Body: If root == null Then Return; print(root[0]); print_prefix(root[1]); print_prefix(root[2]); EndIf. EndBody. **root is array with 0-> value 1->left 2-> right**','Program([FuncDecl(Id(print_prefix)[VarDecl(Id(root))],([][If(BinaryOp(==,Id(root),Id(null)),[],[Return(),CallStmt(Id(print),[ArrayCell(Id(root),[IntLiteral(0)])]),CallStmt(Id(print_prefix),[ArrayCell(Id(root),[IntLiteral(1)])]),CallStmt(Id(print_prefix),[ArrayCell(Id(root),[IntLiteral(2)])])])Else([],[])]))])',392))
    def test_number_93(self):
        """full var decl program"""
        self.assertTrue(TestAST.checkASTGen('Function: dumb_var Parameter: a,b,c[2] Body: Var: a,b[2][3] = False; If a[2][3] == False Then Var: a = "This is a"; print(a); EndIf. While a== null Do Var: a = {"Totally not null"}; Continue; EndWhile. EndBody.','Program([FuncDecl(Id(dumb_var)[VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c),[2])],([VarDecl(Id(a)),VarDecl(Id(b),[2,3],BooleanLiteral(false))][If(BinaryOp(==,ArrayCell(Id(a),[IntLiteral(2),IntLiteral(3)]),BooleanLiteral(false)),[VarDecl(Id(a),StringLiteral(This is a))],[CallStmt(Id(print),[Id(a)])])Else([],[]),While(BinaryOp(==,Id(a),Id(null)),[VarDecl(Id(a),ArrayLiteral(StringLiteral(Totally not null)))],[Continue()])]))])',393))
    def test_number_94(self):
        """full program structure"""
        self.assertTrue(TestAST.checkASTGen('Var: a[6][5]; Var: b=5; Function: main Parameter: a,b,c[6][7] Body: Var: g[7] = {1,2,3};   If g != null Then print_list(g);  Return;EndIf.  print("Null list"); EndBody. Function: print_list Parameter: g[100] Body: elem = g[0]; i=0; While elem != null Do print(elem); i = i+1; elem = g[i]; EndWhile.  EndBody.','Program([VarDecl(Id(a),[6,5]),VarDecl(Id(b),IntLiteral(5)),FuncDecl(Id(main)[VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c),[6,7])],([VarDecl(Id(g),[7],ArrayLiteral(IntLiteral(1),IntLiteral(2),IntLiteral(3)))][If(BinaryOp(!=,Id(g),Id(null)),[],[CallStmt(Id(print_list),[Id(g)]),Return()])Else([],[]),CallStmt(Id(print),[StringLiteral(Null list)])])),FuncDecl(Id(print_list)[VarDecl(Id(g),[100])],([][Assign(Id(elem),ArrayCell(Id(g),[IntLiteral(0)])),Assign(Id(i),IntLiteral(0)),While(BinaryOp(!=,Id(elem),Id(null)),[],[CallStmt(Id(print),[Id(elem)]),Assign(Id(i),BinaryOp(+,Id(i),IntLiteral(1))),Assign(Id(elem),ArrayCell(Id(g),[Id(i)]))])]))])',394))
    def test_number_95(self):
        """full program structure"""
        self.assertTrue(TestAST.checkASTGen('Var: a,b; Function: main Body: Var: x,y[1],y={1}, g[2][3]= "String"; f(g)[1] = {1,2,3}; For (i=0, i<len(g), 1%2) Do For (j=0,j<len(g[i]),3-2) Do If g[i][j] \\5 %(2+2*2) <= f(g[0])[0] Then print(g[i][j]); Else Continue; EndIf. EndFor. EndFor. EndBody. Function: f Parameter: any Body: Return any; EndBody.','Program([VarDecl(Id(a)),VarDecl(Id(b)),FuncDecl(Id(main)[],([VarDecl(Id(x)),VarDecl(Id(y),[1]),VarDecl(Id(y),ArrayLiteral(IntLiteral(1))),VarDecl(Id(g),[2,3],StringLiteral(String))][Assign(ArrayCell(CallExpr(Id(f),[Id(g)]),[IntLiteral(1)]),ArrayLiteral(IntLiteral(1),IntLiteral(2),IntLiteral(3))),For(Id(i),IntLiteral(0),BinaryOp(<,Id(i),CallExpr(Id(len),[Id(g)])),BinaryOp(%,IntLiteral(1),IntLiteral(2)),[],[For(Id(j),IntLiteral(0),BinaryOp(<,Id(j),CallExpr(Id(len),[ArrayCell(Id(g),[Id(i)])])),BinaryOp(-,IntLiteral(3),IntLiteral(2)),[],[If(BinaryOp(<=,BinaryOp(%,BinaryOp(\\,ArrayCell(Id(g),[Id(i),Id(j)]),IntLiteral(5)),BinaryOp(+,IntLiteral(2),BinaryOp(*,IntLiteral(2),IntLiteral(2)))),ArrayCell(CallExpr(Id(f),[ArrayCell(Id(g),[IntLiteral(0)])]),[IntLiteral(0)])),[],[CallStmt(Id(print),[ArrayCell(Id(g),[Id(i),Id(j)])])])Else([],[Continue()])])])])),FuncDecl(Id(f)[VarDecl(Id(any))],([][Return(Id(any))]))])',395))
    def test_number_96(self):
        """full program structure"""
        self.assertTrue(TestAST.checkASTGen('Var: a,b=2e-13,d[2]=0x12; Function: main Body: a=1+2%3 \\ (5>6) == -True || !"False" --3 +-3 -!3 && {1}; If a%2 == 0 Then b= True ||2.3 * 5 == 3 && 1 + -6 ; Else b= False; EndIf. print(f()[5],a,print(b),c[2]); EndBody.','Program([VarDecl(Id(a)),VarDecl(Id(b),FloatLiteral(2e-13)),VarDecl(Id(d),[2],IntLiteral(18)),FuncDecl(Id(main)[],([][Assign(Id(a),BinaryOp(==,BinaryOp(+,IntLiteral(1),BinaryOp(\\,BinaryOp(%,IntLiteral(2),IntLiteral(3)),BinaryOp(>,IntLiteral(5),IntLiteral(6)))),BinaryOp(&&,BinaryOp(||,UnaryOp(-,BooleanLiteral(true)),BinaryOp(-,BinaryOp(+,BinaryOp(-,UnaryOp(!,StringLiteral(False)),UnaryOp(-,IntLiteral(3))),UnaryOp(-,IntLiteral(3))),UnaryOp(!,IntLiteral(3)))),ArrayLiteral(IntLiteral(1))))),If(BinaryOp(==,BinaryOp(%,Id(a),IntLiteral(2)),IntLiteral(0)),[],[Assign(Id(b),BinaryOp(==,BinaryOp(||,BooleanLiteral(true),BinaryOp(*,FloatLiteral(2.3),IntLiteral(5))),BinaryOp(&&,IntLiteral(3),BinaryOp(+,IntLiteral(1),UnaryOp(-,IntLiteral(6))))))])Else([],[Assign(Id(b),BooleanLiteral(false))]),CallStmt(Id(print),[ArrayCell(CallExpr(Id(f),[]),[IntLiteral(5)]),Id(a),CallExpr(Id(print),[Id(b)]),ArrayCell(Id(c),[IntLiteral(2)])])]))])',396))
    def test_number_97(self):
        """full program structure"""
        self.assertTrue(TestAST.checkASTGen('Var: n; Function: switch Parameter: n Body: If n == 1 Then print("+"); ElseIf n==2 Then print(n,"Even"); ElseIf n ==3 Then Return False; ElseIf n ==4 Then Return switch(5); ElseIf n==5 Then Return {1,2,3,{4,5,{6}}, 7, {8}};  ElseIf n==6 Then Return switch(5)[3]; Else print("Cant think of anything :)), brain dead!");  EndIf. EndBody.','Program([VarDecl(Id(n)),FuncDecl(Id(switch)[VarDecl(Id(n))],([][If(BinaryOp(==,Id(n),IntLiteral(1)),[],[CallStmt(Id(print),[StringLiteral(+)])])ElseIf(BinaryOp(==,Id(n),IntLiteral(2)),[],[CallStmt(Id(print),[Id(n),StringLiteral(Even)])])ElseIf(BinaryOp(==,Id(n),IntLiteral(3)),[],[Return(BooleanLiteral(false))])ElseIf(BinaryOp(==,Id(n),IntLiteral(4)),[],[Return(CallExpr(Id(switch),[IntLiteral(5)]))])ElseIf(BinaryOp(==,Id(n),IntLiteral(5)),[],[Return(ArrayLiteral(IntLiteral(1),IntLiteral(2),IntLiteral(3),ArrayLiteral(IntLiteral(4),IntLiteral(5),ArrayLiteral(IntLiteral(6))),IntLiteral(7),ArrayLiteral(IntLiteral(8))))])ElseIf(BinaryOp(==,Id(n),IntLiteral(6)),[],[Return(ArrayCell(CallExpr(Id(switch),[IntLiteral(5)]),[IntLiteral(3)]))])Else([],[CallStmt(Id(print),[StringLiteral(Cant think of anything :)), brain dead!)])])]))])',397))
    def test_number_98(self):
        """full program structure"""
        self.assertTrue(TestAST.checkASTGen('Var: plus="+"; Function: print_pattern Parameter: line_number, char Body: For (i=0, i<line_number, 1) Do Var: j; j= i+1; While j>0 Do print(char); EndWhile. print("\\n"); EndFor. EndBody. Function: main Body: print_pattern(10,plus); EndBody.','Program([VarDecl(Id(plus),StringLiteral(+)),FuncDecl(Id(print_pattern)[VarDecl(Id(line_number)),VarDecl(Id(char))],([][For(Id(i),IntLiteral(0),BinaryOp(<,Id(i),Id(line_number)),IntLiteral(1),[VarDecl(Id(j))],[Assign(Id(j),BinaryOp(+,Id(i),IntLiteral(1))),While(BinaryOp(>,Id(j),IntLiteral(0)),[],[CallStmt(Id(print),[Id(char)])]),CallStmt(Id(print),[StringLiteral(\\n)])])])),FuncDecl(Id(main)[],([][CallStmt(Id(print_pattern),[IntLiteral(10),Id(plus)])]))])',398))
    def test_number_99(self):
        """empty every thing"""
        self.assertTrue(TestAST.checkASTGen('Function: emp Body: If 1 Then Else EndIf. While 1 Do EndWhile. For (x=1,1,1) Do EndFor.EndBody. Function: main Parameter: n Body: Do While 1 EndDo. Continue; Return; EndBody.','Program([FuncDecl(Id(emp)[],([][If(IntLiteral(1),[],[])Else([],[]),While(IntLiteral(1),[],[]),For(Id(x),IntLiteral(1),IntLiteral(1),IntLiteral(1),[],[])])),FuncDecl(Id(main)[VarDecl(Id(n))],([][Dowhile([],[],IntLiteral(1)),Continue(),Return()]))])',399))

