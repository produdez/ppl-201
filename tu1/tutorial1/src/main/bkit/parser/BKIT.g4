grammar BKIT;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:       
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;
}

options{
	language=Python3;
}
program:;
/* TUTORIAL 1 */

//question1
// INDENTIFIER: [a-z][a-z0-9]*;

//question2
fragment LOWER_CASE: [a-z];
fragment DIGIT: [0-9];
IDENTIFIER: LOWER_CASE (LOWER_CASE |DIGIT)*;
//question3
// fragment DIGIT: [0-9];
fragment EXPONENT: [eE] [+-]? DIGIT+;
FLOAT:
    (DIGIT+ EXPONENT)
    |(( DIGIT+ '.' | '.' (DIGIT)+ | DIGIT+ '.' DIGIT+ ) EXPONENT?);

// fragment Digit: [0-9];

// fragment EXPONENT: [eE] [+-]? Digit+ ;

// fragment FRACTION: '.'Digit+ ;

// fragment POINTFLOAT: (Digit* FRACTION) | (Digit+ '.');

// fragment EXPFLOAT: (Digit+ | (Digit* FRACTION)) EXPONENT ;

// FLOAT: (POINTFLOAT | EXPFLOAT);
STRING: '\'' (~'\'' | '\'\'')* '\'';

WS: ' ' -> skip;


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
UNTERMINATED_COMMENT: .;
