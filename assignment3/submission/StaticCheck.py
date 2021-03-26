
"""
 * @author nhphung - mentor
"""

"""
 * @author thlong - writer
"""

#NOTE: starts here
from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import BinaryIO, List, Tuple
from AST import *
from functools import *
from Visitor import *
from StaticError import *

class Type(ABC):
    __metaclass__ = ABCMeta
    def __eq__(self,otherType):
        return type(self) == type(otherType)
class PrimitiveType(Type):
    __metaclass__ = ABCMeta
    pass
class IntType(PrimitiveType):
    pass
class FloatType(PrimitiveType):
    pass
class StringType(PrimitiveType):
    pass
class BoolType(PrimitiveType):
    pass
class VoidType(Type):
    pass
class Unknown(Type):
    pass

@dataclass
class ArrayType(Type):
    dimension:List[int]
    elemtype: Type
    def __eq__(self, other):
        if type(self) != type(other): return False
        return self.dimension == other.dimension and self.elemtype == other.elemtype
    

class TypeCheckSymbol:
    def __init__(self,name: str, symbolType: Type, kind:Kind = Function()):
        self.name = name
        self. symbolType = symbolType
        self.kind = kind
    def __eq__(self,other):
        return self.name == other.name and self.symbolType == other.symbolType
    def toFunc(self): 
        self.kind = Function()
        return self
    def toVar(self): 
        self.kind = Variable()
        return self
    def toParam(self): 
        self.kind = Parameter()
        return self
    def toId(self): 
        self.kind = Identifier()
        return self

    def getParams(self):
        if type(self.symbolType) == FunctionType: return self.symbolType.params
        else: return None

    def returnType(self):
        if type(self.symbolType) == FunctionType: return self.symbolType.rtype

        else: return self.symbolType
    def setReturnType(self,return_type):
        if type(self.symbolType) == FunctionType: self.symbolType.rtype = return_type
        else:  self.symbolType = return_type
        return self.returnType()

    def __str__(self):
        return "Symbol( " + (self.name if self.name else '') + ', ' + (type(self.symbolType).__name__ if type(self.symbolType) != FunctionType else str(self.symbolType)) + ', ' + type(self.kind).__name__+ ',' + type(self.returnType()).__name__ +')'

@dataclass
class FunctionType:
    params:List[TypeCheckSymbol]
    rtype:Type
    #NOTE: functions are the same if same param
    def __eq__(self, other):
        return self.params == other.param_type
    def __str__(self):
        return "Function( "+ str([type(p.returnType()).__name__ for p in self.params] if self.params else ['None']) + '---'+ type(self.rtype).__name__+' )'


def scope_decorator(visit_func):
    return visit_func #comment this to use
    def print_name(*arg):
        print('Begin......',visit_func.__name__,'.......\n')
        ret_val =  visit_func(*arg)
        print('End......',visit_func.__name__,'.......\n')
        return ret_val
    return print_name

class TypeCheckHelper:
    @staticmethod
    def check_redeclare_and_expand( sym_list, local_env):
        for s in sym_list:
            for symbol in local_env:
                if symbol.name == s.name:
                    # print('init: ',symbol,'redecl:', s)
                    raise Redeclared(s.kind,s.name)
            local_env.append(s)
        return local_env
    @staticmethod
    def symbol_lookup(name,env):
        for scope in env:
            for symbol in scope:
                if symbol.name == name: return symbol
        return None #NOTE: none if not found
    
    @staticmethod
    def printScope(lst,name):

        print('-------',name,'-----')
        for s in lst:
            print(str(s))
        print('-------',name,'-----')
    
    @staticmethod
    def isUnknownArray( array_type: ArrayType):
        if type(array_type) != ArrayType: return False
        arr_type = array_type
        while type(arr_type) == ArrayType:
            arr_type = arr_type.elemtype
        return arr_type == Unknown()

    @staticmethod
    def checkEntryPoint(env):
        for symbol in env[-1]:
            if symbol.name == 'main' and type(symbol.kind) == Function:
                return
        raise NoEntryPoint()

    @staticmethod
    def infer(symbol,infer_type):
        if not infer_type: 
            return symbol.returnType()
        
        if TypeCheckHelper.isUnknownArray(symbol.symbolType): #case infering unknown array
            if type(infer_type) != ArrayType:
                return symbol.returnType()
            if infer_type.dimension == symbol.symbolType.dimension:
                symbol.symbolType = infer_type
            return symbol.symbolType

        if symbol.returnType() != Unknown(): 
            return symbol.returnType()
        
        symbol.setReturnType(infer_type)

        return symbol.returnType()

