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

//MYPART: TEST PARSER and LEXER

//Parser
program: variable_declaration_part function_declaration_part EOF;


//variable declaration
variable_declaration_part: variable_declaration*;
variable_declaration: VAR COLON declaration_list SEMI;

declaration_list:  initialization (COMMA initialization)*; //either a var or an initialization

initialization: variable (ASSIGN literal)?; 
variable: ID (LEFT_SQUARE INT_LIT RIGHT_SQUARE)*; //single or composite

literal:
    bool_lit
    |INT_LIT 
    |FLOAT_LIT
    |STRING_LIT
    |array_lit;

//function declaration
function_declaration_part: function_declaration*;
function_declaration:
    function_name
    function_parameter?
    function_body 
;
function_name: FUNCTION COLON ID;
function_parameter: PARAMETER COLON parameter_list;
parameter_list: variable (COMMA variable)*;
function_body:
    BODY COLON
        statement_list
    ENDBODY DOT
    ;

//statements
statement_list: variable_declaration_part //starts with var and then others
    other_statements*;
other_statements:
    assignment_statement # as_stmt
    |if_statement # if_stmt
    |for_statement #for_stmt
    |while_statement # while_stmt
    |do_while_statement #dwhile_stmt
    |break_statement #brk_stmt
    |continue_statement #conti_stmt
    |call_statement #call_stmt
    |return_statement #ret_stmt
    ;
    
assignment_statement: (ID | array_element) ASSIGN expression SEMI;
if_statement: 
    IF expression THEN statement_list
    (ELSEIF expression THEN statement_list)*
    (ELSE statement_list)?
    ENDIF DOT
    ;
for_statement:
    FOR LEFT_PAREN (ID ASSIGN expression) (COMMA expression) (COMMA expression) RIGHT_PAREN DO
        statement_list
    ENDFOR DOT
    ;
while_statement:
    WHILE expression DO statement_list ENDWHILE DOT;
do_while_statement:
    DO statement_list WHILE expression ENDDO DOT;
break_statement: BREAK SEMI;
continue_statement: CONTINUE SEMI;
call_statement:  function_call SEMI;   
return_statement: RETURN expression? SEMI;
//expressions:
expression_list: expression (COMMA expression)*;

// .. BNF Style EXPR
expression: rela_expr;
rela_expr: logic_expr relational_op logic_expr | logic_expr;
logic_expr: logic_expr logical_op add_expr | add_expr;
add_expr: add_expr adding_op mul_expr | mul_expr;
mul_expr: mul_expr multiplying_op negation_expr | negation_expr;
negation_expr: negation_op negation_expr | sign_expr;
sign_expr: sign_op sign_expr | element_expr;
element_expr: array_element | func_expr;        
func_expr: function_call | sub_expr;
sub_expr: LEFT_PAREN expression RIGHT_PAREN | operative;
operative: literal | ID ;

array_element: (function_call | ID) index_op;
index_op: (LEFT_SQUARE expression RIGHT_SQUARE)+;
function_call: ID LEFT_PAREN expression_list? RIGHT_PAREN;
sign_op: MINUS | MINUS_DOT;
negation_op: NOT;
multiplying_op:  (STAR|STAR_DOT|DIV|DIV_DOT|MOD) ;
adding_op:  (PLUS|PLUS_DOT|MINUS|MINUS_DOT) ;
logical_op:  (AND| OR) ;
relational_op: (EQUAL | NOT_EQUAL | LESS | LESS_DOT | GREATER | GREATER_DOT | LESS_EQUAL | LESS_EQUAL_DOT | GREATER_EQUAL | GREATER_EQUAL_DOT | EQUAL_DIV_EQUAL);



//Lexer

//fragments
fragment LOWERCASE  : [a-z] ;
fragment UPPERCASE  : [A-Z] ;
fragment DIGIT: [0-9];


//words
ID: LOWERCASE (LOWERCASE | UPPERCASE | '_' | DIGIT)*;
//keywords
BODY: 'Body'; 
BREAK: 'Break';
CONTINUE:'Continue';
DO: 'Do';
ELSE: 'Else';
ELSEIF: 'ElseIf';
ENDBODY: 'EndBody';
ENDIF: 'EndIf';
ENDFOR: 'EndFor';
ENDWHILE: 'EndWhile';
FOR: 'For';
FUNCTION: 'Function';
IF: 'If';
PARAMETER: 'Parameter';
RETURN: 'Return';
THEN: 'Then';
VAR: 'Var';
WHILE: 'While';
ENDDO: 'EndDo';
TRUE: 'True'; 
FALSE: 'False';

//operators
    //assignment
ASSIGN: '=';
    //arithmetic
PLUS: '+';
PLUS_DOT:'+.';
MINUS: '-';
MINUS_DOT:'-.';
STAR:'*';
STAR_DOT:'*.';
DIV:'\\';
DIV_DOT:'\\.';
MOD:'%';
    //bool
NOT:'!';
AND:'&&';
OR:'||';
    //relational
EQUAL:'==';
NOT_EQUAL:'!=';
LESS:'<';
GREATER:'>';
LESS_EQUAL:'<=';
GREATER_EQUAL:'>=';
EQUAL_DIV_EQUAL:'=/=';
LESS_DOT:'<.';
GREATER_DOT:'>.';
LESS_EQUAL_DOT:'<=.';
GREATER_EQUAL_DOT:'>=.';
    //bracets
LEFT_PAREN: '(';
RIGHT_PAREN: ')';
LEFT_SQUARE: '[';
RIGHT_SQUARE: ']';
LEFT_CURLY: '{';
RIGHT_CURLY: '}';
    //punctuation
SEMI:';';
COLON:':';
DOT: '.';
COMMA: ',';

//skip
WS : [ \t\r\f\n]+ -> skip ;

//comment
BLOCK_COMMENT : '**' .*?'**' -> skip; 
UNTERMINATED_COMMENT: '**'.*? ; //COMMENT ERROR

//literals 
fragment BASE_10: '0' | [1-9] DIGIT*;
fragment BASE_16: '0' ('x'|'X') [1-9A-F][0-9A-F]*;
fragment BASE_8: '0' ('o'|'O') [1-7][0-7]*;
INT_LIT: BASE_10 | BASE_16 | BASE_8; // three different bases for integer

fragment EXPONENT_P : [eE] [+-]? DIGIT+;
fragment DECIMAL_P : '.' DIGIT*;
FLOAT_LIT : DIGIT+ (DECIMAL_P | EXPONENT_P | DECIMAL_P EXPONENT_P); //float must at least have decimal or exponent

bool_lit: TRUE | FALSE; //this is parser

fragment ESCAPE_SEQUENCE: 
    '\\\''
	| '\\\\'
	| '\\b'
	| '\\f'
	| '\\n'
	| '\\r'
	| '\\t';
fragment CHAR_STRING : ~["\\\r\n'] | ESCAPE_SEQUENCE | '\'"'; // '" is used to write "
STRING_LIT: '"' CHAR_STRING* '"' {self.text = self.text.strip('"')};
ILLEGAL_ESCAPE: '"' CHAR_STRING* ('\\' ~([bfnrt\\] | '\'') )  {self.text = self.text.replace('"','',1)};
UNCLOSE_STRING: '"' CHAR_STRING* {self.text = self.text.replace('"','',1)}; 

//array

array_lit:  '{'(literal_list)'}'; //array must have same type but it's not for lex/parser
literal_list: literal(',' literal)*;


//ERRORs
ERROR_CHAR: .;
