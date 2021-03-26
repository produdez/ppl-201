grammar csv;

//parser
file: header_row row+ EOF;
header_row: row;
row: field (',' field)* '\r'? '\n';
//lexer
field:
    TEXT
    | STRING
    |
    ; //text or string or nothing
TEXT: ~["\n\r,]+; //can be empty but has to put in parser instead cause lexer will not match empty
STRING: '"' (~["] | '""')* '"';


