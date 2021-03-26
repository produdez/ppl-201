// Generated from json.g4 by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class jsonParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, STRING=7, NUMBER=8, BOOLEAN=9, 
		WS=10;
	public static final int
		RULE_file = 0, RULE_collection = 1, RULE_single_line_collection = 2, RULE_array = 3, 
		RULE_primitive = 4;
	private static String[] makeRuleNames() {
		return new String[] {
			"file", "collection", "single_line_collection", "array", "primitive"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'{'", "'}'", "':'", "','", "'['", "']'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, "STRING", "NUMBER", "BOOLEAN", 
			"WS"
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
	public String getGrammarFileName() { return "json.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public jsonParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class FileContext extends ParserRuleContext {
		public CollectionContext collection() {
			return getRuleContext(CollectionContext.class,0);
		}
		public FileContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_file; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof jsonListener ) ((jsonListener)listener).enterFile(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof jsonListener ) ((jsonListener)listener).exitFile(this);
		}
	}

	public final FileContext file() throws RecognitionException {
		FileContext _localctx = new FileContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_file);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(10);
			match(T__0);
			setState(11);
			collection();
			setState(12);
			match(T__1);
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

	public static class CollectionContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(jsonParser.STRING, 0); }
		public List<CollectionContext> collection() {
			return getRuleContexts(CollectionContext.class);
		}
		public CollectionContext collection(int i) {
			return getRuleContext(CollectionContext.class,i);
		}
		public List<Single_line_collectionContext> single_line_collection() {
			return getRuleContexts(Single_line_collectionContext.class);
		}
		public Single_line_collectionContext single_line_collection(int i) {
			return getRuleContext(Single_line_collectionContext.class,i);
		}
		public CollectionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_collection; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof jsonListener ) ((jsonListener)listener).enterCollection(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof jsonListener ) ((jsonListener)listener).exitCollection(this);
		}
	}

	public final CollectionContext collection() throws RecognitionException {
		CollectionContext _localctx = new CollectionContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_collection);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(14);
			match(STRING);
			setState(15);
			match(T__2);
			setState(16);
			match(T__0);
			setState(19);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				{
				setState(17);
				collection();
				}
				break;
			case 2:
				{
				setState(18);
				single_line_collection();
				}
				break;
			}
			setState(28);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__3) {
				{
				{
				setState(21);
				match(T__3);
				setState(24);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
				case 1:
					{
					setState(22);
					collection();
					}
					break;
				case 2:
					{
					setState(23);
					single_line_collection();
					}
					break;
				}
				}
				}
				setState(30);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(31);
			match(T__1);
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

	public static class Single_line_collectionContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(jsonParser.STRING, 0); }
		public ArrayContext array() {
			return getRuleContext(ArrayContext.class,0);
		}
		public PrimitiveContext primitive() {
			return getRuleContext(PrimitiveContext.class,0);
		}
		public Single_line_collectionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_single_line_collection; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof jsonListener ) ((jsonListener)listener).enterSingle_line_collection(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof jsonListener ) ((jsonListener)listener).exitSingle_line_collection(this);
		}
	}

	public final Single_line_collectionContext single_line_collection() throws RecognitionException {
		Single_line_collectionContext _localctx = new Single_line_collectionContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_single_line_collection);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(33);
			match(STRING);
			setState(34);
			match(T__2);
			setState(37);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__4:
				{
				setState(35);
				array();
				}
				break;
			case STRING:
			case NUMBER:
			case BOOLEAN:
				{
				setState(36);
				primitive();
				}
				break;
			default:
				throw new NoViableAltException(this);
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

	public static class ArrayContext extends ParserRuleContext {
		public List<PrimitiveContext> primitive() {
			return getRuleContexts(PrimitiveContext.class);
		}
		public PrimitiveContext primitive(int i) {
			return getRuleContext(PrimitiveContext.class,i);
		}
		public ArrayContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_array; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof jsonListener ) ((jsonListener)listener).enterArray(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof jsonListener ) ((jsonListener)listener).exitArray(this);
		}
	}

	public final ArrayContext array() throws RecognitionException {
		ArrayContext _localctx = new ArrayContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_array);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(39);
			match(T__4);
			{
			setState(40);
			primitive();
			}
			setState(45);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__3) {
				{
				{
				setState(41);
				match(T__3);
				setState(42);
				primitive();
				}
				}
				setState(47);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(48);
			match(T__5);
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

	public static class PrimitiveContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(jsonParser.STRING, 0); }
		public TerminalNode NUMBER() { return getToken(jsonParser.NUMBER, 0); }
		public TerminalNode BOOLEAN() { return getToken(jsonParser.BOOLEAN, 0); }
		public PrimitiveContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primitive; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof jsonListener ) ((jsonListener)listener).enterPrimitive(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof jsonListener ) ((jsonListener)listener).exitPrimitive(this);
		}
	}

	public final PrimitiveContext primitive() throws RecognitionException {
		PrimitiveContext _localctx = new PrimitiveContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_primitive);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(50);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << STRING) | (1L << NUMBER) | (1L << BOOLEAN))) != 0)) ) {
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

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\f\67\4\2\t\2\4\3"+
		"\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\5\3\26"+
		"\n\3\3\3\3\3\3\3\5\3\33\n\3\7\3\35\n\3\f\3\16\3 \13\3\3\3\3\3\3\4\3\4"+
		"\3\4\3\4\5\4(\n\4\3\5\3\5\3\5\3\5\7\5.\n\5\f\5\16\5\61\13\5\3\5\3\5\3"+
		"\6\3\6\3\6\2\2\7\2\4\6\b\n\2\3\3\2\t\13\2\66\2\f\3\2\2\2\4\20\3\2\2\2"+
		"\6#\3\2\2\2\b)\3\2\2\2\n\64\3\2\2\2\f\r\7\3\2\2\r\16\5\4\3\2\16\17\7\4"+
		"\2\2\17\3\3\2\2\2\20\21\7\t\2\2\21\22\7\5\2\2\22\25\7\3\2\2\23\26\5\4"+
		"\3\2\24\26\5\6\4\2\25\23\3\2\2\2\25\24\3\2\2\2\26\36\3\2\2\2\27\32\7\6"+
		"\2\2\30\33\5\4\3\2\31\33\5\6\4\2\32\30\3\2\2\2\32\31\3\2\2\2\33\35\3\2"+
		"\2\2\34\27\3\2\2\2\35 \3\2\2\2\36\34\3\2\2\2\36\37\3\2\2\2\37!\3\2\2\2"+
		" \36\3\2\2\2!\"\7\4\2\2\"\5\3\2\2\2#$\7\t\2\2$\'\7\5\2\2%(\5\b\5\2&(\5"+
		"\n\6\2\'%\3\2\2\2\'&\3\2\2\2(\7\3\2\2\2)*\7\7\2\2*/\5\n\6\2+,\7\6\2\2"+
		",.\5\n\6\2-+\3\2\2\2.\61\3\2\2\2/-\3\2\2\2/\60\3\2\2\2\60\62\3\2\2\2\61"+
		"/\3\2\2\2\62\63\7\b\2\2\63\t\3\2\2\2\64\65\t\2\2\2\65\13\3\2\2\2\7\25"+
		"\32\36\'/";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}