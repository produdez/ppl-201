// Generated from BKIT.g4 by ANTLR 4.8
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
		RULE_array_element = 6, RULE_index_operator = 7, RULE_literal = 8, RULE_function_declaration_part = 9, 
		RULE_function_declaration = 10, RULE_function_name = 11, RULE_function_parameter = 12, 
		RULE_parameter_list = 13, RULE_function_body = 14, RULE_statement_list = 15, 
		RULE_assignment_statement = 16, RULE_if_statement = 17, RULE_for_statement = 18, 
		RULE_while_statement = 19, RULE_do_while_statement = 20, RULE_break_statement = 21, 
		RULE_continue_statement = 22, RULE_call_statement = 23, RULE_return_statement = 24, 
		RULE_expression_list = 25, RULE_expression = 26, RULE_expression2 = 27, 
		RULE_function_call = 28, RULE_sign_op = 29, RULE_negation_op = 30, RULE_multiplying_op = 31, 
		RULE_adding_op = 32, RULE_logical_op = 33, RULE_relational_op = 34, RULE_bool_lit = 35, 
		RULE_array_lit = 36, RULE_literal_list = 37;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "variable_declaration_part", "variable_declaration", "declaration_list", 
			"initialization", "variable", "array_element", "index_operator", "literal", 
			"function_declaration_part", "function_declaration", "function_name", 
			"function_parameter", "parameter_list", "function_body", "statement_list", 
			"assignment_statement", "if_statement", "for_statement", "while_statement", 
			"do_while_statement", "break_statement", "continue_statement", "call_statement", 
			"return_statement", "expression_list", "expression", "expression2", "function_call", 
			"sign_op", "negation_op", "multiplying_op", "adding_op", "logical_op", 
			"relational_op", "bool_lit", "array_lit", "literal_list"
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterProgram(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitProgram(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(76);
			variable_declaration_part();
			setState(77);
			function_declaration_part();
			setState(78);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterVariable_declaration_part(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitVariable_declaration_part(this);
		}
	}

	public final Variable_declaration_partContext variable_declaration_part() throws RecognitionException {
		Variable_declaration_partContext _localctx = new Variable_declaration_partContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_variable_declaration_part);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(83);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==VAR) {
				{
				{
				setState(80);
				variable_declaration();
				}
				}
				setState(85);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterVariable_declaration(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitVariable_declaration(this);
		}
	}

	public final Variable_declarationContext variable_declaration() throws RecognitionException {
		Variable_declarationContext _localctx = new Variable_declarationContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_variable_declaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(86);
			match(VAR);
			setState(87);
			match(COLON);
			setState(88);
			declaration_list();
			setState(89);
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
		public List<VariableContext> variable() {
			return getRuleContexts(VariableContext.class);
		}
		public VariableContext variable(int i) {
			return getRuleContext(VariableContext.class,i);
		}
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterDeclaration_list(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitDeclaration_list(this);
		}
	}

	public final Declaration_listContext declaration_list() throws RecognitionException {
		Declaration_listContext _localctx = new Declaration_listContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_declaration_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(93);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				{
				setState(91);
				variable();
				}
				break;
			case 2:
				{
				setState(92);
				initialization();
				}
				break;
			}
			setState(102);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(95);
				match(COMMA);
				setState(98);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
				case 1:
					{
					setState(96);
					variable();
					}
					break;
				case 2:
					{
					setState(97);
					initialization();
					}
					break;
				}
				}
				}
				setState(104);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterInitialization(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitInitialization(this);
		}
	}

	public final InitializationContext initialization() throws RecognitionException {
		InitializationContext _localctx = new InitializationContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_initialization);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(105);
			variable();
			setState(106);
			match(ASSIGN);
			setState(107);
			literal();
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
		public Array_elementContext array_element() {
			return getRuleContext(Array_elementContext.class,0);
		}
		public VariableContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variable; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterVariable(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitVariable(this);
		}
	}

	public final VariableContext variable() throws RecognitionException {
		VariableContext _localctx = new VariableContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_variable);
		try {
			setState(111);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(109);
				match(ID);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(110);
				array_element();
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

	public static class Array_elementContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(BKITParser.ID, 0); }
		public Index_operatorContext index_operator() {
			return getRuleContext(Index_operatorContext.class,0);
		}
		public Array_elementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_array_element; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterArray_element(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitArray_element(this);
		}
	}

	public final Array_elementContext array_element() throws RecognitionException {
		Array_elementContext _localctx = new Array_elementContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_array_element);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(113);
			match(ID);
			setState(114);
			index_operator();
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

	public static class Index_operatorContext extends ParserRuleContext {
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
		public Index_operatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_index_operator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterIndex_operator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitIndex_operator(this);
		}
	}

	public final Index_operatorContext index_operator() throws RecognitionException {
		Index_operatorContext _localctx = new Index_operatorContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_index_operator);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(120); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(116);
					match(LEFT_SQUARE);
					setState(117);
					expression();
					setState(118);
					match(RIGHT_SQUARE);
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(122); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterLiteral(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitLiteral(this);
		}
	}

	public final LiteralContext literal() throws RecognitionException {
		LiteralContext _localctx = new LiteralContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_literal);
		try {
			setState(129);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case TRUE:
			case FALSE:
				enterOuterAlt(_localctx, 1);
				{
				setState(124);
				bool_lit();
				}
				break;
			case INT_LIT:
				enterOuterAlt(_localctx, 2);
				{
				setState(125);
				match(INT_LIT);
				}
				break;
			case FLOAT_LIT:
				enterOuterAlt(_localctx, 3);
				{
				setState(126);
				match(FLOAT_LIT);
				}
				break;
			case STRING_LIT:
				enterOuterAlt(_localctx, 4);
				{
				setState(127);
				match(STRING_LIT);
				}
				break;
			case LEFT_CURLY:
				enterOuterAlt(_localctx, 5);
				{
				setState(128);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterFunction_declaration_part(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitFunction_declaration_part(this);
		}
	}

	public final Function_declaration_partContext function_declaration_part() throws RecognitionException {
		Function_declaration_partContext _localctx = new Function_declaration_partContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_function_declaration_part);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(134);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==FUNCTION) {
				{
				{
				setState(131);
				function_declaration();
				}
				}
				setState(136);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterFunction_declaration(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitFunction_declaration(this);
		}
	}

	public final Function_declarationContext function_declaration() throws RecognitionException {
		Function_declarationContext _localctx = new Function_declarationContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_function_declaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(137);
			function_name();
			setState(139);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==PARAMETER) {
				{
				setState(138);
				function_parameter();
				}
			}

			setState(141);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterFunction_name(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitFunction_name(this);
		}
	}

	public final Function_nameContext function_name() throws RecognitionException {
		Function_nameContext _localctx = new Function_nameContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_function_name);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(143);
			match(FUNCTION);
			setState(144);
			match(COLON);
			setState(145);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterFunction_parameter(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitFunction_parameter(this);
		}
	}

	public final Function_parameterContext function_parameter() throws RecognitionException {
		Function_parameterContext _localctx = new Function_parameterContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_function_parameter);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(147);
			match(PARAMETER);
			setState(148);
			match(COLON);
			setState(149);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterParameter_list(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitParameter_list(this);
		}
	}

	public final Parameter_listContext parameter_list() throws RecognitionException {
		Parameter_listContext _localctx = new Parameter_listContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_parameter_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(151);
			variable();
			setState(156);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(152);
				match(COMMA);
				setState(153);
				variable();
				}
				}
				setState(158);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterFunction_body(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitFunction_body(this);
		}
	}

	public final Function_bodyContext function_body() throws RecognitionException {
		Function_bodyContext _localctx = new Function_bodyContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_function_body);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(159);
			match(BODY);
			setState(160);
			match(COLON);
			setState(161);
			statement_list();
			setState(162);
			match(ENDBODY);
			setState(163);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterStatement_list(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitStatement_list(this);
		}
	}

	public final Statement_listContext statement_list() throws RecognitionException {
		Statement_listContext _localctx = new Statement_listContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_statement_list);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(168);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==VAR) {
				{
				{
				setState(165);
				variable_declaration();
				}
				}
				setState(170);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(182);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					setState(180);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
					case 1:
						{
						setState(171);
						assignment_statement();
						}
						break;
					case 2:
						{
						setState(172);
						if_statement();
						}
						break;
					case 3:
						{
						setState(173);
						for_statement();
						}
						break;
					case 4:
						{
						setState(174);
						while_statement();
						}
						break;
					case 5:
						{
						setState(175);
						do_while_statement();
						}
						break;
					case 6:
						{
						setState(176);
						break_statement();
						}
						break;
					case 7:
						{
						setState(177);
						continue_statement();
						}
						break;
					case 8:
						{
						setState(178);
						call_statement();
						}
						break;
					case 9:
						{
						setState(179);
						return_statement();
						}
						break;
					}
					} 
				}
				setState(184);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterAssignment_statement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitAssignment_statement(this);
		}
	}

	public final Assignment_statementContext assignment_statement() throws RecognitionException {
		Assignment_statementContext _localctx = new Assignment_statementContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_assignment_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(185);
			variable();
			setState(186);
			match(ASSIGN);
			setState(187);
			expression();
			setState(188);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterIf_statement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitIf_statement(this);
		}
	}

	public final If_statementContext if_statement() throws RecognitionException {
		If_statementContext _localctx = new If_statementContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_if_statement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(190);
			match(IF);
			setState(191);
			expression();
			setState(192);
			match(THEN);
			setState(193);
			statement_list();
			setState(201);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ELSEIF) {
				{
				{
				setState(194);
				match(ELSEIF);
				setState(195);
				expression();
				setState(196);
				match(THEN);
				setState(197);
				statement_list();
				}
				}
				setState(203);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(206);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELSE) {
				{
				setState(204);
				match(ELSE);
				setState(205);
				statement_list();
				}
			}

			setState(208);
			match(ENDIF);
			setState(209);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterFor_statement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitFor_statement(this);
		}
	}

	public final For_statementContext for_statement() throws RecognitionException {
		For_statementContext _localctx = new For_statementContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_for_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(211);
			match(FOR);
			setState(212);
			match(LEFT_PAREN);
			{
			setState(213);
			match(ID);
			setState(214);
			match(ASSIGN);
			setState(215);
			expression();
			}
			{
			setState(217);
			match(COMMA);
			setState(218);
			expression();
			}
			{
			setState(220);
			match(COMMA);
			setState(221);
			expression();
			}
			setState(223);
			match(RIGHT_PAREN);
			setState(224);
			match(DO);
			setState(225);
			statement_list();
			setState(226);
			match(ENDFOR);
			setState(227);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterWhile_statement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitWhile_statement(this);
		}
	}

	public final While_statementContext while_statement() throws RecognitionException {
		While_statementContext _localctx = new While_statementContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_while_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(229);
			match(WHILE);
			setState(230);
			expression();
			setState(231);
			match(DO);
			setState(232);
			statement_list();
			setState(233);
			match(ENDWHILE);
			setState(234);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterDo_while_statement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitDo_while_statement(this);
		}
	}

	public final Do_while_statementContext do_while_statement() throws RecognitionException {
		Do_while_statementContext _localctx = new Do_while_statementContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_do_while_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(236);
			match(DO);
			setState(237);
			statement_list();
			setState(238);
			match(WHILE);
			setState(239);
			expression();
			setState(240);
			match(ENDDO);
			setState(241);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterBreak_statement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitBreak_statement(this);
		}
	}

	public final Break_statementContext break_statement() throws RecognitionException {
		Break_statementContext _localctx = new Break_statementContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_break_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(243);
			match(BREAK);
			setState(244);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterContinue_statement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitContinue_statement(this);
		}
	}

	public final Continue_statementContext continue_statement() throws RecognitionException {
		Continue_statementContext _localctx = new Continue_statementContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_continue_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(246);
			match(CONTINUE);
			setState(247);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterCall_statement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitCall_statement(this);
		}
	}

	public final Call_statementContext call_statement() throws RecognitionException {
		Call_statementContext _localctx = new Call_statementContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_call_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(249);
			function_call();
			setState(250);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterReturn_statement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitReturn_statement(this);
		}
	}

	public final Return_statementContext return_statement() throws RecognitionException {
		Return_statementContext _localctx = new Return_statementContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_return_statement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(252);
			match(RETURN);
			setState(254);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << ID) | (1L << TRUE) | (1L << FALSE) | (1L << MINUS) | (1L << MINUS_DOT) | (1L << NOT) | (1L << LEFT_PAREN) | (1L << LEFT_SQUARE) | (1L << LEFT_CURLY) | (1L << INT_LIT) | (1L << FLOAT_LIT) | (1L << STRING_LIT))) != 0)) {
				{
				setState(253);
				expression();
				}
			}

			setState(256);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterExpression_list(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitExpression_list(this);
		}
	}

	public final Expression_listContext expression_list() throws RecognitionException {
		Expression_listContext _localctx = new Expression_listContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_expression_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(258);
			expression();
			setState(263);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(259);
				match(COMMA);
				setState(260);
				expression();
				}
				}
				setState(265);
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
		public List<Expression2Context> expression2() {
			return getRuleContexts(Expression2Context.class);
		}
		public Expression2Context expression2(int i) {
			return getRuleContext(Expression2Context.class,i);
		}
		public Relational_opContext relational_op() {
			return getRuleContext(Relational_opContext.class,0);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitExpression(this);
		}
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_expression);
		try {
			setState(271);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,17,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(266);
				expression2(0);
				setState(267);
				relational_op();
				setState(268);
				expression2(0);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(270);
				expression2(0);
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

	public static class Expression2Context extends ParserRuleContext {
		public TerminalNode LEFT_PAREN() { return getToken(BKITParser.LEFT_PAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RIGHT_PAREN() { return getToken(BKITParser.RIGHT_PAREN, 0); }
		public Function_callContext function_call() {
			return getRuleContext(Function_callContext.class,0);
		}
		public Index_operatorContext index_operator() {
			return getRuleContext(Index_operatorContext.class,0);
		}
		public Sign_opContext sign_op() {
			return getRuleContext(Sign_opContext.class,0);
		}
		public List<Expression2Context> expression2() {
			return getRuleContexts(Expression2Context.class);
		}
		public Expression2Context expression2(int i) {
			return getRuleContext(Expression2Context.class,i);
		}
		public Negation_opContext negation_op() {
			return getRuleContext(Negation_opContext.class,0);
		}
		public VariableContext variable() {
			return getRuleContext(VariableContext.class,0);
		}
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public Multiplying_opContext multiplying_op() {
			return getRuleContext(Multiplying_opContext.class,0);
		}
		public Adding_opContext adding_op() {
			return getRuleContext(Adding_opContext.class,0);
		}
		public Logical_opContext logical_op() {
			return getRuleContext(Logical_opContext.class,0);
		}
		public Expression2Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression2; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterExpression2(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitExpression2(this);
		}
	}

	public final Expression2Context expression2() throws RecognitionException {
		return expression2(0);
	}

	private Expression2Context expression2(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Expression2Context _localctx = new Expression2Context(_ctx, _parentState);
		Expression2Context _prevctx = _localctx;
		int _startState = 54;
		enterRecursionRule(_localctx, 54, RULE_expression2, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(288);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,18,_ctx) ) {
			case 1:
				{
				setState(274);
				match(LEFT_PAREN);
				setState(275);
				expression();
				setState(276);
				match(RIGHT_PAREN);
				}
				break;
			case 2:
				{
				setState(278);
				function_call();
				}
				break;
			case 3:
				{
				setState(279);
				index_operator();
				}
				break;
			case 4:
				{
				setState(280);
				sign_op();
				setState(281);
				expression2(7);
				}
				break;
			case 5:
				{
				setState(283);
				negation_op();
				setState(284);
				expression2(6);
				}
				break;
			case 6:
				{
				setState(286);
				variable();
				}
				break;
			case 7:
				{
				setState(287);
				literal();
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(304);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,20,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(302);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,19,_ctx) ) {
					case 1:
						{
						_localctx = new Expression2Context(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression2);
						setState(290);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(291);
						multiplying_op();
						setState(292);
						expression2(6);
						}
						break;
					case 2:
						{
						_localctx = new Expression2Context(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression2);
						setState(294);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(295);
						adding_op();
						setState(296);
						expression2(5);
						}
						break;
					case 3:
						{
						_localctx = new Expression2Context(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression2);
						setState(298);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(299);
						logical_op();
						setState(300);
						expression2(4);
						}
						break;
					}
					} 
				}
				setState(306);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,20,_ctx);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterFunction_call(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitFunction_call(this);
		}
	}

	public final Function_callContext function_call() throws RecognitionException {
		Function_callContext _localctx = new Function_callContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_function_call);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(307);
			match(ID);
			setState(308);
			match(LEFT_PAREN);
			setState(310);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << ID) | (1L << TRUE) | (1L << FALSE) | (1L << MINUS) | (1L << MINUS_DOT) | (1L << NOT) | (1L << LEFT_PAREN) | (1L << LEFT_SQUARE) | (1L << LEFT_CURLY) | (1L << INT_LIT) | (1L << FLOAT_LIT) | (1L << STRING_LIT))) != 0)) {
				{
				setState(309);
				expression_list();
				}
			}

			setState(312);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterSign_op(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitSign_op(this);
		}
	}

	public final Sign_opContext sign_op() throws RecognitionException {
		Sign_opContext _localctx = new Sign_opContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_sign_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(314);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterNegation_op(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitNegation_op(this);
		}
	}

	public final Negation_opContext negation_op() throws RecognitionException {
		Negation_opContext _localctx = new Negation_opContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_negation_op);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(316);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterMultiplying_op(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitMultiplying_op(this);
		}
	}

	public final Multiplying_opContext multiplying_op() throws RecognitionException {
		Multiplying_opContext _localctx = new Multiplying_opContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_multiplying_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(318);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterAdding_op(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitAdding_op(this);
		}
	}

	public final Adding_opContext adding_op() throws RecognitionException {
		Adding_opContext _localctx = new Adding_opContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_adding_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(320);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterLogical_op(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitLogical_op(this);
		}
	}

	public final Logical_opContext logical_op() throws RecognitionException {
		Logical_opContext _localctx = new Logical_opContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_logical_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(322);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterRelational_op(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitRelational_op(this);
		}
	}

	public final Relational_opContext relational_op() throws RecognitionException {
		Relational_opContext _localctx = new Relational_opContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_relational_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(324);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterBool_lit(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitBool_lit(this);
		}
	}

	public final Bool_litContext bool_lit() throws RecognitionException {
		Bool_litContext _localctx = new Bool_litContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_bool_lit);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(326);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterArray_lit(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitArray_lit(this);
		}
	}

	public final Array_litContext array_lit() throws RecognitionException {
		Array_litContext _localctx = new Array_litContext(_ctx, getState());
		enterRule(_localctx, 72, RULE_array_lit);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(328);
			match(LEFT_CURLY);
			{
			setState(329);
			literal_list();
			}
			setState(330);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterLiteral_list(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitLiteral_list(this);
		}
	}

	public final Literal_listContext literal_list() throws RecognitionException {
		Literal_listContext _localctx = new Literal_listContext(_ctx, getState());
		enterRule(_localctx, 74, RULE_literal_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(332);
			literal();
			setState(337);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(333);
				match(COMMA);
				setState(334);
				literal();
				}
				}
				setState(339);
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
		case 27:
			return expression2_sempred((Expression2Context)_localctx, predIndex);
		}
		return true;
	}
	private boolean expression2_sempred(Expression2Context _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 5);
		case 1:
			return precpred(_ctx, 4);
		case 2:
			return precpred(_ctx, 3);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3C\u0157\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\3\2\3\2\3\2\3\2\3\3\7\3T\n"+
		"\3\f\3\16\3W\13\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\5\5`\n\5\3\5\3\5\3\5\5\5"+
		"e\n\5\7\5g\n\5\f\5\16\5j\13\5\3\6\3\6\3\6\3\6\3\7\3\7\5\7r\n\7\3\b\3\b"+
		"\3\b\3\t\3\t\3\t\3\t\6\t{\n\t\r\t\16\t|\3\n\3\n\3\n\3\n\3\n\5\n\u0084"+
		"\n\n\3\13\7\13\u0087\n\13\f\13\16\13\u008a\13\13\3\f\3\f\5\f\u008e\n\f"+
		"\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17\7\17\u009d"+
		"\n\17\f\17\16\17\u00a0\13\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\7\21\u00a9"+
		"\n\21\f\21\16\21\u00ac\13\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3"+
		"\21\7\21\u00b7\n\21\f\21\16\21\u00ba\13\21\3\22\3\22\3\22\3\22\3\22\3"+
		"\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\7\23\u00ca\n\23\f\23\16\23"+
		"\u00cd\13\23\3\23\3\23\5\23\u00d1\n\23\3\23\3\23\3\23\3\24\3\24\3\24\3"+
		"\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3"+
		"\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3"+
		"\26\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32\5\32\u0101"+
		"\n\32\3\32\3\32\3\33\3\33\3\33\7\33\u0108\n\33\f\33\16\33\u010b\13\33"+
		"\3\34\3\34\3\34\3\34\3\34\5\34\u0112\n\34\3\35\3\35\3\35\3\35\3\35\3\35"+
		"\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u0123\n\35\3\35\3\35"+
		"\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\7\35\u0131\n\35\f\35"+
		"\16\35\u0134\13\35\3\36\3\36\3\36\5\36\u0139\n\36\3\36\3\36\3\37\3\37"+
		"\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3&\3&\3\'\3\'\3\'\7\'\u0152"+
		"\n\'\f\'\16\'\u0155\13\'\3\'\2\38(\2\4\6\b\n\f\16\20\22\24\26\30\32\34"+
		"\36 \"$&(*,.\60\62\64\668:<>@BDFHJL\2\b\3\2\34\35\3\2\36\"\3\2\32\35\3"+
		"\2$%\3\2&\60\3\2\27\30\2\u0157\2N\3\2\2\2\4U\3\2\2\2\6X\3\2\2\2\b_\3\2"+
		"\2\2\nk\3\2\2\2\fq\3\2\2\2\16s\3\2\2\2\20z\3\2\2\2\22\u0083\3\2\2\2\24"+
		"\u0088\3\2\2\2\26\u008b\3\2\2\2\30\u0091\3\2\2\2\32\u0095\3\2\2\2\34\u0099"+
		"\3\2\2\2\36\u00a1\3\2\2\2 \u00aa\3\2\2\2\"\u00bb\3\2\2\2$\u00c0\3\2\2"+
		"\2&\u00d5\3\2\2\2(\u00e7\3\2\2\2*\u00ee\3\2\2\2,\u00f5\3\2\2\2.\u00f8"+
		"\3\2\2\2\60\u00fb\3\2\2\2\62\u00fe\3\2\2\2\64\u0104\3\2\2\2\66\u0111\3"+
		"\2\2\28\u0122\3\2\2\2:\u0135\3\2\2\2<\u013c\3\2\2\2>\u013e\3\2\2\2@\u0140"+
		"\3\2\2\2B\u0142\3\2\2\2D\u0144\3\2\2\2F\u0146\3\2\2\2H\u0148\3\2\2\2J"+
		"\u014a\3\2\2\2L\u014e\3\2\2\2NO\5\4\3\2OP\5\24\13\2PQ\7\2\2\3Q\3\3\2\2"+
		"\2RT\5\6\4\2SR\3\2\2\2TW\3\2\2\2US\3\2\2\2UV\3\2\2\2V\5\3\2\2\2WU\3\2"+
		"\2\2XY\7\24\2\2YZ\78\2\2Z[\5\b\5\2[\\\7\67\2\2\\\7\3\2\2\2]`\5\f\7\2^"+
		"`\5\n\6\2_]\3\2\2\2_^\3\2\2\2`h\3\2\2\2ad\7:\2\2be\5\f\7\2ce\5\n\6\2d"+
		"b\3\2\2\2dc\3\2\2\2eg\3\2\2\2fa\3\2\2\2gj\3\2\2\2hf\3\2\2\2hi\3\2\2\2"+
		"i\t\3\2\2\2jh\3\2\2\2kl\5\f\7\2lm\7\31\2\2mn\5\22\n\2n\13\3\2\2\2or\7"+
		"\3\2\2pr\5\16\b\2qo\3\2\2\2qp\3\2\2\2r\r\3\2\2\2st\7\3\2\2tu\5\20\t\2"+
		"u\17\3\2\2\2vw\7\63\2\2wx\5\66\34\2xy\7\64\2\2y{\3\2\2\2zv\3\2\2\2{|\3"+
		"\2\2\2|z\3\2\2\2|}\3\2\2\2}\21\3\2\2\2~\u0084\5H%\2\177\u0084\7>\2\2\u0080"+
		"\u0084\7?\2\2\u0081\u0084\7@\2\2\u0082\u0084\5J&\2\u0083~\3\2\2\2\u0083"+
		"\177\3\2\2\2\u0083\u0080\3\2\2\2\u0083\u0081\3\2\2\2\u0083\u0082\3\2\2"+
		"\2\u0084\23\3\2\2\2\u0085\u0087\5\26\f\2\u0086\u0085\3\2\2\2\u0087\u008a"+
		"\3\2\2\2\u0088\u0086\3\2\2\2\u0088\u0089\3\2\2\2\u0089\25\3\2\2\2\u008a"+
		"\u0088\3\2\2\2\u008b\u008d\5\30\r\2\u008c\u008e\5\32\16\2\u008d\u008c"+
		"\3\2\2\2\u008d\u008e\3\2\2\2\u008e\u008f\3\2\2\2\u008f\u0090\5\36\20\2"+
		"\u0090\27\3\2\2\2\u0091\u0092\7\17\2\2\u0092\u0093\78\2\2\u0093\u0094"+
		"\7\3\2\2\u0094\31\3\2\2\2\u0095\u0096\7\21\2\2\u0096\u0097\78\2\2\u0097"+
		"\u0098\5\34\17\2\u0098\33\3\2\2\2\u0099\u009e\5\f\7\2\u009a\u009b\7:\2"+
		"\2\u009b\u009d\5\f\7\2\u009c\u009a\3\2\2\2\u009d\u00a0\3\2\2\2\u009e\u009c"+
		"\3\2\2\2\u009e\u009f\3\2\2\2\u009f\35\3\2\2\2\u00a0\u009e\3\2\2\2\u00a1"+
		"\u00a2\7\4\2\2\u00a2\u00a3\78\2\2\u00a3\u00a4\5 \21\2\u00a4\u00a5\7\n"+
		"\2\2\u00a5\u00a6\79\2\2\u00a6\37\3\2\2\2\u00a7\u00a9\5\6\4\2\u00a8\u00a7"+
		"\3\2\2\2\u00a9\u00ac\3\2\2\2\u00aa\u00a8\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab"+
		"\u00b8\3\2\2\2\u00ac\u00aa\3\2\2\2\u00ad\u00b7\5\"\22\2\u00ae\u00b7\5"+
		"$\23\2\u00af\u00b7\5&\24\2\u00b0\u00b7\5(\25\2\u00b1\u00b7\5*\26\2\u00b2"+
		"\u00b7\5,\27\2\u00b3\u00b7\5.\30\2\u00b4\u00b7\5\60\31\2\u00b5\u00b7\5"+
		"\62\32\2\u00b6\u00ad\3\2\2\2\u00b6\u00ae\3\2\2\2\u00b6\u00af\3\2\2\2\u00b6"+
		"\u00b0\3\2\2\2\u00b6\u00b1\3\2\2\2\u00b6\u00b2\3\2\2\2\u00b6\u00b3\3\2"+
		"\2\2\u00b6\u00b4\3\2\2\2\u00b6\u00b5\3\2\2\2\u00b7\u00ba\3\2\2\2\u00b8"+
		"\u00b6\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9!\3\2\2\2\u00ba\u00b8\3\2\2\2"+
		"\u00bb\u00bc\5\f\7\2\u00bc\u00bd\7\31\2\2\u00bd\u00be\5\66\34\2\u00be"+
		"\u00bf\7\67\2\2\u00bf#\3\2\2\2\u00c0\u00c1\7\20\2\2\u00c1\u00c2\5\66\34"+
		"\2\u00c2\u00c3\7\23\2\2\u00c3\u00cb\5 \21\2\u00c4\u00c5\7\t\2\2\u00c5"+
		"\u00c6\5\66\34\2\u00c6\u00c7\7\23\2\2\u00c7\u00c8\5 \21\2\u00c8\u00ca"+
		"\3\2\2\2\u00c9\u00c4\3\2\2\2\u00ca\u00cd\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cb"+
		"\u00cc\3\2\2\2\u00cc\u00d0\3\2\2\2\u00cd\u00cb\3\2\2\2\u00ce\u00cf\7\b"+
		"\2\2\u00cf\u00d1\5 \21\2\u00d0\u00ce\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1"+
		"\u00d2\3\2\2\2\u00d2\u00d3\7\13\2\2\u00d3\u00d4\79\2\2\u00d4%\3\2\2\2"+
		"\u00d5\u00d6\7\16\2\2\u00d6\u00d7\7\61\2\2\u00d7\u00d8\7\3\2\2\u00d8\u00d9"+
		"\7\31\2\2\u00d9\u00da\5\66\34\2\u00da\u00db\3\2\2\2\u00db\u00dc\7:\2\2"+
		"\u00dc\u00dd\5\66\34\2\u00dd\u00de\3\2\2\2\u00de\u00df\7:\2\2\u00df\u00e0"+
		"\5\66\34\2\u00e0\u00e1\3\2\2\2\u00e1\u00e2\7\62\2\2\u00e2\u00e3\7\7\2"+
		"\2\u00e3\u00e4\5 \21\2\u00e4\u00e5\7\f\2\2\u00e5\u00e6\79\2\2\u00e6\'"+
		"\3\2\2\2\u00e7\u00e8\7\25\2\2\u00e8\u00e9\5\66\34\2\u00e9\u00ea\7\7\2"+
		"\2\u00ea\u00eb\5 \21\2\u00eb\u00ec\7\r\2\2\u00ec\u00ed\79\2\2\u00ed)\3"+
		"\2\2\2\u00ee\u00ef\7\7\2\2\u00ef\u00f0\5 \21\2\u00f0\u00f1\7\25\2\2\u00f1"+
		"\u00f2\5\66\34\2\u00f2\u00f3\7\26\2\2\u00f3\u00f4\79\2\2\u00f4+\3\2\2"+
		"\2\u00f5\u00f6\7\5\2\2\u00f6\u00f7\7\67\2\2\u00f7-\3\2\2\2\u00f8\u00f9"+
		"\7\6\2\2\u00f9\u00fa\7\67\2\2\u00fa/\3\2\2\2\u00fb\u00fc\5:\36\2\u00fc"+
		"\u00fd\7\67\2\2\u00fd\61\3\2\2\2\u00fe\u0100\7\22\2\2\u00ff\u0101\5\66"+
		"\34\2\u0100\u00ff\3\2\2\2\u0100\u0101\3\2\2\2\u0101\u0102\3\2\2\2\u0102"+
		"\u0103\7\67\2\2\u0103\63\3\2\2\2\u0104\u0109\5\66\34\2\u0105\u0106\7:"+
		"\2\2\u0106\u0108\5\66\34\2\u0107\u0105\3\2\2\2\u0108\u010b\3\2\2\2\u0109"+
		"\u0107\3\2\2\2\u0109\u010a\3\2\2\2\u010a\65\3\2\2\2\u010b\u0109\3\2\2"+
		"\2\u010c\u010d\58\35\2\u010d\u010e\5F$\2\u010e\u010f\58\35\2\u010f\u0112"+
		"\3\2\2\2\u0110\u0112\58\35\2\u0111\u010c\3\2\2\2\u0111\u0110\3\2\2\2\u0112"+
		"\67\3\2\2\2\u0113\u0114\b\35\1\2\u0114\u0115\7\61\2\2\u0115\u0116\5\66"+
		"\34\2\u0116\u0117\7\62\2\2\u0117\u0123\3\2\2\2\u0118\u0123\5:\36\2\u0119"+
		"\u0123\5\20\t\2\u011a\u011b\5<\37\2\u011b\u011c\58\35\t\u011c\u0123\3"+
		"\2\2\2\u011d\u011e\5> \2\u011e\u011f\58\35\b\u011f\u0123\3\2\2\2\u0120"+
		"\u0123\5\f\7\2\u0121\u0123\5\22\n\2\u0122\u0113\3\2\2\2\u0122\u0118\3"+
		"\2\2\2\u0122\u0119\3\2\2\2\u0122\u011a\3\2\2\2\u0122\u011d\3\2\2\2\u0122"+
		"\u0120\3\2\2\2\u0122\u0121\3\2\2\2\u0123\u0132\3\2\2\2\u0124\u0125\f\7"+
		"\2\2\u0125\u0126\5@!\2\u0126\u0127\58\35\b\u0127\u0131\3\2\2\2\u0128\u0129"+
		"\f\6\2\2\u0129\u012a\5B\"\2\u012a\u012b\58\35\7\u012b\u0131\3\2\2\2\u012c"+
		"\u012d\f\5\2\2\u012d\u012e\5D#\2\u012e\u012f\58\35\6\u012f\u0131\3\2\2"+
		"\2\u0130\u0124\3\2\2\2\u0130\u0128\3\2\2\2\u0130\u012c\3\2\2\2\u0131\u0134"+
		"\3\2\2\2\u0132\u0130\3\2\2\2\u0132\u0133\3\2\2\2\u01339\3\2\2\2\u0134"+
		"\u0132\3\2\2\2\u0135\u0136\7\3\2\2\u0136\u0138\7\61\2\2\u0137\u0139\5"+
		"\64\33\2\u0138\u0137\3\2\2\2\u0138\u0139\3\2\2\2\u0139\u013a\3\2\2\2\u013a"+
		"\u013b\7\62\2\2\u013b;\3\2\2\2\u013c\u013d\t\2\2\2\u013d=\3\2\2\2\u013e"+
		"\u013f\7#\2\2\u013f?\3\2\2\2\u0140\u0141\t\3\2\2\u0141A\3\2\2\2\u0142"+
		"\u0143\t\4\2\2\u0143C\3\2\2\2\u0144\u0145\t\5\2\2\u0145E\3\2\2\2\u0146"+
		"\u0147\t\6\2\2\u0147G\3\2\2\2\u0148\u0149\t\7\2\2\u0149I\3\2\2\2\u014a"+
		"\u014b\7\65\2\2\u014b\u014c\5L\'\2\u014c\u014d\7\66\2\2\u014dK\3\2\2\2"+
		"\u014e\u0153\5\22\n\2\u014f\u0150\7:\2\2\u0150\u0152\5\22\n\2\u0151\u014f"+
		"\3\2\2\2\u0152\u0155\3\2\2\2\u0153\u0151\3\2\2\2\u0153\u0154\3\2\2\2\u0154"+
		"M\3\2\2\2\u0155\u0153\3\2\2\2\31U_dhq|\u0083\u0088\u008d\u009e\u00aa\u00b6"+
		"\u00b8\u00cb\u00d0\u0100\u0109\u0111\u0122\u0130\u0132\u0138\u0153";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}