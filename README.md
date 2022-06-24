<!-- icons  -->
[1.1]: https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white
[2.1]: https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white
[3.1]: https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white
[4.1]: https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white

<!-- links to your social media accounts -->
[1]: https://github.com/produdez
[2]: https://www.linkedin.com/in/produdez/
[3]: https://medium.com/@produde
[4]: https://twitter.com/_Produde_

# BKIT programing language

'Principle of Programing Languages'

**Description:**

This project is the process of building and compiling a new programming language (called `BKIT`) with these [requirements](./BKIT2009\_Specification.pdf).

The process goes through four different assignments (each representing a step of building):

1. Tokenization (Lexer) and tree parsing (Parser)
2. Abstract Syntax Tree (AST) generation
3. Type checking
4. Machine code generation and compiling

Each assignment is in its own folder.

## Details

- NOTE:

```[text]
Each assignment is in its own folder and is separated into two parts:
1. code/src: The full code of the assignment, including:
    - main: main code
    - test: test code
2. submission: The important part of the assignment, including:
    - Main part 
    - Test cases
3. Each subsequent assignment also include all previous assignments as its predecessor
```

1. Assignment 1: Lexer + Parser
   - BKIT.g4 is the vocabulary file containing
   - Tokenization and other syntaxes
2. Assignment 2: AST gen
    - We use the `visitor` pattern to visit each node on the parse tree
    - And generate the AST tree from that
    - Main code in `ASTGeneration.py`
3. Assignment 3: Type check
    - Traverse the AST tree
    - Assign types to literals, also
    - Check if any nodes (or node combination) violating type rules
    - Code in `StaticCheck.py`
4. Assignment 4: Code gen
    - Again traverse the AST tree
    - And generate code based on the information given (node name + node type)
    - The `Emmiter` is the interface that's responsible for generating Jasmine code 
    - That will later be used in JVM to generate lower level machine code that's hardware specific

## Technologies Used

- Python
- Java
- Jasmine
- ANTRL

## Acknowledgements

- This project was based on original code of my teacher Mr. Nguyen Hua Phung
- Many thanks to him and his course.

## Contact

Created by [@produdez](https://github.com/produdez) - feel free to contact me or follow my blog on medium ❤️!

<!-- [![alt text][1.1]][1] -->
[![alt text][2.1]][2]
[![alt text][3.1]][3]
[![alt text][4.1]][4]
