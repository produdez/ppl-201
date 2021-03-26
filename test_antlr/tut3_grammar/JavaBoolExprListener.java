// Generated from JavaBoolExpr.g4 by ANTLR 4.8
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link JavaBoolExprParser}.
 */
public interface JavaBoolExprListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link JavaBoolExprParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(JavaBoolExprParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link JavaBoolExprParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(JavaBoolExprParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link JavaBoolExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(JavaBoolExprParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link JavaBoolExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(JavaBoolExprParser.ExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link JavaBoolExprParser#expr2}.
	 * @param ctx the parse tree
	 */
	void enterExpr2(JavaBoolExprParser.Expr2Context ctx);
	/**
	 * Exit a parse tree produced by {@link JavaBoolExprParser#expr2}.
	 * @param ctx the parse tree
	 */
	void exitExpr2(JavaBoolExprParser.Expr2Context ctx);
	/**
	 * Enter a parse tree produced by {@link JavaBoolExprParser#expr3}.
	 * @param ctx the parse tree
	 */
	void enterExpr3(JavaBoolExprParser.Expr3Context ctx);
	/**
	 * Exit a parse tree produced by {@link JavaBoolExprParser#expr3}.
	 * @param ctx the parse tree
	 */
	void exitExpr3(JavaBoolExprParser.Expr3Context ctx);
}