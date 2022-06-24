from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *
from functools import reduce


class ASTGeneration(BKITVisitor):
    
    def visitProgram(self,ctx:BKITParser.ProgramContext):
        return Program(ctx.variable_declaration_part().accept(self)+ctx.function_declaration_part().accept(self))


    # Visit a parse tree produced by BKITParser#variable_declaration_part.
    def visitVariable_declaration_part(self, ctx:BKITParser.Variable_declaration_partContext):
        def flatten_lst(lst):
            return reduce(lambda a,b: a+b, lst)
        if ctx.variable_declaration():
            return flatten_lst(list(map(lambda var_decl: var_decl.accept(self),ctx.variable_declaration())))
        else: return []


    # Visit a parse tree produced by BKITParser#variable_declaration.
    def visitVariable_declaration(self, ctx:BKITParser.Variable_declarationContext):
        return ctx.declaration_list().accept(self)


    # Visit a parse tree produced by BKITParser#declaration_list.
    def visitDeclaration_list(self, ctx:BKITParser.Declaration_listContext):
        return list(map(lambda initialization: initialization.accept(self), ctx.initialization()))


    # Visit a parse tree produced by BKITParser#initialization.
    def visitInitialization(self, ctx:BKITParser.InitializationContext):
        variable = ctx.variable().accept(self) #single or composite
        literal = ctx.literal().accept(self) if ctx.literal() else None # may or maynot

        return VarDecl(variable[0], variable[1], literal)

    # Visit a parse tree produced by BKITParser#variable.
    def visitVariable(self, ctx:BKITParser.VariableContext):
        id = Id(ctx.ID().getText())
        init = []
        if ctx.INT_LIT():
            init = list(map(lambda lit: self.visitINT_LIT(lit.getText()),ctx.INT_LIT()))
        
        return (id, init)
            

    def visitINT_LIT(self,int_lit: str):
        """HELPER function to generate IntLiteral from INT_LIT lexer token's string"""
        def str_base(str):
            if len(str) == 1:
                return (str,10)
            if str[0:2] == '0x' or str[0:2] == '0X':
                return (str[2:],16)
            if str[0:2] == '0o' or str[0:2] == '0O':
                return (str[2:],8)
            else: return (str,10)
        s_b = str_base(int_lit)
        return int(s_b[0],s_b[1])
    
    # Visit a parse tree produced by BKITParser#literal.
    def visitLiteral(self, ctx:BKITParser.LiteralContext):
        if ctx.bool_lit():
            return ctx.bool_lit().accept(self)
        if ctx.INT_LIT(): #use helper function visitINT_LIT
            return IntLiteral(self.visitINT_LIT(ctx.INT_LIT().getText()))
        if ctx.FLOAT_LIT():
            return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
        if ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        else: #case array lit:
            return ctx.array_lit().accept(self)


    # Visit a parse tree produced by BKITParser#function_declaration_part.
    def visitFunction_declaration_part(self, ctx:BKITParser.Function_declaration_partContext):
        if ctx.function_declaration():
            return list(map(lambda func_dec: func_dec.accept(self),ctx.function_declaration()))
        else: return []


    # Visit a parse tree produced by BKITParser#function_declaration.
    def visitFunction_declaration(self, ctx:BKITParser.Function_declarationContext):
        func_name = ctx.function_name().accept(self)
        func_param = ctx.function_parameter().accept(self) if ctx.function_parameter() else []
        func_body = ctx.function_body().accept(self)
        return FuncDecl(func_name,func_param,func_body)


    # Visit a parse tree produced by BKITParser#function_name.
    def visitFunction_name(self, ctx:BKITParser.Function_nameContext):
        return Id(ctx.ID().getText())


    # Visit a parse tree produced by BKITParser#function_parameter.
    def visitFunction_parameter(self, ctx:BKITParser.Function_parameterContext):
        return ctx.parameter_list().accept(self)


    # Visit a parse tree produced by BKITParser#parameter_list.
    def visitParameter_list(self, ctx:BKITParser.Parameter_listContext):
        visitor = self
        def param_to_vardecl(param): #NOTE: param here is of type variable in g4.
            variable = param.accept(visitor)
            return VarDecl(variable[0],variable[1],None)

        return list(map(lambda param: param_to_vardecl(param),ctx.variable()))


    # Visit a parse tree produced by BKITParser#function_body.
    def visitFunction_body(self, ctx:BKITParser.Function_bodyContext):
        return ctx.statement_list().accept(self)


    # Visit a parse tree produced by BKITParser#statement_list.
    def visitStatement_list(self, ctx:BKITParser.Statement_listContext):
        stmts = []
        var_decl = ctx.variable_declaration_part().accept(self)
        if ctx.other_statements():
            stmts = list(map(lambda stmt: stmt.accept(self), ctx.other_statements()))
        return (var_decl,stmts)
    
    #NOTE: other_stmts replaced by alternatives below 

    # Visit a parse tree produced by BKITParser#as_stmt.
    def visitAs_stmt(self, ctx:BKITParser.As_stmtContext):
        return ctx.assignment_statement().accept(self)


    # Visit a parse tree produced by BKITParser#if_stmt.
    def visitIf_stmt(self, ctx:BKITParser.If_stmtContext):
        return ctx.if_statement().accept(self)


    # Visit a parse tree produced by BKITParser#for_stmt.
    def visitFor_stmt(self, ctx:BKITParser.For_stmtContext):
        return ctx.for_statement().accept(self)


    # Visit a parse tree produced by BKITParser#while_stmt.
    def visitWhile_stmt(self, ctx:BKITParser.While_stmtContext):
        return ctx.while_statement().accept(self)


    # Visit a parse tree produced by BKITParser#dwhile_stmt.
    def visitDwhile_stmt(self, ctx:BKITParser.Dwhile_stmtContext):
        return ctx.do_while_statement().accept(self)


    # Visit a parse tree produced by BKITParser#brk_stmt.
    def visitBrk_stmt(self, ctx:BKITParser.Brk_stmtContext):
        return ctx.break_statement().accept(self)


    # Visit a parse tree produced by BKITParser#conti_stmt.
    def visitConti_stmt(self, ctx:BKITParser.Conti_stmtContext):
        return ctx.continue_statement().accept(self)


    # Visit a parse tree produced by BKITParser#call_stmt.
    def visitCall_stmt(self, ctx:BKITParser.Call_stmtContext):
        return ctx.call_statement().accept(self)


    # Visit a parse tree produced by BKITParser#ret_stmt.
    def visitRet_stmt(self, ctx:BKITParser.Ret_stmtContext):
        return ctx.return_statement().accept(self)

    # Visit a parse tree produced by BKITParser#assignment_statement.
    def visitAssignment_statement(self, ctx:BKITParser.Assignment_statementContext):
        #the child 0 can be array_elem of id
        lhs = Id(ctx.ID().getText()) if ctx.ID() else ctx.array_element().accept(self)
        return Assign(lhs,ctx.expression().accept(self))

    # Visit a parse tree produced by BKITParser#if_statement.
    def visitIf_statement(self, ctx:BKITParser.If_statementContext):
        exprs = list(map(lambda expr: expr.accept(self), ctx.expression())) # all the exprs
        stmtlist_lst = list(map(lambda stmt_lst: stmt_lst.accept(self), ctx.statement_list())) #all the tuple of (var_decl, stmts)
        ifThenStmts = list(map(lambda tuple: [tuple[0]] + list(tuple[1]), zip(exprs,stmtlist_lst))) # combine expr and tuple () into 1 tuple
        
        elseStmt = stmtlist_lst[-1] if ctx.ELSE() else ([],[]) # if ELSE() is there, the expr has less compared to the stmtlist_lst
        
        return If(ifThenStmts,elseStmt)



    # Visit a parse tree produced by BKITParser#for_statement.
    def visitFor_statement(self, ctx:BKITParser.For_statementContext):
        id = Id(ctx.ID().getText())
        exprs = list(map(lambda expr: expr.accept(self), ctx.expression())) # 3 exprs here
        loop = ctx.statement_list().accept(self)
        return For(id,exprs[0],exprs[1],exprs[2],loop)


    # Visit a parse tree produced by BKITParser#while_statement.
    def visitWhile_statement(self, ctx:BKITParser.While_statementContext):
        return While(ctx.expression().accept(self), ctx.statement_list().accept(self))


    # Visit a parse tree produced by BKITParser#do_while_statement.
    def visitDo_while_statement(self, ctx:BKITParser.Do_while_statementContext):
        return Dowhile(ctx.statement_list().accept(self),ctx.expression().accept(self))



    # Visit a parse tree produced by BKITParser#break_statement.
    def visitBreak_statement(self, ctx:BKITParser.Break_statementContext):
        return Break()


    # Visit a parse tree produced by BKITParser#continue_statement.
    def visitContinue_statement(self, ctx:BKITParser.Continue_statementContext):
        return Continue()


    # Visit a parse tree produced by BKITParser#call_statement.
    def visitCall_statement(self, ctx:BKITParser.Call_statementContext):
        call_expr = ctx.function_call().accept(self)
        return CallStmt(call_expr.method,call_expr.param)


    # Visit a parse tree produced by BKITParser#return_statement.
    def visitReturn_statement(self, ctx:BKITParser.Return_statementContext):
        return Return(expr = ctx.expression().accept(self) if ctx.expression() else None)


    # Visit a parse tree produced by BKITParser#expression_list.
    def visitExpression_list(self, ctx:BKITParser.Expression_listContext):
        return list(map(lambda expr: expr.accept(self), ctx.expression()))


    # Visit a parse tree produced by BKITParser#expression.
    def visitExpression(self, ctx:BKITParser.ExpressionContext):
        return ctx.rela_expr().accept(self)


    # Visit a parse tree produced by BKITParser#rela_expr.
    def visitRela_expr(self, ctx:BKITParser.Rela_exprContext):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.relational_op().accept(self),ctx.logic_expr()[0].accept(self),ctx.logic_expr()[1].accept(self))
        else:
            return ctx.logic_expr(0).accept(self)


    # Visit a parse tree produced by BKITParser#logic_expr.
    def visitLogic_expr(self, ctx:BKITParser.Logic_exprContext):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.logical_op().accept(self),ctx.logic_expr().accept(self),ctx.add_expr().accept(self))
        else:
            return ctx.add_expr().accept(self)


    # Visit a parse tree produced by BKITParser#add_expr.
    def visitAdd_expr(self, ctx:BKITParser.Add_exprContext):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.adding_op().accept(self),ctx.add_expr().accept(self),ctx.mul_expr().accept(self))
        else:
            return ctx.mul_expr().accept(self)


    # Visit a parse tree produced by BKITParser#mul_expr.
    def visitMul_expr(self, ctx:BKITParser.Mul_exprContext):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.multiplying_op().accept(self),ctx.mul_expr().accept(self),ctx.negation_expr().accept(self))
        else:
            return ctx.negation_expr().accept(self)


    # Visit a parse tree produced by BKITParser#negation_expr.
    def visitNegation_expr(self, ctx:BKITParser.Negation_exprContext):
        if ctx.getChildCount() == 2:
            return UnaryOp(ctx.negation_op().accept(self),ctx.negation_expr().accept(self))
        else:
            return ctx.sign_expr().accept(self)


    # Visit a parse tree produced by BKITParser#sign_expr.
    def visitSign_expr(self, ctx:BKITParser.Sign_exprContext):
        if ctx.getChildCount() == 2:
            return UnaryOp(ctx.sign_op().accept(self),ctx.sign_expr().accept(self))
        else:
            return ctx.element_expr().accept(self)


    # Visit a parse tree produced by BKITParser#element_expr.
    def visitElement_expr(self, ctx:BKITParser.Element_exprContext):
        if ctx.array_element():
            return ctx.array_element().accept(self)
        else:
            return ctx.func_expr().accept(self)


    # Visit a parse tree produced by BKITParser#func_expr.
    def visitFunc_expr(self, ctx:BKITParser.Func_exprContext):
        if ctx.function_call():
            return ctx.function_call().accept(self)
        else:
            return ctx.sub_expr().accept(self)


    # Visit a parse tree produced by BKITParser#sub_expr.
    def visitSub_expr(self, ctx:BKITParser.Sub_exprContext):
        if ctx.getChildCount() == 3:
            return ctx.expression().accept(self)
        else:
            return ctx.operative().accept(self)


    # Visit a parse tree produced by BKITParser#operative.
    def visitOperative(self, ctx:BKITParser.OperativeContext):
        if ctx.literal():
            return ctx.literal().accept(self)
        else:
            return Id(ctx.ID().getText())

    # Visit a parse tree produced by BKITParser#array_element.
    def visitArray_element(self, ctx:BKITParser.Array_elementContext):
        #child 0 can be ID or function call
        arr = Id(ctx.ID().getText()) if ctx.ID() else ctx.function_call().accept(self)
        return ArrayCell(arr,ctx.index_op().accept(self))

    # Visit a parse tree produced by BKITParser#index_op.
    def visitIndex_op(self, ctx:BKITParser.Index_opContext):
        return list(map(lambda expr: expr.accept(self),ctx.expression()))


    # Visit a parse tree produced by BKITParser#function_call.
    def visitFunction_call(self, ctx:BKITParser.Function_callContext):
        expr_list = ctx.expression_list().accept(self) if ctx.expression_list() else []
        return CallExpr(Id(ctx.ID().getText()), expr_list)

    #NOTE: down here just string return
    # Visit a parse tree produced by BKITParser#sign_op.
    def visitSign_op(self, ctx:BKITParser.Sign_opContext):
        return ctx.getChild(0).getText()


    # Visit a parse tree produced by BKITParser#negation_op.
    def visitNegation_op(self, ctx:BKITParser.Negation_opContext):
        return ctx.getChild(0).getText()


    # Visit a parse tree produced by BKITParser#multiplying_op.
    def visitMultiplying_op(self, ctx:BKITParser.Multiplying_opContext):
        return ctx.getChild(0).getText()


    # Visit a parse tree produced by BKITParser#adding_op.
    def visitAdding_op(self, ctx:BKITParser.Adding_opContext):
        return ctx.getChild(0).getText()


    # Visit a parse tree produced by BKITParser#logical_op.
    def visitLogical_op(self, ctx:BKITParser.Logical_opContext):
        return ctx.getChild(0).getText()


    # Visit a parse tree produced by BKITParser#relational_op.
    def visitRelational_op(self, ctx:BKITParser.Relational_opContext):
        return ctx.getChild(0).getText()


    # Visit a parse tree produced by BKITParser#bool_lit.
    def visitBool_lit(self, ctx:BKITParser.Bool_litContext):
        text = ctx.getChild(0).getText()
        if text == 'True': return BooleanLiteral(True)
        else: return BooleanLiteral(False)


    # Visit a parse tree produced by BKITParser#array_lit.
    def visitArray_lit(self, ctx:BKITParser.Array_litContext):
        return ArrayLiteral(ctx.literal_list().accept(self))


    # Visit a parse tree produced by BKITParser#literal_list.
    def visitLiteral_list(self, ctx:BKITParser.Literal_listContext):
        return list(map(lambda lit: lit.accept(self), ctx.literal()))

    

