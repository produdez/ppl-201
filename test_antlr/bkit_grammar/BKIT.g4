grammar BKIT;

// @lexer::header {
// from lexererr import *
// }

// @lexer::members {
// def emit(self):
//     tk = self.type
//     result = super().emit()
//     if tk == self.UNCLOSE_STRING:       
//         raise UncloseString(result.text)
//     elif tk == self.ILLEGAL_ESCAPE:
//         raise IllegalEscape(result.text)
//     elif tk == self.ERROR_CHAR:
//         raise ErrorToken(result.text)
//     elif tk == self.UNTERMINATED_COMMENT:
//         raise UnterminatedComment()
//     else:
//         return result;
// }

// options{
// 	language=Python3;
// }

//MYPART: TEST PARSER and LEXER

//Parser
program: variable_declaration_part function_declaration_part EOF;


//variable declaration
variable_declaration_part: variable_declaration*;
variable_declaration: VAR COLON declaration_list SEMI;

declaration_list: (variable | initialization)(COMMA (variable | initialization))*; //either a var or an initialization

initialization: variable ASSIGN literal; 
variable: ID | array_element;

array_element: ID index_operator;
index_operator: (LEFT_SQUARE expression RIGHT_SQUARE)+;

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
statement_list: variable_declaration* //starts with var and then others
    (assignment_statement
    |if_statement
    |for_statement
    |while_statement
    |do_while_statement
    |break_statement
    |continue_statement
    |call_statement
    |return_statement)*
    ;
    
assignment_statement: variable ASSIGN expression SEMI;
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

expression: 
    expression2 relational_op expression2 
    | expression2;
expression2: 
    LEFT_PAREN expression RIGHT_PAREN
    | function_call
    | index_operator
    | <assoc=right> sign_op expression2
    | <assoc=right> negation_op expression2
    | expression2 multiplying_op expression2
    | expression2 adding_op expression2
    | expression2 logical_op expression2
    | variable
    | literal;
function_call: ID LEFT_PAREN expression_list? RIGHT_PAREN;


//.. The BNF style
// expression: rela_expr;
// rela_expr: logic_expr relational_op logic_expr | logic_expr;
// logic_expr: logic_expr logical_op add_expr | add_expr;
// add_expr: add_expr adding_op mul_expr | mul_expr;
// mul_expr: mul_expr multiplying_op negation_expr | negation_expr;
// negation_expr: negation_op negation_expr | sign_expr;
// sign_expr: sign_op sign_expr | index_expr;
// index_expr: index_operator | function_call;
// function_call: ID LEFT_PAREN expression_list? RIGHT_PAREN | sub_expr;
// sub_expr: LEFT_PAREN expression RIGHT_PAREN | operative;
// operative: literal | variable ;


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
STRING_LIT: '"' CHAR_STRING* '"' /* {self.text = self.text.strip('"')} */;
ILLEGAL_ESCAPE: '"' CHAR_STRING* ('\\' ~([bfnrt\\] | '\'') ) /* {self.text = self.text.replace('"','',1)} */;
UNCLOSE_STRING: '"' CHAR_STRING* /* {self.text = self.text.replace('"','',1)} */; 

//array

array_lit:  '{'(literal_list)'}'; //array must have same type but it's not for lex/parser
literal_list: literal(',' literal)*;


//ERRORs
ERROR_CHAR: .;
