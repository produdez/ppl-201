grammar q1;

assign: id '=' expr;
id: 'A' | 'B' | 'C';
expr: expr '+' term | term;
term: term '*' factor | factor;
factor: '(' expr ')' | id;

WS: [\n\r\f\t ]-> skip;