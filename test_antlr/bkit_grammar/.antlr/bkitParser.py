# Generated from e:\Messy\Downloads\BKIT ASSIGN\test_antlr\bkit_grammar\bkit.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3B")
        buf.write("@\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\7\3\34")
        buf.write("\n\3\f\3\16\3\37\13\3\3\4\3\4\3\4\5\4$\n\4\3\5\3\5\3\5")
        buf.write("\7\5)\n\5\f\5\16\5,\13\5\3\6\6\6/\n\6\r\6\16\6\60\3\7")
        buf.write("\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\5\b<\n\b\3\t\3\t\3\t")
        buf.write("\2\2\n\2\4\6\b\n\f\16\20\2\2\2?\2\22\3\2\2\2\4\30\3\2")
        buf.write("\2\2\6#\3\2\2\2\b%\3\2\2\2\n.\3\2\2\2\f\62\3\2\2\2\16")
        buf.write(";\3\2\2\2\20=\3\2\2\2\22\23\7\25\2\2\23\24\7\65\2\2\24")
        buf.write("\25\5\4\3\2\25\26\7\3\2\2\26\27\5\b\5\2\27\3\3\2\2\2\30")
        buf.write("\35\5\6\4\2\31\32\7\67\2\2\32\34\5\6\4\2\33\31\3\2\2\2")
        buf.write("\34\37\3\2\2\2\35\33\3\2\2\2\35\36\3\2\2\2\36\5\3\2\2")
        buf.write("\2\37\35\3\2\2\2 $\7\4\2\2!\"\7\4\2\2\"$\5\n\6\2# \3\2")
        buf.write("\2\2#!\3\2\2\2$\7\3\2\2\2%*\5\16\b\2&\'\7\67\2\2\')\5")
        buf.write("\16\b\2(&\3\2\2\2),\3\2\2\2*(\3\2\2\2*+\3\2\2\2+\t\3\2")
        buf.write("\2\2,*\3\2\2\2-/\5\f\7\2.-\3\2\2\2/\60\3\2\2\2\60.\3\2")
        buf.write("\2\2\60\61\3\2\2\2\61\13\3\2\2\2\62\63\7\60\2\2\63\64")
        buf.write("\7:\2\2\64\65\7\61\2\2\65\r\3\2\2\2\66<\7<\2\2\67<\7:")
        buf.write("\2\28<\7;\2\29<\7=\2\2:<\5\20\t\2;\66\3\2\2\2;\67\3\2")
        buf.write("\2\2;8\3\2\2\2;9\3\2\2\2;:\3\2\2\2<\17\3\2\2\2=>\3\2\2")
        buf.write("\2>\21\3\2\2\2\7\35#*\60;")
        return buf.getvalue()


