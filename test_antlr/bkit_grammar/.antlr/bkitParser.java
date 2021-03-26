// Generated from e:\Messy\Downloads\BKIT ASSIGN\test_antlr\bkit_grammar\bkit.g4 by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class bkitParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, INT_OF_FLOAT=2, FLOAT_TO_INT=3, INT_OF_STRING=4, STRING_OF_INT=5, 
		FLOAT_OF_STRING=6, STRING_OF_FLOAT=7, BOOL_OF_STRING=8, STRING_OF_BOOL=9, 
		PRINTLN=10, PRINT=11, PRINTSTRLN=12, READ=13, IDENTIFIER=14, BODY=15, 
		BREAK=16, CONTINUE=17, DO=18, ELSE=19, ELSEIF=20, ENDBODY=21, ENDIF=22, 
		ENDFOR=23, ENDWHILE=24, FOR=25, FUNCTION=26, IF=27, PARAMETER=28, RETURN=29, 
		THEN=30, VAR=31, WHILE=32, ENDDO=33, PLUS=34, PLUS_DOT=35, MINUS=36, MINUS_DOT=37, 
		STAR=38, STAR_DOT=39, DIV=40, DIV_DOT=41, MOD=42, NOT=43, AND=44, OR=45, 
		EQUAL=46, NOT_EQUAL=47, LESS=48, GREATER=49, LESS_EQUAL=50, GREATER_EQUAL=51, 
		EQUAL_DIV_EQUAL=52, LESS_DOT=53, GREATER_DOT=54, LESS_EQUAL_DOT=55, GREATER_EQUAL_DOT=56, 
		LEFT_PAREN=57, RIGHT_PAREN=58, LEFT_SQUARE=59, RIGHT_SQUARE=60, LEFT_CURLY=61, 
		RIGHT_CURLY=62, SEMI=63, COLON=64, DOT=65, COMMA=66, WS=67, BLOCK_COMMENT=68, 
		UNTERMINATED_COMMENT=69, INTEGER=70, FLOAT=71, BOOLEAN=72, STRING=73, 
		ILLEGAL_ESCAPE=74, UNCLOSE_STRING=75, ERROR_CHAR=76;
	public static final int
		RULE_program = 0, RULE_global_variable_declaration_part = 1, RULE_local_variable_declaration = 2, 
		RULE_variable_declaration = 3, RULE_variable_list = 4, RULE_initialization = 5, 
		RULE_variable = 6, RULE_composite_variable = 7, RULE_array_subscript = 8, 
		RULE_subscript = 9, RULE_literal = 10, RULE_array = 11, RULE_literal_list = 12, 
		RULE_function_declaration_part = 13, RULE_function_declaration = 14, RULE_function_name = 15, 
		RULE_function_parameter = 16, RULE_parameter_list = 17, RULE_function_body = 18, 
		RULE_statement_list = 19, RULE_other_statements = 20, RULE_assignment_statement = 21, 
		RULE_if_statement = 22, RULE_for_statement = 23, RULE_while_statement = 24, 
		RULE_do_while_statement = 25, RULE_break_statement = 26, RULE_continue_statement = 27, 
		RULE_call_statement = 28, RULE_return_statement = 29, RULE_expression = 30, 
		RULE_arithmetic_expression = 31, RULE_boolean_expression = 32, RULE_relational_expression = 33, 
		RULE_indexing = 34, RULE_function_call = 35;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "global_variable_declaration_part", "local_variable_declaration", 
			"variable_declaration", "variable_list", "initialization", "variable", 
			"composite_variable", "array_subscript", "subscript", "literal", "array", 
			"literal_list", "function_declaration_part", "function_declaration", 
			"function_name", "function_parameter", "parameter_list", "function_body", 
			"statement_list", "other_statements", "assignment_statement", "if_statement", 
			"for_statement", "while_statement", "do_while_statement", "break_statement", 
			"continue_statement", "call_statement", "return_statement", "expression", 
			"arithmetic_expression", "boolean_expression", "relational_expression", 
			"indexing", "function_call"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'='", "'int_of_float'", "'float_to_int'", "'int_of_string'", "'string_of_int'", 
			"'float_of_int'", "'string_of_float'", "'bool_of_string'", "'string_of_bool'", 
			"'printLn'", "'print'", "'printStrLn'", "'read'", null, "'Body'", "'Break'", 
			"'Continue'", "'Do'", "'Else'", "'ElseIf'", "'EndBody'", "'EndIf'", "'EndFor'", 
			"'EndWhile'", "'For'", "'Function'", "'If'", "'Parameter'", "'Return'", 
			"'Then'", "'Var'", "'While'", "'EndDo'", "'+'", "'+.'", "'-'", "'-.'", 
			"'*'", "'*.'", "'\\'", "'\\.'", "'%'", "'!'", "'&&'", "'||'", "'=='", 
			"'!='", "'<'", "'>'", "'<='", "'>='", "'=/='", "'<.'", "'>.'", "'<=.'", 
			"'>=.'", "'('", "')'", "'['", "']'", "'{'", "'}'", "';'", "':'", "'.'", 
			"','"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, "INT_OF_FLOAT", "FLOAT_TO_INT", "INT_OF_STRING", "STRING_OF_INT", 
			"FLOAT_OF_STRING", "STRING_OF_FLOAT", "BOOL_OF_STRING", "STRING_OF_BOOL", 
			"PRINTLN", "PRINT", "PRINTSTRLN", "READ", "IDENTIFIER", "BODY", "BREAK", 
			"CONTINUE", "DO", "ELSE", "ELSEIF", "ENDBODY", "ENDIF", "ENDFOR", "ENDWHILE", 
			"FOR", "FUNCTION", "IF", "PARAMETER", "RETURN", "THEN", "VAR", "WHILE", 
			"ENDDO", "PLUS", "PLUS_DOT", "MINUS", "MINUS_DOT", "STAR", "STAR_DOT", 
			"DIV", "DIV_DOT", "MOD", "NOT", "AND", "OR", "EQUAL", "NOT_EQUAL", "LESS", 
			"GREATER", "LESS_EQUAL", "GREATER_EQUAL", "EQUAL_DIV_EQUAL", "LESS_DOT", 
			"GREATER_DOT", "LESS_EQUAL_DOT", "GREATER_EQUAL_DOT", "LEFT_PAREN", "RIGHT_PAREN", 
			"LEFT_SQUARE", "RIGHT_SQUARE", "LEFT_CURLY", "RIGHT_CURLY", "SEMI", "COLON", 
			"DOT", "COMMA", "WS", "BLOCK_COMMENT", "UNTERMINATED_COMMENT", "INTEGER", 
			"FLOAT", "BOOLEAN", "STRING", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR"
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
	public String getGrammarFileName() { return "bkit.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public bkitParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public List<Variable_declarationContext> variable_declaration() {
			return getRuleContexts(Variable_declarationContext.class);
		}
		public Variable_declarationContext variable_declaration(int i) {
			return getRuleContext(Variable_declarationContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(75);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==VAR) {
				{
				{
				setState(72);
				variable_declaration();
				}
				}
				setState(77);
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

	public static class Global_variable_declaration_partContext extends ParserRuleContext {
		public List<Variable_declarationContext> variable_declaration() {
			return getRuleContexts(Variable_declarationContext.class);
		}
		public Variable_declarationContext variable_declaration(int i) {
			return getRuleContext(Variable_declarationContext.class,i);
		}
		public Global_variable_declaration_partContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_global_variable_declaration_part; }
	}

	public final Global_variable_declaration_partContext global_variable_declaration_part() throws RecognitionException {
		Global_variable_declaration_partContext _localctx = new Global_variable_declaration_partContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_global_variable_declaration_part);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(81);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==VAR) {
				{
				{
				setState(78);
				variable_declaration();
				}
				}
				setState(83);
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

	public static class Local_variable_declarationContext extends ParserRuleContext {
		public List<Variable_declarationContext> variable_declaration() {
			return getRuleContexts(Variable_declarationContext.class);
		}
		public Variable_declarationContext variable_declaration(int i) {
			return getRuleContext(Variable_declarationContext.class,i);
		}
		public Local_variable_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_local_variable_declaration; }
	}

	public final Local_variable_declarationContext local_variable_declaration() throws RecognitionException {
		Local_variable_declarationContext _localctx = new Local_variable_declarationContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_local_variable_declaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(87);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==VAR) {
				{
				{
				setState(84);
				variable_declaration();
				}
				}
				setState(89);
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
		public TerminalNode VAR() { return getToken(bkitParser.VAR, 0); }
		public TerminalNode COLON() { return getToken(bkitParser.COLON, 0); }
		public Variable_listContext variable_list() {
			return getRuleContext(Variable_listContext.class,0);
		}
		public Variable_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variable_declaration; }
	}

	public final Variable_declarationContext variable_declaration() throws RecognitionException {
		Variable_declarationContext _localctx = new Variable_declarationContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_variable_declaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(90);
			match(VAR);
			setState(91);
			match(COLON);
			setState(92);
			variable_list();
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

	public static class Variable_listContext extends ParserRuleContext {
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
		public List<TerminalNode> COMMA() { return getTokens(bkitParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(bkitParser.COMMA, i);
		}
		public Variable_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variable_list; }
	}

	public final Variable_listContext variable_list() throws RecognitionException {
		Variable_listContext _localctx = new Variable_listContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_variable_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(96);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				{
				setState(94);
				variable();
				}
				break;
			case 2:
				{
				setState(95);
				initialization();
				}
				break;
			}
			setState(105);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(98);
				match(COMMA);
				setState(101);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
				case 1:
					{
					setState(99);
					variable();
					}
					break;
				case 2:
					{
					setState(100);
					initialization();
					}
					break;
				}
				}
				}
				setState(107);
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
		enterRule(_localctx, 10, RULE_initialization);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(108);
			variable();
			setState(109);
			match(T__0);
			setState(110);
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
		public TerminalNode IDENTIFIER() { return getToken(bkitParser.IDENTIFIER, 0); }
		public Composite_variableContext composite_variable() {
			return getRuleContext(Composite_variableContext.class,0);
		}
		public VariableContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variable; }
	}

	public final VariableContext variable() throws RecognitionException {
		VariableContext _localctx = new VariableContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_variable);
		try {
			setState(114);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(112);
				match(IDENTIFIER);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(113);
				composite_variable();
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

	public static class Composite_variableContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(bkitParser.IDENTIFIER, 0); }
		public List<Array_subscriptContext> array_subscript() {
			return getRuleContexts(Array_subscriptContext.class);
		}
		public Array_subscriptContext array_subscript(int i) {
			return getRuleContext(Array_subscriptContext.class,i);
		}
		public Composite_variableContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_composite_variable; }
	}

	public final Composite_variableContext composite_variable() throws RecognitionException {
		Composite_variableContext _localctx = new Composite_variableContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_composite_variable);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(116);
			match(IDENTIFIER);
			setState(118); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(117);
					array_subscript();
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(120); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
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

	public static class Array_subscriptContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(bkitParser.IDENTIFIER, 0); }
		public List<SubscriptContext> subscript() {
			return getRuleContexts(SubscriptContext.class);
		}
		public SubscriptContext subscript(int i) {
			return getRuleContext(SubscriptContext.class,i);
		}
		public Array_subscriptContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_array_subscript; }
	}

	public final Array_subscriptContext array_subscript() throws RecognitionException {
		Array_subscriptContext _localctx = new Array_subscriptContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_array_subscript);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(122);
			match(IDENTIFIER);
			setState(124); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(123);
				subscript();
				}
				}
				setState(126); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==LEFT_SQUARE );
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

	public static class SubscriptContext extends ParserRuleContext {
		public TerminalNode LEFT_SQUARE() { return getToken(bkitParser.LEFT_SQUARE, 0); }
		public TerminalNode INTEGER() { return getToken(bkitParser.INTEGER, 0); }
		public TerminalNode RIGHT_SQUARE() { return getToken(bkitParser.RIGHT_SQUARE, 0); }
		public SubscriptContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_subscript; }
	}

	public final SubscriptContext subscript() throws RecognitionException {
		SubscriptContext _localctx = new SubscriptContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_subscript);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(128);
			match(LEFT_SQUARE);
			setState(129);
			match(INTEGER);
			setState(130);
			match(RIGHT_SQUARE);
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
		public TerminalNode BOOLEAN() { return getToken(bkitParser.BOOLEAN, 0); }
		public TerminalNode INTEGER() { return getToken(bkitParser.INTEGER, 0); }
		public TerminalNode FLOAT() { return getToken(bkitParser.FLOAT, 0); }
		public TerminalNode STRING() { return getToken(bkitParser.STRING, 0); }
		public ArrayContext array() {
			return getRuleContext(ArrayContext.class,0);
		}
		public LiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literal; }
	}

	public final LiteralContext literal() throws RecognitionException {
		LiteralContext _localctx = new LiteralContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_literal);
		try {
			setState(137);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case BOOLEAN:
				enterOuterAlt(_localctx, 1);
				{
				setState(132);
				match(BOOLEAN);
				}
				break;
			case INTEGER:
				enterOuterAlt(_localctx, 2);
				{
				setState(133);
				match(INTEGER);
				}
				break;
			case FLOAT:
				enterOuterAlt(_localctx, 3);
				{
				setState(134);
				match(FLOAT);
				}
				break;
			case STRING:
				enterOuterAlt(_localctx, 4);
				{
				setState(135);
				match(STRING);
				}
				break;
			case LEFT_CURLY:
				enterOuterAlt(_localctx, 5);
				{
				setState(136);
				array();
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

	public static class ArrayContext extends ParserRuleContext {
		public TerminalNode LEFT_CURLY() { return getToken(bkitParser.LEFT_CURLY, 0); }
		public TerminalNode RIGHT_CURLY() { return getToken(bkitParser.RIGHT_CURLY, 0); }
		public Literal_listContext literal_list() {
			return getRuleContext(Literal_listContext.class,0);
		}
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public ArrayContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_array; }
	}

	public final ArrayContext array() throws RecognitionException {
		ArrayContext _localctx = new ArrayContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_array);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(139);
			match(LEFT_CURLY);
			setState(143);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
			case 1:
				{
				setState(140);
				literal_list();
				}
				break;
			case 2:
				{
				setState(141);
				literal();
				}
				break;
			case 3:
				{
				}
				break;
			}
			setState(145);
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
		public List<TerminalNode> COMMA() { return getTokens(bkitParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(bkitParser.COMMA, i);
		}
		public Literal_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literal_list; }
	}

	public final Literal_listContext literal_list() throws RecognitionException {
		Literal_listContext _localctx = new Literal_listContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_literal_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(147);
			literal();
			setState(152);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(148);
				match(COMMA);
				setState(149);
				literal();
				}
				}
				setState(154);
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
		enterRule(_localctx, 26, RULE_function_declaration_part);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(158);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==FUNCTION) {
				{
				{
				setState(155);
				function_declaration();
				}
				}
				setState(160);
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
		enterRule(_localctx, 28, RULE_function_declaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(161);
			function_name();
			setState(163);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==PARAMETER) {
				{
				setState(162);
				function_parameter();
				}
			}

			setState(165);
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
		public TerminalNode FUNCTION() { return getToken(bkitParser.FUNCTION, 0); }
		public TerminalNode COLON() { return getToken(bkitParser.COLON, 0); }
		public TerminalNode IDENTIFIER() { return getToken(bkitParser.IDENTIFIER, 0); }
		public Function_nameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_name; }
	}

	public final Function_nameContext function_name() throws RecognitionException {
		Function_nameContext _localctx = new Function_nameContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_function_name);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(167);
			match(FUNCTION);
			setState(168);
			match(COLON);
			setState(169);
			match(IDENTIFIER);
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
		public TerminalNode PARAMETER() { return getToken(bkitParser.PARAMETER, 0); }
		public TerminalNode COLON() { return getToken(bkitParser.COLON, 0); }
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
		enterRule(_localctx, 32, RULE_function_parameter);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(171);
			match(PARAMETER);
			setState(172);
			match(COLON);
			setState(173);
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
		public List<TerminalNode> IDENTIFIER() { return getTokens(bkitParser.IDENTIFIER); }
		public TerminalNode IDENTIFIER(int i) {
			return getToken(bkitParser.IDENTIFIER, i);
		}
		public List<TerminalNode> COMMA() { return getTokens(bkitParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(bkitParser.COMMA, i);
		}
		public Parameter_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameter_list; }
	}

	public final Parameter_listContext parameter_list() throws RecognitionException {
		Parameter_listContext _localctx = new Parameter_listContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_parameter_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(175);
			match(IDENTIFIER);
			setState(180);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(176);
				match(COMMA);
				setState(177);
				match(IDENTIFIER);
				}
				}
				setState(182);
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
		public TerminalNode BODY() { return getToken(bkitParser.BODY, 0); }
		public Statement_listContext statement_list() {
			return getRuleContext(Statement_listContext.class,0);
		}
		public TerminalNode ENDBODY() { return getToken(bkitParser.ENDBODY, 0); }
		public TerminalNode DOT() { return getToken(bkitParser.DOT, 0); }
		public Function_bodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_body; }
	}

	public final Function_bodyContext function_body() throws RecognitionException {
		Function_bodyContext _localctx = new Function_bodyContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_function_body);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(183);
			match(BODY);
			setState(184);
			statement_list();
			setState(185);
			match(ENDBODY);
			setState(186);
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
		public Local_variable_declarationContext local_variable_declaration() {
			return getRuleContext(Local_variable_declarationContext.class,0);
		}
		public List<Other_statementsContext> other_statements() {
			return getRuleContexts(Other_statementsContext.class);
		}
		public Other_statementsContext other_statements(int i) {
			return getRuleContext(Other_statementsContext.class,i);
		}
		public Statement_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement_list; }
	}

	public final Statement_listContext statement_list() throws RecognitionException {
		Statement_listContext _localctx = new Statement_listContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_statement_list);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(188);
			local_variable_declaration();
			setState(192);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,15,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(189);
					other_statements();
					}
					} 
				}
				setState(194);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,15,_ctx);
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

	public static class Other_statementsContext extends ParserRuleContext {
		public Assignment_statementContext assignment_statement() {
			return getRuleContext(Assignment_statementContext.class,0);
		}
		public If_statementContext if_statement() {
			return getRuleContext(If_statementContext.class,0);
		}
		public For_statementContext for_statement() {
			return getRuleContext(For_statementContext.class,0);
		}
		public While_statementContext while_statement() {
			return getRuleContext(While_statementContext.class,0);
		}
		public Do_while_statementContext do_while_statement() {
			return getRuleContext(Do_while_statementContext.class,0);
		}
		public Break_statementContext break_statement() {
			return getRuleContext(Break_statementContext.class,0);
		}
		public Continue_statementContext continue_statement() {
			return getRuleContext(Continue_statementContext.class,0);
		}
		public Call_statementContext call_statement() {
			return getRuleContext(Call_statementContext.class,0);
		}
		public Return_statementContext return_statement() {
			return getRuleContext(Return_statementContext.class,0);
		}
		public Other_statementsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_other_statements; }
	}

	public final Other_statementsContext other_statements() throws RecognitionException {
		Other_statementsContext _localctx = new Other_statementsContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_other_statements);
		try {
			setState(204);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(195);
				assignment_statement();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(196);
				if_statement();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(197);
				for_statement();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(198);
				while_statement();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(199);
				do_while_statement();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(200);
				break_statement();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(201);
				continue_statement();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(202);
				call_statement();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(203);
				return_statement();
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

	public static class Assignment_statementContext extends ParserRuleContext {
		public VariableContext variable() {
			return getRuleContext(VariableContext.class,0);
		}
		public TerminalNode EQUAL() { return getToken(bkitParser.EQUAL, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(bkitParser.SEMI, 0); }
		public Assignment_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment_statement; }
	}

	public final Assignment_statementContext assignment_statement() throws RecognitionException {
		Assignment_statementContext _localctx = new Assignment_statementContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_assignment_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(206);
			variable();
			setState(207);
			match(EQUAL);
			setState(208);
			expression();
			setState(209);
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
		public TerminalNode IF() { return getToken(bkitParser.IF, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> THEN() { return getTokens(bkitParser.THEN); }
		public TerminalNode THEN(int i) {
			return getToken(bkitParser.THEN, i);
		}
		public List<Statement_listContext> statement_list() {
			return getRuleContexts(Statement_listContext.class);
		}
		public Statement_listContext statement_list(int i) {
			return getRuleContext(Statement_listContext.class,i);
		}
		public TerminalNode ENDIF() { return getToken(bkitParser.ENDIF, 0); }
		public TerminalNode DOT() { return getToken(bkitParser.DOT, 0); }
		public List<TerminalNode> ELSEIF() { return getTokens(bkitParser.ELSEIF); }
		public TerminalNode ELSEIF(int i) {
			return getToken(bkitParser.ELSEIF, i);
		}
		public TerminalNode ELSE() { return getToken(bkitParser.ELSE, 0); }
		public If_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_if_statement; }
	}

	public final If_statementContext if_statement() throws RecognitionException {
		If_statementContext _localctx = new If_statementContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_if_statement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(211);
			match(IF);
			setState(212);
			expression();
			setState(213);
			match(THEN);
			setState(214);
			statement_list();
			setState(222);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ELSEIF) {
				{
				{
				setState(215);
				match(ELSEIF);
				setState(216);
				expression();
				setState(217);
				match(THEN);
				setState(218);
				statement_list();
				}
				}
				setState(224);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(227);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELSE) {
				{
				setState(225);
				match(ELSE);
				setState(226);
				statement_list();
				}
			}

			setState(229);
			match(ENDIF);
			setState(230);
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
		public TerminalNode FOR() { return getToken(bkitParser.FOR, 0); }
		public TerminalNode LEFT_PAREN() { return getToken(bkitParser.LEFT_PAREN, 0); }
		public TerminalNode RIGHT_PAREN() { return getToken(bkitParser.RIGHT_PAREN, 0); }
		public TerminalNode DO() { return getToken(bkitParser.DO, 0); }
		public Statement_listContext statement_list() {
			return getRuleContext(Statement_listContext.class,0);
		}
		public TerminalNode ENDFOR() { return getToken(bkitParser.ENDFOR, 0); }
		public TerminalNode DOT() { return getToken(bkitParser.DOT, 0); }
		public TerminalNode IDENTIFIER() { return getToken(bkitParser.IDENTIFIER, 0); }
		public TerminalNode EQUAL() { return getToken(bkitParser.EQUAL, 0); }
		public TerminalNode INTEGER() { return getToken(bkitParser.INTEGER, 0); }
		public List<TerminalNode> COLON() { return getTokens(bkitParser.COLON); }
		public TerminalNode COLON(int i) {
			return getToken(bkitParser.COLON, i);
		}
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public For_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_for_statement; }
	}

	public final For_statementContext for_statement() throws RecognitionException {
		For_statementContext _localctx = new For_statementContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_for_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(232);
			match(FOR);
			setState(233);
			match(LEFT_PAREN);
			{
			setState(234);
			match(IDENTIFIER);
			setState(235);
			match(EQUAL);
			setState(236);
			match(INTEGER);
			}
			{
			setState(238);
			match(COLON);
			setState(239);
			expression();
			}
			{
			setState(241);
			match(COLON);
			setState(242);
			expression();
			}
			setState(244);
			match(RIGHT_PAREN);
			setState(245);
			match(DO);
			setState(246);
			statement_list();
			setState(247);
			match(ENDFOR);
			setState(248);
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
		public TerminalNode WHILE() { return getToken(bkitParser.WHILE, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode DO() { return getToken(bkitParser.DO, 0); }
		public Statement_listContext statement_list() {
			return getRuleContext(Statement_listContext.class,0);
		}
		public TerminalNode ENDWHILE() { return getToken(bkitParser.ENDWHILE, 0); }
		public TerminalNode DOT() { return getToken(bkitParser.DOT, 0); }
		public While_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_while_statement; }
	}

	public final While_statementContext while_statement() throws RecognitionException {
		While_statementContext _localctx = new While_statementContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_while_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(250);
			match(WHILE);
			setState(251);
			expression();
			setState(252);
			match(DO);
			setState(253);
			statement_list();
			setState(254);
			match(ENDWHILE);
			setState(255);
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
		public TerminalNode DO() { return getToken(bkitParser.DO, 0); }
		public Statement_listContext statement_list() {
			return getRuleContext(Statement_listContext.class,0);
		}
		public TerminalNode WHILE() { return getToken(bkitParser.WHILE, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode ENDDO() { return getToken(bkitParser.ENDDO, 0); }
		public TerminalNode DOT() { return getToken(bkitParser.DOT, 0); }
		public Do_while_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_do_while_statement; }
	}

	public final Do_while_statementContext do_while_statement() throws RecognitionException {
		Do_while_statementContext _localctx = new Do_while_statementContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_do_while_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(257);
			match(DO);
			setState(258);
			statement_list();
			setState(259);
			match(WHILE);
			setState(260);
			expression();
			setState(261);
			match(ENDDO);
			setState(262);
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
		public TerminalNode BREAK() { return getToken(bkitParser.BREAK, 0); }
		public TerminalNode SEMI() { return getToken(bkitParser.SEMI, 0); }
		public Break_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_break_statement; }
	}

	public final Break_statementContext break_statement() throws RecognitionException {
		Break_statementContext _localctx = new Break_statementContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_break_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(264);
			match(BREAK);
			setState(265);
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
		public TerminalNode CONTINUE() { return getToken(bkitParser.CONTINUE, 0); }
		public TerminalNode SEMI() { return getToken(bkitParser.SEMI, 0); }
		public Continue_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_continue_statement; }
	}

	public final Continue_statementContext continue_statement() throws RecognitionException {
		Continue_statementContext _localctx = new Continue_statementContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_continue_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(267);
			match(CONTINUE);
			setState(268);
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
		public TerminalNode IDENTIFIER() { return getToken(bkitParser.IDENTIFIER, 0); }
		public TerminalNode LEFT_PAREN() { return getToken(bkitParser.LEFT_PAREN, 0); }
		public TerminalNode RIGHT_PAREN() { return getToken(bkitParser.RIGHT_PAREN, 0); }
		public TerminalNode SEMI() { return getToken(bkitParser.SEMI, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(bkitParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(bkitParser.COMMA, i);
		}
		public Call_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_call_statement; }
	}

	public final Call_statementContext call_statement() throws RecognitionException {
		Call_statementContext _localctx = new Call_statementContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_call_statement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(270);
			match(IDENTIFIER);
			setState(271);
			match(LEFT_PAREN);
			{
			setState(272);
			expression();
			setState(277);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(273);
				match(COMMA);
				setState(274);
				expression();
				}
				}
				setState(279);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
			setState(280);
			match(RIGHT_PAREN);
			setState(281);
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
		public TerminalNode RETURN() { return getToken(bkitParser.RETURN, 0); }
		public TerminalNode SEMI() { return getToken(bkitParser.SEMI, 0); }
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
		enterRule(_localctx, 58, RULE_return_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(283);
			match(RETURN);
			setState(285);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,20,_ctx) ) {
			case 1:
				{
				setState(284);
				expression();
				}
				break;
			}
			setState(287);
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

	public static class ExpressionContext extends ParserRuleContext {
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
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

	public static class Arithmetic_expressionContext extends ParserRuleContext {
		public Arithmetic_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arithmetic_expression; }
	}

	public final Arithmetic_expressionContext arithmetic_expression() throws RecognitionException {
		Arithmetic_expressionContext _localctx = new Arithmetic_expressionContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_arithmetic_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
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

	public static class Boolean_expressionContext extends ParserRuleContext {
		public Boolean_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_boolean_expression; }
	}

	public final Boolean_expressionContext boolean_expression() throws RecognitionException {
		Boolean_expressionContext _localctx = new Boolean_expressionContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_boolean_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
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

	public static class Relational_expressionContext extends ParserRuleContext {
		public Relational_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_relational_expression; }
	}

	public final Relational_expressionContext relational_expression() throws RecognitionException {
		Relational_expressionContext _localctx = new Relational_expressionContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_relational_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
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

	public static class IndexingContext extends ParserRuleContext {
		public IndexingContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_indexing; }
	}

	public final IndexingContext indexing() throws RecognitionException {
		IndexingContext _localctx = new IndexingContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_indexing);
		try {
			enterOuterAlt(_localctx, 1);
			{
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
		public Function_callContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_call; }
	}

	public final Function_callContext function_call() throws RecognitionException {
		Function_callContext _localctx = new Function_callContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_function_call);
		try {
			enterOuterAlt(_localctx, 1);
			{
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

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3N\u0130\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\3\2\7\2L\n\2\f\2\16\2O\13\2\3\3\7\3R\n\3"+
		"\f\3\16\3U\13\3\3\4\7\4X\n\4\f\4\16\4[\13\4\3\5\3\5\3\5\3\5\3\6\3\6\5"+
		"\6c\n\6\3\6\3\6\3\6\5\6h\n\6\7\6j\n\6\f\6\16\6m\13\6\3\7\3\7\3\7\3\7\3"+
		"\b\3\b\5\bu\n\b\3\t\3\t\6\ty\n\t\r\t\16\tz\3\n\3\n\6\n\177\n\n\r\n\16"+
		"\n\u0080\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\5\f\u008c\n\f\3\r\3\r"+
		"\3\r\3\r\5\r\u0092\n\r\3\r\3\r\3\16\3\16\3\16\7\16\u0099\n\16\f\16\16"+
		"\16\u009c\13\16\3\17\7\17\u009f\n\17\f\17\16\17\u00a2\13\17\3\20\3\20"+
		"\5\20\u00a6\n\20\3\20\3\20\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\23"+
		"\3\23\3\23\7\23\u00b5\n\23\f\23\16\23\u00b8\13\23\3\24\3\24\3\24\3\24"+
		"\3\24\3\25\3\25\7\25\u00c1\n\25\f\25\16\25\u00c4\13\25\3\26\3\26\3\26"+
		"\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u00cf\n\26\3\27\3\27\3\27\3\27\3\27"+
		"\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\7\30\u00df\n\30\f\30\16"+
		"\30\u00e2\13\30\3\30\3\30\5\30\u00e6\n\30\3\30\3\30\3\30\3\31\3\31\3\31"+
		"\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31"+
		"\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33"+
		"\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\7\36\u0116"+
		"\n\36\f\36\16\36\u0119\13\36\3\36\3\36\3\36\3\37\3\37\5\37\u0120\n\37"+
		"\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3%\2\2&\2\4\6\b\n\f\16"+
		"\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFH\2\2\2\u012b\2M"+
		"\3\2\2\2\4S\3\2\2\2\6Y\3\2\2\2\b\\\3\2\2\2\nb\3\2\2\2\fn\3\2\2\2\16t\3"+
		"\2\2\2\20v\3\2\2\2\22|\3\2\2\2\24\u0082\3\2\2\2\26\u008b\3\2\2\2\30\u008d"+
		"\3\2\2\2\32\u0095\3\2\2\2\34\u00a0\3\2\2\2\36\u00a3\3\2\2\2 \u00a9\3\2"+
		"\2\2\"\u00ad\3\2\2\2$\u00b1\3\2\2\2&\u00b9\3\2\2\2(\u00be\3\2\2\2*\u00ce"+
		"\3\2\2\2,\u00d0\3\2\2\2.\u00d5\3\2\2\2\60\u00ea\3\2\2\2\62\u00fc\3\2\2"+
		"\2\64\u0103\3\2\2\2\66\u010a\3\2\2\28\u010d\3\2\2\2:\u0110\3\2\2\2<\u011d"+
		"\3\2\2\2>\u0123\3\2\2\2@\u0125\3\2\2\2B\u0127\3\2\2\2D\u0129\3\2\2\2F"+
		"\u012b\3\2\2\2H\u012d\3\2\2\2JL\5\b\5\2KJ\3\2\2\2LO\3\2\2\2MK\3\2\2\2"+
		"MN\3\2\2\2N\3\3\2\2\2OM\3\2\2\2PR\5\b\5\2QP\3\2\2\2RU\3\2\2\2SQ\3\2\2"+
		"\2ST\3\2\2\2T\5\3\2\2\2US\3\2\2\2VX\5\b\5\2WV\3\2\2\2X[\3\2\2\2YW\3\2"+
		"\2\2YZ\3\2\2\2Z\7\3\2\2\2[Y\3\2\2\2\\]\7!\2\2]^\7B\2\2^_\5\n\6\2_\t\3"+
		"\2\2\2`c\5\16\b\2ac\5\f\7\2b`\3\2\2\2ba\3\2\2\2ck\3\2\2\2dg\7D\2\2eh\5"+
		"\16\b\2fh\5\f\7\2ge\3\2\2\2gf\3\2\2\2hj\3\2\2\2id\3\2\2\2jm\3\2\2\2ki"+
		"\3\2\2\2kl\3\2\2\2l\13\3\2\2\2mk\3\2\2\2no\5\16\b\2op\7\3\2\2pq\5\26\f"+
		"\2q\r\3\2\2\2ru\7\20\2\2su\5\20\t\2tr\3\2\2\2ts\3\2\2\2u\17\3\2\2\2vx"+
		"\7\20\2\2wy\5\22\n\2xw\3\2\2\2yz\3\2\2\2zx\3\2\2\2z{\3\2\2\2{\21\3\2\2"+
		"\2|~\7\20\2\2}\177\5\24\13\2~}\3\2\2\2\177\u0080\3\2\2\2\u0080~\3\2\2"+
		"\2\u0080\u0081\3\2\2\2\u0081\23\3\2\2\2\u0082\u0083\7=\2\2\u0083\u0084"+
		"\7H\2\2\u0084\u0085\7>\2\2\u0085\25\3\2\2\2\u0086\u008c\7J\2\2\u0087\u008c"+
		"\7H\2\2\u0088\u008c\7I\2\2\u0089\u008c\7K\2\2\u008a\u008c\5\30\r\2\u008b"+
		"\u0086\3\2\2\2\u008b\u0087\3\2\2\2\u008b\u0088\3\2\2\2\u008b\u0089\3\2"+
		"\2\2\u008b\u008a\3\2\2\2\u008c\27\3\2\2\2\u008d\u0091\7?\2\2\u008e\u0092"+
		"\5\32\16\2\u008f\u0092\5\26\f\2\u0090\u0092\3\2\2\2\u0091\u008e\3\2\2"+
		"\2\u0091\u008f\3\2\2\2\u0091\u0090\3\2\2\2\u0092\u0093\3\2\2\2\u0093\u0094"+
		"\7@\2\2\u0094\31\3\2\2\2\u0095\u009a\5\26\f\2\u0096\u0097\7D\2\2\u0097"+
		"\u0099\5\26\f\2\u0098\u0096\3\2\2\2\u0099\u009c\3\2\2\2\u009a\u0098\3"+
		"\2\2\2\u009a\u009b\3\2\2\2\u009b\33\3\2\2\2\u009c\u009a\3\2\2\2\u009d"+
		"\u009f\5\36\20\2\u009e\u009d\3\2\2\2\u009f\u00a2\3\2\2\2\u00a0\u009e\3"+
		"\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\35\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a3"+
		"\u00a5\5 \21\2\u00a4\u00a6\5\"\22\2\u00a5\u00a4\3\2\2\2\u00a5\u00a6\3"+
		"\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\u00a8\5&\24\2\u00a8\37\3\2\2\2\u00a9"+
		"\u00aa\7\34\2\2\u00aa\u00ab\7B\2\2\u00ab\u00ac\7\20\2\2\u00ac!\3\2\2\2"+
		"\u00ad\u00ae\7\36\2\2\u00ae\u00af\7B\2\2\u00af\u00b0\5$\23\2\u00b0#\3"+
		"\2\2\2\u00b1\u00b6\7\20\2\2\u00b2\u00b3\7D\2\2\u00b3\u00b5\7\20\2\2\u00b4"+
		"\u00b2\3\2\2\2\u00b5\u00b8\3\2\2\2\u00b6\u00b4\3\2\2\2\u00b6\u00b7\3\2"+
		"\2\2\u00b7%\3\2\2\2\u00b8\u00b6\3\2\2\2\u00b9\u00ba\7\21\2\2\u00ba\u00bb"+
		"\5(\25\2\u00bb\u00bc\7\27\2\2\u00bc\u00bd\7C\2\2\u00bd\'\3\2\2\2\u00be"+
		"\u00c2\5\6\4\2\u00bf\u00c1\5*\26\2\u00c0\u00bf\3\2\2\2\u00c1\u00c4\3\2"+
		"\2\2\u00c2\u00c0\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3)\3\2\2\2\u00c4\u00c2"+
		"\3\2\2\2\u00c5\u00cf\5,\27\2\u00c6\u00cf\5.\30\2\u00c7\u00cf\5\60\31\2"+
		"\u00c8\u00cf\5\62\32\2\u00c9\u00cf\5\64\33\2\u00ca\u00cf\5\66\34\2\u00cb"+
		"\u00cf\58\35\2\u00cc\u00cf\5:\36\2\u00cd\u00cf\5<\37\2\u00ce\u00c5\3\2"+
		"\2\2\u00ce\u00c6\3\2\2\2\u00ce\u00c7\3\2\2\2\u00ce\u00c8\3\2\2\2\u00ce"+
		"\u00c9\3\2\2\2\u00ce\u00ca\3\2\2\2\u00ce\u00cb\3\2\2\2\u00ce\u00cc\3\2"+
		"\2\2\u00ce\u00cd\3\2\2\2\u00cf+\3\2\2\2\u00d0\u00d1\5\16\b\2\u00d1\u00d2"+
		"\7\60\2\2\u00d2\u00d3\5> \2\u00d3\u00d4\7A\2\2\u00d4-\3\2\2\2\u00d5\u00d6"+
		"\7\35\2\2\u00d6\u00d7\5> \2\u00d7\u00d8\7 \2\2\u00d8\u00e0\5(\25\2\u00d9"+
		"\u00da\7\26\2\2\u00da\u00db\5> \2\u00db\u00dc\7 \2\2\u00dc\u00dd\5(\25"+
		"\2\u00dd\u00df\3\2\2\2\u00de\u00d9\3\2\2\2\u00df\u00e2\3\2\2\2\u00e0\u00de"+
		"\3\2\2\2\u00e0\u00e1\3\2\2\2\u00e1\u00e5\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e3"+
		"\u00e4\7\25\2\2\u00e4\u00e6\5(\25\2\u00e5\u00e3\3\2\2\2\u00e5\u00e6\3"+
		"\2\2\2\u00e6\u00e7\3\2\2\2\u00e7\u00e8\7\30\2\2\u00e8\u00e9\7C\2\2\u00e9"+
		"/\3\2\2\2\u00ea\u00eb\7\33\2\2\u00eb\u00ec\7;\2\2\u00ec\u00ed\7\20\2\2"+
		"\u00ed\u00ee\7\60\2\2\u00ee\u00ef\7H\2\2\u00ef\u00f0\3\2\2\2\u00f0\u00f1"+
		"\7B\2\2\u00f1\u00f2\5> \2\u00f2\u00f3\3\2\2\2\u00f3\u00f4\7B\2\2\u00f4"+
		"\u00f5\5> \2\u00f5\u00f6\3\2\2\2\u00f6\u00f7\7<\2\2\u00f7\u00f8\7\24\2"+
		"\2\u00f8\u00f9\5(\25\2\u00f9\u00fa\7\31\2\2\u00fa\u00fb\7C\2\2\u00fb\61"+
		"\3\2\2\2\u00fc\u00fd\7\"\2\2\u00fd\u00fe\5> \2\u00fe\u00ff\7\24\2\2\u00ff"+
		"\u0100\5(\25\2\u0100\u0101\7\32\2\2\u0101\u0102\7C\2\2\u0102\63\3\2\2"+
		"\2\u0103\u0104\7\24\2\2\u0104\u0105\5(\25\2\u0105\u0106\7\"\2\2\u0106"+
		"\u0107\5> \2\u0107\u0108\7#\2\2\u0108\u0109\7C\2\2\u0109\65\3\2\2\2\u010a"+
		"\u010b\7\22\2\2\u010b\u010c\7A\2\2\u010c\67\3\2\2\2\u010d\u010e\7\23\2"+
		"\2\u010e\u010f\7A\2\2\u010f9\3\2\2\2\u0110\u0111\7\20\2\2\u0111\u0112"+
		"\7;\2\2\u0112\u0117\5> \2\u0113\u0114\7D\2\2\u0114\u0116\5> \2\u0115\u0113"+
		"\3\2\2\2\u0116\u0119\3\2\2\2\u0117\u0115\3\2\2\2\u0117\u0118\3\2\2\2\u0118"+
		"\u011a\3\2\2\2\u0119\u0117\3\2\2\2\u011a\u011b\7<\2\2\u011b\u011c\7A\2"+
		"\2\u011c;\3\2\2\2\u011d\u011f\7\37\2\2\u011e\u0120\5> \2\u011f\u011e\3"+
		"\2\2\2\u011f\u0120\3\2\2\2\u0120\u0121\3\2\2\2\u0121\u0122\7A\2\2\u0122"+
		"=\3\2\2\2\u0123\u0124\3\2\2\2\u0124?\3\2\2\2\u0125\u0126\3\2\2\2\u0126"+
		"A\3\2\2\2\u0127\u0128\3\2\2\2\u0128C\3\2\2\2\u0129\u012a\3\2\2\2\u012a"+
		"E\3\2\2\2\u012b\u012c\3\2\2\2\u012cG\3\2\2\2\u012d\u012e\3\2\2\2\u012e"+
		"I\3\2\2\2\27MSYbgktz\u0080\u008b\u0091\u009a\u00a0\u00a5\u00b6\u00c2\u00ce"+
		"\u00e0\u00e5\u0117\u011f";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}