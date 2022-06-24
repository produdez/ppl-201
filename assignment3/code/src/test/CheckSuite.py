import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):
    #CODE
    def test_number_0(self):
        """Complex program"""
        raw_input= """Function: main Body: printStrLn(); EndBody."""
        input = Program([FuncDecl(Id('main'), [], ([], [CallStmt(Id('printStrLn'), [])]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
        self.assertTrue(TestChecker.test(input,expect,400))
    def test_number_1(self):
        """Simple program"""
        raw_input= """Function: main Body: printStrLn(read(4)); EndBody."""
        input = Program([FuncDecl(Id('main'), [], ([], [CallStmt(Id('printStrLn'), [CallExpr(Id('read'), [IntLiteral(4)])])]))])
        expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input,expect,401))
    def test_number_2(self):
        """using non-declared var"""
        raw_input= """Function: main Parameter: n Body: Var: i =0; assign = 10; EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('n'), [], None)], ([VarDecl(Id('i'), [], IntLiteral(0))], [Assign(Id('assign'), IntLiteral(10))]))])
        expect = str(Undeclared(Identifier(), 'assign'))
        self.assertTrue(TestChecker.test(input,expect,402))
    def test_number_3(self):
        """using non-declared fuc"""
        raw_input= """Function: main Body: fact(); EndBody."""
        input = Program([FuncDecl(Id('main'), [], ([], [CallStmt(Id('fact'), [])]))])
        expect = str(Undeclared(Function(), 'fact'))
        self.assertTrue(TestChecker.test(input,expect,403))
    def test_number_4(self):
        """variable already in param"""
        raw_input= """Function: main Parameter: n Body: Var: n = 0; n=10;  EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('n'), [], None)], ([VarDecl(Id('n'), [], IntLiteral(0))], [Assign(Id('n'), IntLiteral(10))]))])
        expect = str(Redeclared(Variable(), 'n'))
        self.assertTrue(TestChecker.test(input,expect,404))
    def test_number_5(self):
        """duplicate function"""
        raw_input= """Function: main Parameter: n,a[2][3] Body: i = 5; EndBody. Function: main Parameter: n,a[2][3] Body: i = 5; EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('n'), [], None), VarDecl(Id('a'), [2, 3], None)], ([], [Assign(Id('i'), IntLiteral(5))])), FuncDecl(Id('main'), [VarDecl(Id('n'), [], None), VarDecl(Id('a'), [2, 3], None)], ([], [Assign(Id('i'), IntLiteral(5))]))])
        expect = str(Redeclared(Function(), 'main'))
        self.assertTrue(TestChecker.test(input,expect,405))
    def test_number_6(self):
        """redeclaring pre-defined function"""
        raw_input= """Function: main Body: EndBody. Function: printLn Body: EndBody."""
        input = Program([FuncDecl(Id('main'), [], ([], [])), FuncDecl(Id('printLn'), [], ([], []))])
        expect = str(Redeclared(Function(), 'printLn'))
        self.assertTrue(TestChecker.test(input,expect,406))
    def test_number_7(self):
        """overloading pre-defined funcion"""
        raw_input= """Function: main Body: EndBody. Function: printLn Parameter: n  Body: EndBody."""
        input = Program([FuncDecl(Id('main'), [], ([], [])), FuncDecl(Id('printLn'), [VarDecl(Id('n'), [], None)], ([], []))])
        expect = str(Redeclared(Function(), 'printLn'))
        self.assertTrue(TestChecker.test(input,expect,407))
    def test_number_8(self):
        """if wrong first"""
        raw_input= """Function: main Parameter: a,b,c Body: If a+b Then a=5; ElseIf a!=b Then Return; EndIf. EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None), VarDecl(Id('c'), [], None)], ([], [If([[BinaryOp('+', Id('a'), Id('b')), [], [Assign(Id('a'), IntLiteral(5))]], [BinaryOp('!=', Id('a'), Id('b')), [], [Return(None)]]], ([], []))]))])
        expect = str(TypeMismatchInStatement(If([[BinaryOp('+', Id('a'), Id('b')), [], [Assign(Id('a'), IntLiteral(5))]], [BinaryOp('!=', Id('a'), Id('b')), [], [Return(None)]]], ([], []))))
        self.assertTrue(TestChecker.test(input,expect,408))
    def test_number_9(self):
        """if wrong second"""
        raw_input= """Function: main Parameter: a,b,c Body: If a==b Then a=5; ElseIf 1.1 *. 2e3 Then Return; EndIf. EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None), VarDecl(Id('c'), [], None)], ([], [If([[BinaryOp('==', Id('a'), Id('b')), [], [Assign(Id('a'), IntLiteral(5))]], [BinaryOp('*.', FloatLiteral(1.1), FloatLiteral(2000.0)), [], [Return(None)]]], ([], []))]))])
        expect = str(TypeMismatchInStatement(If([[BinaryOp('==', Id('a'), Id('b')), [], [Assign(Id('a'), IntLiteral(5))]], [BinaryOp('*.', FloatLiteral(1.1), FloatLiteral(2000.0)), [], [Return(None)]]], ([], []))))
        self.assertTrue(TestChecker.test(input,expect,409))
    def test_number_10(self):
        """normal and no error"""
        raw_input= """Function: main \n Parameter: n,c,y Body: EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('n'), [], None), VarDecl(Id('c'), [], None), VarDecl(Id('y'), [], None)], ([], []))])
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,410))
    def test_number_11(self):
        """type infer in if"""
        raw_input= """Function: main Body: Var: x,y,z; If x Then x = !!(1>(y+5)); ElseIf z Then y = z; EndIf. EndBody."""
        input = Program([FuncDecl(Id('main'), [], ([VarDecl(Id('x'), [], None), VarDecl(Id('y'), [], None), VarDecl(Id('z'), [], None)], [If([[Id('x'), [], [Assign(Id('x'), UnaryOp('!', UnaryOp('!', BinaryOp('>', IntLiteral(1), BinaryOp('+', Id('y'), IntLiteral(5))))))]], [Id('z'), [], [Assign(Id('y'), Id('z'))]]], ([], []))]))])
        expect = str(TypeMismatchInStatement(Assign(Id('y'), Id('z'))))
        self.assertTrue(TestChecker.test(input,expect,411))
    def test_number_12(self):
        """type infer in if"""
        raw_input= """Function: main Body: Var: a,b,c; If a * b > c Then a = b - c; Else a = True; EndIf. EndBody."""
        input = Program([FuncDecl(Id('main'), [], ([VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None), VarDecl(Id('c'), [], None)], [If([[BinaryOp('>', BinaryOp('*', Id('a'), Id('b')), Id('c')), [], [Assign(Id('a'), BinaryOp('-', Id('b'), Id('c')))]]], ([], [Assign(Id('a'), BooleanLiteral(True))]))]))])
        expect = str(TypeMismatchInStatement(Assign(Id('a'), BooleanLiteral(True))))
        self.assertTrue(TestChecker.test(input,expect,412))
    def test_number_13(self):
        """literal, scalar vars and operators"""
        raw_input= """Function: main Parameter: x,y,z Body: x = !(2%3); EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('x'), [], None), VarDecl(Id('y'), [], None), VarDecl(Id('z'), [], None)], ([], [Assign(Id('x'), UnaryOp('!', BinaryOp('%', IntLiteral(2), IntLiteral(3))))]))])
        expect = str(TypeMismatchInExpression(UnaryOp('!', BinaryOp('%', IntLiteral(2), IntLiteral(3)))))
        self.assertTrue(TestChecker.test(input,expect,413))
    def test_number_14(self):
        """literal, scalar vars and operators"""
        raw_input= """Function: main Parameter: x,y,z Body: x = -(1>2); EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('x'), [], None), VarDecl(Id('y'), [], None), VarDecl(Id('z'), [], None)], ([], [Assign(Id('x'), UnaryOp('-', BinaryOp('>', IntLiteral(1), IntLiteral(2))))]))])
        expect = str(TypeMismatchInExpression(UnaryOp('-', BinaryOp('>', IntLiteral(1), IntLiteral(2)))))
        self.assertTrue(TestChecker.test(input,expect,414))
    def test_number_15(self):
        """literal, scalar vars and operators"""
        raw_input= """Function: main Parameter: x,y,z Body: x = "Str" + "ing"; EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('x'), [], None), VarDecl(Id('y'), [], None), VarDecl(Id('z'), [], None)], ([], [Assign(Id('x'), BinaryOp('+', StringLiteral('Str'), StringLiteral('ing')))]))])
        expect = str(TypeMismatchInExpression(BinaryOp('+', StringLiteral('Str'), StringLiteral('ing'))))
        self.assertTrue(TestChecker.test(input,expect,415))
    def test_number_16(self):
        """literal, scalar vars and operators"""
        raw_input= """Function: main Parameter: x,y,z Body: x = "StringTypeVar"; EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('x'), [], None), VarDecl(Id('y'), [], None), VarDecl(Id('z'), [], None)], ([], [Assign(Id('x'), StringLiteral('StringTypeVar'))]))])
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,416))
    def test_number_17(self):
        """literal, scalar vars and operators"""
        raw_input= """Function: main Parameter: x,y,z Body: x = 1 % 2 == 1.2-.5e3; EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('x'), [], None), VarDecl(Id('y'), [], None), VarDecl(Id('z'), [], None)], ([], [Assign(Id('x'), BinaryOp('==', BinaryOp('%', IntLiteral(1), IntLiteral(2)), BinaryOp('-.', FloatLiteral(1.2), FloatLiteral(5000.0))))]))])
        expect = str(TypeMismatchInExpression(BinaryOp('==', BinaryOp('%', IntLiteral(1), IntLiteral(2)), BinaryOp('-.', FloatLiteral(1.2), FloatLiteral(5000.0)))))
        self.assertTrue(TestChecker.test(input,expect,417))
    def test_number_18(self):
        """literal, scalar vars and operators"""
        raw_input= """Function: main Parameter: x,y,z Body: x = 1+2 > 4+5 || True; EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('x'), [], None), VarDecl(Id('y'), [], None), VarDecl(Id('z'), [], None)], ([], [Assign(Id('x'), BinaryOp('>', BinaryOp('+', IntLiteral(1), IntLiteral(2)), BinaryOp('||', BinaryOp('+', IntLiteral(4), IntLiteral(5)), BooleanLiteral(True))))]))])
        expect = str(TypeMismatchInExpression(BinaryOp('||', BinaryOp('+', IntLiteral(4), IntLiteral(5)), BooleanLiteral(True))))
        self.assertTrue(TestChecker.test(input,expect,418))
    def test_number_19(self):
        """literal, scalar vars and operators"""
        raw_input= """Function: main Parameter: x,y,z Body: x =  !-2; EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('x'), [], None), VarDecl(Id('y'), [], None), VarDecl(Id('z'), [], None)], ([], [Assign(Id('x'), UnaryOp('!', UnaryOp('-', IntLiteral(2))))]))])
        expect = str(TypeMismatchInExpression(UnaryOp('!', UnaryOp('-', IntLiteral(2)))))
        self.assertTrue(TestChecker.test(input,expect,419))
    def test_number_20(self):
        """literal, scalar vars and operators"""
        raw_input= """Function: main Parameter: x,y,z Body: x =  y  * x - -(z >.1.5); EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('x'), [], None), VarDecl(Id('y'), [], None), VarDecl(Id('z'), [], None)], ([], [Assign(Id('x'), BinaryOp('-', BinaryOp('*', Id('y'), Id('x')), UnaryOp('-', BinaryOp('>.', Id('z'), FloatLiteral(1.5)))))]))])
        expect = str(TypeMismatchInExpression(UnaryOp('-', BinaryOp('>.', Id('z'), FloatLiteral(1.5)))))
        self.assertTrue(TestChecker.test(input,expect,420))
    def test_number_21(self):
        """literal, scalar vars and operators"""
        raw_input= """Function: main Parameter: x,y,z Body: x =  y  * x - -.(z +.1.5); EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('x'), [], None), VarDecl(Id('y'), [], None), VarDecl(Id('z'), [], None)], ([], [Assign(Id('x'), BinaryOp('-', BinaryOp('*', Id('y'), Id('x')), UnaryOp('-.', BinaryOp('+.', Id('z'), FloatLiteral(1.5)))))]))])
        expect = str(TypeMismatchInExpression(BinaryOp('-', BinaryOp('*', Id('y'), Id('x')), UnaryOp('-.', BinaryOp('+.', Id('z'), FloatLiteral(1.5))))))
        self.assertTrue(TestChecker.test(input,expect,421))
    def test_number_22(self):
        """empty program"""
        raw_input= """Function: main Body: EndBody."""
        input = Program([FuncDecl(Id('main'), [], ([], []))])
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,422))
    def test_number_23(self):
        """many func_inference call stmt"""
        raw_input= """Function: main Parameter: x,y Body: x=5; EndBody. Function: main2 Body: main(1.2,5); EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('x'), [], None), VarDecl(Id('y'), [], None)], ([], [Assign(Id('x'), IntLiteral(5))])), FuncDecl(Id('main2'), [], ([], [CallStmt(Id('main'), [FloatLiteral(1.2), IntLiteral(5)])]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id('main'), [FloatLiteral(1.2), IntLiteral(5)])))
        self.assertTrue(TestChecker.test(input,expect,423))
    def test_number_24(self):
        """infer func param inside func call stmt"""
        raw_input= """Function: test Parameter: x Body: x = 5; EndBody. Function: main Body: Var: x = 2.5; test(x); EndBody."""
        input = Program([FuncDecl(Id('test'), [VarDecl(Id('x'), [], None)], ([], [Assign(Id('x'), IntLiteral(5))])), FuncDecl(Id('main'), [], ([VarDecl(Id('x'), [], FloatLiteral(2.5))], [CallStmt(Id('test'), [Id('x')])]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id('test'), [Id('x')])))
        self.assertTrue(TestChecker.test(input,expect,424))
    def test_number_25(self):
        """recursive function"""
        raw_input= """Function: main Parameter: x,y Body: x =5; main(x,y); EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('x'), [], None), VarDecl(Id('y'), [], None)], ([], [Assign(Id('x'), IntLiteral(5)), CallStmt(Id('main'), [Id('x'), Id('y')])]))])
        expect = str(TypeCannotBeInferred(CallStmt(Id('main'), [Id('x'), Id('y')])))
        self.assertTrue(TestChecker.test(input,expect,425))
    def test_number_26(self):
        """recursive function (tricky)"""
        raw_input= """Function: recur Parameter: x,y Body: x=2.2; recur(y,x); EndBody. Function: main Body: EndBody."""
        input = Program([FuncDecl(Id('recur'), [VarDecl(Id('x'), [], None), VarDecl(Id('y'), [], None)], ([], [Assign(Id('x'), FloatLiteral(2.2)), CallStmt(Id('recur'), [Id('y'), Id('x')])])), FuncDecl(Id('main'), [], ([], []))])
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,426))
    def test_number_27(self):
        """function same name as glob var"""
        raw_input= """Var: a,b,c,d; Function: b Body: EndBody."""
        input = Program([VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None), VarDecl(Id('c'), [], None), VarDecl(Id('d'), [], None), FuncDecl(Id('b'), [], ([], []))])
        expect = str(Redeclared(Function(), 'b'))
        self.assertTrue(TestChecker.test(input,expect,427))
    def test_number_28(self):
        """Calling a var as a funcion"""
        raw_input= """Var: a; Function: main Body: Var: b; a(); EndBody."""
        input = Program([VarDecl(Id('a'), [], None), FuncDecl(Id('main'), [], ([VarDecl(Id('b'), [], None)], [CallStmt(Id('a'), [])]))])
        expect = str(Undeclared(Function(), 'a'))
        self.assertTrue(TestChecker.test(input,expect,428))
    def test_number_29(self):
        """Using variable in wrong scope"""
        raw_input= """Var: a,b; Function: main Body: If True Then Var: c = 5; EndIf. a=b+c; EndBody."""
        input = Program([VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None), FuncDecl(Id('main'), [], ([], [If([[BooleanLiteral(True), [VarDecl(Id('c'), [], IntLiteral(5))], []]], ([], [])), Assign(Id('a'), BinaryOp('+', Id('b'), Id('c')))]))])
        expect = str(Undeclared(Identifier(), 'c'))
        self.assertTrue(TestChecker.test(input,expect,429))
    def test_number_30(self):
        """infering a variable from function param"""
        raw_input= """Var: a,b; Function: fung Parameter: a,b Body: EndBody. Function: main Body: fung(3,2.5); fung(a,b); a=b; EndBody."""
        input = Program([VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None), FuncDecl(Id('fung'), [VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None)], ([], [])), FuncDecl(Id('main'), [], ([], [CallStmt(Id('fung'), [IntLiteral(3), FloatLiteral(2.5)]), CallStmt(Id('fung'), [Id('a'), Id('b')]), Assign(Id('a'), Id('b'))]))])
        expect = str(TypeMismatchInStatement(Assign(Id('a'), Id('b'))))
        self.assertTrue(TestChecker.test(input,expect,430))
    def test_number_31(self):
        """infering a variable from function param"""
        raw_input= """Function: wow Parameter: x,y Body: y=5e3; EndBody. Function: main Parameter: a,b Body: wow(5,a); wow(a,5); EndBody."""
        input = Program([FuncDecl(Id('wow'), [VarDecl(Id('x'), [], None), VarDecl(Id('y'), [], None)], ([], [Assign(Id('y'), FloatLiteral(5000.0))])), FuncDecl(Id('main'), [VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None)], ([], [CallStmt(Id('wow'), [IntLiteral(5), Id('a')]), CallStmt(Id('wow'), [Id('a'), IntLiteral(5)])]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id('wow'), [Id('a'), IntLiteral(5)])))
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_number_32(self):
        """some param/arg cant be inffered"""
        raw_input= """Function: main Parameter: a,b Body: Var: x; main(5,x); EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None)], ([VarDecl(Id('x'), [], None)], [CallStmt(Id('main'), [IntLiteral(5), Id('x')])]))])
        expect = str(TypeCannotBeInferred(CallStmt(Id('main'), [IntLiteral(5), Id('x')])))
        self.assertTrue(TestChecker.test(input,expect,432))
    def test_number_33(self):
        """redecl in one Var"""
        raw_input= """Var: a,x,y=5,z,g,f,y;"""
        input = Program([VarDecl(Id('a'), [], None), VarDecl(Id('x'), [], None), VarDecl(Id('y'), [], IntLiteral(5)), VarDecl(Id('z'), [], None), VarDecl(Id('g'), [], None), VarDecl(Id('f'), [], None), VarDecl(Id('y'), [], None)])
        expect = str(Redeclared(Variable(), 'y'))
        self.assertTrue(TestChecker.test(input,expect,433))
    def test_number_34(self):
        """redecl in two Var?"""
        raw_input= """Function: main Body: Var: a,b; Var: c,d; Var: b,f; EndBody."""
        input = Program([FuncDecl(Id('main'), [], ([VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None), VarDecl(Id('c'), [], None), VarDecl(Id('d'), [], None), VarDecl(Id('b'), [], None), VarDecl(Id('f'), [], None)], []))])
        expect = str(Redeclared(Variable(), 'b'))
        self.assertTrue(TestChecker.test(input,expect,434))
    def test_number_35(self):
        """dup skip dup function"""
        raw_input= """Function: fun Body: EndBody. Function: main Body: EndBody. Function: fun Body: EndBody."""
        input = Program([FuncDecl(Id('fun'), [], ([], [])), FuncDecl(Id('main'), [], ([], [])), FuncDecl(Id('fun'), [], ([], []))])
        expect = str(Redeclared(Function(), 'fun'))
        self.assertTrue(TestChecker.test(input,expect,435))
    def test_number_36(self):
        """duplicate parameter"""
        raw_input= """Function: main Parameter: a,b,x,x Body: EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None), VarDecl(Id('x'), [], None), VarDecl(Id('x'), [], None)], ([], []))])
        expect = str(Redeclared(Parameter(), 'x'))
        self.assertTrue(TestChecker.test(input,expect,436))
    def test_number_37(self):
        """calling before decl but one is not decled"""
        raw_input= """Function: main Body: f1(); f2(b); EndBody. Function: f1 Body: EndBody. """
        input = Program([FuncDecl(Id('main'), [], ([], [CallStmt(Id('f1'), []), CallStmt(Id('f2'), [Id('b')])])), FuncDecl(Id('f1'), [], ([], []))])
        expect = str(Undeclared(Function(), 'f2'))
        self.assertTrue(TestChecker.test(input,expect,437))
    def test_number_38(self):
        """int ops"""
        raw_input= """Var:a,b,c,d,e,f; Function: main Body: If a == 5 Then a = b*c - 7; ElseIf a+b*c % 4 % (6*b -2 + 3 + c--6) > a Then a =testf(); EndIf.  EndBody. Function: testf Body: Return; EndBody."""
        input = Program([VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None), VarDecl(Id('c'), [], None), VarDecl(Id('d'), [], None), VarDecl(Id('e'), [], None), VarDecl(Id('f'), [], None), FuncDecl(Id('main'), [], ([], [If([[BinaryOp('==', Id('a'), IntLiteral(5)), [], [Assign(Id('a'), BinaryOp('-', BinaryOp('*', Id('b'), Id('c')), IntLiteral(7)))]], [BinaryOp('>', BinaryOp('+', Id('a'), BinaryOp('%', BinaryOp('%', BinaryOp('*', Id('b'), Id('c')), IntLiteral(4)), BinaryOp('-', BinaryOp('+', BinaryOp('+', BinaryOp('-', BinaryOp('*', IntLiteral(6), Id('b')), IntLiteral(2)), IntLiteral(3)), Id('c')), UnaryOp('-', IntLiteral(6))))), Id('a')), [], [Assign(Id('a'), CallExpr(Id('testf'), []))]]], ([], []))])), FuncDecl(Id('testf'), [], ([], [Return(None)]))])
        expect = str(TypeMismatchInStatement(Return(None)))
        self.assertTrue(TestChecker.test(input,expect,438))
    def test_number_39(self):
        """float ops"""
        raw_input= """Var:a,b,c,d,e,f; Function: main Body: If a >. 5.3 Then a = b*.c -. 9.5; ElseIf a+.b*.c -.-. 4 % (6e3 *. b -.2.0 +. 0.5 +. c-.-.6e-4) > a Then Return; EndIf.  EndBody. """
        input =  Program([VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None), VarDecl(Id('c'), [], None), VarDecl(Id('d'), [], None), VarDecl(Id('e'), [], None), VarDecl(Id('f'), [], None), FuncDecl(Id('main'), [], ([], [If([[BinaryOp('>.', Id('a'), FloatLiteral(5.3)), [], [Assign(Id('a'), BinaryOp('-.', BinaryOp('*.', Id('b'), Id('c')), FloatLiteral(9.5)))]], [BinaryOp('>', BinaryOp('-.', BinaryOp('+.', Id('a'), BinaryOp('*.', Id('b'), Id('c'))), BinaryOp('%', UnaryOp('-.', IntLiteral(4)), BinaryOp('-.', BinaryOp('+.', BinaryOp('+.', BinaryOp('-.', BinaryOp('*.', FloatLiteral(6000.0), Id('b')), FloatLiteral(2.0)), FloatLiteral(0.5)), Id('c')), UnaryOp('-.', FloatLiteral(0.0006))))), Id('a')), [], [Return(None)]]], ([], []))]))])
        expect = str(TypeMismatchInExpression(UnaryOp('-.', IntLiteral(4))))
        self.assertTrue(TestChecker.test(input,expect,439))
    def test_number_40(self):
        """bool ops"""
        raw_input= """Function: main Parameter: a,b,c Body: c =( (a>b) || c && (1.5 >.2e3) || !!True); main(0,1,0); EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None), VarDecl(Id('c'), [], None)], ([], [Assign(Id('c'), BinaryOp('||', BinaryOp('&&', BinaryOp('||', BinaryOp('>', Id('a'), Id('b')), Id('c')), BinaryOp('>.', FloatLiteral(1.5), FloatLiteral(2000.0))), UnaryOp('!', UnaryOp('!', BooleanLiteral(True))))), CallStmt(Id('main'), [IntLiteral(0), IntLiteral(1), IntLiteral(0)])]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id('main'), [IntLiteral(0), IntLiteral(1), IntLiteral(0)])))
        self.assertTrue(TestChecker.test(input,expect,440))
    def test_number_41(self):
        """normal for"""
        raw_input= """Function: main Parameter: a,c,b Body: For (a= 10, a > b, 1) Do Return c; EndFor. EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('a'), [], None), VarDecl(Id('c'), [], None), VarDecl(Id('b'), [], None)], ([], [For(Id('a'), IntLiteral(10), BinaryOp('>', Id('a'), Id('b')), IntLiteral(1), ([], [Return(Id('c'))]))]))])
        expect = str(TypeCannotBeInferred(Return(Id('c'))))
        self.assertTrue(TestChecker.test(input,expect,441))
    def test_number_42(self):
        """for loop wrong update"""
        raw_input= """Function: main Parameter: a,b,c Body: For(a= b + 1, (a> int_of_float (c-.5.5)) || True || !False, c) Do Return; EndFor. EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None), VarDecl(Id('c'), [], None)], ([], [For(Id('a'), BinaryOp('+', Id('b'), IntLiteral(1)), BinaryOp('||', BinaryOp('||', BinaryOp('>', Id('a'), CallExpr(Id('int_of_float'), [BinaryOp('-.', Id('c'), FloatLiteral(5.5))])), BooleanLiteral(True)), UnaryOp('!', BooleanLiteral(False))), Id('c'), ([], [Return(None)]))]))])
        expect = str(TypeMismatchInStatement(For(Id('a'), BinaryOp('+', Id('b'), IntLiteral(1)), BinaryOp('||', BinaryOp('||', BinaryOp('>', Id('a'), CallExpr(Id('int_of_float'), [BinaryOp('-.', Id('c'), FloatLiteral(5.5))])), BooleanLiteral(True)), UnaryOp('!', BooleanLiteral(False))), Id('c'), ([], [Return(None)]))))
        self.assertTrue(TestChecker.test(input,expect,442))
    def test_number_43(self):
        """whiles"""
        raw_input= """Function: main Parameter: a,b,e Body: While (a <. 5.5) Do e = 1; e = b; EndWhile. While b Do Return; EndWhile. EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None), VarDecl(Id('e'), [], None)], ([], [While(BinaryOp('<.', Id('a'), FloatLiteral(5.5)), ([], [Assign(Id('e'), IntLiteral(1)), Assign(Id('e'), Id('b'))])), While(Id('b'), ([], [Return(None)]))]))])
        expect = str(TypeMismatchInStatement(While(Id('b'), ([], [Return(None)]))))
        self.assertTrue(TestChecker.test(input,expect,443))
    def test_number_44(self):
        """do whiles"""
        raw_input= """Function: main Parameter: a,b,c Body: Do a = a+ 1 * b == c; While b EndDo. EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None), VarDecl(Id('c'), [], None)], ([], [Dowhile(([], [Assign(Id('a'), BinaryOp('==', BinaryOp('+', Id('a'), BinaryOp('*', IntLiteral(1), Id('b'))), Id('c')))]), Id('b'))]))])
        expect = str(TypeMismatchInStatement(Assign(Id('a'), BinaryOp('==', BinaryOp('+', Id('a'), BinaryOp('*', IntLiteral(1), Id('b'))), Id('c')))))
        self.assertTrue(TestChecker.test(input,expect,444))
    def test_number_45(self):
        """sequences of assignment"""
        raw_input= """Function: main Parameter: a,b,c,d,e,f,g,h Body: a=1; b=6.2; a=c; d=b; f = g >. h -. 1.2; c = h[2]; EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None), VarDecl(Id('c'), [], None), VarDecl(Id('d'), [], None), VarDecl(Id('e'), [], None), VarDecl(Id('f'), [], None), VarDecl(Id('g'), [], None), VarDecl(Id('h'), [], None)], ([], [Assign(Id('a'), IntLiteral(1)), Assign(Id('b'), FloatLiteral(6.2)), Assign(Id('a'), Id('c')), Assign(Id('d'), Id('b')), Assign(Id('f'), BinaryOp('>.', Id('g'), BinaryOp('-.', Id('h'), FloatLiteral(1.2)))), Assign(Id('c'), ArrayCell(Id('h'), [IntLiteral(2)]))]))])
        expect = str(TypeMismatchInExpression(ArrayCell(Id('h'), [IntLiteral(2)])))
        self.assertTrue(TestChecker.test(input,expect,445))
    def test_number_46(self):
        """array cell indexing and array literals"""
        raw_input= """Function: main Parameter: a,b,c Body: a = {{1,2,3},{4,5,6}}; b = a[1][2];  c = a[2]; EndBody. """
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None), VarDecl(Id('c'), [], None)], ([], [Assign(Id('a'), ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3)]), ArrayLiteral([IntLiteral(4), IntLiteral(5), IntLiteral(6)])])), Assign(Id('b'), ArrayCell(Id('a'), [IntLiteral(1), IntLiteral(2)])), Assign(Id('c'), ArrayCell(Id('a'), [IntLiteral(2)]))]))])
        expect = str(TypeMismatchInStatement(Assign(Id('a'), ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3)]), ArrayLiteral([IntLiteral(4), IntLiteral(5), IntLiteral(6)])]))))
        self.assertTrue(TestChecker.test(input,expect,446))
    def test_number_47(self):
        """Function that return string, array cell"""
        raw_input= """Function: main Parameter: a,b Body: a = f1(); b = f2(); a=b; EndBody. Function: f1 Body: Return {1}; EndBody. Function: f2 Body: Return ""; EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None)], ([], [Assign(Id('a'), CallExpr(Id('f1'), [])), Assign(Id('b'), CallExpr(Id('f2'), [])), Assign(Id('a'), Id('b'))])), FuncDecl(Id('f1'), [], ([], [Return(ArrayLiteral([IntLiteral(1)]))])), FuncDecl(Id('f2'), [], ([], [Return(StringLiteral(''))]))])
        expect = str(TypeCannotBeInferred(Assign(Id('a'), CallExpr(Id('f1'), []))))
        self.assertTrue(TestChecker.test(input,expect,447))
    def test_number_48(self):
        """Inference in an inner inner scope"""
        raw_input= """Function: main Parameter: x Body: If True Then Var: x;  If False Then Var: y;  x = y+x; EndIf. x=1.2;  EndIf. x=5; EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('x'), [], None)], ([], [If([[BooleanLiteral(True), [VarDecl(Id('x'), [], None)], [If([[BooleanLiteral(False), [VarDecl(Id('y'), [], None)], [Assign(Id('x'), BinaryOp('+', Id('y'), Id('x')))]]], ([], [])), Assign(Id('x'), FloatLiteral(1.2))]]], ([], [])), Assign(Id('x'), IntLiteral(5))]))])
        expect = str(TypeMismatchInStatement(Assign(Id('x'), FloatLiteral(1.2))))
        self.assertTrue(TestChecker.test(input,expect,448))
    def test_number_49(self):
        """Inference in an inner inner scope"""
        raw_input= """Function: main Parameter: a Body: If 1>2 Then a=5; Else a=2.5; EndIf. EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('a'), [], None)], ([], [If([[BinaryOp('>', IntLiteral(1), IntLiteral(2)), [], [Assign(Id('a'), IntLiteral(5))]]], ([], [Assign(Id('a'), FloatLiteral(2.5))]))]))])
        expect = str( TypeMismatchInStatement(Assign(Id('a'), FloatLiteral(2.5))))
        self.assertTrue(TestChecker.test(input,expect,449))
    def test_number_50(self):
        """How to infer array cell?"""
        raw_input= """Var: a,b;Function: main Parameter: x Body: main(5)[2][3] = b % 2; EndBody."""
        input = Program([VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None), FuncDecl(Id('main'), [VarDecl(Id('x'), [], None)], ([], [Assign(ArrayCell(CallExpr(Id('main'), [IntLiteral(5)]), [IntLiteral(2), IntLiteral(3)]), BinaryOp('%', Id('b'), IntLiteral(2)))]))])
        expect = str(TypeCannotBeInferred(Assign(ArrayCell(CallExpr(Id('main'), [IntLiteral(5)]), [IntLiteral(2), IntLiteral(3)]), BinaryOp('%', Id('b'), IntLiteral(2)))))
        self.assertTrue(TestChecker.test(input,expect,450))
    def test_number_51(self):
        """return mismatch cause function return is infered"""
        raw_input= """Var: a= {1}, b = ""; Function: main Body: a = f1(); Return; EndBody. Function: f1 Body: Return b; EndBody."""
        input = Program([VarDecl(Id('a'), [], ArrayLiteral([IntLiteral(1)])), VarDecl(Id('b'), [], StringLiteral('')), FuncDecl(Id('main'), [], ([], [Assign(Id('a'), CallExpr(Id('f1'), [])), Return(None)])), FuncDecl(Id('f1'), [], ([], [Return(Id('b'))]))])
        expect = str(TypeMismatchInStatement(Return(Id('b'))))
        self.assertTrue(TestChecker.test(input,expect,451))
    def test_number_52(self):
        """Mismatch parameter length"""
        raw_input= """Function: main Body: printLn("String to Print"); EndBody."""
        input = Program([FuncDecl(Id('main'), [], ([], [CallStmt(Id('printLn'), [StringLiteral('String to Print')])]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id('printLn'), [StringLiteral('String to Print')])))
        self.assertTrue(TestChecker.test(input,expect,452))
    def test_number_53(self):
        """Recur + param infer means error"""
        raw_input= """Function: main Parameter: a Body: Var: b=7.0; a = 5; main(b); EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('a'), [], None)], ([VarDecl(Id('b'), [], FloatLiteral(7.0))], [Assign(Id('a'), IntLiteral(5)), CallStmt(Id('main'), [Id('b')])]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id('main'), [Id('b')])))
        self.assertTrue(TestChecker.test(input,expect,453))
    def test_number_54(self):
        """Recur + param infer means error"""
        raw_input= """Function: main Parameter: a Body: Var: b=5.5e-6;  main(b); a = 0x12; EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('a'), [], None)], ([VarDecl(Id('b'), [], FloatLiteral(5.5e-06))], [CallStmt(Id('main'), [Id('b')]), Assign(Id('a'), IntLiteral(18))]))])
        expect = str(TypeMismatchInStatement(Assign(Id('a'), IntLiteral(18))))
        self.assertTrue(TestChecker.test(input,expect,454))
    def test_number_55(self):
        """Many returns"""
        raw_input= """Function: main Parameter: a,b Body: Return 1; Return a + b; Return main(a,b); Return True; EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None)], ([], [Return(IntLiteral(1)), Return(BinaryOp('+', Id('a'), Id('b'))), Return(CallExpr(Id('main'), [Id('a'), Id('b')])), Return(BooleanLiteral(True))]))])
        expect = str(TypeMismatchInStatement(Return(BooleanLiteral(True))))
        self.assertTrue(TestChecker.test(input,expect,455))
    def test_number_56(self):
        """Funcall in expression"""
        raw_input= """Function: main Parameter: a,b Body: a = f1() + 5; b = "strin"; b= main(a,b); Return {1}; EndBody. Function: f1 Body: Return 0x12; EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None)], ([], [Assign(Id('a'), BinaryOp('+', CallExpr(Id('f1'), []), IntLiteral(5))), Assign(Id('b'), StringLiteral('strin')), Assign(Id('b'), CallExpr(Id('main'), [Id('a'), Id('b')])), Return(ArrayLiteral([IntLiteral(1)]))])), FuncDecl(Id('f1'), [], ([], [Return(IntLiteral(18))]))])
        expect = str(TypeMismatchInStatement(Return(ArrayLiteral([IntLiteral(1)]))))
        self.assertTrue(TestChecker.test(input,expect,456))
    def test_number_57(self):
        """Funcall in funcall?"""
        raw_input= """Function: main Parameter: x Body: x = main(main(main(main(5)))); Return; EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('x'), [], None)], ([], [Assign(Id('x'), CallExpr(Id('main'), [CallExpr(Id('main'), [CallExpr(Id('main'), [CallExpr(Id('main'), [IntLiteral(5)])])])])), Return(None)]))])
        expect = str(TypeMismatchInStatement(Return(None)))
        self.assertTrue(TestChecker.test(input,expect,457))
    def test_number_58(self):
        """Funcall and expression"""
        raw_input= """Function: main Parameter: x Body: x = main(x) =/= main(5); EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('x'), [], None)], ([], [Assign(Id('x'), BinaryOp('=/=', CallExpr(Id('main'), [Id('x')]), CallExpr(Id('main'), [IntLiteral(5)])))]))])
        expect = str(TypeCannotBeInferred(Assign(Id('x'), BinaryOp('=/=', CallExpr(Id('main'), [Id('x')]), CallExpr(Id('main'), [IntLiteral(5)])))))
        self.assertTrue(TestChecker.test(input,expect,458))
    def test_number_59(self):
        """self infer"""
        raw_input= """Function: main Parameter: x Body: Return main(x+5) > main(0o45); Return; EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('x'), [], None)], ([], [Return(BinaryOp('>', CallExpr(Id('main'), [BinaryOp('+', Id('x'), IntLiteral(5))]), CallExpr(Id('main'), [IntLiteral(37)]))), Return(None)]))])
        expect = str(TypeMismatchInStatement(Return(BinaryOp('>', CallExpr(Id('main'), [BinaryOp('+', Id('x'), IntLiteral(5))]), CallExpr(Id('main'), [IntLiteral(37)])))))
        self.assertTrue(TestChecker.test(input,expect,459))
    def test_number_60(self):
        """Funcall and expression"""
        raw_input= """Function: main Parameter: x Body: x = main(6.5) =/= main(x); EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('x'), [], None)], ([], [Assign(Id('x'), BinaryOp('=/=', CallExpr(Id('main'), [FloatLiteral(6.5)]), CallExpr(Id('main'), [Id('x')])))]))])
        expect = str(TypeMismatchInStatement(Assign(Id('x'), BinaryOp('=/=', CallExpr(Id('main'), [FloatLiteral(6.5)]), CallExpr(Id('main'), [Id('x')])))))
        self.assertTrue(TestChecker.test(input,expect,460))
    def test_number_61(self):
        """composite var assignment"""
        raw_input= """Function: main Parameter: a,b Body: a[5] = 2; EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None)], ([], [Assign(ArrayCell(Id('a'), [IntLiteral(5)]), IntLiteral(2))]))])
        expect = str(TypeMismatchInExpression(ArrayCell(Id('a'), [IntLiteral(5)])))
        self.assertTrue(TestChecker.test(input,expect,461))
    def test_number_62(self):
        """composite var assignment"""
        raw_input= """Function: main Body: Var: a={{1,2},{3,4}}; a[1][2] = 6; a[2][1] = 1.2; EndBody."""
        input = Program([FuncDecl(Id('main'), [], ([VarDecl(Id('a'), [], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(3), IntLiteral(4)])]))], [Assign(ArrayCell(Id('a'), [IntLiteral(1), IntLiteral(2)]), IntLiteral(6)), Assign(ArrayCell(Id('a'), [IntLiteral(2), IntLiteral(1)]), FloatLiteral(1.2))]))])
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id('a'), [IntLiteral(2), IntLiteral(1)]), FloatLiteral(1.2))))
        self.assertTrue(TestChecker.test(input,expect,462))
    def test_number_63(self):
        """nested funcall in call stmt"""
        raw_input= """Function: main Parameter: a,b Body: main(main(2,3),5);  EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None)], ([], [CallStmt(Id('main'), [CallExpr(Id('main'), [IntLiteral(2), IntLiteral(3)]), IntLiteral(5)])]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id('main'), [CallExpr(Id('main'), [IntLiteral(2), IntLiteral(3)]), IntLiteral(5)])))
        self.assertTrue(TestChecker.test(input,expect,463))
    def test_number_64(self):
        """nested funcall in callstmt"""
        raw_input= """Function: main Parameter: a Body: main(main(2.5));  EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('a'), [], None)], ([], [CallStmt(Id('main'), [CallExpr(Id('main'), [FloatLiteral(2.5)])])]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id('main'), [CallExpr(Id('main'), [FloatLiteral(2.5)])])))
        self.assertTrue(TestChecker.test(input,expect,464))
    def test_number_65(self):
        """nested funcall 2"""
        raw_input= """Function: f Parameter: x Body:  x = 5; Return float_to_int(x); EndBody. Function: main Parameter: x Body: Return f(main(f(main(2.5))));  EndBody. Function: test Parameter: x Body: x = f(main(x)) - x; EndBody."""
        input = Program([FuncDecl(Id('f'), [VarDecl(Id('x'), [], None)], ([], [Assign(Id('x'), IntLiteral(5)), Return(CallExpr(Id('float_to_int'), [Id('x')]))])), FuncDecl(Id('main'), [VarDecl(Id('x'), [], None)], ([], [Return(CallExpr(Id('f'), [CallExpr(Id('main'), [CallExpr(Id('f'), [CallExpr(Id('main'), [FloatLiteral(2.5)])])])]))])), FuncDecl(Id('test'), [VarDecl(Id('x'), [], None)], ([], [Assign(Id('x'), BinaryOp('-', CallExpr(Id('f'), [CallExpr(Id('main'), [Id('x')])]), Id('x')))]))])
        expect = str(TypeMismatchInStatement(Return(CallExpr(Id('f'), [CallExpr(Id('main'), [CallExpr(Id('f'), [CallExpr(Id('main'), [FloatLiteral(2.5)])])])]))))
        self.assertTrue(TestChecker.test(input,expect,465))
    def test_number_66(self):
        """funcall -> infer -> func decl -> use param"""
        raw_input= """Function: main Body: f1(2,2.4); EndBody. Function: f1 Parameter: a,b Body: f1(a,b); Return; a= b-.5.5; EndBody."""
        input = Program([FuncDecl(Id('main'), [], ([], [CallStmt(Id('f1'), [IntLiteral(2), FloatLiteral(2.4)])])), FuncDecl(Id('f1'), [VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None)], ([], [CallStmt(Id('f1'), [Id('a'), Id('b')]), Return(None), Assign(Id('a'), BinaryOp('-.', Id('b'), FloatLiteral(5.5)))]))])
        expect = str(TypeMismatchInStatement(Assign(Id('a'), BinaryOp('-.', Id('b'), FloatLiteral(5.5)))))
        self.assertTrue(TestChecker.test(input,expect,466))
    def test_number_67(self):
        """do while infer in do and wrong in expr"""
        raw_input= """Function: main Parameter: a,b Body: Do a = 5; While a EndDo. EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None)], ([], [Dowhile(([], [Assign(Id('a'), IntLiteral(5))]), Id('a'))]))])
        expect = str(TypeMismatchInStatement(Dowhile(([], [Assign(Id('a'), IntLiteral(5))]), Id('a'))))
        self.assertTrue(TestChecker.test(input,expect,467))
    def test_number_68(self):
        """while infer in expr and wrong in do"""
        raw_input= """Function: main Parameter: a,b Body: While a Do a = 5; EndWhile.  EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None)], ([], [While(Id('a'), ([], [Assign(Id('a'), IntLiteral(5))]))]))])
        expect = str(TypeMismatchInStatement(Assign(Id('a'), IntLiteral(5))))
        self.assertTrue(TestChecker.test(input,expect,468))
    def test_number_69(self):
        """for wrong init value"""
        raw_input= """Function: main Parameter: a,b Body: For ( a = 1.2, a > b, 5) Do Return; EndFor. EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None)], ([], [For(Id('a'), FloatLiteral(1.2), BinaryOp('>', Id('a'), Id('b')), IntLiteral(5), ([], [Return(None)]))]))])
        expect = str(TypeMismatchInStatement(For(Id('a'), FloatLiteral(1.2), BinaryOp('>', Id('a'), Id('b')), IntLiteral(5), ([], [Return(None)]))))
        self.assertTrue(TestChecker.test(input,expect,469))
    def test_number_70(self):
        """for init infer"""
        raw_input= """Function: main Parameter: a,b Body: For (a = 5, a>0, -1) Do Continue; EndFor. b = !a; EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None)], ([], [For(Id('a'), IntLiteral(5), BinaryOp('>', Id('a'), IntLiteral(0)), UnaryOp('-', IntLiteral(1)), ([], [Continue()])), Assign(Id('b'), UnaryOp('!', Id('a')))]))])
        expect = str(TypeMismatchInExpression(UnaryOp('!', Id('a'))))
        self.assertTrue(TestChecker.test(input,expect,470))
    def test_number_71(self):
        """for init variable is already infered as another type"""
        raw_input= """Function: main Body: Var: a = "String"; For ( a = 1, 5 == 6, 0x12) Do Return; EndFor. EndBody."""
        input = Program([FuncDecl(Id('main'), [], ([VarDecl(Id('a'), [], StringLiteral('String'))], [For(Id('a'), IntLiteral(1), BinaryOp('==', IntLiteral(5), IntLiteral(6)), IntLiteral(18), ([], [Return(None)]))]))])
        expect = str(TypeMismatchInStatement(For(Id('a'), IntLiteral(1), BinaryOp('==', IntLiteral(5), IntLiteral(6)), IntLiteral(18), ([], [Return(None)]))))
        self.assertTrue(TestChecker.test(input,expect,471))
    def test_number_72(self):
        """for wrong condition"""
        raw_input= """Function: main Body: Var: a ; For (a = 1, a , 1) Do EndFor. EndBody."""
        input = Program([FuncDecl(Id('main'), [], ([VarDecl(Id('a'), [], None)], [For(Id('a'), IntLiteral(1), Id('a'), IntLiteral(1), ([], []))]))])
        expect = str(TypeMismatchInStatement(For(Id('a'), IntLiteral(1), Id('a'), IntLiteral(1), ([], []))))
        self.assertTrue(TestChecker.test(input,expect,472))
    def test_number_73(self):
        """func in array cell index"""
        raw_input= """Function: main Body: Var: arr = {1,3,2}; Return arr[main()]; EndBody. Function: test Body: main(); EndBody."""
        input = Program([FuncDecl(Id('main'), [], ([VarDecl(Id('arr'), [], ArrayLiteral([IntLiteral(1), IntLiteral(3), IntLiteral(2)]))], [Return(ArrayCell(Id('arr'), [CallExpr(Id('main'), [])]))])), FuncDecl(Id('test'), [], ([], [CallStmt(Id('main'), [])]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id('main'), [])))
        self.assertTrue(TestChecker.test(input,expect,473))
    def test_number_74(self):
        """infer variable in array cell index"""
        raw_input= """Function: main Parameter: a,b Body: Var: arr = {{1,2,3},{4,5,6}};  arr[1][2] = arr[a][int_of_float(b)] + arr[5][a*b]; EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None)], ([VarDecl(Id('arr'), [], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3)]), ArrayLiteral([IntLiteral(4), IntLiteral(5), IntLiteral(6)])]))], [Assign(ArrayCell(Id('arr'), [IntLiteral(1), IntLiteral(2)]), BinaryOp('+', ArrayCell(Id('arr'), [Id('a'), CallExpr(Id('int_of_float'), [Id('b')])]), ArrayCell(Id('arr'), [IntLiteral(5), BinaryOp('*', Id('a'), Id('b'))])))]))])
        expect = str(TypeMismatchInExpression(BinaryOp('*', Id('a'), Id('b'))))
        self.assertTrue(TestChecker.test(input,expect,474))
    def test_number_75(self):
        """return arraycell"""
        raw_input= """Var: arr = {{{1.2},{5e3}},{{0.5},{3e-6}}}; Function: main Parameter: a,b Body: Return arr[2][3][1]; EndBody. Function: test Body: Return 5 == main(1,2); EndBody."""
        input = Program([VarDecl(Id('arr'), [], ArrayLiteral([ArrayLiteral([ArrayLiteral([FloatLiteral(1.2)]), ArrayLiteral([FloatLiteral(5000.0)])]), ArrayLiteral([ArrayLiteral([FloatLiteral(0.5)]), ArrayLiteral([FloatLiteral(3e-06)])])])), FuncDecl(Id('main'), [VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None)], ([], [Return(ArrayCell(Id('arr'), [IntLiteral(2), IntLiteral(3), IntLiteral(1)]))])), FuncDecl(Id('test'), [], ([], [Return(BinaryOp('==', IntLiteral(5), CallExpr(Id('main'), [IntLiteral(1), IntLiteral(2)])))]))])
        expect = str(TypeMismatchInExpression(BinaryOp('==', IntLiteral(5), CallExpr(Id('main'), [IntLiteral(1), IntLiteral(2)]))))
        self.assertTrue(TestChecker.test(input,expect,475))
    def test_number_76(self):
        """both var infer and func infer in array cell"""
        raw_input= """Function: main Parameter: x Body: Var: arr = {{"a","b","c"},{"d","e","f"}}; arr[x][main(x)] = ""; Return arr[2][x+1]; EndBody."""
        input =  Program([FuncDecl(Id('main'), [VarDecl(Id('x'), [], None)], ([VarDecl(Id('arr'), [], ArrayLiteral([ArrayLiteral([StringLiteral('a'), StringLiteral('b'), StringLiteral('c')]), ArrayLiteral([StringLiteral('d'), StringLiteral('e'), StringLiteral('f')])]))], [Assign(ArrayCell(Id('arr'), [Id('x'), CallExpr(Id('main'), [Id('x')])]), StringLiteral('')), Return(ArrayCell(Id('arr'), [IntLiteral(2), BinaryOp('+', Id('x'), IntLiteral(1))]))]))])
        expect = str(TypeMismatchInStatement(Return(ArrayCell(Id('arr'), [IntLiteral(2), BinaryOp('+', Id('x'), IntLiteral(1))]))))
        self.assertTrue(TestChecker.test(input,expect,476))
    def test_number_77(self):
        """Arraycell in while"""
        raw_input= """Function: main Body: Var: a = {True,False,True}; While a[2] Do Return a[3] == a[5]; EndWhile. EndBody."""
        input = Program([FuncDecl(Id('main'), [], ([VarDecl(Id('a'), [], ArrayLiteral([BooleanLiteral(True), BooleanLiteral(False), BooleanLiteral(True)]))], [While(ArrayCell(Id('a'), [IntLiteral(2)]), ([], [Return(BinaryOp('==', ArrayCell(Id('a'), [IntLiteral(3)]), ArrayCell(Id('a'), [IntLiteral(5)])))]))]))])
        expect = str(TypeMismatchInExpression(BinaryOp('==', ArrayCell(Id('a'), [IntLiteral(3)]), ArrayCell(Id('a'), [IntLiteral(5)]))))
        self.assertTrue(TestChecker.test(input,expect,477))
    def test_number_78(self):
        """Arratcell in for """
        raw_input= """Function: main Body: Var: a = {1,2,3,4,5}, b; For ( b = a[2], a[3] > a[4], a[6]) Do If a Then Return; EndIf. EndFor. EndBody."""
        input = Program([FuncDecl(Id('main'), [], ([VarDecl(Id('a'), [], ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3), IntLiteral(4), IntLiteral(5)])), VarDecl(Id('b'), [], None)], [For(Id('b'), ArrayCell(Id('a'), [IntLiteral(2)]), BinaryOp('>', ArrayCell(Id('a'), [IntLiteral(3)]), ArrayCell(Id('a'), [IntLiteral(4)])), ArrayCell(Id('a'), [IntLiteral(6)]), ([], [If([[Id('a'), [], [Return(None)]]], ([], []))]))]))])
        expect = str(TypeMismatchInStatement(If([[Id('a'), [], [Return(None)]]], ([], []))))
        self.assertTrue(TestChecker.test(input,expect,478))
    def test_number_79(self):
        """Lots of predefined functions"""
        raw_input= """Function: main Body: Var:a, i=5, arr = {"1","2","3"}; For (i = int_of_string(arr[5]), float_of_string("12") <. float_to_int(i), a) Do a = i; arr[2] = arr[3];  print(read()); arr[5] = read();  printStrLn(a); EndFor. EndBody."""
        input = Program([FuncDecl(Id('main'), [], ([VarDecl(Id('a'), [], None), VarDecl(Id('i'), [], IntLiteral(5)), VarDecl(Id('arr'), [], ArrayLiteral([StringLiteral('1'), StringLiteral('2'), StringLiteral('3')]))], [For(Id('i'), CallExpr(Id('int_of_string'), [ArrayCell(Id('arr'), [IntLiteral(5)])]), BinaryOp('<.', CallExpr(Id('float_of_string'), [StringLiteral('12')]), CallExpr(Id('float_to_int'), [Id('i')])), Id('a'), ([], [Assign(Id('a'), Id('i')), Assign(ArrayCell(Id('arr'), [IntLiteral(2)]), ArrayCell(Id('arr'), [IntLiteral(3)])), CallStmt(Id('print'), [CallExpr(Id('read'), [])]), Assign(ArrayCell(Id('arr'), [IntLiteral(5)]), CallExpr(Id('read'), [])), CallStmt(Id('printStrLn'), [Id('a')])]))]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id('printStrLn'), [Id('a')])))
        self.assertTrue(TestChecker.test(input,expect,479))
    def test_number_80(self):
        """func id instead of var id in assignment"""
        raw_input= """Function: f1 Parameter: x Body: Return 76; EndBody. Function: main Body: f1 = 5; EndBody."""
        input = Program([FuncDecl(Id('f1'), [VarDecl(Id('x'), [], None)], ([], [Return(IntLiteral(76))])), FuncDecl(Id('main'), [], ([], [Assign(Id('f1'), IntLiteral(5))]))])
        expect = str(Undeclared(Identifier(), 'f1'))
        self.assertTrue(TestChecker.test(input,expect,480))
    def test_number_81(self):
        """func id instead of var id in argument"""
        raw_input= """Function: main Parameter: a,b Body: main(main,5); EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None)], ([], [CallStmt(Id('main'), [Id('main'), IntLiteral(5)])]))])
        expect = str(Undeclared(Identifier(), 'main'))
        self.assertTrue(TestChecker.test(input,expect,481))
    def test_number_82(self):
        """just func id in array index"""
        raw_input= """Function: main Body: Var: arr = {6,5}; a[main] = 5; EndBody."""
        input = Program([FuncDecl(Id('main'), [], ([VarDecl(Id('arr'), [], ArrayLiteral([IntLiteral(6), IntLiteral(5)]))], [Assign(ArrayCell(Id('a'), [Id('main')]), IntLiteral(5))]))])
        expect = str(Undeclared(Identifier(), 'a'))
        self.assertTrue(TestChecker.test(input,expect,482))
    def test_number_83(self):
        """wrong arg num in call expr"""
        raw_input= """Function: main Parameter: x Body: Var: a,b,c; x = a + b == int_of_string(main()); EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('x'), [], None)], ([VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None), VarDecl(Id('c'), [], None)], [Assign(Id('x'), BinaryOp('==', BinaryOp('+', Id('a'), Id('b')), CallExpr(Id('int_of_string'), [CallExpr(Id('main'), [])])))]))])
        expect = str(TypeMismatchInExpression(CallExpr(Id('main'), [])))
        self.assertTrue(TestChecker.test(input,expect,483))
    def test_number_84(self):
        """cant infer if"""
        raw_input= """Function: main Parameter: a,b Body: If main(b,5) Then EndIf. EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None)], ([], [If([[CallExpr(Id('main'), [Id('b'), IntLiteral(5)]), [], []]], ([], []))]))])
        expect = str(TypeCannotBeInferred(If([[CallExpr(Id('main'), [Id('b'), IntLiteral(5)]), [], []]], ([], []))))
        self.assertTrue(TestChecker.test(input,expect,484))
    def test_number_85(self):
        """cant infer for"""
        raw_input= """Function: main Parameter: a,b Body: For (a=5, a> main(a,b), a) Do EndFor. EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None)], ([], [For(Id('a'), IntLiteral(5), BinaryOp('>', Id('a'), CallExpr(Id('main'), [Id('a'), Id('b')])), Id('a'), ([], []))]))])
        expect = str(TypeCannotBeInferred(For(Id('a'), IntLiteral(5), BinaryOp('>', Id('a'), CallExpr(Id('main'), [Id('a'), Id('b')])), Id('a'), ([], []))))
        self.assertTrue(TestChecker.test(input,expect,485))
    def test_number_86(self):
        """cant infer while"""
        raw_input= """Function: main Parameter: a,b Body: While main(b,x) > a Do EndWhile. EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None)], ([], [While(BinaryOp('>', CallExpr(Id('main'), [Id('b'), Id('x')]), Id('a')), ([], []))]))])
        expect = str(TypeCannotBeInferred(While(BinaryOp('>', CallExpr(Id('main'), [Id('b'), Id('x')]), Id('a')), ([], []))))
        self.assertTrue(TestChecker.test(input,expect,486))
    def test_number_87(self):
        """infering a variable to void type"""
        raw_input= """Function: main Parameter: x Body: x = printLn(); EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('x'), [], None)], ([], [Assign(Id('x'), CallExpr(Id('printLn'), []))]))])
        expect = str(TypeMismatchInStatement(Assign(Id('x'), CallExpr(Id('printLn'), []))))
        self.assertTrue(TestChecker.test(input,expect,487))
    def test_number_88(self):
        """void type func in expression"""
        raw_input= """Function: main Parameter: x Body: x = bool_of_string("") || printStrLn(string_of_bool(1>2)); EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('x'), [], None)], ([], [Assign(Id('x'), BinaryOp('||', CallExpr(Id('bool_of_string'), [StringLiteral('')]), CallExpr(Id('printStrLn'), [CallExpr(Id('string_of_bool'), [BinaryOp('>', IntLiteral(1), IntLiteral(2))])])))]))])
        expect = str(TypeMismatchInExpression(BinaryOp('||', CallExpr(Id('bool_of_string'), [StringLiteral('')]), CallExpr(Id('printStrLn'), [CallExpr(Id('string_of_bool'), [BinaryOp('>', IntLiteral(1), IntLiteral(2))])]))))
        self.assertTrue(TestChecker.test(input,expect,488))
    def test_number_89(self):
        """some empty statement structures"""
        raw_input= """Var: a,b,c; Function: main Body: EndBody. Function: nani Body: If True Then ElseIf False Then Else EndIf. For (a=a,a>c,b) Do EndFor.  Return nani(); EndBody."""
        input = Program([VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None), VarDecl(Id('c'), [], None), FuncDecl(Id('main'), [], ([], [])), FuncDecl(Id('nani'), [], ([], [If([[BooleanLiteral(True), [], []], [BooleanLiteral(False), [], []]], ([], [])), For(Id('a'), Id('a'), BinaryOp('>', Id('a'), Id('c')), Id('b'), ([], [])), Return(CallExpr(Id('nani'), []))]))])
        expect = str(TypeCannotBeInferred(Return(CallExpr(Id('nani'), []))))
        self.assertTrue(TestChecker.test(input,expect,489))
    def test_number_90(self):
        """some empty statement structures"""
        raw_input= """Function: main Body: While main() Do EndWhile. Do While  1>2 EndDo. Return; EndBody."""
        input = Program([FuncDecl(Id('main'), [], ([], [While(CallExpr(Id('main'), []), ([], [])), Dowhile(([], []), BinaryOp('>', IntLiteral(1), IntLiteral(2))), Return(None)]))])
        expect = str(TypeMismatchInStatement(Return(None)))
        self.assertTrue(TestChecker.test(input,expect,490))
    def test_number_91(self):
        """for with x=y and both are inffered """
        raw_input= """Function: main Parameter: a,b Body: For (a=b, 1>2, 3) Do main(1,1.4); EndFor. EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None)], ([], [For(Id('a'), Id('b'), BinaryOp('>', IntLiteral(1), IntLiteral(2)), IntLiteral(3), ([], [CallStmt(Id('main'), [IntLiteral(1), FloatLiteral(1.4)])]))]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id('main'), [IntLiteral(1), FloatLiteral(1.4)])))
        self.assertTrue(TestChecker.test(input,expect,491))
    def test_number_92(self):
        """separate scope decls in if"""
        raw_input= """Function: main Parameter: a,b,c Body: Var: d,e,f; If a > 5 Then Var: a = 1.2; ElseIf a<6 Then Var: a= "asfd"; Else a = True; EndIf. EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None), VarDecl(Id('c'), [], None)], ([VarDecl(Id('d'), [], None), VarDecl(Id('e'), [], None), VarDecl(Id('f'), [], None)], [If([[BinaryOp('>', Id('a'), IntLiteral(5)), [VarDecl(Id('a'), [], FloatLiteral(1.2))], []], [BinaryOp('<', Id('a'), IntLiteral(6)), [VarDecl(Id('a'), [], StringLiteral('asfd'))], []]], ([], [Assign(Id('a'), BooleanLiteral(True))]))]))])
        expect = str(TypeMismatchInStatement(Assign(Id('a'), BooleanLiteral(True))))
        self.assertTrue(TestChecker.test(input,expect,492))
    def test_number_93(self):
        """init var in for loop is outside or inside"""
        raw_input= """Function: main Parameter: x Body: For ( x = 5 , True, x) Do Var: x=1.2; Return x; EndFor. x=main(x); EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('x'), [], None)], ([], [For(Id('x'), IntLiteral(5), BooleanLiteral(True), Id('x'), ([VarDecl(Id('x'), [], FloatLiteral(1.2))], [Return(Id('x'))])), Assign(Id('x'), CallExpr(Id('main'), [Id('x')]))]))])
        expect = str(TypeMismatchInStatement(Assign(Id('x'), CallExpr(Id('main'), [Id('x')]))))
        self.assertTrue(TestChecker.test(input,expect,493))
    def test_number_94(self):
        """call expr can infer in assign"""
        raw_input= """Function: main Parameter: x,y Body: y=5; y = main(x,y); EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('x'), [], None), VarDecl(Id('y'), [], None)], ([], [Assign(Id('y'), IntLiteral(5)), Assign(Id('y'), CallExpr(Id('main'), [Id('x'), Id('y')]))]))])
        expect = str(TypeCannotBeInferred(Assign(Id('y'), CallExpr(Id('main'), [Id('x'), Id('y')]))))
        self.assertTrue(TestChecker.test(input,expect,494))
    def test_number_95(self):
        """cant infer from array cell"""
        raw_input= """Function: main Parameter: x Body: Var: arr= {1,2,3}; Return arr[main(x)]; EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('x'), [], None)], ([VarDecl(Id('arr'), [], ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3)]))], [Return(ArrayCell(Id('arr'), [CallExpr(Id('main'), [Id('x')])]))]))])
        expect = str(TypeCannotBeInferred(Return(ArrayCell(Id('arr'), [CallExpr(Id('main'), [Id('x')])]))))
        self.assertTrue(TestChecker.test(input,expect,495))
    def test_number_96(self):
        """no entry"""
        raw_input= """Function: f1 Body: EndBody. Function: f2 Body: EndBody. Function: maini Body: EndBody."""
        input = Program([FuncDecl(Id('f1'), [], ([], [])), FuncDecl(Id('f2'), [], ([], [])), FuncDecl(Id('maini'), [], ([], []))])
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,496))
    def test_number_97(self):
        """funcall cant infer in a very inner expr"""
        raw_input= """Function: main Parameter: x Body: Var: a,b,c; x = a + b * (a-b * (a+b % c + 1 +(1+-main(x)))); EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('x'), [], None)], ([VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None), VarDecl(Id('c'), [], None)], [Assign(Id('x'), BinaryOp('+', Id('a'), BinaryOp('*', Id('b'), BinaryOp('-', Id('a'), BinaryOp('*', Id('b'), BinaryOp('+', BinaryOp('+', BinaryOp('+', Id('a'), BinaryOp('%', Id('b'), Id('c'))), IntLiteral(1)), BinaryOp('+', IntLiteral(1), UnaryOp('-', CallExpr(Id('main'), [Id('x')])))))))))]))])
        expect = str(TypeCannotBeInferred(Assign(Id('x'), BinaryOp('+', Id('a'), BinaryOp('*', Id('b'), BinaryOp('-', Id('a'), BinaryOp('*', Id('b'), BinaryOp('+', BinaryOp('+', BinaryOp('+', Id('a'), BinaryOp('%', Id('b'), Id('c'))), IntLiteral(1)), BinaryOp('+', IntLiteral(1), UnaryOp('-', CallExpr(Id('main'), [Id('x')])))))))))))
        self.assertTrue(TestChecker.test(input,expect,497))
    def test_number_98(self):
        """declare both func and var same name, use both"""
        raw_input= """Function: main Parameter: main Body: main = main(main + 5) * 2 * main; EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('main'), [], None)], ([], [Assign(Id('main'), BinaryOp('*', BinaryOp('*', CallExpr(Id('main'), [BinaryOp('+', Id('main'), IntLiteral(5))]), IntLiteral(2)), Id('main')))]))])
        expect = str(Undeclared(Function(), 'main'))
        self.assertTrue(TestChecker.test(input,expect,498))
    def test_number_99(self):
        """array unknown and inferred, error while assigning elem"""
        raw_input= """Function: main Body: Var: a[2][3],b[5][6][7],c[1];  a[1][2] = 5; a[3][4] = 1.2; EndBody."""
        input = Program([FuncDecl(Id('main'), [], ([VarDecl(Id('a'), [2, 3], None), VarDecl(Id('b'), [5, 6, 7], None), VarDecl(Id('c'), [1], None)], [Assign(ArrayCell(Id('a'), [IntLiteral(1), IntLiteral(2)]), IntLiteral(5)), Assign(ArrayCell(Id('a'), [IntLiteral(3), IntLiteral(4)]), FloatLiteral(1.2))]))])
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id('a'), [IntLiteral(3), IntLiteral(4)]), FloatLiteral(1.2))))
        self.assertTrue(TestChecker.test(input,expect,499))
    def test_number_100(self):
        """array infer, error while assigning whole array"""
        raw_input= """Function: main Body: Var: a[2][3]; a= {1}; EndBody."""
        input = Program([FuncDecl(Id('main'), [], ([VarDecl(Id('a'), [2, 3], None)], [Assign(Id('a'), ArrayLiteral([IntLiteral(1)]))]))])
        expect = str(TypeMismatchInStatement(Assign(Id('a'), ArrayLiteral([IntLiteral(1)]))))
        self.assertTrue(TestChecker.test(input,expect,500))
    def test_number_101(self):
        """cant infer array cell unkown type"""
        raw_input= """Function: main Body: Var: a, b[2][3]; a=b; EndBody."""
        input = Program([FuncDecl(Id('main'), [], ([VarDecl(Id('a'), [], None), VarDecl(Id('b'), [2, 3], None)], [Assign(Id('a'), Id('b'))]))])
        expect = str(TypeMismatchInStatement(Assign(Id('a'), Id('b'))))
        self.assertTrue(TestChecker.test(input,expect,501))
    def test_number_102(self):
        """cant infer func call on right side"""
        raw_input= """Function: main Parameter: x Body: Var: a = {1,2}; main(x)[2]= 5; EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('x'), [], None)], ([VarDecl(Id('a'), [], ArrayLiteral([IntLiteral(1), IntLiteral(2)]))], [Assign(ArrayCell(CallExpr(Id('main'), [Id('x')]), [IntLiteral(2)]), IntLiteral(5))]))])
        expect = str(TypeCannotBeInferred(Assign(ArrayCell(CallExpr(Id('main'), [Id('x')]), [IntLiteral(2)]), IntLiteral(5))))
        self.assertTrue(TestChecker.test(input,expect,502))
    def test_number_103(self):
        """array assignment"""
        raw_input= """Function: main Body: Var: a[3]; a = {1,2,3}; a= {4,5,6}; a={1,2,3,4,5}; EndBody."""
        input = Program([FuncDecl(Id('main'), [], ([VarDecl(Id('a'), [3], None)], [Assign(Id('a'), ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3)])), Assign(Id('a'), ArrayLiteral([IntLiteral(4), IntLiteral(5), IntLiteral(6)])), Assign(Id('a'), ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3), IntLiteral(4), IntLiteral(5)]))]))])
        expect = str(TypeMismatchInStatement(Assign(Id('a'), ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3), IntLiteral(4), IntLiteral(5)]))))
        self.assertTrue(TestChecker.test(input,expect,503))
    def test_number_104(self):
        """array elem cant infer to var"""
        raw_input= """Function: main Body: Var: a[3],b; a[2]=b; EndBody."""
        input = Program([FuncDecl(Id('main'), [], ([VarDecl(Id('a'), [3], None), VarDecl(Id('b'), [], None)], [Assign(ArrayCell(Id('a'), [IntLiteral(2)]), Id('b'))]))])
        expect = str(TypeCannotBeInferred(Assign(ArrayCell(Id('a'), [IntLiteral(2)]), Id('b'))))
        self.assertTrue(TestChecker.test(input,expect,504))
    def test_number_105(self):
        """Infer array elem"""
        raw_input= """Function: main Body: Var: a[3]; a[2] = "sti"; a[1] = 3; EndBody."""
        input = Program([FuncDecl(Id('main'), [], ([VarDecl(Id('a'), [3], None)], [Assign(ArrayCell(Id('a'), [IntLiteral(2)]), StringLiteral('sti')), Assign(ArrayCell(Id('a'), [IntLiteral(1)]), IntLiteral(3))]))])
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id('a'), [IntLiteral(1)]), IntLiteral(3))))
        self.assertTrue(TestChecker.test(input,expect,505))
    def test_number_106(self):
        """function cant infer because no return """
        raw_input= """Function: test Body: EndBody. Function: main Body: Return test(); EndBody."""
        input = Program([FuncDecl(Id('test'), [], ([], [])), FuncDecl(Id('main'), [], ([], [Return(CallExpr(Id('test'), []))]))])
        expect = str(TypeCannotBeInferred(Return(CallExpr(Id('test'), []))))
        self.assertTrue(TestChecker.test(input,expect,506))
    def test_number_107(self):
        """indexing non array element"""
        raw_input= """Var:a; Function: main Body: a[2][3] = 5; EndBody."""
        input = Program([VarDecl(Id('a'), [], None), FuncDecl(Id('main'), [], ([], [Assign(ArrayCell(Id('a'), [IntLiteral(2), IntLiteral(3)]), IntLiteral(5))]))])
        expect = str(TypeMismatchInExpression(ArrayCell(Id('a'), [IntLiteral(2), IntLiteral(3)])))
        self.assertTrue(TestChecker.test(input,expect,507))
    def test_number_108(self):
        """return unknown array type"""
        raw_input= """Var: a[3][4]; Function: main Body: Return  a; EndBody."""
        input = Program([VarDecl(Id('a'), [3, 4], None), FuncDecl(Id('main'), [], ([], [Return(Id('a'))]))])
        expect = str(TypeCannotBeInferred(Return(Id('a'))))
        self.assertTrue(TestChecker.test(input,expect,508))
    def test_number_109(self):
        """cant infer func return type in call expr"""
        raw_input= """Function: main Parameter: a Body: a =  1+ main(1); EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('a'), [], None)], ([], [Assign(Id('a'), BinaryOp('+', IntLiteral(1), CallExpr(Id('main'), [IntLiteral(1)])))]))])
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,509))
    def test_number_110(self):
        """call stmt with uninfered array"""
        raw_input= """Function: main Parameter: x Body: Var: arr[2][3]; main(arr); EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('x'), [], None)], ([VarDecl(Id('arr'), [2, 3], None)], [CallStmt(Id('main'), [Id('arr')])]))])
        expect = str(TypeCannotBeInferred(CallStmt(Id('main'), [Id('arr')])))
        self.assertTrue(TestChecker.test(input,expect,510))
    def test_number_111(self):
        """assigning non arrray to array with init dim"""
        raw_input= """Function: main Body: Var: arr[3]; arr = 5; EndBody."""
        input =  Program([FuncDecl(Id('main'), [], ([VarDecl(Id('arr'), [3], None)], [Assign(Id('arr'), IntLiteral(5))]))])
        expect = str(TypeMismatchInStatement(Assign(Id('arr'), IntLiteral(5))))
        self.assertTrue(TestChecker.test(input,expect,511))
    def test_number_112(self):
        """function param infered into array"""
        raw_input= """Function: main Parameter: x Body: Var: arr[3] = {1,2,3},b,a; b = a + main(arr); Return arr; EndBody. """
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('x'), [], None)], ([VarDecl(Id('arr'), [3], ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3)])), VarDecl(Id('b'), [], None), VarDecl(Id('a'), [], None)], [Assign(Id('b'), BinaryOp('+', Id('a'), CallExpr(Id('main'), [Id('arr')]))), Return(Id('arr'))]))])
        expect = str(TypeMismatchInExpression(CallExpr(Id('main'), [Id('arr')])))
        self.assertTrue(TestChecker.test(input,expect,512))
    def test_number_113(self):
        """call expr  with array unkown"""
        raw_input= """Function: main Parameter: x Body: Var: arr[1],b; b = main(arr) + 2; EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('x'), [], None)], ([VarDecl(Id('arr'), [1], None), VarDecl(Id('b'), [], None)], [Assign(Id('b'), BinaryOp('+', CallExpr(Id('main'), [Id('arr')]), IntLiteral(2)))]))])
        expect = str(TypeMismatchInExpression(CallExpr(Id('main'), [Id('arr')])))
        self.assertTrue(TestChecker.test(input,expect,513))
    def test_number_114(self):
        """infer init dim array"""
        raw_input= """Function: main Body: Var: arr[3]; arr = {1.2,2.2,3.3}; arr = {1.2,2.2}; EndBody."""
        input = Program([FuncDecl(Id('main'), [], ([VarDecl(Id('arr'), [3], None)], [Assign(Id('arr'), ArrayLiteral([FloatLiteral(1.2), FloatLiteral(2.2), FloatLiteral(3.3)])), Assign(Id('arr'), ArrayLiteral([FloatLiteral(1.2), FloatLiteral(2.2)]))]))])
        expect = str(TypeMismatchInStatement(Assign(Id('arr'), ArrayLiteral([FloatLiteral(1.2), FloatLiteral(2.2)]))))
        self.assertTrue(TestChecker.test(input,expect,514))
    def test_number_115(self):
        """composite function param infer in call stmt"""
        raw_input= """Function: main Parameter: a[3] Body: main({1,2,3}); main({4,5,6}); main({1}); EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('a'), [3], None)], ([], [CallStmt(Id('main'), [ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3)])]), CallStmt(Id('main'), [ArrayLiteral([IntLiteral(4), IntLiteral(5), IntLiteral(6)])]), CallStmt(Id('main'), [ArrayLiteral([IntLiteral(1)])])]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id('main'), [ArrayLiteral([IntLiteral(1)])])))
        self.assertTrue(TestChecker.test(input,expect,515))
    def test_number_116(self):
        """composite function param infer mismatch"""
        raw_input= """Function: main Parameter: a[3] Body: main(2); EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('a'), [3], None)], ([], [CallStmt(Id('main'), [IntLiteral(2)])]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id('main'), [IntLiteral(2)])))
        self.assertTrue(TestChecker.test(input,expect,516))
    def test_number_117(self):
        """composite function param infer in assignment"""
        raw_input= """Function: main Parameter: a[2] Body: a={5,6}; Return main(a); EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('a'), [2], None)], ([], [Assign(Id('a'), ArrayLiteral([IntLiteral(5), IntLiteral(6)])), Return(CallExpr(Id('main'), [Id('a')]))]))])
        expect = str(TypeCannotBeInferred(Return(CallExpr(Id('main'), [Id('a')]))))
        self.assertTrue(TestChecker.test(input,expect,517))
    def test_number_118(self):
        """composite function param infer in call expr"""
        raw_input= """Function: main Parameter: a[3],b Body: b = a[2] + b; main({1,2,3},5); main({1,5},2); EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('a'), [3], None), VarDecl(Id('b'), [], None)], ([], [Assign(Id('b'), BinaryOp('+', ArrayCell(Id('a'), [IntLiteral(2)]), Id('b'))), CallStmt(Id('main'), [ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3)]), IntLiteral(5)]), CallStmt(Id('main'), [ArrayLiteral([IntLiteral(1), IntLiteral(5)]), IntLiteral(2)])]))])
        expect = str( TypeMismatchInStatement(CallStmt(Id('main'), [ArrayLiteral([IntLiteral(1), IntLiteral(5)]), IntLiteral(2)])))
        self.assertTrue(TestChecker.test(input,expect,518))
    def test_number_119(self):
        """many composite function params"""
        raw_input= """Function: main Parameter: a[2],b[1],c[3] Body: Var: x[2],y[1],z[3]; x={1,2}; y = main(x,{1}, {2,3,4}) ; y = main(x,c,{4,5,6}); c = y; EndBody.  """
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('a'), [2], None), VarDecl(Id('b'), [1], None), VarDecl(Id('c'), [3], None)], ([VarDecl(Id('x'), [2], None), VarDecl(Id('y'), [1], None), VarDecl(Id('z'), [3], None)], [Assign(Id('x'), ArrayLiteral([IntLiteral(1), IntLiteral(2)])), Assign(Id('y'), CallExpr(Id('main'), [Id('x'), ArrayLiteral([IntLiteral(1)]), ArrayLiteral([IntLiteral(2), IntLiteral(3), IntLiteral(4)])])), Assign(Id('y'), CallExpr(Id('main'), [Id('x'), Id('c'), ArrayLiteral([IntLiteral(4), IntLiteral(5), IntLiteral(6)])])), Assign(Id('c'), Id('y'))]))])
        expect = str(TypeCannotBeInferred(Assign(Id('y'), CallExpr(Id('main'), [Id('x'), ArrayLiteral([IntLiteral(1)]), ArrayLiteral([IntLiteral(2), IntLiteral(3), IntLiteral(4)])]))))
        self.assertTrue(TestChecker.test(input,expect,519))
    def test_number_120(self):
        """many composite function params update"""
        raw_input= """Function: main Parameter: a[2],b[1],c[3] Body: Var: x[2],y[1],z[3]; x={1,2}; y[2] = 5;  y = main(x,{1}, {2,3,4}) ; y = main(x,c,{4,5,6}); c = y; EndBody.  """
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('a'), [2], None), VarDecl(Id('b'), [1], None), VarDecl(Id('c'), [3], None)], ([VarDecl(Id('x'), [2], None), VarDecl(Id('y'), [1], None), VarDecl(Id('z'), [3], None)], [Assign(Id('x'), ArrayLiteral([IntLiteral(1), IntLiteral(2)])), Assign(ArrayCell(Id('y'), [IntLiteral(2)]), IntLiteral(5)), Assign(Id('y'), CallExpr(Id('main'), [Id('x'), ArrayLiteral([IntLiteral(1)]), ArrayLiteral([IntLiteral(2), IntLiteral(3), IntLiteral(4)])])), Assign(Id('y'), CallExpr(Id('main'), [Id('x'), Id('c'), ArrayLiteral([IntLiteral(4), IntLiteral(5), IntLiteral(6)])])), Assign(Id('c'), Id('y'))]))])
        expect = str(TypeMismatchInExpression(CallExpr(Id('main'), [Id('x'), Id('c'), ArrayLiteral([IntLiteral(4), IntLiteral(5), IntLiteral(6)])])))
        self.assertTrue(TestChecker.test(input,expect,520))
    def test_number_121(self):
        """many composite function params update 3"""
        raw_input= """Function: main Parameter: a[2],b[1],c[3] Body: Var: x[2],y[1],z[1]; x={1,2}; y[2] = 5;  y = main(x,{1}, {2,3,4}) ; y = main(x,z,{4,5,6}); c = y; EndBody.  """
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('a'), [2], None), VarDecl(Id('b'), [1], None), VarDecl(Id('c'), [3], None)], ([VarDecl(Id('x'), [2], None), VarDecl(Id('y'), [1], None), VarDecl(Id('z'), [1], None)], [Assign(Id('x'), ArrayLiteral([IntLiteral(1), IntLiteral(2)])), Assign(ArrayCell(Id('y'), [IntLiteral(2)]), IntLiteral(5)), Assign(Id('y'), CallExpr(Id('main'), [Id('x'), ArrayLiteral([IntLiteral(1)]), ArrayLiteral([IntLiteral(2), IntLiteral(3), IntLiteral(4)])])), Assign(Id('y'), CallExpr(Id('main'), [Id('x'), Id('z'), ArrayLiteral([IntLiteral(4), IntLiteral(5), IntLiteral(6)])])), Assign(Id('c'), Id('y'))]))])
        expect = str(TypeMismatchInStatement(Assign(Id('c'), Id('y'))))
        self.assertTrue(TestChecker.test(input,expect,521))
    def test_number_122(self):
        """many composite function params update 4"""
        raw_input= """Function: main Parameter: a[2],b[1],c[3] Body: Var: x[2],y[1],z[1]; x={1,2}; y[2] = 5;  y = main(x,{1}, {2,3,4}) ; y = main(x,z,{4,5,6}); z =x; EndBody.  """
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('a'), [2], None), VarDecl(Id('b'), [1], None), VarDecl(Id('c'), [3], None)], ([VarDecl(Id('x'), [2], None), VarDecl(Id('y'), [1], None), VarDecl(Id('z'), [1], None)], [Assign(Id('x'), ArrayLiteral([IntLiteral(1), IntLiteral(2)])), Assign(ArrayCell(Id('y'), [IntLiteral(2)]), IntLiteral(5)), Assign(Id('y'), CallExpr(Id('main'), [Id('x'), ArrayLiteral([IntLiteral(1)]), ArrayLiteral([IntLiteral(2), IntLiteral(3), IntLiteral(4)])])), Assign(Id('y'), CallExpr(Id('main'), [Id('x'), Id('z'), ArrayLiteral([IntLiteral(4), IntLiteral(5), IntLiteral(6)])])), Assign(Id('z'), Id('x'))]))])
        expect = str(TypeMismatchInStatement(Assign(Id('z'), Id('x'))))
        self.assertTrue(TestChecker.test(input,expect,522))
    def test_number_123(self):
        """function as array cell id"""
        raw_input= """Function: main Parameter: x Body: Var: a[2]; main(main(2))[2] = 5; EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('x'), [], None)], ([VarDecl(Id('a'), [2], None)], [Assign(ArrayCell(CallExpr(Id('main'), [CallExpr(Id('main'), [IntLiteral(2)])]), [IntLiteral(2)]), IntLiteral(5))]))])
        expect = str(TypeMismatchInExpression(ArrayCell(CallExpr(Id('main'), [CallExpr(Id('main'), [IntLiteral(2)])]), [IntLiteral(2)])))
        self.assertTrue(TestChecker.test(input,expect,523))
    def test_number_124(self):
        """function as array cell id"""
        raw_input= """Function: f Parameter: x Body: Return {1,2,3}; EndBody. Function: main Parameter: a[3] Body: Var: x; x = main(f(3)) + 6; main({1,2,3})[5] = f(6); EndBody."""
        input = Program([FuncDecl(Id('f'), [VarDecl(Id('x'), [], None)], ([], [Return(ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3)]))])), FuncDecl(Id('main'), [VarDecl(Id('a'), [3], None)], ([VarDecl(Id('x'), [], None)], [Assign(Id('x'), BinaryOp('+', CallExpr(Id('main'), [CallExpr(Id('f'), [IntLiteral(3)])]), IntLiteral(6))), Assign(ArrayCell(CallExpr(Id('main'), [ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3)])]), [IntLiteral(5)]), CallExpr(Id('f'), [IntLiteral(6)]))]))])
        expect = str(TypeMismatchInExpression(ArrayCell(CallExpr(Id('main'), [ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3)])]), [IntLiteral(5)])))
        self.assertTrue(TestChecker.test(input,expect,524))
    def test_number_125(self):
        """function as array cell id"""
        raw_input= """Function: f Parameter: x Body: Return {1,2,3}; EndBody. Function: main Parameter: x, y Body: x = f(2)[3]; y = f(6+f(f(x)[3])[7]); f(y+x)[3] = f(5); EndBody. """
        input = Program([FuncDecl(Id('f'), [VarDecl(Id('x'), [], None)], ([], [Return(ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3)]))])), FuncDecl(Id('main'), [VarDecl(Id('x'), [], None), VarDecl(Id('y'), [], None)], ([], [Assign(Id('x'), ArrayCell(CallExpr(Id('f'), [IntLiteral(2)]), [IntLiteral(3)])), Assign(Id('y'), CallExpr(Id('f'), [BinaryOp('+', IntLiteral(6), ArrayCell(CallExpr(Id('f'), [ArrayCell(CallExpr(Id('f'), [Id('x')]), [IntLiteral(3)])]), [IntLiteral(7)]))])), Assign(ArrayCell(CallExpr(Id('f'), [BinaryOp('+', Id('y'), Id('x'))]), [IntLiteral(3)]), CallExpr(Id('f'), [IntLiteral(5)]))]))])
        expect = str(TypeMismatchInStatement(Assign(Id('y'), CallExpr(Id('f'), [BinaryOp('+', IntLiteral(6), ArrayCell(CallExpr(Id('f'), [ArrayCell(CallExpr(Id('f'), [Id('x')]), [IntLiteral(3)])]), [IntLiteral(7)]))]))))
        self.assertTrue(TestChecker.test(input,expect,525))
    def test_number_126(self):
        """undecl array shadowing"""
        raw_input= """Var: a,b[2][2]; Function: main Parameter: a[1][1] Body: a= 5; EndBody."""
        input = Program([VarDecl(Id('a'), [], None), VarDecl(Id('b'), [2, 2], None), FuncDecl(Id('main'), [VarDecl(Id('a'), [1, 1], None)], ([], [Assign(Id('a'), IntLiteral(5))]))])
        expect = str(TypeMismatchInStatement(Assign(Id('a'), IntLiteral(5))))
        self.assertTrue(TestChecker.test(input,expect,526))
    def test_number_127(self):
        """undecl array infer complex"""
        raw_input= """Var: a,b[2][2]; Function: main Parameter: a[1][1] Body: a[3][2] = b[3][1] + main({{1}}); Return main({{1},{2}})[2][3]; EndBody."""
        input = Program([VarDecl(Id('a'), [], None), VarDecl(Id('b'), [2, 2], None), FuncDecl(Id('main'), [VarDecl(Id('a'), [1, 1], None)], ([], [Assign(ArrayCell(Id('a'), [IntLiteral(3), IntLiteral(2)]), BinaryOp('+', ArrayCell(Id('b'), [IntLiteral(3), IntLiteral(1)]), CallExpr(Id('main'), [ArrayLiteral([ArrayLiteral([IntLiteral(1)])])]))), Return(ArrayCell(CallExpr(Id('main'), [ArrayLiteral([ArrayLiteral([IntLiteral(1)]), ArrayLiteral([IntLiteral(2)])])]), [IntLiteral(2), IntLiteral(3)]))]))])
        expect = str(TypeMismatchInExpression(CallExpr(Id('main'), [ArrayLiteral([ArrayLiteral([IntLiteral(1)]), ArrayLiteral([IntLiteral(2)])])])))
        self.assertTrue(TestChecker.test(input,expect,527))
    def test_number_128(self):
        """calling function with unknown array"""
        raw_input= """Function: main Parameter: a[2] Body:  main(a); EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('a'), [2], None)], ([], [CallStmt(Id('main'), [Id('a')])]))])
        expect = str(TypeCannotBeInferred(CallStmt(Id('main'), [Id('a')])))
        self.assertTrue(TestChecker.test(input,expect,528))
    def test_number_129(self):
        """complex array cell function id"""
        raw_input= """Function: f1 Parameter: x Body: Return {1,2}; EndBody. Function: main Parameter: a,b[2] Body:f1(a + 5 * f1(6)[2] % 0x12)[1*(a-----7) * 4 * 5] = f1(2)[3] - f1(f1(5))[2]; EndBody. """
        input = Program([FuncDecl(Id('f1'), [VarDecl(Id('x'), [], None)], ([], [Return(ArrayLiteral([IntLiteral(1), IntLiteral(2)]))])), FuncDecl(Id('main'), [VarDecl(Id('a'), [], None), VarDecl(Id('b'), [2], None)], ([], [Assign(ArrayCell(CallExpr(Id('f1'), [BinaryOp('+', Id('a'), BinaryOp('%', BinaryOp('*', IntLiteral(5), ArrayCell(CallExpr(Id('f1'), [IntLiteral(6)]), [IntLiteral(2)])), IntLiteral(18)))]), [BinaryOp('*', BinaryOp('*', BinaryOp('*', IntLiteral(1), BinaryOp('-', Id('a'), UnaryOp('-', UnaryOp('-', UnaryOp('-', UnaryOp('-', IntLiteral(7))))))), IntLiteral(4)), IntLiteral(5))]), BinaryOp('-', ArrayCell(CallExpr(Id('f1'), [IntLiteral(2)]), [IntLiteral(3)]), ArrayCell(CallExpr(Id('f1'), [CallExpr(Id('f1'), [IntLiteral(5)])]), [IntLiteral(2)])))]))])
        expect = str(TypeMismatchInExpression(CallExpr(Id('f1'), [CallExpr(Id('f1'), [IntLiteral(5)])])))
        self.assertTrue(TestChecker.test(input,expect,529))
    def test_number_130(self):
        """func id in arraycell dim mismatch"""
        raw_input= """Function: f1 Parameter: x Body: Return {1,2}; EndBody. Function: main Parameter: a,b[2] Body: f1(5)[1][2] = 5; EndBody."""
        input = Program([FuncDecl(Id('f1'), [VarDecl(Id('x'), [], None)], ([], [Return(ArrayLiteral([IntLiteral(1), IntLiteral(2)]))])), FuncDecl(Id('main'), [VarDecl(Id('a'), [], None), VarDecl(Id('b'), [2], None)], ([], [Assign(ArrayCell(CallExpr(Id('f1'), [IntLiteral(5)]), [IntLiteral(1), IntLiteral(2)]), IntLiteral(5))]))])
        expect = str(TypeMismatchInExpression(ArrayCell(CallExpr(Id('f1'), [IntLiteral(5)]), [IntLiteral(1), IntLiteral(2)])))
        self.assertTrue(TestChecker.test(input,expect,530))
    def test_number_131(self):
        """array cell with cant inferfunction rhs"""
        raw_input= """Function: f Parameter: x Body: Return {1,2,3}; EndBody. Function: main Body: f(main())[2] = 5; EndBody."""
        input = Program([FuncDecl(Id('f'), [VarDecl(Id('x'), [], None)], ([], [Return(ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3)]))])), FuncDecl(Id('main'), [], ([], [Assign(ArrayCell(CallExpr(Id('f'), [CallExpr(Id('main'), [])]), [IntLiteral(2)]), IntLiteral(5))]))])
        expect = str(TypeCannotBeInferred(Assign(ArrayCell(CallExpr(Id('f'), [CallExpr(Id('main'), [])]), [IntLiteral(2)]), IntLiteral(5))))
        self.assertTrue(TestChecker.test(input,expect,531))
    def test_number_132(self):
        """arraycell in for loop"""
        raw_input= """Function: main Parameter: a[2],b[2],c[2] Body: Var: x; For (a = 5, b[2],c[3]) Do EndFor. EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('a'), [2], None), VarDecl(Id('b'), [2], None), VarDecl(Id('c'), [2], None)], ([VarDecl(Id('x'), [], None)], [For(Id('a'), IntLiteral(5), ArrayCell(Id('b'), [IntLiteral(2)]), ArrayCell(Id('c'), [IntLiteral(3)]), ([], []))]))])
        expect = str(TypeMismatchInStatement(For(Id('a'), IntLiteral(5), ArrayCell(Id('b'), [IntLiteral(2)]), ArrayCell(Id('c'), [IntLiteral(3)]), ([], []))))
        self.assertTrue(TestChecker.test(input,expect,532))
    def test_number_133(self):
        """arraycell in for loop"""
        raw_input= """Function: main Parameter: a[2],b[2],c[2] Body: Var: x; For (x=a[2],b[2], c[2]) Do  a[3] = c[3] + main({1,2},{True,False},{3,4}); EndFor. Return b[2]; EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('a'), [2], None), VarDecl(Id('b'), [2], None), VarDecl(Id('c'), [2], None)], ([VarDecl(Id('x'), [], None)], [For(Id('x'), ArrayCell(Id('a'), [IntLiteral(2)]), ArrayCell(Id('b'), [IntLiteral(2)]), ArrayCell(Id('c'), [IntLiteral(2)]), ([], [Assign(ArrayCell(Id('a'), [IntLiteral(3)]), BinaryOp('+', ArrayCell(Id('c'), [IntLiteral(3)]), CallExpr(Id('main'), [ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([BooleanLiteral(True), BooleanLiteral(False)]), ArrayLiteral([IntLiteral(3), IntLiteral(4)])])))])), Return(ArrayCell(Id('b'), [IntLiteral(2)]))]))])
        expect = str(TypeMismatchInStatement(Return(ArrayCell(Id('b'), [IntLiteral(2)]))))
        self.assertTrue(TestChecker.test(input,expect,533))
    def test_number_134(self):
        """infering array cell from while"""
        raw_input= """Function: main Parameter: a[2] Body: While a[1] Do main({1,2})[5] = True; EndWhile. EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('a'), [2], None)], ([], [While(ArrayCell(Id('a'), [IntLiteral(1)]), ([], [Assign(ArrayCell(CallExpr(Id('main'), [ArrayLiteral([IntLiteral(1), IntLiteral(2)])]), [IntLiteral(5)]), BooleanLiteral(True))]))]))])
        expect = str(TypeMismatchInExpression(CallExpr(Id('main'), [ArrayLiteral([IntLiteral(1), IntLiteral(2)])])))
        self.assertTrue(TestChecker.test(input,expect,534))
    def test_number_135(self):
        """type mismatch in returning unkown array cell func id"""
        raw_input= """Function: main Parameter: a[2] Body: Return {1,2};  Return main(5)[2]; EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('a'), [2], None)], ([], [Return(ArrayLiteral([IntLiteral(1), IntLiteral(2)])), Return(ArrayCell(CallExpr(Id('main'), [IntLiteral(5)]), [IntLiteral(2)]))]))])
        expect = str(TypeMismatchInExpression(CallExpr(Id('main'), [IntLiteral(5)])))
        self.assertTrue(TestChecker.test(input,expect,535))
    def test_number_136(self):
        """Just normal full array decl"""
        raw_input= """Var: a[2] = {1,2}, b[3] = {1.2,1.2,1.2}; Function: main Body: a[2] = 1.2; b[3] = 5; EndBody."""
        input = Program([VarDecl(Id('a'), [2], ArrayLiteral([IntLiteral(1), IntLiteral(2)])), VarDecl(Id('b'), [3], ArrayLiteral([FloatLiteral(1.2), FloatLiteral(1.2), FloatLiteral(1.2)])), FuncDecl(Id('main'), [], ([], [Assign(ArrayCell(Id('a'), [IntLiteral(2)]), FloatLiteral(1.2)), Assign(ArrayCell(Id('b'), [IntLiteral(3)]), IntLiteral(5))]))])
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id('a'), [IntLiteral(2)]), FloatLiteral(1.2))))
        self.assertTrue(TestChecker.test(input,expect,536))
    def test_number_137(self):
        """assignment left or right first"""
        raw_input= """Function: test Parameter: x Body: x=5; Return {2,3}; EndBody. Function: main Parameter: a,b Body: test(a)[2] = main(2.2, b+5); EndBody."""
        input = Program([FuncDecl(Id('test'), [VarDecl(Id('x'), [], None)], ([], [Assign(Id('x'), IntLiteral(5)), Return(ArrayLiteral([IntLiteral(2), IntLiteral(3)]))])), FuncDecl(Id('main'), [VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None)], ([], [Assign(ArrayCell(CallExpr(Id('test'), [Id('a')]), [IntLiteral(2)]), CallExpr(Id('main'), [FloatLiteral(2.2), BinaryOp('+', Id('b'), IntLiteral(5))]))]))])
        expect = str(TypeMismatchInExpression(CallExpr(Id('main'), [FloatLiteral(2.2), BinaryOp('+', Id('b'), IntLiteral(5))])))
        self.assertTrue(TestChecker.test(input,expect,537))
    def test_number_138(self):
        """cant infer like this cause inner param is checked first"""
        raw_input= """Function: main Parameter: x Body: If main(main(x)) Then x = 5; EndIf. EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('x'), [], None)], ([], [If([[CallExpr(Id('main'), [CallExpr(Id('main'), [Id('x')])]), [], [Assign(Id('x'), IntLiteral(5))]]], ([], []))]))])
        expect = str(TypeCannotBeInferred(If([[CallExpr(Id('main'), [CallExpr(Id('main'), [Id('x')])]), [], [Assign(Id('x'), IntLiteral(5))]]], ([], []))))
        self.assertTrue(TestChecker.test(input,expect,538))
    def test_number_139(self):
        """nested func call in for"""
        raw_input= """Function: main Parameter: x Body: Var: y,z,k,l,m,n; For (y = f1(f1(z-2)), f2(f2(False)), main(main(n+m)) ) Do EndFor.  EndBody. Function: f1 Parameter: x Body: Return 4; EndBody. Function: f2 Parameter: y Body: Return "Wrong Here"; EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('x'), [], None)], ([VarDecl(Id('y'), [], None), VarDecl(Id('z'), [], None), VarDecl(Id('k'), [], None), VarDecl(Id('l'), [], None), VarDecl(Id('m'), [], None), VarDecl(Id('n'), [], None)], [For(Id('y'), CallExpr(Id('f1'), [CallExpr(Id('f1'), [BinaryOp('-', Id('z'), IntLiteral(2))])]), CallExpr(Id('f2'), [CallExpr(Id('f2'), [BooleanLiteral(False)])]), CallExpr(Id('main'), [CallExpr(Id('main'), [BinaryOp('+', Id('n'), Id('m'))])]), ([], []))])), FuncDecl(Id('f1'), [VarDecl(Id('x'), [], None)], ([], [Return(IntLiteral(4))])), FuncDecl(Id('f2'), [VarDecl(Id('y'), [], None)], ([], [Return(StringLiteral('Wrong Here'))]))])
        expect = str(TypeMismatchInStatement(Return(StringLiteral('Wrong Here'))))
        self.assertTrue(TestChecker.test(input,expect,539))
    def test_number_140(self):
        """nested func call in while"""
        raw_input= """Function: main Parameter: x Body: While (main(main(main(10)))) Do EndWhile. EndBody."""
        input = Program([FuncDecl(Id('main'), [VarDecl(Id('x'), [], None)], ([], [While(CallExpr(Id('main'), [CallExpr(Id('main'), [CallExpr(Id('main'), [IntLiteral(10)])])]), ([], []))]))])
        expect = str(TypeMismatchInExpression(CallExpr(Id('main'), [CallExpr(Id('main'), [IntLiteral(10)])])))
        self.assertTrue(TestChecker.test(input,expect,540))
    def test_number_141(self):
        """declare inside use outside"""
        raw_input= """Function: main Body: If True Then Var: x =5; EndIf. Return x+.5.5; EndBody."""
        input = Program([FuncDecl(Id('main'), [], ([], [If([[BooleanLiteral(True), [VarDecl(Id('x'), [], IntLiteral(5))], []]], ([], [])), Return(BinaryOp('+.', Id('x'), FloatLiteral(5.5)))]))])
        expect = str(Undeclared(Identifier(), 'x'))
        self.assertTrue(TestChecker.test(input,expect,541))
    def test_number_142(self):
        """var decl as main and no real main func"""
        raw_input= """Var: a,c,b,d,main,foo,fuc,pung; Function: f2 Body: EndBody."""
        input = Program([VarDecl(Id('a'), [], None), VarDecl(Id('c'), [], None), VarDecl(Id('b'), [], None), VarDecl(Id('d'), [], None), VarDecl(Id('main'), [], None), VarDecl(Id('foo'), [], None), VarDecl(Id('fuc'), [], None), VarDecl(Id('pung'), [], None), FuncDecl(Id('f2'), [], ([], []))])
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,542))
    def test_number_143(self):
        """func with same name as global var"""
        raw_input= """Var: main; Function: main Body: EndBody."""
        input = Program([VarDecl(Id('main'), [], None), FuncDecl(Id('main'), [], ([], []))])
        expect = str(Redeclared(Function(), 'main'))
        self.assertTrue(TestChecker.test(input,expect,543))

