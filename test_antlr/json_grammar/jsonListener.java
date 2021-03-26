// Generated from json.g4 by ANTLR 4.8
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link jsonParser}.
 */
public interface jsonListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link jsonParser#file}.
	 * @param ctx the parse tree
	 */
	void enterFile(jsonParser.FileContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsonParser#file}.
	 * @param ctx the parse tree
	 */
	void exitFile(jsonParser.FileContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsonParser#collection}.
	 * @param ctx the parse tree
	 */
	void enterCollection(jsonParser.CollectionContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsonParser#collection}.
	 * @param ctx the parse tree
	 */
	void exitCollection(jsonParser.CollectionContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsonParser#single_line_collection}.
	 * @param ctx the parse tree
	 */
	void enterSingle_line_collection(jsonParser.Single_line_collectionContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsonParser#single_line_collection}.
	 * @param ctx the parse tree
	 */
	void exitSingle_line_collection(jsonParser.Single_line_collectionContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsonParser#array}.
	 * @param ctx the parse tree
	 */
	void enterArray(jsonParser.ArrayContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsonParser#array}.
	 * @param ctx the parse tree
	 */
	void exitArray(jsonParser.ArrayContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsonParser#primitive}.
	 * @param ctx the parse tree
	 */
	void enterPrimitive(jsonParser.PrimitiveContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsonParser#primitive}.
	 * @param ctx the parse tree
	 */
	void exitPrimitive(jsonParser.PrimitiveContext ctx);
}