// Generated from e:\Dev\Coding\Project Folders\Python_VSCODE\BKIT ASSIGN\assignment1\assignment1\src\main\bkit\parser\BKIT.g4 by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class BKITParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		ID=1, BODY=2, BREAK=3, CONTINUE=4, DO=5, ELSE=6, ELSEIF=7, ENDBODY=8, 
		ENDIF=9, ENDFOR=10, ENDWHILE=11, FOR=12, FUNCTION=13, IF=14, PARAMETER=15, 
		RETURN=16, THEN=17, VAR=18, WHILE=19, ENDDO=20, TRUE=21, FALSE=22, ASSIGN=23, 
		PLUS=24, PLUS_DOT=25, MINUS=26, MINUS_DOT=27, STAR=28, STAR_DOT=29, DIV=30, 
		DIV_DOT=31, MOD=32, NOT=33, AND=34, OR=35, EQUAL=36, NOT_EQUAL=37, LESS=38, 
		GREATER=39, LESS_EQUAL=40, GREATER_EQUAL=41, EQUAL_DIV_EQUAL=42, LESS_DOT=43, 
		GREATER_DOT=44, LESS_EQUAL_DOT=45, GREATER_EQUAL_DOT=46, LEFT_PAREN=47, 
		RIGHT_PAREN=48, LEFT_SQUARE=49, RIGHT_SQUARE=50, LEFT_CURLY=51, RIGHT_CURLY=52, 
		SEMI=53, COLON=54, DOT=55, COMMA=56, WS=57, BLOCK_COMMENT=58, UNTERMINATED_COMMENT=59, 
		INT_LIT=60, FLOAT_LIT=61, STRING_LIT=62, ILLEGAL_ESCAPE=63, UNCLOSE_STRING=64, 
		ERROR_CHAR=65;
	public static final int
		RULE_program = 0, RULE_variable_declaration_part = 1, RULE_variable_declaration = 2, 
		RULE_declaration_list = 3, RULE_initialization = 4, RULE_variable = 5, 
		RULE_literal = 6, RULE_function_declaration_part = 7, RULE_function_declaration = 8, 
		RULE_function_name = 9, RULE_function_parameter = 10, RULE_parameter_list = 11, 
		RULE_function_body = 12, RULE_statement_list = 13, RULE_assignment_statement = 14, 
		RULE_if_statement = 15, RULE_for_statement = 16, RULE_while_statement = 17, 
		RULE_do_while_statement = 18, RULE_break_statement = 19, RULE_continue_statement = 20, 
		RULE_call_statement = 21, RULE_return_statement = 22, RULE_expression_list = 23, 
		RULE_expression = 24, RULE_rela_expr = 25, RULE_logic_expr = 26, RULE_add_expr = 27, 
		RULE_mul_expr = 28, RULE_negation_expr = 29, RULE_sign_expr = 30, RULE_element_expr = 31, 
		RULE_func_expr = 32, RULE_sub_expr = 33, RULE_operative = 34, RULE_index_op = 35, 
		RULE_function_call = 36, RULE_sign_op = 37, RULE_negation_op = 38, RULE_multiplying_op = 39, 
		RULE_adding_op = 40, RULE_logical_op = 41, RULE_relational_op = 42, RULE_bool_lit = 43, 
		RULE_array_lit = 44, RULE_literal_list = 45;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "variable_declaration_part", "variable_declaration", "declaration_list", 
			"initialization", "variable", "literal", "function_declaration_part", 
			"function_declaration", "function_name", "function_parameter", "parameter_list", 
			"function_body", "statement_list", "assignment_statement", "if_statement", 
			"for_statement", "while_statement", "do_while_statement", "break_statement", 
			"continue_statement", "call_statement", "return_statement", "expression_list", 
			"expression", "rela_expr", "logic_expr", "add_expr", "mul_expr", "negation_expr", 
			"sign_expr", "element_expr", "func_expr", "sub_expr", "operative", "index_op", 
			"function_call", "sign_op", "negation_op", "multiplying_op", "adding_op", 
			"logical_op", "relational_op", "bool_lit", "array_lit", "literal_list"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, "'Body'", "'Break'", "'Continue'", "'Do'", "'Else'", "'ElseIf'", 
			"'EndBody'", "'EndIf'", "'EndFor'", "'EndWhile'", "'For'", "'Function'", 
			"'If'", "'Parameter'", "'Return'", "'Then'", "'Var'", "'While'", "'EndDo'", 
			"'True'", "'False'", "'='", "'+'", "'+.'", "'-'", "'-.'", "'*'", "'*.'", 
			"'\\'", "'\\.'", "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", 
			"'>'", "'<='", "'>='", "'=/='", "'<.'", "'>.'", "'<=.'", "'>=.'", "'('", 
			"')'", "'['", "']'", "'{'", "'}'", "';'", "':'", "'.'", "','"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "ID", "BODY", "BREAK", "CONTINUE", "DO", "ELSE", "ELSEIF", "ENDBODY", 
			"ENDIF", "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", 
			"RETURN", "THEN", "VAR", "WHILE", "ENDDO", "TRUE", "FALSE", "ASSIGN", 
			"PLUS", "PLUS_DOT", "MINUS", "MINUS_DOT", "STAR", "STAR_DOT", "DIV", 
			"DIV_DOT", "MOD", "NOT", "AND", "OR", "EQUAL", "NOT_EQUAL", "LESS", "GREATER", 
			"LESS_EQUAL", "GREATER_EQUAL", "EQUAL_DIV_EQUAL", "LESS_DOT", "GREATER_DOT", 
			"LESS_EQUAL_DOT", "GREATER_EQUAL_DOT", "LEFT_PAREN", "RIGHT_PAREN", "LEFT_SQUARE", 
			"RIGHT_SQUARE", "LEFT_CURLY", "RIGHT_CURLY", "SEMI", "COLON", "DOT", 
			"COMMA", "WS", "BLOCK_COMMENT", "UNTERMINATED_COMMENT", "INT_LIT", "FLOAT_LIT", 
			"STRING_LIT", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "BKIT.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public BKITParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public Variable_declaration_partContext variable_declaration_part() {
			return getRuleContext(Variable_declaration_partContext.class,0);
		}
		public Function_declaration_partContext function_declaration_part() {
			return getRuleContext(Function_declaration_partContext.class,0);
		}
		public TerminalNode EOF() { return getToken(BKITParser.EOF, 0); }
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(92);
			variable_declaration_part();
			setState(93);
			function_declaration_part();
			setState(94);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Variable_declaration_partContext extends ParserRuleContext {
		public List<Variable_declarationContext> variable_declaration() {
			return getRuleContexts(Variable_declarationContext.class);
		}
		public Variable_declarationContext variable_declaration(int i) {
			return getRuleContext(Variable_declarationContext.class,i);
		}
		public Variable_declaration_partContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variable_declaration_part; }
	}

	public final Variable_declaration_partContext variable_declaration_part() throws RecognitionException {
		Variable_declaration_partContext _localctx = new Variable_declaration_partContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_variable_declaration_part);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(99);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==VAR) {
				{
				{
				setState(96);
				variable_declaration();
				}
				}
				setState(101);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Variable_declarationContext extends ParserRuleContext {
		public TerminalNode VAR() { return getToken(BKITParser.VAR, 0); }
		public TerminalNode COLON() { return getToken(BKITParser.COLON, 0); }
		public Declaration_listContext declaration_list() {
			return getRuleContext(Declaration_listContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(BKITParser.SEMI, 0); }
		public Variable_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variable_declaration; }
	}

	public final Variable_declarationContext variable_declaration() throws RecognitionException {
		Variable_declarationContext _localctx = new Variable_declarationContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_variable_declaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(102);
			match(VAR);
			setState(103);
			match(COLON);
			setState(104);
			declaration_list();
			setState(105);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Declaration_listContext extends ParserRuleContext {
		public List<InitializationContext> initialization() {
			return getRuleContexts(InitializationContext.class);
		}
		public InitializationContext initialization(int i) {
			return getRuleContext(InitializationContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(BKITParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(BKITParser.COMMA, i);
		}
		public Declaration_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaration_list; }
	}

	public final Declaration_listContext declaration_list() throws RecognitionException {
		Declaration_listContext _localctx = new Declaration_listContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_declaration_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(107);
			initialization();
			setState(112);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(108);
				match(COMMA);
				setState(109);
				initialization();
				}
				}
				setState(114);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class InitializationContext extends ParserRuleContext {
		public VariableContext variable() {
			return getRuleContext(VariableContext.class,0);
		}
		public TerminalNode ASSIGN() { return getToken(BKITParser.ASSIGN, 0); }
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public InitializationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_initialization; }
	}

	public final InitializationContext initialization() throws RecognitionException {
		InitializationContext _localctx = new InitializationContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_initialization);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(115);
			variable();
			setState(118);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ASSIGN) {
				{
				setState(116);
				match(ASSIGN);
				setState(117);
				literal();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VariableContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(BKITParser.ID, 0); }
		public List<TerminalNode> LEFT_SQUARE() { return getTokens(BKITParser.LEFT_SQUARE); }
		public TerminalNode LEFT_SQUARE(int i) {
			return getToken(BKITParser.LEFT_SQUARE, i);
		}
		public List<TerminalNode> INT_LIT() { return getTokens(BKITParser.INT_LIT); }
		public TerminalNode INT_LIT(int i) {
			return getToken(BKITParser.INT_LIT, i);
		}
		public List<TerminalNode> RIGHT_SQUARE() { return getTokens(BKITParser.RIGHT_SQUARE); }
		public TerminalNode RIGHT_SQUARE(int i) {
			return getToken(BKITParser.RIGHT_SQUARE, i);
		}
		public VariableContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variable; }
	}

	public final VariableContext variable() throws RecognitionException {
		VariableContext _localctx = new VariableContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_variable);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(120);
			match(ID);
			setState(126);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==LEFT_SQUARE) {
				{
				{
				setState(121);
				match(LEFT_SQUARE);
				setState(122);
				match(INT_LIT);
				setState(123);
				match(RIGHT_SQUARE);
				}
				}
				setState(128);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LiteralContext extends ParserRuleContext {
		public Bool_litContext bool_lit() {
			return getRuleContext(Bool_litContext.class,0);
		}
		public TerminalNode INT_LIT() { return getToken(BKITParser.INT_LIT, 0); }
		public TerminalNode FLOAT_LIT() { return getToken(BKITParser.FLOAT_LIT, 0); }
		public TerminalNode STRING_LIT() { return getToken(BKITParser.STRING_LIT, 0); }
		public Array_litContext array_lit() {
			return getRuleContext(Array_litContext.class,0);
		}
		public LiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literal; }
	}

	public final LiteralContext literal() throws RecognitionException {
		LiteralContext _localctx = new LiteralContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_literal);
		try {
			setState(134);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case TRUE:
			case FALSE:
				enterOuterAlt(_localctx, 1);
				{
				setState(129);
				bool_lit();
				}
				break;
			case INT_LIT:
				enterOuterAlt(_localctx, 2);
				{
				setState(130);
				match(INT_LIT);
				}
				break;
			case FLOAT_LIT:
				enterOuterAlt(_localctx, 3);
				{
				setState(131);
				match(FLOAT_LIT);
				}
				break;
			case STRING_LIT:
				enterOuterAlt(_localctx, 4);
				{
				setState(132);
				match(STRING_LIT);
				}
				break;
			case LEFT_CURLY:
				enterOuterAlt(_localctx, 5);
				{
				setState(133);
				array_lit();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Function_declaration_partContext extends ParserRuleContext {
		public List<Function_declarationContext> function_declaration() {
			return getRuleContexts(Function_declarationContext.class);
		}
		public Function_declarationContext function_declaration(int i) {
			return getRuleContext(Function_declarationContext.class,i);
		}
		public Function_declaration_partContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_declaration_part; }
	}

	public final Function_declaration_partContext function_declaration_part() throws RecognitionException {
		Function_declaration_partContext _localctx = new Function_declaration_partContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_function_declaration_part);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(139);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==FUNCTION) {
				{
				{
				setState(136);
				function_declaration();
				}
				}
				setState(141);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Function_declarationContext extends ParserRuleContext {
		public Function_nameContext function_name() {
			return getRuleContext(Function_nameContext.class,0);
		}
		public Function_bodyContext function_body() {
			return getRuleContext(Function_bodyContext.class,0);
		}
		public Function_parameterContext function_parameter() {
			return getRuleContext(Function_parameterContext.class,0);
		}
		public Function_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_declaration; }
	}

	public final Function_declarationContext function_declaration() throws RecognitionException {
		Function_declarationContext _localctx = new Function_declarationContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_function_declaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(142);
			function_name();
			setState(144);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==PARAMETER) {
				{
				setState(143);
				function_parameter();
				}
			}

			setState(146);
			function_body();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Function_nameContext extends ParserRuleContext {
		public TerminalNode FUNCTION() { return getToken(BKITParser.FUNCTION, 0); }
		public TerminalNode COLON() { return getToken(BKITParser.COLON, 0); }
		public TerminalNode ID() { return getToken(BKITParser.ID, 0); }
		public Function_nameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_name; }
	}

	public final Function_nameContext function_name() throws RecognitionException {
		Function_nameContext _localctx = new Function_nameContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_function_name);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(148);
			match(FUNCTION);
			setState(149);
			match(COLON);
			setState(150);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Function_parameterContext extends ParserRuleContext {
		public TerminalNode PARAMETER() { return getToken(BKITParser.PARAMETER, 0); }
		public TerminalNode COLON() { return getToken(BKITParser.COLON, 0); }
		public Parameter_listContext parameter_list() {
			return getRuleContext(Parameter_listContext.class,0);
		}
		public Function_parameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_parameter; }
	}

	public final Function_parameterContext function_parameter() throws RecognitionException {
		Function_parameterContext _localctx = new Function_parameterContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_function_parameter);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(152);
			match(PARAMETER);
			setState(153);
			match(COLON);
			setState(154);
			parameter_list();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Parameter_listContext extends ParserRuleContext {
		public List<VariableContext> variable() {
			return getRuleContexts(VariableContext.class);
		}
		public VariableContext variable(int i) {
			return getRuleContext(VariableContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(BKITParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(BKITParser.COMMA, i);
		}
		public Parameter_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameter_list; }
	}

	public final Parameter_listContext parameter_list() throws RecognitionException {
		Parameter_listContext _localctx = new Parameter_listContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_parameter_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(156);
			variable();
			setState(161);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(157);
				match(COMMA);
				setState(158);
				variable();
				}
				}
				setState(163);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Function_bodyContext extends ParserRuleContext {
		public TerminalNode BODY() { return getToken(BKITParser.BODY, 0); }
		public TerminalNode COLON() { return getToken(BKITParser.COLON, 0); }
		public Statement_listContext statement_list() {
			return getRuleContext(Statement_listContext.class,0);
		}
		public TerminalNode ENDBODY() { return getToken(BKITParser.ENDBODY, 0); }
		public TerminalNode DOT() { return getToken(BKITParser.DOT, 0); }
		public Function_bodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_body; }
	}

	public final Function_bodyContext function_body() throws RecognitionException {
		Function_bodyContext _localctx = new Function_bodyContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_function_body);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(164);
			match(BODY);
			setState(165);
			match(COLON);
			setState(166);
			statement_list();
			setState(167);
			match(ENDBODY);
			setState(168);
			match(DOT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Statement_listContext extends ParserRuleContext {
		public List<Variable_declarationContext> variable_declaration() {
			return getRuleContexts(Variable_declarationContext.class);
		}
		public Variable_declarationContext variable_declaration(int i) {
			return getRuleContext(Variable_declarationContext.class,i);
		}
		public List<Assignment_statementContext> assignment_statement() {
			return getRuleContexts(Assignment_statementContext.class);
		}
		public Assignment_statementContext assignment_statement(int i) {
			return getRuleContext(Assignment_statementContext.class,i);
		}
		public List<If_statementContext> if_statement() {
			return getRuleContexts(If_statementContext.class);
		}
		public If_statementContext if_statement(int i) {
			return getRuleContext(If_statementContext.class,i);
		}
		public List<For_statementContext> for_statement() {
			return getRuleContexts(For_statementContext.class);
		}
		public For_statementContext for_statement(int i) {
			return getRuleContext(For_statementContext.class,i);
		}
		public List<While_statementContext> while_statement() {
			return getRuleContexts(While_statementContext.class);
		}
		public While_statementContext while_statement(int i) {
			return getRuleContext(While_statementContext.class,i);
		}
		public List<Do_while_statementContext> do_while_statement() {
			return getRuleContexts(Do_while_statementContext.class);
		}
		public Do_while_statementContext do_while_statement(int i) {
			return getRuleContext(Do_while_statementContext.class,i);
		}
		public List<Break_statementContext> break_statement() {
			return getRuleContexts(Break_statementContext.class);
		}
		public Break_statementContext break_statement(int i) {
			return getRuleContext(Break_statementContext.class,i);
		}
		public List<Continue_statementContext> continue_statement() {
			return getRuleContexts(Continue_statementContext.class);
		}
		public Continue_statementContext continue_statement(int i) {
			return getRuleContext(Continue_statementContext.class,i);
		}
		public List<Call_statementContext> call_statement() {
			return getRuleContexts(Call_statementContext.class);
		}
		public Call_statementContext call_statement(int i) {
			return getRuleContext(Call_statementContext.class,i);
		}
		public List<Return_statementContext> return_statement() {
			return getRuleContexts(Return_statementContext.class);
		}
		public Return_statementContext return_statement(int i) {
			return getRuleContext(Return_statementContext.class,i);
		}
		public Statement_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement_list; }
	}

	public final Statement_listContext statement_list() throws RecognitionException {
		Statement_listContext _localctx = new Statement_listContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_statement_list);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(173);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==VAR) {
				{
				{
				setState(170);
				variable_declaration();
				}
				}
				setState(175);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(187);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					setState(185);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
					case 1:
						{
						setState(176);
						assignment_statement();
						}
						break;
					case 2:
						{
						setState(177);
						if_statement();
						}
						break;
					case 3:
						{
						setState(178);
						for_statement();
						}
						break;
					case 4:
						{
						setState(179);
						while_statement();
						}
						break;
					case 5:
						{
						setState(180);
						do_while_statement();
						}
						break;
					case 6:
						{
						setState(181);
						break_statement();
						}
						break;
					case 7:
						{
						setState(182);
						continue_statement();
						}
						break;
					case 8:
						{
						setState(183);
						call_statement();
						}
						break;
					case 9:
						{
						setState(184);
						return_statement();
						}
						break;
					}
					} 
				}
				setState(189);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Assignment_statementContext extends ParserRuleContext {
		public VariableContext variable() {
			return getRuleContext(VariableContext.class,0);
		}
		public TerminalNode ASSIGN() { return getToken(BKITParser.ASSIGN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(BKITParser.SEMI, 0); }
		public Assignment_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment_statement; }
	}

	public final Assignment_statementContext assignment_statement() throws RecognitionException {
		Assignment_statementContext _localctx = new Assignment_statementContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_assignment_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(190);
			variable();
			setState(191);
			match(ASSIGN);
			setState(192);
			expression();
			setState(193);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class If_statementContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(BKITParser.IF, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> THEN() { return getTokens(BKITParser.THEN); }
		public TerminalNode THEN(int i) {
			return getToken(BKITParser.THEN, i);
		}
		public List<Statement_listContext> statement_list() {
			return getRuleContexts(Statement_listContext.class);
		}
		public Statement_listContext statement_list(int i) {
			return getRuleContext(Statement_listContext.class,i);
		}
		public TerminalNode ENDIF() { return getToken(BKITParser.ENDIF, 0); }
		public TerminalNode DOT() { return getToken(BKITParser.DOT, 0); }
		public List<TerminalNode> ELSEIF() { return getTokens(BKITParser.ELSEIF); }
		public TerminalNode ELSEIF(int i) {
			return getToken(BKITParser.ELSEIF, i);
		}
		public TerminalNode ELSE() { return getToken(BKITParser.ELSE, 0); }
		public If_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_if_statement; }
	}

	public final If_statementContext if_statement() throws RecognitionException {
		If_statementContext _localctx = new If_statementContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_if_statement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(195);
			match(IF);
			setState(196);
			expression();
			setState(197);
			match(THEN);
			setState(198);
			statement_list();
			setState(206);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ELSEIF) {
				{
				{
				setState(199);
				match(ELSEIF);
				setState(200);
				expression();
				setState(201);
				match(THEN);
				setState(202);
				statement_list();
				}
				}
				setState(208);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(211);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELSE) {
				{
				setState(209);
				match(ELSE);
				setState(210);
				statement_list();
				}
			}

			setState(213);
			match(ENDIF);
			setState(214);
			match(DOT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class For_statementContext extends ParserRuleContext {
		public TerminalNode FOR() { return getToken(BKITParser.FOR, 0); }
		public TerminalNode LEFT_PAREN() { return getToken(BKITParser.LEFT_PAREN, 0); }
		public TerminalNode RIGHT_PAREN() { return getToken(BKITParser.RIGHT_PAREN, 0); }
		public TerminalNode DO() { return getToken(BKITParser.DO, 0); }
		public Statement_listContext statement_list() {
			return getRuleContext(Statement_listContext.class,0);
		}
		public TerminalNode ENDFOR() { return getToken(BKITParser.ENDFOR, 0); }
		public TerminalNode DOT() { return getToken(BKITParser.DOT, 0); }
		public TerminalNode ID() { return getToken(BKITParser.ID, 0); }
		public TerminalNode ASSIGN() { return getToken(BKITParser.ASSIGN, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(BKITParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(BKITParser.COMMA, i);
		}
		public For_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_for_statement; }
	}

	public final For_statementContext for_statement() throws RecognitionException {
		For_statementContext _localctx = new For_statementContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_for_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(216);
			match(FOR);
			setState(217);
			match(LEFT_PAREN);
			{
			setState(218);
			match(ID);
			setState(219);
			match(ASSIGN);
			setState(220);
			expression();
			}
			{
			setState(222);
			match(COMMA);
			setState(223);
			expression();
			}
			{
			setState(225);
			match(COMMA);
			setState(226);
			expression();
			}
			setState(228);
			match(RIGHT_PAREN);
			setState(229);
			match(DO);
			setState(230);
			statement_list();
			setState(231);
			match(ENDFOR);
			setState(232);
			match(DOT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class While_statementContext extends ParserRuleContext {
		public TerminalNode WHILE() { return getToken(BKITParser.WHILE, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode DO() { return getToken(BKITParser.DO, 0); }
		public Statement_listContext statement_list() {
			return getRuleContext(Statement_listContext.class,0);
		}
		public TerminalNode ENDWHILE() { return getToken(BKITParser.ENDWHILE, 0); }
		public TerminalNode DOT() { return getToken(BKITParser.DOT, 0); }
		public While_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_while_statement; }
	}

	public final While_statementContext while_statement() throws RecognitionException {
		While_statementContext _localctx = new While_statementContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_while_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(234);
			match(WHILE);
			setState(235);
			expression();
			setState(236);
			match(DO);
			setState(237);
			statement_list();
			setState(238);
			match(ENDWHILE);
			setState(239);
			match(DOT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Do_while_statementContext extends ParserRuleContext {
		public TerminalNode DO() { return getToken(BKITParser.DO, 0); }
		public Statement_listContext statement_list() {
			return getRuleContext(Statement_listContext.class,0);
		}
		public TerminalNode WHILE() { return getToken(BKITParser.WHILE, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode ENDDO() { return getToken(BKITParser.ENDDO, 0); }
		public TerminalNode DOT() { return getToken(BKITParser.DOT, 0); }
		public Do_while_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_do_while_statement; }
	}

	public final Do_while_statementContext do_while_statement() throws RecognitionException {
		Do_while_statementContext _localctx = new Do_while_statementContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_do_while_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(241);
			match(DO);
			setState(242);
			statement_list();
			setState(243);
			match(WHILE);
			setState(244);
			expression();
			setState(245);
			match(ENDDO);
			setState(246);
			match(DOT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Break_statementContext extends ParserRuleContext {
		public TerminalNode BREAK() { return getToken(BKITParser.BREAK, 0); }
		public TerminalNode SEMI() { return getToken(BKITParser.SEMI, 0); }
		public Break_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_break_statement; }
	}

	public final Break_statementContext break_statement() throws RecognitionException {
		Break_statementContext _localctx = new Break_statementContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_break_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(248);
			match(BREAK);
			setState(249);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Continue_statementContext extends ParserRuleContext {
		public TerminalNode CONTINUE() { return getToken(BKITParser.CONTINUE, 0); }
		public TerminalNode SEMI() { return getToken(BKITParser.SEMI, 0); }
		public Continue_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_continue_statement; }
	}

	public final Continue_statementContext continue_statement() throws RecognitionException {
		Continue_statementContext _localctx = new Continue_statementContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_continue_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(251);
			match(CONTINUE);
			setState(252);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Call_statementContext extends ParserRuleContext {
		public Function_callContext function_call() {
			return getRuleContext(Function_callContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(BKITParser.SEMI, 0); }
		public Call_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_call_statement; }
	}

	public final Call_statementContext call_statement() throws RecognitionException {
		Call_statementContext _localctx = new Call_statementContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_call_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(254);
			function_call();
			setState(255);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Return_statementContext extends ParserRuleContext {
		public TerminalNode RETURN() { return getToken(BKITParser.RETURN, 0); }
		public TerminalNode SEMI() { return getToken(BKITParser.SEMI, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Return_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_return_statement; }
	}

	public final Return_statementContext return_statement() throws RecognitionException {
		Return_statementContext _localctx = new Return_statementContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_return_statement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(257);
			match(RETURN);
			setState(259);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << ID) | (1L << TRUE) | (1L << FALSE) | (1L << MINUS) | (1L << MINUS_DOT) | (1L << NOT) | (1L << LEFT_PAREN) | (1L << LEFT_CURLY) | (1L << INT_LIT) | (1L << FLOAT_LIT) | (1L << STRING_LIT))) != 0)) {
				{
				setState(258);
				expression();
				}
			}

			setState(261);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Expression_listContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(BKITParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(BKITParser.COMMA, i);
		}
		public Expression_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression_list; }
	}

	public final Expression_listContext expression_list() throws RecognitionException {
		Expression_listContext _localctx = new Expression_listContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_expression_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(263);
			expression();
			setState(268);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(264);
				match(COMMA);
				setState(265);
				expression();
				}
				}
				setState(270);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionContext extends ParserRuleContext {
		public Rela_exprContext rela_expr() {
			return getRuleContext(Rela_exprContext.class,0);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(271);
			rela_expr();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Rela_exprContext extends ParserRuleContext {
		public List<Logic_exprContext> logic_expr() {
			return getRuleContexts(Logic_exprContext.class);
		}
		public Logic_exprContext logic_expr(int i) {
			return getRuleContext(Logic_exprContext.class,i);
		}
		public Relational_opContext relational_op() {
			return getRuleContext(Relational_opContext.class,0);
		}
		public Rela_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_rela_expr; }
	}

	public final Rela_exprContext rela_expr() throws RecognitionException {
		Rela_exprContext _localctx = new Rela_exprContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_rela_expr);
		try {
			setState(278);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(273);
				logic_expr(0);
				setState(274);
				relational_op();
				setState(275);
				logic_expr(0);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(277);
				logic_expr(0);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Logic_exprContext extends ParserRuleContext {
		public Add_exprContext add_expr() {
			return getRuleContext(Add_exprContext.class,0);
		}
		public Logic_exprContext logic_expr() {
			return getRuleContext(Logic_exprContext.class,0);
		}
		public Logical_opContext logical_op() {
			return getRuleContext(Logical_opContext.class,0);
		}
		public Logic_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logic_expr; }
	}

	public final Logic_exprContext logic_expr() throws RecognitionException {
		return logic_expr(0);
	}

	private Logic_exprContext logic_expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Logic_exprContext _localctx = new Logic_exprContext(_ctx, _parentState);
		Logic_exprContext _prevctx = _localctx;
		int _startState = 52;
		enterRecursionRule(_localctx, 52, RULE_logic_expr, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(281);
			add_expr(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(289);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,16,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Logic_exprContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_logic_expr);
					setState(283);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(284);
					logical_op();
					setState(285);
					add_expr(0);
					}
					} 
				}
				setState(291);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,16,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class Add_exprContext extends ParserRuleContext {
		public Mul_exprContext mul_expr() {
			return getRuleContext(Mul_exprContext.class,0);
		}
		public Add_exprContext add_expr() {
			return getRuleContext(Add_exprContext.class,0);
		}
		public Adding_opContext adding_op() {
			return getRuleContext(Adding_opContext.class,0);
		}
		public Add_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_add_expr; }
	}

	public final Add_exprContext add_expr() throws RecognitionException {
		return add_expr(0);
	}

	private Add_exprContext add_expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Add_exprContext _localctx = new Add_exprContext(_ctx, _parentState);
		Add_exprContext _prevctx = _localctx;
		int _startState = 54;
		enterRecursionRule(_localctx, 54, RULE_add_expr, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(293);
			mul_expr(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(301);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,17,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Add_exprContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_add_expr);
					setState(295);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(296);
					adding_op();
					setState(297);
					mul_expr(0);
					}
					} 
				}
				setState(303);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,17,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class Mul_exprContext extends ParserRuleContext {
		public Negation_exprContext negation_expr() {
			return getRuleContext(Negation_exprContext.class,0);
		}
		public Mul_exprContext mul_expr() {
			return getRuleContext(Mul_exprContext.class,0);
		}
		public Multiplying_opContext multiplying_op() {
			return getRuleContext(Multiplying_opContext.class,0);
		}
		public Mul_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mul_expr; }
	}

	public final Mul_exprContext mul_expr() throws RecognitionException {
		return mul_expr(0);
	}

	private Mul_exprContext mul_expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Mul_exprContext _localctx = new Mul_exprContext(_ctx, _parentState);
		Mul_exprContext _prevctx = _localctx;
		int _startState = 56;
		enterRecursionRule(_localctx, 56, RULE_mul_expr, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(305);
			negation_expr();
			}
			_ctx.stop = _input.LT(-1);
			setState(313);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,18,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Mul_exprContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_mul_expr);
					setState(307);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(308);
					multiplying_op();
					setState(309);
					negation_expr();
					}
					} 
				}
				setState(315);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,18,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class Negation_exprContext extends ParserRuleContext {
		public Negation_opContext negation_op() {
			return getRuleContext(Negation_opContext.class,0);
		}
		public Negation_exprContext negation_expr() {
			return getRuleContext(Negation_exprContext.class,0);
		}
		public Sign_exprContext sign_expr() {
			return getRuleContext(Sign_exprContext.class,0);
		}
		public Negation_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_negation_expr; }
	}

	public final Negation_exprContext negation_expr() throws RecognitionException {
		Negation_exprContext _localctx = new Negation_exprContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_negation_expr);
		try {
			setState(320);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NOT:
				enterOuterAlt(_localctx, 1);
				{
				setState(316);
				negation_op();
				setState(317);
				negation_expr();
				}
				break;
			case ID:
			case TRUE:
			case FALSE:
			case MINUS:
			case MINUS_DOT:
			case LEFT_PAREN:
			case LEFT_CURLY:
			case INT_LIT:
			case FLOAT_LIT:
			case STRING_LIT:
				enterOuterAlt(_localctx, 2);
				{
				setState(319);
				sign_expr();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Sign_exprContext extends ParserRuleContext {
		public Sign_opContext sign_op() {
			return getRuleContext(Sign_opContext.class,0);
		}
		public Sign_exprContext sign_expr() {
			return getRuleContext(Sign_exprContext.class,0);
		}
		public Element_exprContext element_expr() {
			return getRuleContext(Element_exprContext.class,0);
		}
		public Sign_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sign_expr; }
	}

	public final Sign_exprContext sign_expr() throws RecognitionException {
		Sign_exprContext _localctx = new Sign_exprContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_sign_expr);
		try {
			setState(326);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case MINUS:
			case MINUS_DOT:
				enterOuterAlt(_localctx, 1);
				{
				setState(322);
				sign_op();
				setState(323);
				sign_expr();
				}
				break;
			case ID:
			case TRUE:
			case FALSE:
			case LEFT_PAREN:
			case LEFT_CURLY:
			case INT_LIT:
			case FLOAT_LIT:
			case STRING_LIT:
				enterOuterAlt(_localctx, 2);
				{
				setState(325);
				element_expr();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Element_exprContext extends ParserRuleContext {
		public Index_opContext index_op() {
			return getRuleContext(Index_opContext.class,0);
		}
		public Function_callContext function_call() {
			return getRuleContext(Function_callContext.class,0);
		}
		public TerminalNode ID() { return getToken(BKITParser.ID, 0); }
		public Func_exprContext func_expr() {
			return getRuleContext(Func_exprContext.class,0);
		}
		public Element_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_element_expr; }
	}

	public final Element_exprContext element_expr() throws RecognitionException {
		Element_exprContext _localctx = new Element_exprContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_element_expr);
		try {
			setState(334);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,22,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(330);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,21,_ctx) ) {
				case 1:
					{
					setState(328);
					function_call();
					}
					break;
				case 2:
					{
					setState(329);
					match(ID);
					}
					break;
				}
				setState(332);
				index_op();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(333);
				func_expr();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Func_exprContext extends ParserRuleContext {
		public Function_callContext function_call() {
			return getRuleContext(Function_callContext.class,0);
		}
		public Sub_exprContext sub_expr() {
			return getRuleContext(Sub_exprContext.class,0);
		}
		public Func_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_func_expr; }
	}

	public final Func_exprContext func_expr() throws RecognitionException {
		Func_exprContext _localctx = new Func_exprContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_func_expr);
		try {
			setState(338);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,23,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(336);
				function_call();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(337);
				sub_expr();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Sub_exprContext extends ParserRuleContext {
		public TerminalNode LEFT_PAREN() { return getToken(BKITParser.LEFT_PAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RIGHT_PAREN() { return getToken(BKITParser.RIGHT_PAREN, 0); }
		public OperativeContext operative() {
			return getRuleContext(OperativeContext.class,0);
		}
		public Sub_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sub_expr; }
	}

	public final Sub_exprContext sub_expr() throws RecognitionException {
		Sub_exprContext _localctx = new Sub_exprContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_sub_expr);
		try {
			setState(345);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LEFT_PAREN:
				enterOuterAlt(_localctx, 1);
				{
				setState(340);
				match(LEFT_PAREN);
				setState(341);
				expression();
				setState(342);
				match(RIGHT_PAREN);
				}
				break;
			case ID:
			case TRUE:
			case FALSE:
			case LEFT_CURLY:
			case INT_LIT:
			case FLOAT_LIT:
			case STRING_LIT:
				enterOuterAlt(_localctx, 2);
				{
				setState(344);
				operative();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class OperativeContext extends ParserRuleContext {
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public TerminalNode ID() { return getToken(BKITParser.ID, 0); }
		public OperativeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operative; }
	}

	public final OperativeContext operative() throws RecognitionException {
		OperativeContext _localctx = new OperativeContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_operative);
		try {
			setState(349);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case TRUE:
			case FALSE:
			case LEFT_CURLY:
			case INT_LIT:
			case FLOAT_LIT:
			case STRING_LIT:
				enterOuterAlt(_localctx, 1);
				{
				setState(347);
				literal();
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(348);
				match(ID);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Index_opContext extends ParserRuleContext {
		public List<TerminalNode> LEFT_SQUARE() { return getTokens(BKITParser.LEFT_SQUARE); }
		public TerminalNode LEFT_SQUARE(int i) {
			return getToken(BKITParser.LEFT_SQUARE, i);
		}
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> RIGHT_SQUARE() { return getTokens(BKITParser.RIGHT_SQUARE); }
		public TerminalNode RIGHT_SQUARE(int i) {
			return getToken(BKITParser.RIGHT_SQUARE, i);
		}
		public Index_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_index_op; }
	}

	public final Index_opContext index_op() throws RecognitionException {
		Index_opContext _localctx = new Index_opContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_index_op);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(355); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(351);
					match(LEFT_SQUARE);
					setState(352);
					expression();
					setState(353);
					match(RIGHT_SQUARE);
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(357); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,26,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Function_callContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(BKITParser.ID, 0); }
		public TerminalNode LEFT_PAREN() { return getToken(BKITParser.LEFT_PAREN, 0); }
		public TerminalNode RIGHT_PAREN() { return getToken(BKITParser.RIGHT_PAREN, 0); }
		public Expression_listContext expression_list() {
			return getRuleContext(Expression_listContext.class,0);
		}
		public Function_callContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_call; }
	}

	public final Function_callContext function_call() throws RecognitionException {
		Function_callContext _localctx = new Function_callContext(_ctx, getState());
		enterRule(_localctx, 72, RULE_function_call);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(359);
			match(ID);
			setState(360);
			match(LEFT_PAREN);
			setState(362);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << ID) | (1L << TRUE) | (1L << FALSE) | (1L << MINUS) | (1L << MINUS_DOT) | (1L << NOT) | (1L << LEFT_PAREN) | (1L << LEFT_CURLY) | (1L << INT_LIT) | (1L << FLOAT_LIT) | (1L << STRING_LIT))) != 0)) {
				{
				setState(361);
				expression_list();
				}
			}

			setState(364);
			match(RIGHT_PAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Sign_opContext extends ParserRuleContext {
		public TerminalNode MINUS() { return getToken(BKITParser.MINUS, 0); }
		public TerminalNode MINUS_DOT() { return getToken(BKITParser.MINUS_DOT, 0); }
		public Sign_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sign_op; }
	}

	public final Sign_opContext sign_op() throws RecognitionException {
		Sign_opContext _localctx = new Sign_opContext(_ctx, getState());
		enterRule(_localctx, 74, RULE_sign_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(366);
			_la = _input.LA(1);
			if ( !(_la==MINUS || _la==MINUS_DOT) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Negation_opContext extends ParserRuleContext {
		public TerminalNode NOT() { return getToken(BKITParser.NOT, 0); }
		public Negation_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_negation_op; }
	}

	public final Negation_opContext negation_op() throws RecognitionException {
		Negation_opContext _localctx = new Negation_opContext(_ctx, getState());
		enterRule(_localctx, 76, RULE_negation_op);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(368);
			match(NOT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Multiplying_opContext extends ParserRuleContext {
		public TerminalNode STAR() { return getToken(BKITParser.STAR, 0); }
		public TerminalNode STAR_DOT() { return getToken(BKITParser.STAR_DOT, 0); }
		public TerminalNode DIV() { return getToken(BKITParser.DIV, 0); }
		public TerminalNode DIV_DOT() { return getToken(BKITParser.DIV_DOT, 0); }
		public TerminalNode MOD() { return getToken(BKITParser.MOD, 0); }
		public Multiplying_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_multiplying_op; }
	}

	public final Multiplying_opContext multiplying_op() throws RecognitionException {
		Multiplying_opContext _localctx = new Multiplying_opContext(_ctx, getState());
		enterRule(_localctx, 78, RULE_multiplying_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(370);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << STAR) | (1L << STAR_DOT) | (1L << DIV) | (1L << DIV_DOT) | (1L << MOD))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Adding_opContext extends ParserRuleContext {
		public TerminalNode PLUS() { return getToken(BKITParser.PLUS, 0); }
		public TerminalNode PLUS_DOT() { return getToken(BKITParser.PLUS_DOT, 0); }
		public TerminalNode MINUS() { return getToken(BKITParser.MINUS, 0); }
		public TerminalNode MINUS_DOT() { return getToken(BKITParser.MINUS_DOT, 0); }
		public Adding_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_adding_op; }
	}

	public final Adding_opContext adding_op() throws RecognitionException {
		Adding_opContext _localctx = new Adding_opContext(_ctx, getState());
		enterRule(_localctx, 80, RULE_adding_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(372);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << PLUS) | (1L << PLUS_DOT) | (1L << MINUS) | (1L << MINUS_DOT))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Logical_opContext extends ParserRuleContext {
		public TerminalNode AND() { return getToken(BKITParser.AND, 0); }
		public TerminalNode OR() { return getToken(BKITParser.OR, 0); }
		public Logical_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logical_op; }
	}

	public final Logical_opContext logical_op() throws RecognitionException {
		Logical_opContext _localctx = new Logical_opContext(_ctx, getState());
		enterRule(_localctx, 82, RULE_logical_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(374);
			_la = _input.LA(1);
			if ( !(_la==AND || _la==OR) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Relational_opContext extends ParserRuleContext {
		public TerminalNode EQUAL() { return getToken(BKITParser.EQUAL, 0); }
		public TerminalNode NOT_EQUAL() { return getToken(BKITParser.NOT_EQUAL, 0); }
		public TerminalNode LESS() { return getToken(BKITParser.LESS, 0); }
		public TerminalNode LESS_DOT() { return getToken(BKITParser.LESS_DOT, 0); }
		public TerminalNode GREATER() { return getToken(BKITParser.GREATER, 0); }
		public TerminalNode GREATER_DOT() { return getToken(BKITParser.GREATER_DOT, 0); }
		public TerminalNode LESS_EQUAL() { return getToken(BKITParser.LESS_EQUAL, 0); }
		public TerminalNode LESS_EQUAL_DOT() { return getToken(BKITParser.LESS_EQUAL_DOT, 0); }
		public TerminalNode GREATER_EQUAL() { return getToken(BKITParser.GREATER_EQUAL, 0); }
		public TerminalNode GREATER_EQUAL_DOT() { return getToken(BKITParser.GREATER_EQUAL_DOT, 0); }
		public TerminalNode EQUAL_DIV_EQUAL() { return getToken(BKITParser.EQUAL_DIV_EQUAL, 0); }
		public Relational_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_relational_op; }
	}

	public final Relational_opContext relational_op() throws RecognitionException {
		Relational_opContext _localctx = new Relational_opContext(_ctx, getState());
		enterRule(_localctx, 84, RULE_relational_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(376);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << EQUAL) | (1L << NOT_EQUAL) | (1L << LESS) | (1L << GREATER) | (1L << LESS_EQUAL) | (1L << GREATER_EQUAL) | (1L << EQUAL_DIV_EQUAL) | (1L << LESS_DOT) | (1L << GREATER_DOT) | (1L << LESS_EQUAL_DOT) | (1L << GREATER_EQUAL_DOT))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Bool_litContext extends ParserRuleContext {
		public TerminalNode TRUE() { return getToken(BKITParser.TRUE, 0); }
		public TerminalNode FALSE() { return getToken(BKITParser.FALSE, 0); }
		public Bool_litContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bool_lit; }
	}

	public final Bool_litContext bool_lit() throws RecognitionException {
		Bool_litContext _localctx = new Bool_litContext(_ctx, getState());
		enterRule(_localctx, 86, RULE_bool_lit);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(378);
			_la = _input.LA(1);
			if ( !(_la==TRUE || _la==FALSE) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Array_litContext extends ParserRuleContext {
		public TerminalNode LEFT_CURLY() { return getToken(BKITParser.LEFT_CURLY, 0); }
		public TerminalNode RIGHT_CURLY() { return getToken(BKITParser.RIGHT_CURLY, 0); }
		public Literal_listContext literal_list() {
			return getRuleContext(Literal_listContext.class,0);
		}
		public Array_litContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_array_lit; }
	}

	public final Array_litContext array_lit() throws RecognitionException {
		Array_litContext _localctx = new Array_litContext(_ctx, getState());
		enterRule(_localctx, 88, RULE_array_lit);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(380);
			match(LEFT_CURLY);
			{
			setState(381);
			literal_list();
			}
			setState(382);
			match(RIGHT_CURLY);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Literal_listContext extends ParserRuleContext {
		public List<LiteralContext> literal() {
			return getRuleContexts(LiteralContext.class);
		}
		public LiteralContext literal(int i) {
			return getRuleContext(LiteralContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(BKITParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(BKITParser.COMMA, i);
		}
		public Literal_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literal_list; }
	}

	public final Literal_listContext literal_list() throws RecognitionException {
		Literal_listContext _localctx = new Literal_listContext(_ctx, getState());
		enterRule(_localctx, 90, RULE_literal_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(384);
			literal();
			setState(389);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(385);
				match(COMMA);
				setState(386);
				literal();
				}
				}
				setState(391);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 26:
			return logic_expr_sempred((Logic_exprContext)_localctx, predIndex);
		case 27:
			return add_expr_sempred((Add_exprContext)_localctx, predIndex);
		case 28:
			return mul_expr_sempred((Mul_exprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean logic_expr_sempred(Logic_exprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean add_expr_sempred(Add_exprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 1:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean mul_expr_sempred(Mul_exprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 2:
			return precpred(_ctx, 2);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3C\u018b\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\3\2\3\2\3\2\3\2\3\3\7\3d\n\3\f\3\16\3g\13\3\3\4"+
		"\3\4\3\4\3\4\3\4\3\5\3\5\3\5\7\5q\n\5\f\5\16\5t\13\5\3\6\3\6\3\6\5\6y"+
		"\n\6\3\7\3\7\3\7\3\7\7\7\177\n\7\f\7\16\7\u0082\13\7\3\b\3\b\3\b\3\b\3"+
		"\b\5\b\u0089\n\b\3\t\7\t\u008c\n\t\f\t\16\t\u008f\13\t\3\n\3\n\5\n\u0093"+
		"\n\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\7\r\u00a2"+
		"\n\r\f\r\16\r\u00a5\13\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\7\17\u00ae"+
		"\n\17\f\17\16\17\u00b1\13\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3"+
		"\17\7\17\u00bc\n\17\f\17\16\17\u00bf\13\17\3\20\3\20\3\20\3\20\3\20\3"+
		"\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\7\21\u00cf\n\21\f\21\16\21"+
		"\u00d2\13\21\3\21\3\21\5\21\u00d6\n\21\3\21\3\21\3\21\3\22\3\22\3\22\3"+
		"\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3"+
		"\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3"+
		"\24\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30\5\30\u0106"+
		"\n\30\3\30\3\30\3\31\3\31\3\31\7\31\u010d\n\31\f\31\16\31\u0110\13\31"+
		"\3\32\3\32\3\33\3\33\3\33\3\33\3\33\5\33\u0119\n\33\3\34\3\34\3\34\3\34"+
		"\3\34\3\34\3\34\7\34\u0122\n\34\f\34\16\34\u0125\13\34\3\35\3\35\3\35"+
		"\3\35\3\35\3\35\3\35\7\35\u012e\n\35\f\35\16\35\u0131\13\35\3\36\3\36"+
		"\3\36\3\36\3\36\3\36\3\36\7\36\u013a\n\36\f\36\16\36\u013d\13\36\3\37"+
		"\3\37\3\37\3\37\5\37\u0143\n\37\3 \3 \3 \3 \5 \u0149\n \3!\3!\5!\u014d"+
		"\n!\3!\3!\5!\u0151\n!\3\"\3\"\5\"\u0155\n\"\3#\3#\3#\3#\3#\5#\u015c\n"+
		"#\3$\3$\5$\u0160\n$\3%\3%\3%\3%\6%\u0166\n%\r%\16%\u0167\3&\3&\3&\5&\u016d"+
		"\n&\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3.\3.\3/\3"+
		"/\3/\7/\u0186\n/\f/\16/\u0189\13/\3/\2\5\668:\60\2\4\6\b\n\f\16\20\22"+
		"\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\\2\b\3\2\34"+
		"\35\3\2\36\"\3\2\32\35\3\2$%\3\2&\60\3\2\27\30\2\u0183\2^\3\2\2\2\4e\3"+
		"\2\2\2\6h\3\2\2\2\bm\3\2\2\2\nu\3\2\2\2\fz\3\2\2\2\16\u0088\3\2\2\2\20"+
		"\u008d\3\2\2\2\22\u0090\3\2\2\2\24\u0096\3\2\2\2\26\u009a\3\2\2\2\30\u009e"+
		"\3\2\2\2\32\u00a6\3\2\2\2\34\u00af\3\2\2\2\36\u00c0\3\2\2\2 \u00c5\3\2"+
		"\2\2\"\u00da\3\2\2\2$\u00ec\3\2\2\2&\u00f3\3\2\2\2(\u00fa\3\2\2\2*\u00fd"+
		"\3\2\2\2,\u0100\3\2\2\2.\u0103\3\2\2\2\60\u0109\3\2\2\2\62\u0111\3\2\2"+
		"\2\64\u0118\3\2\2\2\66\u011a\3\2\2\28\u0126\3\2\2\2:\u0132\3\2\2\2<\u0142"+
		"\3\2\2\2>\u0148\3\2\2\2@\u0150\3\2\2\2B\u0154\3\2\2\2D\u015b\3\2\2\2F"+
		"\u015f\3\2\2\2H\u0165\3\2\2\2J\u0169\3\2\2\2L\u0170\3\2\2\2N\u0172\3\2"+
		"\2\2P\u0174\3\2\2\2R\u0176\3\2\2\2T\u0178\3\2\2\2V\u017a\3\2\2\2X\u017c"+
		"\3\2\2\2Z\u017e\3\2\2\2\\\u0182\3\2\2\2^_\5\4\3\2_`\5\20\t\2`a\7\2\2\3"+
		"a\3\3\2\2\2bd\5\6\4\2cb\3\2\2\2dg\3\2\2\2ec\3\2\2\2ef\3\2\2\2f\5\3\2\2"+
		"\2ge\3\2\2\2hi\7\24\2\2ij\78\2\2jk\5\b\5\2kl\7\67\2\2l\7\3\2\2\2mr\5\n"+
		"\6\2no\7:\2\2oq\5\n\6\2pn\3\2\2\2qt\3\2\2\2rp\3\2\2\2rs\3\2\2\2s\t\3\2"+
		"\2\2tr\3\2\2\2ux\5\f\7\2vw\7\31\2\2wy\5\16\b\2xv\3\2\2\2xy\3\2\2\2y\13"+
		"\3\2\2\2z\u0080\7\3\2\2{|\7\63\2\2|}\7>\2\2}\177\7\64\2\2~{\3\2\2\2\177"+
		"\u0082\3\2\2\2\u0080~\3\2\2\2\u0080\u0081\3\2\2\2\u0081\r\3\2\2\2\u0082"+
		"\u0080\3\2\2\2\u0083\u0089\5X-\2\u0084\u0089\7>\2\2\u0085\u0089\7?\2\2"+
		"\u0086\u0089\7@\2\2\u0087\u0089\5Z.\2\u0088\u0083\3\2\2\2\u0088\u0084"+
		"\3\2\2\2\u0088\u0085\3\2\2\2\u0088\u0086\3\2\2\2\u0088\u0087\3\2\2\2\u0089"+
		"\17\3\2\2\2\u008a\u008c\5\22\n\2\u008b\u008a\3\2\2\2\u008c\u008f\3\2\2"+
		"\2\u008d\u008b\3\2\2\2\u008d\u008e\3\2\2\2\u008e\21\3\2\2\2\u008f\u008d"+
		"\3\2\2\2\u0090\u0092\5\24\13\2\u0091\u0093\5\26\f\2\u0092\u0091\3\2\2"+
		"\2\u0092\u0093\3\2\2\2\u0093\u0094\3\2\2\2\u0094\u0095\5\32\16\2\u0095"+
		"\23\3\2\2\2\u0096\u0097\7\17\2\2\u0097\u0098\78\2\2\u0098\u0099\7\3\2"+
		"\2\u0099\25\3\2\2\2\u009a\u009b\7\21\2\2\u009b\u009c\78\2\2\u009c\u009d"+
		"\5\30\r\2\u009d\27\3\2\2\2\u009e\u00a3\5\f\7\2\u009f\u00a0\7:\2\2\u00a0"+
		"\u00a2\5\f\7\2\u00a1\u009f\3\2\2\2\u00a2\u00a5\3\2\2\2\u00a3\u00a1\3\2"+
		"\2\2\u00a3\u00a4\3\2\2\2\u00a4\31\3\2\2\2\u00a5\u00a3\3\2\2\2\u00a6\u00a7"+
		"\7\4\2\2\u00a7\u00a8\78\2\2\u00a8\u00a9\5\34\17\2\u00a9\u00aa\7\n\2\2"+
		"\u00aa\u00ab\79\2\2\u00ab\33\3\2\2\2\u00ac\u00ae\5\6\4\2\u00ad\u00ac\3"+
		"\2\2\2\u00ae\u00b1\3\2\2\2\u00af\u00ad\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0"+
		"\u00bd\3\2\2\2\u00b1\u00af\3\2\2\2\u00b2\u00bc\5\36\20\2\u00b3\u00bc\5"+
		" \21\2\u00b4\u00bc\5\"\22\2\u00b5\u00bc\5$\23\2\u00b6\u00bc\5&\24\2\u00b7"+
		"\u00bc\5(\25\2\u00b8\u00bc\5*\26\2\u00b9\u00bc\5,\27\2\u00ba\u00bc\5."+
		"\30\2\u00bb\u00b2\3\2\2\2\u00bb\u00b3\3\2\2\2\u00bb\u00b4\3\2\2\2\u00bb"+
		"\u00b5\3\2\2\2\u00bb\u00b6\3\2\2\2\u00bb\u00b7\3\2\2\2\u00bb\u00b8\3\2"+
		"\2\2\u00bb\u00b9\3\2\2\2\u00bb\u00ba\3\2\2\2\u00bc\u00bf\3\2\2\2\u00bd"+
		"\u00bb\3\2\2\2\u00bd\u00be\3\2\2\2\u00be\35\3\2\2\2\u00bf\u00bd\3\2\2"+
		"\2\u00c0\u00c1\5\f\7\2\u00c1\u00c2\7\31\2\2\u00c2\u00c3\5\62\32\2\u00c3"+
		"\u00c4\7\67\2\2\u00c4\37\3\2\2\2\u00c5\u00c6\7\20\2\2\u00c6\u00c7\5\62"+
		"\32\2\u00c7\u00c8\7\23\2\2\u00c8\u00d0\5\34\17\2\u00c9\u00ca\7\t\2\2\u00ca"+
		"\u00cb\5\62\32\2\u00cb\u00cc\7\23\2\2\u00cc\u00cd\5\34\17\2\u00cd\u00cf"+
		"\3\2\2\2\u00ce\u00c9\3\2\2\2\u00cf\u00d2\3\2\2\2\u00d0\u00ce\3\2\2\2\u00d0"+
		"\u00d1\3\2\2\2\u00d1\u00d5\3\2\2\2\u00d2\u00d0\3\2\2\2\u00d3\u00d4\7\b"+
		"\2\2\u00d4\u00d6\5\34\17\2\u00d5\u00d3\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6"+
		"\u00d7\3\2\2\2\u00d7\u00d8\7\13\2\2\u00d8\u00d9\79\2\2\u00d9!\3\2\2\2"+
		"\u00da\u00db\7\16\2\2\u00db\u00dc\7\61\2\2\u00dc\u00dd\7\3\2\2\u00dd\u00de"+
		"\7\31\2\2\u00de\u00df\5\62\32\2\u00df\u00e0\3\2\2\2\u00e0\u00e1\7:\2\2"+
		"\u00e1\u00e2\5\62\32\2\u00e2\u00e3\3\2\2\2\u00e3\u00e4\7:\2\2\u00e4\u00e5"+
		"\5\62\32\2\u00e5\u00e6\3\2\2\2\u00e6\u00e7\7\62\2\2\u00e7\u00e8\7\7\2"+
		"\2\u00e8\u00e9\5\34\17\2\u00e9\u00ea\7\f\2\2\u00ea\u00eb\79\2\2\u00eb"+
		"#\3\2\2\2\u00ec\u00ed\7\25\2\2\u00ed\u00ee\5\62\32\2\u00ee\u00ef\7\7\2"+
		"\2\u00ef\u00f0\5\34\17\2\u00f0\u00f1\7\r\2\2\u00f1\u00f2\79\2\2\u00f2"+
		"%\3\2\2\2\u00f3\u00f4\7\7\2\2\u00f4\u00f5\5\34\17\2\u00f5\u00f6\7\25\2"+
		"\2\u00f6\u00f7\5\62\32\2\u00f7\u00f8\7\26\2\2\u00f8\u00f9\79\2\2\u00f9"+
		"\'\3\2\2\2\u00fa\u00fb\7\5\2\2\u00fb\u00fc\7\67\2\2\u00fc)\3\2\2\2\u00fd"+
		"\u00fe\7\6\2\2\u00fe\u00ff\7\67\2\2\u00ff+\3\2\2\2\u0100\u0101\5J&\2\u0101"+
		"\u0102\7\67\2\2\u0102-\3\2\2\2\u0103\u0105\7\22\2\2\u0104\u0106\5\62\32"+
		"\2\u0105\u0104\3\2\2\2\u0105\u0106\3\2\2\2\u0106\u0107\3\2\2\2\u0107\u0108"+
		"\7\67\2\2\u0108/\3\2\2\2\u0109\u010e\5\62\32\2\u010a\u010b\7:\2\2\u010b"+
		"\u010d\5\62\32\2\u010c\u010a\3\2\2\2\u010d\u0110\3\2\2\2\u010e\u010c\3"+
		"\2\2\2\u010e\u010f\3\2\2\2\u010f\61\3\2\2\2\u0110\u010e\3\2\2\2\u0111"+
		"\u0112\5\64\33\2\u0112\63\3\2\2\2\u0113\u0114\5\66\34\2\u0114\u0115\5"+
		"V,\2\u0115\u0116\5\66\34\2\u0116\u0119\3\2\2\2\u0117\u0119\5\66\34\2\u0118"+
		"\u0113\3\2\2\2\u0118\u0117\3\2\2\2\u0119\65\3\2\2\2\u011a\u011b\b\34\1"+
		"\2\u011b\u011c\58\35\2\u011c\u0123\3\2\2\2\u011d\u011e\f\4\2\2\u011e\u011f"+
		"\5T+\2\u011f\u0120\58\35\2\u0120\u0122\3\2\2\2\u0121\u011d\3\2\2\2\u0122"+
		"\u0125\3\2\2\2\u0123\u0121\3\2\2\2\u0123\u0124\3\2\2\2\u0124\67\3\2\2"+
		"\2\u0125\u0123\3\2\2\2\u0126\u0127\b\35\1\2\u0127\u0128\5:\36\2\u0128"+
		"\u012f\3\2\2\2\u0129\u012a\f\4\2\2\u012a\u012b\5R*\2\u012b\u012c\5:\36"+
		"\2\u012c\u012e\3\2\2\2\u012d\u0129\3\2\2\2\u012e\u0131\3\2\2\2\u012f\u012d"+
		"\3\2\2\2\u012f\u0130\3\2\2\2\u01309\3\2\2\2\u0131\u012f\3\2\2\2\u0132"+
		"\u0133\b\36\1\2\u0133\u0134\5<\37\2\u0134\u013b\3\2\2\2\u0135\u0136\f"+
		"\4\2\2\u0136\u0137\5P)\2\u0137\u0138\5<\37\2\u0138\u013a\3\2\2\2\u0139"+
		"\u0135\3\2\2\2\u013a\u013d\3\2\2\2\u013b\u0139\3\2\2\2\u013b\u013c\3\2"+
		"\2\2\u013c;\3\2\2\2\u013d\u013b\3\2\2\2\u013e\u013f\5N(\2\u013f\u0140"+
		"\5<\37\2\u0140\u0143\3\2\2\2\u0141\u0143\5> \2\u0142\u013e\3\2\2\2\u0142"+
		"\u0141\3\2\2\2\u0143=\3\2\2\2\u0144\u0145\5L\'\2\u0145\u0146\5> \2\u0146"+
		"\u0149\3\2\2\2\u0147\u0149\5@!\2\u0148\u0144\3\2\2\2\u0148\u0147\3\2\2"+
		"\2\u0149?\3\2\2\2\u014a\u014d\5J&\2\u014b\u014d\7\3\2\2\u014c\u014a\3"+
		"\2\2\2\u014c\u014b\3\2\2\2\u014d\u014e\3\2\2\2\u014e\u0151\5H%\2\u014f"+
		"\u0151\5B\"\2\u0150\u014c\3\2\2\2\u0150\u014f\3\2\2\2\u0151A\3\2\2\2\u0152"+
		"\u0155\5J&\2\u0153\u0155\5D#\2\u0154\u0152\3\2\2\2\u0154\u0153\3\2\2\2"+
		"\u0155C\3\2\2\2\u0156\u0157\7\61\2\2\u0157\u0158\5\62\32\2\u0158\u0159"+
		"\7\62\2\2\u0159\u015c\3\2\2\2\u015a\u015c\5F$\2\u015b\u0156\3\2\2\2\u015b"+
		"\u015a\3\2\2\2\u015cE\3\2\2\2\u015d\u0160\5\16\b\2\u015e\u0160\7\3\2\2"+
		"\u015f\u015d\3\2\2\2\u015f\u015e\3\2\2\2\u0160G\3\2\2\2\u0161\u0162\7"+
		"\63\2\2\u0162\u0163\5\62\32\2\u0163\u0164\7\64\2\2\u0164\u0166\3\2\2\2"+
		"\u0165\u0161\3\2\2\2\u0166\u0167\3\2\2\2\u0167\u0165\3\2\2\2\u0167\u0168"+
		"\3\2\2\2\u0168I\3\2\2\2\u0169\u016a\7\3\2\2\u016a\u016c\7\61\2\2\u016b"+
		"\u016d\5\60\31\2\u016c\u016b\3\2\2\2\u016c\u016d\3\2\2\2\u016d\u016e\3"+
		"\2\2\2\u016e\u016f\7\62\2\2\u016fK\3\2\2\2\u0170\u0171\t\2\2\2\u0171M"+
		"\3\2\2\2\u0172\u0173\7#\2\2\u0173O\3\2\2\2\u0174\u0175\t\3\2\2\u0175Q"+
		"\3\2\2\2\u0176\u0177\t\4\2\2\u0177S\3\2\2\2\u0178\u0179\t\5\2\2\u0179"+
		"U\3\2\2\2\u017a\u017b\t\6\2\2\u017bW\3\2\2\2\u017c\u017d\t\7\2\2\u017d"+
		"Y\3\2\2\2\u017e\u017f\7\65\2\2\u017f\u0180\5\\/\2\u0180\u0181\7\66\2\2"+
		"\u0181[\3\2\2\2\u0182\u0187\5\16\b\2\u0183\u0184\7:\2\2\u0184\u0186\5"+
		"\16\b\2\u0185\u0183\3\2\2\2\u0186\u0189\3\2\2\2\u0187\u0185\3\2\2\2\u0187"+
		"\u0188\3\2\2\2\u0188]\3\2\2\2\u0189\u0187\3\2\2\2\37erx\u0080\u0088\u008d"+
		"\u0092\u00a3\u00af\u00bb\u00bd\u00d0\u00d5\u0105\u010e\u0118\u0123\u012f"+
		"\u013b\u0142\u0148\u014c\u0150\u0154\u015b\u015f\u0167\u016c\u0187";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}