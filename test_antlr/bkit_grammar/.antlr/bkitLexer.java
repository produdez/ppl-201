// Generated from e:\Messy\Downloads\BKIT ASSIGN\test_antlr\bkit_grammar\bkit.g4 by ANTLR 4.8
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class BKITLexer extends Lexer {
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
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"LOWERCASE", "UPPERCASE", "DIGIT", "ID", "BODY", "BREAK", "CONTINUE", 
			"DO", "ELSE", "ELSEIF", "ENDBODY", "ENDIF", "ENDFOR", "ENDWHILE", "FOR", 
			"FUNCTION", "IF", "PARAMETER", "RETURN", "THEN", "VAR", "WHILE", "ENDDO", 
			"TRUE", "FALSE", "ASSIGN", "PLUS", "PLUS_DOT", "MINUS", "MINUS_DOT", 
			"STAR", "STAR_DOT", "DIV", "DIV_DOT", "MOD", "NOT", "AND", "OR", "EQUAL", 
			"NOT_EQUAL", "LESS", "GREATER", "LESS_EQUAL", "GREATER_EQUAL", "EQUAL_DIV_EQUAL", 
			"LESS_DOT", "GREATER_DOT", "LESS_EQUAL_DOT", "GREATER_EQUAL_DOT", "LEFT_PAREN", 
			"RIGHT_PAREN", "LEFT_SQUARE", "RIGHT_SQUARE", "LEFT_CURLY", "RIGHT_CURLY", 
			"SEMI", "COLON", "DOT", "COMMA", "WS", "BLOCK_COMMENT", "UNTERMINATED_COMMENT", 
			"BASE_10", "BASE_16", "BASE_8", "INT_LIT", "EXPONENT_P", "DECIMAL_P", 
			"FLOAT_LIT", "ESCAPE_SEQUENCE", "CHAR_STRING", "STRING_LIT", "ILLEGAL_ESCAPE", 
			"UNCLOSE_STRING", "ERROR_CHAR"
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


	public BKITLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "bkit.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2C\u020e\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t;\4<\t<\4=\t="+
		"\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I"+
		"\tI\4J\tJ\4K\tK\4L\tL\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5\3\5\7\5"+
		"\u00a5\n\5\f\5\16\5\u00a8\13\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7"+
		"\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3"+
		"\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f"+
		"\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17"+
		"\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\21\3\21\3\21"+
		"\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23"+
		"\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25"+
		"\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\30"+
		"\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32"+
		"\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\37\3\37\3\37"+
		"\3 \3 \3!\3!\3!\3\"\3\"\3#\3#\3#\3$\3$\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3"+
		"(\3(\3)\3)\3)\3*\3*\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.\3.\3.\3/\3/\3/\3\60"+
		"\3\60\3\60\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\63\3\63\3\64\3\64"+
		"\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\6=\u0183"+
		"\n=\r=\16=\u0184\3=\3=\3>\3>\3>\3>\7>\u018d\n>\f>\16>\u0190\13>\3>\3>"+
		"\3>\3>\3>\3?\3?\3?\3?\7?\u019b\n?\f?\16?\u019e\13?\3@\3@\3@\7@\u01a3\n"+
		"@\f@\16@\u01a6\13@\5@\u01a8\n@\3A\3A\3A\3A\7A\u01ae\nA\fA\16A\u01b1\13"+
		"A\3B\3B\3B\3B\7B\u01b7\nB\fB\16B\u01ba\13B\3C\3C\3C\5C\u01bf\nC\3D\3D"+
		"\5D\u01c3\nD\3D\6D\u01c6\nD\rD\16D\u01c7\3E\3E\7E\u01cc\nE\fE\16E\u01cf"+
		"\13E\3F\6F\u01d2\nF\rF\16F\u01d3\3F\3F\3F\3F\3F\5F\u01db\nF\3G\3G\3G\3"+
		"G\3G\3G\3G\3G\3G\3G\3G\3G\3G\3G\5G\u01eb\nG\3H\3H\3H\3H\5H\u01f1\nH\3"+
		"I\3I\7I\u01f5\nI\fI\16I\u01f8\13I\3I\3I\3J\3J\7J\u01fe\nJ\fJ\16J\u0201"+
		"\13J\3J\3J\3J\3K\3K\7K\u0208\nK\fK\16K\u020b\13K\3L\3L\4\u018e\u019c\2"+
		"M\3\2\5\2\7\2\t\3\13\4\r\5\17\6\21\7\23\b\25\t\27\n\31\13\33\f\35\r\37"+
		"\16!\17#\20%\21\'\22)\23+\24-\25/\26\61\27\63\30\65\31\67\329\33;\34="+
		"\35?\36A\37C E!G\"I#K$M%O&Q\'S(U)W*Y+[,]-_.a/c\60e\61g\62i\63k\64m\65"+
		"o\66q\67s8u9w:y;{<}=\177\2\u0081\2\u0083\2\u0085>\u0087\2\u0089\2\u008b"+
		"?\u008d\2\u008f\2\u0091@\u0093A\u0095B\u0097C\3\2\21\3\2c|\3\2C\\\3\2"+
		"\62;\5\2\13\f\16\17\"\"\3\2\63;\4\2ZZzz\4\2\63;CH\4\2\62;CH\4\2QQqq\3"+
		"\2\639\3\2\629\4\2GGgg\4\2--//\7\2\f\f\17\17$$))^^\t\2))^^ddhhppttvv\2"+
		"\u0221\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2"+
		"\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35"+
		"\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)"+
		"\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2"+
		"\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2"+
		"A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3"+
		"\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2"+
		"\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2"+
		"g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3"+
		"\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\u0085"+
		"\3\2\2\2\2\u008b\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2"+
		"\2\2\u0097\3\2\2\2\3\u0099\3\2\2\2\5\u009b\3\2\2\2\7\u009d\3\2\2\2\t\u009f"+
		"\3\2\2\2\13\u00a9\3\2\2\2\r\u00ae\3\2\2\2\17\u00b4\3\2\2\2\21\u00bd\3"+
		"\2\2\2\23\u00c0\3\2\2\2\25\u00c5\3\2\2\2\27\u00cc\3\2\2\2\31\u00d4\3\2"+
		"\2\2\33\u00da\3\2\2\2\35\u00e1\3\2\2\2\37\u00ea\3\2\2\2!\u00ee\3\2\2\2"+
		"#\u00f7\3\2\2\2%\u00fa\3\2\2\2\'\u0104\3\2\2\2)\u010b\3\2\2\2+\u0110\3"+
		"\2\2\2-\u0114\3\2\2\2/\u011a\3\2\2\2\61\u0120\3\2\2\2\63\u0125\3\2\2\2"+
		"\65\u012b\3\2\2\2\67\u012d\3\2\2\29\u012f\3\2\2\2;\u0132\3\2\2\2=\u0134"+
		"\3\2\2\2?\u0137\3\2\2\2A\u0139\3\2\2\2C\u013c\3\2\2\2E\u013e\3\2\2\2G"+
		"\u0141\3\2\2\2I\u0143\3\2\2\2K\u0145\3\2\2\2M\u0148\3\2\2\2O\u014b\3\2"+
		"\2\2Q\u014e\3\2\2\2S\u0151\3\2\2\2U\u0153\3\2\2\2W\u0155\3\2\2\2Y\u0158"+
		"\3\2\2\2[\u015b\3\2\2\2]\u015f\3\2\2\2_\u0162\3\2\2\2a\u0165\3\2\2\2c"+
		"\u0169\3\2\2\2e\u016d\3\2\2\2g\u016f\3\2\2\2i\u0171\3\2\2\2k\u0173\3\2"+
		"\2\2m\u0175\3\2\2\2o\u0177\3\2\2\2q\u0179\3\2\2\2s\u017b\3\2\2\2u\u017d"+
		"\3\2\2\2w\u017f\3\2\2\2y\u0182\3\2\2\2{\u0188\3\2\2\2}\u0196\3\2\2\2\177"+
		"\u01a7\3\2\2\2\u0081\u01a9\3\2\2\2\u0083\u01b2\3\2\2\2\u0085\u01be\3\2"+
		"\2\2\u0087\u01c0\3\2\2\2\u0089\u01c9\3\2\2\2\u008b\u01d1\3\2\2\2\u008d"+
		"\u01ea\3\2\2\2\u008f\u01f0\3\2\2\2\u0091\u01f2\3\2\2\2\u0093\u01fb\3\2"+
		"\2\2\u0095\u0205\3\2\2\2\u0097\u020c\3\2\2\2\u0099\u009a\t\2\2\2\u009a"+
		"\4\3\2\2\2\u009b\u009c\t\3\2\2\u009c\6\3\2\2\2\u009d\u009e\t\4\2\2\u009e"+
		"\b\3\2\2\2\u009f\u00a6\5\3\2\2\u00a0\u00a5\5\3\2\2\u00a1\u00a5\5\5\3\2"+
		"\u00a2\u00a5\7a\2\2\u00a3\u00a5\5\7\4\2\u00a4\u00a0\3\2\2\2\u00a4\u00a1"+
		"\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a4\u00a3\3\2\2\2\u00a5\u00a8\3\2\2\2\u00a6"+
		"\u00a4\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\n\3\2\2\2\u00a8\u00a6\3\2\2\2"+
		"\u00a9\u00aa\7D\2\2\u00aa\u00ab\7q\2\2\u00ab\u00ac\7f\2\2\u00ac\u00ad"+
		"\7{\2\2\u00ad\f\3\2\2\2\u00ae\u00af\7D\2\2\u00af\u00b0\7t\2\2\u00b0\u00b1"+
		"\7g\2\2\u00b1\u00b2\7c\2\2\u00b2\u00b3\7m\2\2\u00b3\16\3\2\2\2\u00b4\u00b5"+
		"\7E\2\2\u00b5\u00b6\7q\2\2\u00b6\u00b7\7p\2\2\u00b7\u00b8\7v\2\2\u00b8"+
		"\u00b9\7k\2\2\u00b9\u00ba\7p\2\2\u00ba\u00bb\7w\2\2\u00bb\u00bc\7g\2\2"+
		"\u00bc\20\3\2\2\2\u00bd\u00be\7F\2\2\u00be\u00bf\7q\2\2\u00bf\22\3\2\2"+
		"\2\u00c0\u00c1\7G\2\2\u00c1\u00c2\7n\2\2\u00c2\u00c3\7u\2\2\u00c3\u00c4"+
		"\7g\2\2\u00c4\24\3\2\2\2\u00c5\u00c6\7G\2\2\u00c6\u00c7\7n\2\2\u00c7\u00c8"+
		"\7u\2\2\u00c8\u00c9\7g\2\2\u00c9\u00ca\7K\2\2\u00ca\u00cb\7h\2\2\u00cb"+
		"\26\3\2\2\2\u00cc\u00cd\7G\2\2\u00cd\u00ce\7p\2\2\u00ce\u00cf\7f\2\2\u00cf"+
		"\u00d0\7D\2\2\u00d0\u00d1\7q\2\2\u00d1\u00d2\7f\2\2\u00d2\u00d3\7{\2\2"+
		"\u00d3\30\3\2\2\2\u00d4\u00d5\7G\2\2\u00d5\u00d6\7p\2\2\u00d6\u00d7\7"+
		"f\2\2\u00d7\u00d8\7K\2\2\u00d8\u00d9\7h\2\2\u00d9\32\3\2\2\2\u00da\u00db"+
		"\7G\2\2\u00db\u00dc\7p\2\2\u00dc\u00dd\7f\2\2\u00dd\u00de\7H\2\2\u00de"+
		"\u00df\7q\2\2\u00df\u00e0\7t\2\2\u00e0\34\3\2\2\2\u00e1\u00e2\7G\2\2\u00e2"+
		"\u00e3\7p\2\2\u00e3\u00e4\7f\2\2\u00e4\u00e5\7Y\2\2\u00e5\u00e6\7j\2\2"+
		"\u00e6\u00e7\7k\2\2\u00e7\u00e8\7n\2\2\u00e8\u00e9\7g\2\2\u00e9\36\3\2"+
		"\2\2\u00ea\u00eb\7H\2\2\u00eb\u00ec\7q\2\2\u00ec\u00ed\7t\2\2\u00ed \3"+
		"\2\2\2\u00ee\u00ef\7H\2\2\u00ef\u00f0\7w\2\2\u00f0\u00f1\7p\2\2\u00f1"+
		"\u00f2\7e\2\2\u00f2\u00f3\7v\2\2\u00f3\u00f4\7k\2\2\u00f4\u00f5\7q\2\2"+
		"\u00f5\u00f6\7p\2\2\u00f6\"\3\2\2\2\u00f7\u00f8\7K\2\2\u00f8\u00f9\7h"+
		"\2\2\u00f9$\3\2\2\2\u00fa\u00fb\7R\2\2\u00fb\u00fc\7c\2\2\u00fc\u00fd"+
		"\7t\2\2\u00fd\u00fe\7c\2\2\u00fe\u00ff\7o\2\2\u00ff\u0100\7g\2\2\u0100"+
		"\u0101\7v\2\2\u0101\u0102\7g\2\2\u0102\u0103\7t\2\2\u0103&\3\2\2\2\u0104"+
		"\u0105\7T\2\2\u0105\u0106\7g\2\2\u0106\u0107\7v\2\2\u0107\u0108\7w\2\2"+
		"\u0108\u0109\7t\2\2\u0109\u010a\7p\2\2\u010a(\3\2\2\2\u010b\u010c\7V\2"+
		"\2\u010c\u010d\7j\2\2\u010d\u010e\7g\2\2\u010e\u010f\7p\2\2\u010f*\3\2"+
		"\2\2\u0110\u0111\7X\2\2\u0111\u0112\7c\2\2\u0112\u0113\7t\2\2\u0113,\3"+
		"\2\2\2\u0114\u0115\7Y\2\2\u0115\u0116\7j\2\2\u0116\u0117\7k\2\2\u0117"+
		"\u0118\7n\2\2\u0118\u0119\7g\2\2\u0119.\3\2\2\2\u011a\u011b\7G\2\2\u011b"+
		"\u011c\7p\2\2\u011c\u011d\7f\2\2\u011d\u011e\7F\2\2\u011e\u011f\7q\2\2"+
		"\u011f\60\3\2\2\2\u0120\u0121\7V\2\2\u0121\u0122\7t\2\2\u0122\u0123\7"+
		"w\2\2\u0123\u0124\7g\2\2\u0124\62\3\2\2\2\u0125\u0126\7H\2\2\u0126\u0127"+
		"\7c\2\2\u0127\u0128\7n\2\2\u0128\u0129\7u\2\2\u0129\u012a\7g\2\2\u012a"+
		"\64\3\2\2\2\u012b\u012c\7?\2\2\u012c\66\3\2\2\2\u012d\u012e\7-\2\2\u012e"+
		"8\3\2\2\2\u012f\u0130\7-\2\2\u0130\u0131\7\60\2\2\u0131:\3\2\2\2\u0132"+
		"\u0133\7/\2\2\u0133<\3\2\2\2\u0134\u0135\7/\2\2\u0135\u0136\7\60\2\2\u0136"+
		">\3\2\2\2\u0137\u0138\7,\2\2\u0138@\3\2\2\2\u0139\u013a\7,\2\2\u013a\u013b"+
		"\7\60\2\2\u013bB\3\2\2\2\u013c\u013d\7^\2\2\u013dD\3\2\2\2\u013e\u013f"+
		"\7^\2\2\u013f\u0140\7\60\2\2\u0140F\3\2\2\2\u0141\u0142\7\'\2\2\u0142"+
		"H\3\2\2\2\u0143\u0144\7#\2\2\u0144J\3\2\2\2\u0145\u0146\7(\2\2\u0146\u0147"+
		"\7(\2\2\u0147L\3\2\2\2\u0148\u0149\7~\2\2\u0149\u014a\7~\2\2\u014aN\3"+
		"\2\2\2\u014b\u014c\7?\2\2\u014c\u014d\7?\2\2\u014dP\3\2\2\2\u014e\u014f"+
		"\7#\2\2\u014f\u0150\7?\2\2\u0150R\3\2\2\2\u0151\u0152\7>\2\2\u0152T\3"+
		"\2\2\2\u0153\u0154\7@\2\2\u0154V\3\2\2\2\u0155\u0156\7>\2\2\u0156\u0157"+
		"\7?\2\2\u0157X\3\2\2\2\u0158\u0159\7@\2\2\u0159\u015a\7?\2\2\u015aZ\3"+
		"\2\2\2\u015b\u015c\7?\2\2\u015c\u015d\7\61\2\2\u015d\u015e\7?\2\2\u015e"+
		"\\\3\2\2\2\u015f\u0160\7>\2\2\u0160\u0161\7\60\2\2\u0161^\3\2\2\2\u0162"+
		"\u0163\7@\2\2\u0163\u0164\7\60\2\2\u0164`\3\2\2\2\u0165\u0166\7>\2\2\u0166"+
		"\u0167\7?\2\2\u0167\u0168\7\60\2\2\u0168b\3\2\2\2\u0169\u016a\7@\2\2\u016a"+
		"\u016b\7?\2\2\u016b\u016c\7\60\2\2\u016cd\3\2\2\2\u016d\u016e\7*\2\2\u016e"+
		"f\3\2\2\2\u016f\u0170\7+\2\2\u0170h\3\2\2\2\u0171\u0172\7]\2\2\u0172j"+
		"\3\2\2\2\u0173\u0174\7_\2\2\u0174l\3\2\2\2\u0175\u0176\7}\2\2\u0176n\3"+
		"\2\2\2\u0177\u0178\7\177\2\2\u0178p\3\2\2\2\u0179\u017a\7=\2\2\u017ar"+
		"\3\2\2\2\u017b\u017c\7<\2\2\u017ct\3\2\2\2\u017d\u017e\7\60\2\2\u017e"+
		"v\3\2\2\2\u017f\u0180\7.\2\2\u0180x\3\2\2\2\u0181\u0183\t\5\2\2\u0182"+
		"\u0181\3\2\2\2\u0183\u0184\3\2\2\2\u0184\u0182\3\2\2\2\u0184\u0185\3\2"+
		"\2\2\u0185\u0186\3\2\2\2\u0186\u0187\b=\2\2\u0187z\3\2\2\2\u0188\u0189"+
		"\7,\2\2\u0189\u018a\7,\2\2\u018a\u018e\3\2\2\2\u018b\u018d\13\2\2\2\u018c"+
		"\u018b\3\2\2\2\u018d\u0190\3\2\2\2\u018e\u018f\3\2\2\2\u018e\u018c\3\2"+
		"\2\2\u018f\u0191\3\2\2\2\u0190\u018e\3\2\2\2\u0191\u0192\7,\2\2\u0192"+
		"\u0193\7,\2\2\u0193\u0194\3\2\2\2\u0194\u0195\b>\2\2\u0195|\3\2\2\2\u0196"+
		"\u0197\7,\2\2\u0197\u0198\7,\2\2\u0198\u019c\3\2\2\2\u0199\u019b\13\2"+
		"\2\2\u019a\u0199\3\2\2\2\u019b\u019e\3\2\2\2\u019c\u019d\3\2\2\2\u019c"+
		"\u019a\3\2\2\2\u019d~\3\2\2\2\u019e\u019c\3\2\2\2\u019f\u01a8\7\62\2\2"+
		"\u01a0\u01a4\t\6\2\2\u01a1\u01a3\5\7\4\2\u01a2\u01a1\3\2\2\2\u01a3\u01a6"+
		"\3\2\2\2\u01a4\u01a2\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5\u01a8\3\2\2\2\u01a6"+
		"\u01a4\3\2\2\2\u01a7\u019f\3\2\2\2\u01a7\u01a0\3\2\2\2\u01a8\u0080\3\2"+
		"\2\2\u01a9\u01aa\7\62\2\2\u01aa\u01ab\t\7\2\2\u01ab\u01af\t\b\2\2\u01ac"+
		"\u01ae\t\t\2\2\u01ad\u01ac\3\2\2\2\u01ae\u01b1\3\2\2\2\u01af\u01ad\3\2"+
		"\2\2\u01af\u01b0\3\2\2\2\u01b0\u0082\3\2\2\2\u01b1\u01af\3\2\2\2\u01b2"+
		"\u01b3\7\62\2\2\u01b3\u01b4\t\n\2\2\u01b4\u01b8\t\13\2\2\u01b5\u01b7\t"+
		"\f\2\2\u01b6\u01b5\3\2\2\2\u01b7\u01ba\3\2\2\2\u01b8\u01b6\3\2\2\2\u01b8"+
		"\u01b9\3\2\2\2\u01b9\u0084\3\2\2\2\u01ba\u01b8\3\2\2\2\u01bb\u01bf\5\177"+
		"@\2\u01bc\u01bf\5\u0081A\2\u01bd\u01bf\5\u0083B\2\u01be\u01bb\3\2\2\2"+
		"\u01be\u01bc\3\2\2\2\u01be\u01bd\3\2\2\2\u01bf\u0086\3\2\2\2\u01c0\u01c2"+
		"\t\r\2\2\u01c1\u01c3\t\16\2\2\u01c2\u01c1\3\2\2\2\u01c2\u01c3\3\2\2\2"+
		"\u01c3\u01c5\3\2\2\2\u01c4\u01c6\5\7\4\2\u01c5\u01c4\3\2\2\2\u01c6\u01c7"+
		"\3\2\2\2\u01c7\u01c5\3\2\2\2\u01c7\u01c8\3\2\2\2\u01c8\u0088\3\2\2\2\u01c9"+
		"\u01cd\7\60\2\2\u01ca\u01cc\5\7\4\2\u01cb\u01ca\3\2\2\2\u01cc\u01cf\3"+
		"\2\2\2\u01cd\u01cb\3\2\2\2\u01cd\u01ce\3\2\2\2\u01ce\u008a\3\2\2\2\u01cf"+
		"\u01cd\3\2\2\2\u01d0\u01d2\5\7\4\2\u01d1\u01d0\3\2\2\2\u01d2\u01d3\3\2"+
		"\2\2\u01d3\u01d1\3\2\2\2\u01d3\u01d4\3\2\2\2\u01d4\u01da\3\2\2\2\u01d5"+
		"\u01db\5\u0089E\2\u01d6\u01db\5\u0087D\2\u01d7\u01d8\5\u0089E\2\u01d8"+
		"\u01d9\5\u0087D\2\u01d9\u01db\3\2\2\2\u01da\u01d5\3\2\2\2\u01da\u01d6"+
		"\3\2\2\2\u01da\u01d7\3\2\2\2\u01db\u008c\3\2\2\2\u01dc\u01dd\7^\2\2\u01dd"+
		"\u01eb\7)\2\2\u01de\u01df\7^\2\2\u01df\u01eb\7^\2\2\u01e0\u01e1\7^\2\2"+
		"\u01e1\u01eb\7d\2\2\u01e2\u01e3\7^\2\2\u01e3\u01eb\7h\2\2\u01e4\u01e5"+
		"\7^\2\2\u01e5\u01eb\7p\2\2\u01e6\u01e7\7^\2\2\u01e7\u01eb\7t\2\2\u01e8"+
		"\u01e9\7^\2\2\u01e9\u01eb\7v\2\2\u01ea\u01dc\3\2\2\2\u01ea\u01de\3\2\2"+
		"\2\u01ea\u01e0\3\2\2\2\u01ea\u01e2\3\2\2\2\u01ea\u01e4\3\2\2\2\u01ea\u01e6"+
		"\3\2\2\2\u01ea\u01e8\3\2\2\2\u01eb\u008e\3\2\2\2\u01ec\u01f1\n\17\2\2"+
		"\u01ed\u01f1\5\u008dG\2\u01ee\u01ef\7)\2\2\u01ef\u01f1\7$\2\2\u01f0\u01ec"+
		"\3\2\2\2\u01f0\u01ed\3\2\2\2\u01f0\u01ee\3\2\2\2\u01f1\u0090\3\2\2\2\u01f2"+
		"\u01f6\7$\2\2\u01f3\u01f5\5\u008fH\2\u01f4\u01f3\3\2\2\2\u01f5\u01f8\3"+
		"\2\2\2\u01f6\u01f4\3\2\2\2\u01f6\u01f7\3\2\2\2\u01f7\u01f9\3\2\2\2\u01f8"+
		"\u01f6\3\2\2\2\u01f9\u01fa\7$\2\2\u01fa\u0092\3\2\2\2\u01fb\u01ff\7$\2"+
		"\2\u01fc\u01fe\5\u008fH\2\u01fd\u01fc\3\2\2\2\u01fe\u0201\3\2\2\2\u01ff"+
		"\u01fd\3\2\2\2\u01ff\u0200\3\2\2\2\u0200\u0202\3\2\2\2\u0201\u01ff\3\2"+
		"\2\2\u0202\u0203\7^\2\2\u0203\u0204\n\20\2\2\u0204\u0094\3\2\2\2\u0205"+
		"\u0209\7$\2\2\u0206\u0208\5\u008fH\2\u0207\u0206\3\2\2\2\u0208\u020b\3"+
		"\2\2\2\u0209\u0207\3\2\2\2\u0209\u020a\3\2\2\2\u020a\u0096\3\2\2\2\u020b"+
		"\u0209\3\2\2\2\u020c\u020d\13\2\2\2\u020d\u0098\3\2\2\2\27\2\u00a4\u00a6"+
		"\u0184\u018e\u019c\u01a4\u01a7\u01af\u01b8\u01be\u01c2\u01c7\u01cd\u01d3"+
		"\u01da\u01ea\u01f0\u01f6\u01ff\u0209\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}