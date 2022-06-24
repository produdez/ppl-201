grammar JavaBoolExpr;


program: (expr ';')*;


// expr:
//     <assoc=right>'!'expr
//     |expr2('=='|'!=')expr2 | expr2;
// expr2:
//     expr3('<'|'<='|'>'|'>=')expr3 | expr3;
// expr3:
//     expr3('||')expr3
//     |expr3('&&')expr3
//     |ID
//     |LITERAL;

expr:
    expr('||') expr
    |expr('&&')expr
    |expr2('<'|'<='|'>'|'>=')expr2
    |expr2; 
expr2: //lower level for non-assoc
    expr3('=='|'!=')expr3
    |expr3;
expr3: //lower ...
    <assoc=right> '!' expr3
    |ID
    |LITERAL;

// wrong_bool_expr:
// <assoc=right>'!'wrong_bool_expr
// |wrong_bool_expr('=='|'!=')wrong_bool_expr
// |wrong_bool_expr('<'|'<='|'>'|'>=')wrong_bool_expr
// |wrong_bool_expr('||')wrong_bool_expr
// |wrong_bool_expr('&&')wrong_bool_expr
// |ID
// |LITERAL;

// expr:
//     |and_expr;
// //braced_expr: '(' expr ')' | val_id;
// and_expr: and_expr '&&' or_expr | or_expr;
// or_expr: or_expr '||' greater_less_expr | greater_less_expr;
// greater_less_expr: equal_expr ('<'|'<='|'>'|'>=') equal_expr | equal_expr;
// equal_expr: not_expr ('==' | '!=') not_expr | not_expr;
// not_expr: '!' not_expr | val_id; 
// val_id: ID | LITERAL;

// EXPR_ERROR: ~[;\n]* ';';

LITERAL: //some data
    ('True'|'False')
    | [0-9]+
    | '"' (~'"')* '"';
ID: [a-z][a-z0-9]*;
COMMENT: '//' ~[\n]* '\n' -> skip;

WS: [ \n\t\f\r]->skip;

