// Generated from BKIT.g4 by ANTLR 4.8
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link BKITParser}.
 */
public interface BKITListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link BKITParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(BKITParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(BKITParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#variable_declaration_part}.
	 * @param ctx the parse tree
	 */
	void enterVariable_declaration_part(BKITParser.Variable_declaration_partContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#variable_declaration_part}.
	 * @param ctx the parse tree
	 */
	void exitVariable_declaration_part(BKITParser.Variable_declaration_partContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#variable_declaration}.
	 * @param ctx the parse tree
	 */
	void enterVariable_declaration(BKITParser.Variable_declarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#variable_declaration}.
	 * @param ctx the parse tree
	 */
	void exitVariable_declaration(BKITParser.Variable_declarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#declaration_list}.
	 * @param ctx the parse tree
	 */
	void enterDeclaration_list(BKITParser.Declaration_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#declaration_list}.
	 * @param ctx the parse tree
	 */
	void exitDeclaration_list(BKITParser.Declaration_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#initialization}.
	 * @param ctx the parse tree
	 */
	void enterInitialization(BKITParser.InitializationContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#initialization}.
	 * @param ctx the parse tree
	 */
	void exitInitialization(BKITParser.InitializationContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#variable}.
	 * @param ctx the parse tree
	 */
	void enterVariable(BKITParser.VariableContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#variable}.
	 * @param ctx the parse tree
	 */
	void exitVariable(BKITParser.VariableContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#array_element}.
	 * @param ctx the parse tree
	 */
	void enterArray_element(BKITParser.Array_elementContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#array_element}.
	 * @param ctx the parse tree
	 */
	void exitArray_element(BKITParser.Array_elementContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#index_operator}.
	 * @param ctx the parse tree
	 */
	void enterIndex_operator(BKITParser.Index_operatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#index_operator}.
	 * @param ctx the parse tree
	 */
	void exitIndex_operator(BKITParser.Index_operatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#literal}.
	 * @param ctx the parse tree
	 */
	void enterLiteral(BKITParser.LiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#literal}.
	 * @param ctx the parse tree
	 */
	void exitLiteral(BKITParser.LiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#function_declaration_part}.
	 * @param ctx the parse tree
	 */
	void enterFunction_declaration_part(BKITParser.Function_declaration_partContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#function_declaration_part}.
	 * @param ctx the parse tree
	 */
	void exitFunction_declaration_part(BKITParser.Function_declaration_partContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#function_declaration}.
	 * @param ctx the parse tree
	 */
	void enterFunction_declaration(BKITParser.Function_declarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#function_declaration}.
	 * @param ctx the parse tree
	 */
	void exitFunction_declaration(BKITParser.Function_declarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#function_name}.
	 * @param ctx the parse tree
	 */
	void enterFunction_name(BKITParser.Function_nameContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#function_name}.
	 * @param ctx the parse tree
	 */
	void exitFunction_name(BKITParser.Function_nameContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#function_parameter}.
	 * @param ctx the parse tree
	 */
	void enterFunction_parameter(BKITParser.Function_parameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#function_parameter}.
	 * @param ctx the parse tree
	 */
	void exitFunction_parameter(BKITParser.Function_parameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#parameter_list}.
	 * @param ctx the parse tree
	 */
	void enterParameter_list(BKITParser.Parameter_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#parameter_list}.
	 * @param ctx the parse tree
	 */
	void exitParameter_list(BKITParser.Parameter_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#function_body}.
	 * @param ctx the parse tree
	 */
	void enterFunction_body(BKITParser.Function_bodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#function_body}.
	 * @param ctx the parse tree
	 */
	void exitFunction_body(BKITParser.Function_bodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#statement_list}.
	 * @param ctx the parse tree
	 */
	void enterStatement_list(BKITParser.Statement_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#statement_list}.
	 * @param ctx the parse tree
	 */
	void exitStatement_list(BKITParser.Statement_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#assignment_statement}.
	 * @param ctx the parse tree
	 */
	void enterAssignment_statement(BKITParser.Assignment_statementContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#assignment_statement}.
	 * @param ctx the parse tree
	 */
	void exitAssignment_statement(BKITParser.Assignment_statementContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#if_statement}.
	 * @param ctx the parse tree
	 */
	void enterIf_statement(BKITParser.If_statementContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#if_statement}.
	 * @param ctx the parse tree
	 */
	void exitIf_statement(BKITParser.If_statementContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#for_statement}.
	 * @param ctx the parse tree
	 */
	void enterFor_statement(BKITParser.For_statementContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#for_statement}.
	 * @param ctx the parse tree
	 */
	void exitFor_statement(BKITParser.For_statementContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#while_statement}.
	 * @param ctx the parse tree
	 */
	void enterWhile_statement(BKITParser.While_statementContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#while_statement}.
	 * @param ctx the parse tree
	 */
	void exitWhile_statement(BKITParser.While_statementContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#do_while_statement}.
	 * @param ctx the parse tree
	 */
	void enterDo_while_statement(BKITParser.Do_while_statementContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#do_while_statement}.
	 * @param ctx the parse tree
	 */
	void exitDo_while_statement(BKITParser.Do_while_statementContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#break_statement}.
	 * @param ctx the parse tree
	 */
	void enterBreak_statement(BKITParser.Break_statementContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#break_statement}.
	 * @param ctx the parse tree
	 */
	void exitBreak_statement(BKITParser.Break_statementContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#continue_statement}.
	 * @param ctx the parse tree
	 */
	void enterContinue_statement(BKITParser.Continue_statementContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#continue_statement}.
	 * @param ctx the parse tree
	 */
	void exitContinue_statement(BKITParser.Continue_statementContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#call_statement}.
	 * @param ctx the parse tree
	 */
	void enterCall_statement(BKITParser.Call_statementContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#call_statement}.
	 * @param ctx the parse tree
	 */
	void exitCall_statement(BKITParser.Call_statementContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#return_statement}.
	 * @param ctx the parse tree
	 */
	void enterReturn_statement(BKITParser.Return_statementContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#return_statement}.
	 * @param ctx the parse tree
	 */
	void exitReturn_statement(BKITParser.Return_statementContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#expression_list}.
	 * @param ctx the parse tree
	 */
	void enterExpression_list(BKITParser.Expression_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#expression_list}.
	 * @param ctx the parse tree
	 */
	void exitExpression_list(BKITParser.Expression_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(BKITParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(BKITParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#expression2}.
	 * @param ctx the parse tree
	 */
	void enterExpression2(BKITParser.Expression2Context ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#expression2}.
	 * @param ctx the parse tree
	 */
	void exitExpression2(BKITParser.Expression2Context ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#function_call}.
	 * @param ctx the parse tree
	 */
	void enterFunction_call(BKITParser.Function_callContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#function_call}.
	 * @param ctx the parse tree
	 */
	void exitFunction_call(BKITParser.Function_callContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#sign_op}.
	 * @param ctx the parse tree
	 */
	void enterSign_op(BKITParser.Sign_opContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#sign_op}.
	 * @param ctx the parse tree
	 */
	void exitSign_op(BKITParser.Sign_opContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#negation_op}.
	 * @param ctx the parse tree
	 */
	void enterNegation_op(BKITParser.Negation_opContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#negation_op}.
	 * @param ctx the parse tree
	 */
	void exitNegation_op(BKITParser.Negation_opContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#multiplying_op}.
	 * @param ctx the parse tree
	 */
	void enterMultiplying_op(BKITParser.Multiplying_opContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#multiplying_op}.
	 * @param ctx the parse tree
	 */
	void exitMultiplying_op(BKITParser.Multiplying_opContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#adding_op}.
	 * @param ctx the parse tree
	 */
	void enterAdding_op(BKITParser.Adding_opContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#adding_op}.
	 * @param ctx the parse tree
	 */
	void exitAdding_op(BKITParser.Adding_opContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#logical_op}.
	 * @param ctx the parse tree
	 */
	void enterLogical_op(BKITParser.Logical_opContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#logical_op}.
	 * @param ctx the parse tree
	 */
	void exitLogical_op(BKITParser.Logical_opContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#relational_op}.
	 * @param ctx the parse tree
	 */
	void enterRelational_op(BKITParser.Relational_opContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#relational_op}.
	 * @param ctx the parse tree
	 */
	void exitRelational_op(BKITParser.Relational_opContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#bool_lit}.
	 * @param ctx the parse tree
	 */
	void enterBool_lit(BKITParser.Bool_litContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#bool_lit}.
	 * @param ctx the parse tree
	 */
	void exitBool_lit(BKITParser.Bool_litContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#array_lit}.
	 * @param ctx the parse tree
	 */
	void enterArray_lit(BKITParser.Array_litContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#array_lit}.
	 * @param ctx the parse tree
	 */
	void exitArray_lit(BKITParser.Array_litContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#literal_list}.
	 * @param ctx the parse tree
	 */
	void enterLiteral_list(BKITParser.Literal_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#literal_list}.
	 * @param ctx the parse tree
	 */
	void exitLiteral_list(BKITParser.Literal_listContext ctx);
}