class bkitParser ( Parser ):

    grammarFileName = "bkit.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "<INVALID>", "'Body'", "'Break'", 
                     "'Continue'", "'Do'", "'Else'", "'ElseIf'", "'EndBody'", 
                     "'EndIf'", "'EndFor'", "'EndWhile'", "'For'", "'Function'", 
                     "'If'", "'Parameter'", "'Return'", "'Then'", "'Var'", 
                     "'While'", "'+'", "'+.'", "'-'", "'-.'", "'*'", "'*.'", 
                     "'\\'", "'\\.'", "'%'", "'!'", "'&&'", "'||'", "'=='", 
                     "'!='", "'<'", "'>'", "'<='", "'>='", "'=/='", "'<.'", 
                     "'>.'", "'<=.'", "'>=.'", "'('", "')'", "'['", "']'", 
                     "'{'", "'}'", "';'", "':'", "'.'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "IDENTIFIER", "BODY", "BREAK", 
                      "CONTINUE", "DO", "ELSE", "ELSEIF", "ENDBODY", "ENDIF", 
                      "ENDFOR", "ENDWHILE", "FOR", "Function", "IF", "PARAMETER", 
                      "RETURN", "THEN", "VAR", "WHILE", "PLUS", "PLUS_DOT", 
                      "MINUS", "MINUS_DOT", "STAR", "STAR_DOT", "DIV", "DIV_DOT", 
                      "MOD", "NOT", "AND", "OR", "EQUAL", "NOT_EQUAL", "LESS", 
                      "GREATER", "LESS_EQUAL", "GREATER_EQUAL", "EQUAL_DIV_EQUAL", 
                      "LESS_DOT", "GREATER_DOT", "LESS_EQUAL_DOT", "GREATER_EQUAL_DOT", 
                      "LEFT_PAREN", "RIGHT_PAREN", "LEFT_SQUARE", "RIGHT_SQUARE", 
                      "LEFT_CURLY", "RIGHT_CURLY", "SEMI", "COLON", "DOT", 
                      "COMMA", "WS", "BLOCK_COMMENT", "INTEGER", "FLOAT", 
                      "BOOLEAN", "STRING", "FAKE_ERROR_CHAR", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    RULE_variable_declaration = 0
    RULE_variable_list = 1
    RULE_var_id = 2
    RULE_value_list = 3
    RULE_array_dim = 4
    RULE_array_subscript = 5
    RULE_value = 6
    RULE_array = 7

    ruleNames =  [ "variable_declaration", "variable_list", "var_id", "value_list", 
                   "array_dim", "array_subscript", "value", "array" ]

    EOF = Token.EOF
    T__0=1
    IDENTIFIER=2
    BODY=3
    BREAK=4
    CONTINUE=5
    DO=6
    ELSE=7
    ELSEIF=8
    ENDBODY=9
    ENDIF=10
    ENDFOR=11
    ENDWHILE=12
    FOR=13
    Function=14
    IF=15
    PARAMETER=16
    RETURN=17
    THEN=18
    VAR=19
    WHILE=20
    PLUS=21
    PLUS_DOT=22
    MINUS=23
    MINUS_DOT=24
    STAR=25
    STAR_DOT=26
    DIV=27
    DIV_DOT=28
    MOD=29
    NOT=30
    AND=31
    OR=32
    EQUAL=33
    NOT_EQUAL=34
    LESS=35
    GREATER=36
    LESS_EQUAL=37
    GREATER_EQUAL=38
    EQUAL_DIV_EQUAL=39
    LESS_DOT=40
    GREATER_DOT=41
    LESS_EQUAL_DOT=42
    GREATER_EQUAL_DOT=43
    LEFT_PAREN=44
    RIGHT_PAREN=45
    LEFT_SQUARE=46
    RIGHT_SQUARE=47
    LEFT_CURLY=48
    RIGHT_CURLY=49
    SEMI=50
    COLON=51
    DOT=52
    COMMA=53
    WS=54
    BLOCK_COMMENT=55
    INTEGER=56
    FLOAT=57
    BOOLEAN=58
    STRING=59
    FAKE_ERROR_CHAR=60
    ERROR_CHAR=61
    UNCLOSE_STRING=62
    ILLEGAL_ESCAPE=63
    UNTERMINATED_COMMENT=64

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Variable_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(bkitParser.VAR, 0)

        def COLON(self):
            return self.getToken(bkitParser.COLON, 0)

        def variable_list(self):
            return self.getTypedRuleContext(bkitParser.Variable_listContext,0)


        def value_list(self):
            return self.getTypedRuleContext(bkitParser.Value_listContext,0)


        def getRuleIndex(self):
            return bkitParser.RULE_variable_declaration




    def variable_declaration(self):

        localctx = bkitParser.Variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_variable_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.match(bkitParser.VAR)
            self.state = 17
            self.match(bkitParser.COLON)
            self.state = 18
            self.variable_list()
            self.state = 19
            self.match(bkitParser.T__0)
            self.state = 20
            self.value_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_id(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(bkitParser.Var_idContext)
            else:
                return self.getTypedRuleContext(bkitParser.Var_idContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(bkitParser.COMMA)
            else:
                return self.getToken(bkitParser.COMMA, i)

        def getRuleIndex(self):
            return bkitParser.RULE_variable_list




    def variable_list(self):

        localctx = bkitParser.Variable_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_variable_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.var_id()
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==bkitParser.COMMA:
                self.state = 23
                self.match(bkitParser.COMMA)
                self.state = 24
                self.var_id()
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_idContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(bkitParser.IDENTIFIER, 0)

        def array_dim(self):
            return self.getTypedRuleContext(bkitParser.Array_dimContext,0)


        def getRuleIndex(self):
            return bkitParser.RULE_var_id




    def var_id(self):

        localctx = bkitParser.Var_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_var_id)
        try:
            self.state = 33
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.match(bkitParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.match(bkitParser.IDENTIFIER)
                self.state = 32
                self.array_dim()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Value_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(bkitParser.ValueContext)
            else:
                return self.getTypedRuleContext(bkitParser.ValueContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(bkitParser.COMMA)
            else:
                return self.getToken(bkitParser.COMMA, i)

        def getRuleIndex(self):
            return bkitParser.RULE_value_list




    def value_list(self):

        localctx = bkitParser.Value_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_value_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.value()
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==bkitParser.COMMA:
                self.state = 36
                self.match(bkitParser.COMMA)
                self.state = 37
                self.value()
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_dimContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_subscript(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(bkitParser.Array_subscriptContext)
            else:
                return self.getTypedRuleContext(bkitParser.Array_subscriptContext,i)


        def getRuleIndex(self):
            return bkitParser.RULE_array_dim




    def array_dim(self):

        localctx = bkitParser.Array_dimContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_array_dim)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 43
                self.array_subscript()
                self.state = 46 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==bkitParser.LEFT_SQUARE):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_subscriptContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_SQUARE(self):
            return self.getToken(bkitParser.LEFT_SQUARE, 0)

        def INTEGER(self):
            return self.getToken(bkitParser.INTEGER, 0)

        def RIGHT_SQUARE(self):
            return self.getToken(bkitParser.RIGHT_SQUARE, 0)

        def getRuleIndex(self):
            return bkitParser.RULE_array_subscript




    def array_subscript(self):

        localctx = bkitParser.Array_subscriptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_array_subscript)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(bkitParser.LEFT_SQUARE)
            self.state = 49
            self.match(bkitParser.INTEGER)
            self.state = 50
            self.match(bkitParser.RIGHT_SQUARE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEAN(self):
            return self.getToken(bkitParser.BOOLEAN, 0)

        def INTEGER(self):
            return self.getToken(bkitParser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(bkitParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(bkitParser.STRING, 0)

        def array(self):
            return self.getTypedRuleContext(bkitParser.ArrayContext,0)


        def getRuleIndex(self):
            return bkitParser.RULE_value




    def value(self):

        localctx = bkitParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_value)
        try:
            self.state = 57
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [bkitParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.match(bkitParser.BOOLEAN)
                pass
            elif token in [bkitParser.INTEGER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.match(bkitParser.INTEGER)
                pass
            elif token in [bkitParser.FLOAT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 54
                self.match(bkitParser.FLOAT)
                pass
            elif token in [bkitParser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 55
                self.match(bkitParser.STRING)
                pass
            elif token in [bkitParser.EOF, bkitParser.COMMA]:
                self.enterOuterAlt(localctx, 5)
                self.state = 56
                self.array()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return bkitParser.RULE_array




    def array(self):

        localctx = bkitParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_array)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