class StaticChecker(BaseVisitor):
    def __init__(self,ast):
        self.ast = ast
        self.first_check = True

        self.global_scope = [
TypeCheckSymbol("int_of_float",FunctionType([TypeCheckSymbol(None,FloatType(),Parameter())],IntType())),
TypeCheckSymbol("float_to_int",FunctionType([TypeCheckSymbol(None,IntType(),Parameter())],FloatType())),
TypeCheckSymbol("int_of_string",FunctionType([TypeCheckSymbol(None,StringType(),Parameter())],IntType())),
TypeCheckSymbol("string_of_int",FunctionType([TypeCheckSymbol(None,IntType(),Parameter())],StringType())),
TypeCheckSymbol("float_of_string",FunctionType([TypeCheckSymbol(None,StringType(),Parameter())],FloatType())),
TypeCheckSymbol("string_of_float",FunctionType([TypeCheckSymbol(None,FloatType(),Parameter())],StringType())),
TypeCheckSymbol("bool_of_string",FunctionType([TypeCheckSymbol(None,StringType(),Parameter())],BoolType())),
TypeCheckSymbol("string_of_bool",FunctionType([TypeCheckSymbol(None,BoolType(),Parameter())],StringType())),
TypeCheckSymbol("read",FunctionType([],StringType())),
TypeCheckSymbol("printLn",FunctionType([],VoidType())),
TypeCheckSymbol("print",FunctionType([TypeCheckSymbol(None,StringType(),Parameter())],VoidType())),
TypeCheckSymbol("printStrLn",FunctionType([TypeCheckSymbol(None,StringType(),Parameter())],VoidType()))]


    """NOTE: helper visit functions"""

    def global_lookup(self,name):
        for symbol in self.global_scope:
            if symbol.name == name: return symbol
    def visitCodeBlock(self,decl_ast,stmt_ast,env):
        declarations = [decl.accept(self,env) for decl in decl_ast] if decl_ast else [] 
        env[0] = TypeCheckHelper.check_redeclare_and_expand(declarations,env[0])
        [stmt.accept(self,env) for stmt in stmt_ast]
    def op_type(self,op):
        if op in ['!','&&','||']: return BoolType()
        if op in ['+','-','*','\\','%','==','!=','<','>','<=','>=']: return IntType()
        if op in ['+.','-.','*.','\\.','=/=','<.','>.','<=.','>=.']: return FloatType()
    
                     
    """NOTE: other visit functions"""

    def check(self):
        """
        each element of the program env 
        represents a level of 
        current scope with 0 being the current local scope
        """
        return self.visit(self.ast,[self.global_scope])
    
    @scope_decorator
    def visitProgram(self,ast, env):
        #NOTE: first run to get all functions's init decl and global vars
        global_decls = [decl.accept(self,env) for decl in ast.decl]
        env[0] = TypeCheckHelper.check_redeclare_and_expand(global_decls,env[0])
        #second run on just the functions are needed
        TypeCheckHelper.checkEntryPoint(env)
        self.first_check = False
        [decl.accept(self,env) for decl in ast.decl if type(decl) is FuncDecl]

        # Helper.printScope(env[0],'global_env_end')
        return self.global_scope
    @scope_decorator
    def visitVarDecl(self, ast:VarDecl, env):
        var_name = ast.variable.name

        #NOTE: case composite var with no init
        if ast.varDimen and not ast.varInit:
            var_type = Unknown()
            for dim in ast.varDimen[::-1]:
                prev_dim = var_type.dimension if type(var_type) == ArrayType else []
                var_type = ArrayType([dim] + prev_dim, var_type)

            return TypeCheckSymbol(var_name,var_type,Variable())
        
        #NOTE: vardecl is not check, just put the var-type to id
        #get var type
        var_type = ast.varInit.accept(self,(env,Unknown(),ast)) if ast.varInit else  Unknown()
        
        return TypeCheckSymbol(var_name,var_type,Variable())

    @scope_decorator
    def visitFuncDecl(self, ast, env):
        func_name = ast.name.name
        current_env = [[]] + env    
        #first run only takes the name and parameter to construct function-type
        if self.first_check:
            #pass in empty environment cause each func is a scope             
            param_sym_list = [p.accept(self,current_env).toParam() for p in ast.param] if ast.param else []
            func_type = FunctionType(param_sym_list,Unknown()) 
            return TypeCheckSymbol(func_name,func_type, Function())
       
        #second run checks out body,...
        self.cur_func_name = func_name # set the current function name for infer /return to use

        param_sym_list = self.global_lookup(func_name).getParams()
        current_env[0] = TypeCheckHelper.check_redeclare_and_expand(param_sym_list,current_env[0])
        
        self.visitCodeBlock(ast.body[0],ast.body[1],current_env)

        # print('Done reading function: ', str(self.global_lookup(func_name)))
        # Helper.printScope(current_env[0],'FUNC_ENV')
        
        #NOTE: do not infer voidtype if function does not have return


    """NOTE: expression params (env, infer_type)"""

    @scope_decorator
    def visitBinaryOp(self, ast:BinaryOp, params):
        env, infer_type, current_stmt = params
        op = ast.op
        op_type = self.op_type(op)
        left_type = ast.left.accept(self,(env,op_type,current_stmt))
        right_type = ast.right.accept(self,(env,op_type,current_stmt))

        if op in ['&&','||']:
            if left_type == right_type == BoolType(): return BoolType()
            else: 
                # print("Binary Mismatch: ", op,'..',str(left_type),',',str(right_type))
                raise TypeMismatchInExpression(ast)
        if op in ['+','-','*','\\','%']:
            if left_type == right_type == IntType(): return IntType()
            else: 
                # print("Binary Mismatch: ", op,'..',str(left_type),',',str(right_type))
                raise TypeMismatchInExpression(ast)
        if op in ['==','!=','<','>','<=','>=']:
            if left_type == right_type == IntType(): return BoolType()
            else: 
                # print("Binary Mismatch: ", op,'..',str(left_type),',',str(right_type))
                raise TypeMismatchInExpression(ast)
        if op in ['+.','-.','*.','\\.']:
            if left_type == right_type == FloatType(): return FloatType()
            else: 
                # print("Binary Mismatch: ", op,'..',str(left_type),',',str(right_type))
                raise TypeMismatchInExpression(ast)
        if op in ['=/=','<.','>.','<=.','>=.']:
            if left_type == right_type == FloatType(): return BoolType()
            else: 
                # print("Binary Mismatch: ", op,'..',str(left_type),',',str(right_type))
                raise TypeMismatchInExpression(ast)
        
        #worst case none?
        return None
    @scope_decorator
    def visitUnaryOp(self, ast: UnaryOp, params):
        
        env, infer_type, current_stmt = params
        op = ast.op
        op_type = self.op_type(op)
        expr_type = ast.body.accept(self,(env,op_type,current_stmt))

        if op == '!' and expr_type != BoolType():
            # print("Unary Mismatch: ", op,'..',str(expr_type))
            raise TypeMismatchInExpression(ast)
        if op == '-' and expr_type != IntType():
            # print("Unary Mismatch: ", op,'..',str(expr_type))
            raise TypeMismatchInExpression(ast)
        if op == '-.' and expr_type != FloatType():
            # print("Unary Mismatch: ", op,'..',str(expr_type))
            raise TypeMismatchInExpression(ast)

        return expr_type
    @scope_decorator
    def visitCallExpr(self, ast: CallExpr, params):
        env, infer_type, current_stmt = params
        func_name = ast.method.name
        
        #check declaration and get function type
        func_sym = TypeCheckHelper.symbol_lookup(func_name,env)

        #could not exist or exist but not a function
        if not func_sym:
            # print('Undeclared',ast)
            raise Undeclared(Function(),func_name)
        if type(func_sym.kind) != Function:
            # print('Undeclared',ast)
            raise Undeclared(Function(),func_name)

        #infer return type
        TypeCheckHelper.infer(func_sym,infer_type)

        #check parameter and argument
        param_sym_list = func_sym.getParams()
        #len 
        if len(param_sym_list) != len(ast.param):
            # print("Func Call Length mismatch: ", len(param_sym_list), len(ast.param))
            raise TypeMismatchInExpression(ast)
        
        #check and infer param/arg
        for param_sym,arg_ast in zip(param_sym_list,ast.param):
            atype = arg_ast.accept(self,(env,None,current_stmt))
            ptype = param_sym.returnType()
            # print('P: ',ptype,'A: ', atype)
            if (type(atype) == ArrayType and type(ptype) != ArrayType) or (type(ptype) == ArrayType and type(atype) != ArrayType):
                    raise TypeMismatchInExpression(ast)

            p_unknown = ptype == Unknown() or TypeCheckHelper.isUnknownArray(ptype)
            a_unknown = atype == Unknown() or TypeCheckHelper.isUnknownArray(atype)

            if p_unknown and a_unknown:
                # print("Cant infer func-call-expr: ",param_sym,', Argument: ',arg_ast,'..with type: ',atype)
                raise TypeCannotBeInferred(current_stmt)
            if p_unknown:
                ptype = TypeCheckHelper.infer(param_sym,atype)
            if a_unknown:
                atype = arg_ast.accept(self,(env,ptype,current_stmt))
            if atype != ptype:
                # print("Arg Type mismatch: ", ptype,',',arg_ast,'-',atype)
                raise TypeMismatchInExpression(ast)

        #infer type
        return func_sym.returnType()
    

    @scope_decorator
    def visitId(self, ast:Id, params):
        #NOTE: id can be array id or normal scalar id
        #infer_type = None -> no infer
        env, infer_type, current_stmt = params
        name = ast.name
        symbol = TypeCheckHelper.symbol_lookup(ast.name,env)
        if not symbol:
            # print('Undeclared',ast)
            raise Undeclared(Identifier(),name)

        if type(symbol.kind) == Function:
            # print('Undeclared',ast)
            raise Undeclared(Identifier(),name)
        
        #infer type here
        return TypeCheckHelper.infer(symbol,infer_type)

    @scope_decorator
    def visitArrayCell(self, ast: ArrayCell, params):
        #infer_type = None -> no infer
        env, infer_type, current_stmt = params
        
        id_type = ast.arr.accept(self,(env,None,current_stmt))

        
        #NOTE: there's no way to infer a function dimension from array cell so error in this case
        if id_type == Unknown() and isinstance(ast.arr,CallExpr):
            raise TypeCannotBeInferred(current_stmt)
        
        #indexing a non-array, including unknown that's not function
        if not isinstance(id_type,ArrayType):
            # print('indexing non -array')
            raise TypeMismatchInExpression(ast)

        #as specified, length must be equal
        idx = ast.idx
        if len(id_type.dimension) != len(idx): 
            # print("Array cell dim mismatch: ", len(id_type.dimension),',',len(idx))
            raise TypeMismatchInExpression(ast)

        #indexing element not int
        for i in idx:
            idx_expr_type = i.accept(self,(env,IntType(),current_stmt))

            if idx_expr_type != IntType():
                # print('Not int index expression', i)
                raise TypeMismatchInExpression(ast)
        
        #NOTE: index out of range is not checked.

        #NOTE: given that array cell has same dimension as array, it always return the innermost (primitive) type.
        
        arr_type = id_type
        while type(arr_type.elemtype) is ArrayType:
            arr_type = arr_type.elemtype
        
        #NOTE: infer array element type here
        if infer_type and arr_type.elemtype == Unknown():
            arr_type.elemtype = infer_type
        
        return arr_type.elemtype

    
    """NOTE: visit of statement has param(func-name, env)"""

    @scope_decorator
    def visitAssign(self, ast: Assign, env):      
        #no infer type at first
        left_type = ast.lhs.accept(self,(env,None,ast))
        right_type = ast.rhs.accept(self,(env,None,ast))
        # print('left', left_type)
        # print('right', right_type)
        if VoidType() in [left_type,right_type]:
            # print("Unknown in assignment",'left:',left_type,'right: ',right_type)
            raise TypeMismatchInStatement(ast)
        if type(ast.rhs) == CallExpr and right_type == Unknown():
            pass #NOTE: this is the case rhs is function call expr, which is not composite var but still can be inferred.
        elif ((type(left_type) == ArrayType and type(right_type) != ArrayType) or (type(right_type) == ArrayType and type(left_type) != ArrayType)):
            # print('left right array non array:',left_type,right_type)
            raise TypeMismatchInStatement(ast)
        
        left_unknown = left_type == Unknown() or TypeCheckHelper.isUnknownArray(left_type)
        right_unknown = right_type == Unknown() or TypeCheckHelper.isUnknownArray(right_type)

        if left_unknown and right_unknown:
            raise TypeCannotBeInferred(ast)
        if left_unknown:
            left_type = ast.lhs.accept(self,(env,right_type,ast))
        if right_unknown: 
            right_type = ast.rhs.accept(self,(env,left_type,ast))

        if left_type != right_type:
            # print('assignment left right mismatch:', left_type,',', right_type)
            raise TypeMismatchInStatement(ast)
        

    @scope_decorator
    def visitIf(self, ast, env):

        #if / elseif part
        for if_blk in ast.ifthenStmt:
            #check condition
            expr = if_blk[0]
            expr_type = expr.accept(self,(env,BoolType(),ast))
            if expr_type != BoolType():
                # print('mismatch boolean condition: ', expr)
                raise TypeMismatchInStatement(ast)
            current_env = [[]] + env
            self.visitCodeBlock(if_blk[1],if_blk[2],current_env)
     
        # else part
        current_env = [[]] + env
        self.visitCodeBlock(ast.elseStmt[0],ast.elseStmt[1],current_env)

    @scope_decorator
    def visitFor(self, ast, env):
        
        #check types required
        init_var_type = ast.idx1.accept(self,(env,IntType(),ast))
        init_value_type = ast.expr1.accept(self,(env,IntType(),ast))
        condition_type = ast.expr2.accept(self,(env,BoolType(),ast))
        update_type = ast.expr3.accept(self,(env,IntType(),ast))
        
        if init_value_type != IntType() or update_type != IntType() or init_var_type != IntType():
            # print('index or update not int type ','var:', init_var_type, 'idx:',init_value_type,'upt',update_type)
            raise TypeMismatchInStatement(ast)
        if condition_type != BoolType():
            # print('condition not bool: ', condition_type)
            raise TypeMismatchInStatement(ast)

        #check body
        current_env = [[]] + env
        self.visitCodeBlock(ast.loop[0],ast.loop[1],current_env)

    def visitContinue(self, ast:Continue, params):
        pass

    def visitBreak(self, ast, params):
        pass

    @scope_decorator
    def visitReturn(self, ast:Return, env):
        
        func_symbol = self.global_lookup(self.cur_func_name)
        
        #function return type
        func_rtype = func_symbol.returnType()
        #expression of return stmt is inferred bases on func return type
        #NOTE: infer expression
        expr_type = ast.expr.accept(self,(env,None,ast)) if ast.expr else VoidType() 

        return_unknown = func_rtype == Unknown()
        expr_unknown = expr_type == Unknown() or TypeCheckHelper.isUnknownArray(expr_type)
        
        if return_unknown and expr_unknown:
            # print('function:', func_symbol, 'expr: ', ast.expr)
            raise TypeCannotBeInferred(ast)
        if expr_unknown:
            #infer expr 
            expr_type = ast.expr.accept(self,(env,func_rtype,ast))
        if return_unknown:
            func_rtype = TypeCheckHelper.infer(func_symbol,expr_type)

        if func_rtype != expr_type:
            # print('expected rtype: ' ,func_rtype, 'returned:', expr_type)
            raise TypeMismatchInStatement(ast)

    @scope_decorator
    def visitDowhile(self, ast, env):

        current_env = [[]] + env
        self.visitCodeBlock(ast.sl[0],ast.sl[1],current_env)

        condition_type = ast.exp.accept(self,(env,BoolType(),ast))
        

        if condition_type != BoolType():
            # print('not bool cond: ', condition_type)
            raise TypeMismatchInStatement(ast)
    
    @scope_decorator
    def visitWhile(self, ast, env):
        
        condition_type = ast.exp.accept(self,(env,BoolType(),ast))
        
        if condition_type != BoolType(): 
            # print('not bool cond: ', condition_type)
            raise TypeMismatchInStatement(ast)

        #checkout stmts 
        current_env = [[]] + env
        self.visitCodeBlock(ast.sl[0],ast.sl[1],current_env)

    @scope_decorator
    def visitCallStmt(self, ast:CallStmt, env):
        # Helper.printScope(env[-1],'global')
        func_name = ast.method.name
        func_sym = self.global_lookup(func_name)
        if not func_sym:
            # print('Undeclared',ast)
            raise Undeclared(Function(),ast.method.name)
        if type(func_sym.kind) != Function:
            # print('Undeclared',ast)
            raise Undeclared(Function(),ast.method.name)

        param_sym_list = func_sym.getParams()
        #len 
        if len(param_sym_list) != len(ast.param): 
            # print('paramlist:',[str(p) for p in param_sym_list],'arg:',ast.param)
            # print("Call stmt Length mismatch: ", len(param_sym_list), len(ast.param))
            raise TypeMismatchInStatement(ast)
        
        #infer return type
        func_rtype = TypeCheckHelper.infer(func_sym,VoidType())
        if func_rtype != VoidType():
            raise TypeMismatchInStatement(ast)

        #check and infer param/arg
        for param_sym,arg_ast in zip(param_sym_list,ast.param):
            atype = arg_ast.accept(self,(env,None,ast))
            ptype = param_sym.returnType()
            
            p_unknown = ptype == Unknown() or TypeCheckHelper.isUnknownArray(ptype) #param can only be unknown, not unknown array.
            a_unknown = atype == Unknown() or TypeCheckHelper.isUnknownArray(atype)

            if p_unknown and a_unknown:
                # print("Cant infer: ",param_sym,', Argument: ',arg_ast,'..with type: ',atype)
                raise TypeCannotBeInferred(ast)
            if p_unknown:
                ptype = TypeCheckHelper.infer(param_sym,atype)
            if a_unknown:
                atype = arg_ast.accept(self,(env,ptype,ast))
            if atype != ptype:
                # print("Arg Type mismatch: ", ptype,',',arg_ast,'-',atype)
                raise TypeMismatchInStatement(ast)


    """NOTE: literal part"""


    @scope_decorator
    def visitIntLiteral(self, ast, params):
        return IntType()
    @scope_decorator
    def visitFloatLiteral(self, ast, params):
        return FloatType()
    @scope_decorator
    def visitBooleanLiteral(self, ast, params):
        return BoolType()
    @scope_decorator
    def visitStringLiteral(self, ast, params):
        return StringType()
    @scope_decorator
    def visitArrayLiteral(self, ast, params):
        env,infer_type,current_env = params
        elems = ast.value
        elem_type = elems[0].accept(self,(env,Unknown(),ast))

        #dimension is calculated recursively
        dim = [len(elems)] + (elem_type.dimension if type(elem_type) == ArrayType else [])
        #NOTE: we do not check for same elem type
        return ArrayType(dim,elem_type)




        
