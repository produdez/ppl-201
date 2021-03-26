# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete generic visitor for a parse tree produced by BKITParser.

class BKITVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKITParser#program.
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#variable_declaration_part.
    def visitVariable_declaration_part(self, ctx:BKITParser.Variable_declaration_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#variable_declaration.
    def visitVariable_declaration(self, ctx:BKITParser.Variable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#declaration_list.
    def visitDeclaration_list(self, ctx:BKITParser.Declaration_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#initialization.
    def visitInitialization(self, ctx:BKITParser.InitializationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#variable.
    def visitVariable(self, ctx:BKITParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#literal.
    def visitLiteral(self, ctx:BKITParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#function_declaration_part.
    def visitFunction_declaration_part(self, ctx:BKITParser.Function_declaration_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#function_declaration.
    def visitFunction_declaration(self, ctx:BKITParser.Function_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#function_name.
    def visitFunction_name(self, ctx:BKITParser.Function_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#function_parameter.
    def visitFunction_parameter(self, ctx:BKITParser.Function_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#parameter_list.
    def visitParameter_list(self, ctx:BKITParser.Parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#function_body.
    def visitFunction_body(self, ctx:BKITParser.Function_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#statement_list.
    def visitStatement_list(self, ctx:BKITParser.Statement_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#as_stmt.
    def visitAs_stmt(self, ctx:BKITParser.As_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#if_stmt.
    def visitIf_stmt(self, ctx:BKITParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#for_stmt.
    def visitFor_stmt(self, ctx:BKITParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#while_stmt.
    def visitWhile_stmt(self, ctx:BKITParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#dwhile_stmt.
    def visitDwhile_stmt(self, ctx:BKITParser.Dwhile_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#brk_stmt.
    def visitBrk_stmt(self, ctx:BKITParser.Brk_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#conti_stmt.
    def visitConti_stmt(self, ctx:BKITParser.Conti_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#call_stmt.
    def visitCall_stmt(self, ctx:BKITParser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#ret_stmt.
    def visitRet_stmt(self, ctx:BKITParser.Ret_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#assignment_statement.
    def visitAssignment_statement(self, ctx:BKITParser.Assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#if_statement.
    def visitIf_statement(self, ctx:BKITParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#for_statement.
    def visitFor_statement(self, ctx:BKITParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#while_statement.
    def visitWhile_statement(self, ctx:BKITParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#do_while_statement.
    def visitDo_while_statement(self, ctx:BKITParser.Do_while_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#break_statement.
    def visitBreak_statement(self, ctx:BKITParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#continue_statement.
    def visitContinue_statement(self, ctx:BKITParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#call_statement.
    def visitCall_statement(self, ctx:BKITParser.Call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#return_statement.
    def visitReturn_statement(self, ctx:BKITParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expression_list.
    def visitExpression_list(self, ctx:BKITParser.Expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expression.
    def visitExpression(self, ctx:BKITParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#rela_expr.
    def visitRela_expr(self, ctx:BKITParser.Rela_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#logic_expr.
    def visitLogic_expr(self, ctx:BKITParser.Logic_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#add_expr.
    def visitAdd_expr(self, ctx:BKITParser.Add_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#mul_expr.
    def visitMul_expr(self, ctx:BKITParser.Mul_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#negation_expr.
    def visitNegation_expr(self, ctx:BKITParser.Negation_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#sign_expr.
    def visitSign_expr(self, ctx:BKITParser.Sign_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#element_expr.
    def visitElement_expr(self, ctx:BKITParser.Element_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_expr.
    def visitFunc_expr(self, ctx:BKITParser.Func_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#sub_expr.
    def visitSub_expr(self, ctx:BKITParser.Sub_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#operative.
    def visitOperative(self, ctx:BKITParser.OperativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#array_element.
    def visitArray_element(self, ctx:BKITParser.Array_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#index_op.
    def visitIndex_op(self, ctx:BKITParser.Index_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#function_call.
    def visitFunction_call(self, ctx:BKITParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#sign_op.
    def visitSign_op(self, ctx:BKITParser.Sign_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#negation_op.
    def visitNegation_op(self, ctx:BKITParser.Negation_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#multiplying_op.
    def visitMultiplying_op(self, ctx:BKITParser.Multiplying_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#adding_op.
    def visitAdding_op(self, ctx:BKITParser.Adding_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#logical_op.
    def visitLogical_op(self, ctx:BKITParser.Logical_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#relational_op.
    def visitRelational_op(self, ctx:BKITParser.Relational_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#bool_lit.
    def visitBool_lit(self, ctx:BKITParser.Bool_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#array_lit.
    def visitArray_lit(self, ctx:BKITParser.Array_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#literal_list.
    def visitLiteral_list(self, ctx:BKITParser.Literal_listContext):
        return self.visitChildren(ctx)



del BKITParser