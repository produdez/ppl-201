grammar json;

//parser
file: '{' collection '}';
collection: STRING ':' '{'
    (collection|single_line_collection) 
    (',' (collection|single_line_collection) )* 
    '}'; //solved the ',' ending thing "brute-force way"
single_line_collection: STRING ':' (array | primitive);
array: '[' (primitive) (',' primitive)* ']';
primitive: STRING| NUMBER | BOOLEAN;

//lexer
STRING: '"' (~["\n\r])* '"';
NUMBER: INT|HEX;
fragment INT : '0' | [1-9][0-9]*;
fragment HEX : '0' [xX] INT;
BOOLEAN: 'true' | 'false';
WS: [ \n\r\t]->skip;