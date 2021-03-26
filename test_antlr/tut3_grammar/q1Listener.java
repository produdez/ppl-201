// Generated from q1.g4 by ANTLR 4.8
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link q1Parser}.
 */
public interface q1Listener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link q1Parser#assign}.
	 * @param ctx the parse tree
	 */
	void enterAssign(q1Parser.AssignContext ctx);
	/**
	 * Exit a parse tree produced by {@link q1Parser#assign}.
	 * @param ctx the parse tree
	 */
	void exitAssign(q1Parser.AssignContext ctx);
	/**
	 * Enter a parse tree produced by {@link q1Parser#id}.
	 * @param ctx the parse tree
	 */
	void enterId(q1Parser.IdContext ctx);
	/**
	 * Exit a parse tree produced by {@link q1Parser#id}.
	 * @param ctx the parse tree
	 */
	void exitId(q1Parser.IdContext ctx);
	/**
	 * Enter a parse tree produced by {@link q1Parser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(q1Parser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link q1Parser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(q1Parser.ExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link q1Parser#term}.
	 * @param ctx the parse tree
	 */
	void enterTerm(q1Parser.TermContext ctx);
	/**
	 * Exit a parse tree produced by {@link q1Parser#term}.
	 * @param ctx the parse tree
	 */
	void exitTerm(q1Parser.TermContext ctx);
	/**
	 * Enter a parse tree produced by {@link q1Parser#factor}.
	 * @param ctx the parse tree
	 */
	void enterFactor(q1Parser.FactorContext ctx);
	/**
	 * Exit a parse tree produced by {@link q1Parser#factor}.
	 * @param ctx the parse tree
	 */
	void exitFactor(q1Parser.FactorContext ctx);
}