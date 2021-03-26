'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
from AST import *
from os import symlink
from Visitor import BaseVisitor
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod

class MethodEnv():
    def __init__(self, frame, sym, isLeft = False):
        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft

class Symbol:
    def __init__(self,name,mtype,value = None,initVal=None):
        self.name = name
        self.mtype = mtype
        self.value = value
        self.initVal = initVal
    def __str__(self):
        return  (self.name if self.name else '*')+'-' + str(self.mtype) + '--'+ (str(self.value.value) if self.value else 'NO')
class CName:
    def __init__(self,n):
        self.value = n
class Index:
    def __init__(self,n):
        self.value = n
class Type(ABC):
    def __str__(self): return self.__class__.__name__
    def __eq__(self,otherType):
        return type(self) == type(otherType)
class IntType(Type): pass
class FloatType(Type): pass
class VoidType(Type): pass
class ClassType(Type):
    def __init__(self,n):
        self.cname = n
class StringType(Type):pass
class BoolType(Type): pass
class MType(Type):
    def __init__(self,i,o):
        self.partype = i #List[Symbol]
        self.rettype = o #Type
    def __str__(self):
        return 'Function(' + str([str(x) for x in self.partype])+ ')' + '-->' + str(self.rettype)
class ArrayType(Type):
    def __init__(self,et,s=[1]):
        self.dimen = s   #List[int]  
        self.eleType = et #Type
    def __eq__(self, other):
        if type(self) != type(other): return False
        return self.dimen == other.dimen and self.eleType == other.eleType
    def __str__(self):
        result = "Arr("
        return result + str(self.eleType) + ') -- Dim:' +str(self.dimen)

class CodeGenerator():
    def __init__(self):
        self.libName = "io"

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String
        type_resolver = StaticChecker(ast)
        global_scope = type_resolver.check()
        # TypeCheckHelper.printScope(global_scope,'global_scopes')
        gl = [x.toSymbol() for x in global_scope]
        for idx, sym in enumerate(gl):
            if sym.name == 'main':
                gl[idx] = Symbol("main",MType([Symbol('args',ArrayType
        (StringType()),Index(0))],VoidType()),sym.value)
        # print('/////////////Global_scope////////////////////////////////////')
        # for x in gl:
        #     print(str(x))
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)


class Helper:
    @staticmethod
    def isRefType(ast):
        return isinstance(ast,ArrayLiteral) or isinstance(ast,StringLiteral)
    @staticmethod
    def getArrayType(ast:ArrayLiteral):
        typechecker = StaticChecker(ast)
        return ast.accept(typechecker,(None,None,None))
    @staticmethod
    def expand( sym_list, local_env):
        local_env.extend(sym_list)
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
    def infer(symbol,infer_type):
        if not infer_type: 
            return symbol.returnType()
        
        if Helper.isUnknownArray(symbol.symbolType): #case infering unknown array
            if type(infer_type) != ArrayType:
                return symbol.returnType()
            if infer_type.dimen == symbol.symbolType.dimen:
                symbol.symbolType = infer_type
            return symbol.symbolType

        if symbol.returnType() != Unknown(): 
            return symbol.returnType()
        
        symbol.setReturnType(infer_type)

        return symbol.returnType()




class CodeGenVisitor(BaseVisitor):
    def __init__(self, astTree, global_scope, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.global_var_init = []
        self.env = [global_scope]
        self.className = "MCClass"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")

    """NOTE: helper visit functions"""

    def global_lookup(self,name):
        for symbol in self.env[-1]:
            if symbol.name == name: return symbol
        return None #not found
    def visitCodeBlock(self,decl_ast,stmt_ast,o):  
        returned = False        
        #emit method
        block_frame = o.frame
        new_scope = decl_ast != []
        #enter scope
        
        if new_scope: block_frame.enterScope(True)
        #read local scope + param decl
        current_env = [[]] + o.sym
        var_list = [var_decl.accept(self,MethodEnv(block_frame,current_env)) for var_decl in decl_ast]
        current_env[0].extend(var_list)
        if new_scope:
            #emit scope start label 
            stat_label_dir = self.emit.emitLABEL(block_frame.getStartLabel(),block_frame)
            self.emit.printout(stat_label_dir)
        [self.genInitCode(sym,MethodEnv(block_frame,current_env)) for sym in var_list]
        #read stmts
        # [stmt.accept(self,MethodEnv(block_frame, current_env)) for stmt in stmt_ast]
        for stmt in stmt_ast:
            stmt.accept(self,MethodEnv(block_frame, current_env))
            if isinstance(stmt, Return): returned = True
        if new_scope:
            #emit end label and end method
            end_label_dir = self.emit.emitLABEL(block_frame.getEndLabel(),block_frame)
            self.emit.printout(end_label_dir)
            #done!
            block_frame.exitScope()
        return returned
        
    def op_type(self,op):
        if op in ['!','&&','||']: return BoolType()
        if op in ['+','-','*','\\','%','==','!=','<','>','<=','>=']: return IntType()
        if op in ['+.','-.','*.','\\.','=/=','<.','>.','<=.','>=.']: return FloatType()    
    
    
    def getLiteralType(self,literal):
        if isinstance(literal,IntLiteral): return IntType()
        if isinstance(literal,FloatLiteral): return FloatType()
        if isinstance(literal, StringLiteral): return StringType()
        if isinstance(literal, BooleanLiteral): return BoolType()
        if isinstance(literal,ArrayLiteral): 
            return Helper.getArrayType(literal)

    def visitProgram(self, ast, c):
        #ast: Program
        #c: Any

        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))

        """Decl params: frame, env"""
        o = MethodEnv(None,self.env)
        [decl.accept(self,o) for decl in ast.decl]
        
        self.genInit()
        self.genClInit()
        # generate class init if necessary
        self.emit.emitEPILOG()

        # self.emit.printCurrentCode()
        return c
    def genInit(self):
        methodname,methodtype = "<init>",MType([],VoidType())
        frame = Frame(methodname, methodtype.rettype)
        self.emit.printout(self.emit.emitMETHOD(methodname,methodtype,False,frame))
        frame.enterScope(True)
        varname,vartype,varindex = "this",ClassType(self.className),frame.getNewIndex()
        startLabel, endLabel = frame.getStartLabel(), frame.getEndLabel()
        self.emit.printout(self.emit.emitVAR(varindex, varname, vartype, startLabel, endLabel,frame ))
        self.emit.printout(self.emit.emitLABEL(startLabel,frame))
        self.emit.printout(self.emit.emitREADVAR(varname, vartype, varindex, frame))
        self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        self.emit.printout(self.emit.emitLABEL(endLabel, frame))
        self.emit.printout(self.emit.emitRETURN(methodtype.rettype, frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))

    def genClInit(self):
        methodname,methodtype = "<clinit>",MType([],VoidType())
        frame = Frame(methodname, methodtype.rettype)
        self.emit.printout(self.emit.emitMETHOD(methodname,methodtype,False,frame))
        frame.enterScope(True)
        startLabel, endLabel = frame.getStartLabel(), frame.getEndLabel()
        self.emit.printout(self.emit.emitLABEL(startLabel,frame))
        #NOTE: gen code for init value of global vars
        for symbol, varInit in self.global_var_init:
            name = symbol.name
            className = symbol.value.value
            init_code, init_type = varInit.accept(self,MethodEnv(frame,None))
            self.emit.printout(init_code + self.emit.emitPUTSTATIC(className + '.' + name,init_type,frame))
        
        self.emit.printout(self.emit.emitLABEL(endLabel, frame))
        self.emit.printout(self.emit.emitRETURN(methodtype.rettype, frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))

    # The following code is just for initial, students should remove it and write your visitor from here
    def genMain(self,ast,o):
        symbol = self.global_lookup('main')
        methodname,methodtype = symbol.name, symbol.mtype
        frame = Frame(methodname, methodtype.rettype)
        self.emit.printout(self.emit.emitMETHOD(methodname,methodtype,True,frame))
        frame.enterScope(True)
        varname,vartype,varindex = "args",methodtype.partype[0].mtype,frame.getNewIndex()
        startLabel, endLabel = frame.getStartLabel(), frame.getEndLabel()
        
        self.emit.printout(self.emit.emitVAR(varindex, varname, vartype, startLabel, endLabel,frame ))
        self.emit.printout(self.emit.emitLABEL(startLabel,frame))

        #NOTE: this is main's body
        current_env = [methodtype.partype] + o.sym
        var_list = [var_decl.accept(self,MethodEnv(frame,current_env)) for var_decl in ast.body[0]]
        current_env[0].extend(var_list)
        [self.genInitCode(sym,MethodEnv(frame,current_env)) for sym in var_list]
        # [stmt.accept(self,MethodEnv(frame,current_env)) for stmt in ast.body[1]]
        returned= False
        for stmt in ast.body[1]:
            stmt.accept(self,MethodEnv(frame,current_env))
            if isinstance(stmt,Return): returned = True

        self.emit.printout(self.emit.emitLABEL(endLabel, frame))
        if not returned:
            self.emit.printout(self.emit.emitRETURN(methodtype.rettype, frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))

        return None

    def codeGenParamFromSym(self,symbol: Symbol,o):
        name,typ = symbol.name, symbol.mtype
        frame = o.frame
        index = frame.getNewIndex()
        start_label = frame.getStartLabel()
        end_label = frame.getEndLabel()
        directive = self.emit.emitVAR(index,name,typ,start_label,end_label,frame)
        self.emit.printout(directive)
        return Symbol(name,typ,Index(index))
    
    def genInitCode(self,sym,o):
        name = sym.name
        index = sym.value.value
        initVal = sym.initVal
        #assign init value
        init_code, init_type = initVal.accept(self,o)
        self.emit.printout(init_code + self.emit.emitWRITEVAR(name,init_type,index,o.frame))

    def visitVarDecl(self, ast:VarDecl, o):
        frame = o.frame

        name = ast.variable.name
        typ = self.getLiteralType(ast.varInit)
        #always have init value (except param)
        if frame:
            #local
            #directive
            index = frame.getNewIndex()
            start_label = frame.getStartLabel()
            end_label = frame.getEndLabel()
            directive = self.emit.emitVAR(index,name,typ,start_label,end_label,frame)
            self.emit.printout(directive)
            return Symbol(name,typ,Index(index),initVal=ast.varInit)
        else:
            #global
            directive = self.emit.emitATTRIBUTE(name,typ,False,None)
            self.emit.printout(directive)
            symbol = Symbol(name,typ,CName(self.className))
            #the code for init value of global var is gen in <init>
            self.global_var_init.append((symbol,ast.varInit))
            return symbol
    def visitFuncDecl(self,ctx,o):
        if ctx.name.name == 'main': return self.genMain(ctx,o)
        #emit method

        function_symbol = self.global_lookup(ctx.name.name)
        func_frame = Frame(ctx.name, function_symbol.mtype.rettype)
        method_dir = self.emit.emitMETHOD(ctx.name.name,function_symbol.mtype, True,func_frame)
        self.emit.printout(method_dir)

        #new frame and enter scope
        
        func_frame.enterScope(True)
        #read local scope + param decl
        param_vars = [self.codeGenParamFromSym(sym,MethodEnv(func_frame,None)) for sym in function_symbol.mtype.partype]
        current_env = [param_vars] + o.sym
        var_list = [var_decl.accept(self,MethodEnv(func_frame,current_env)) for var_decl in ctx.body[0]]
        current_env[0].extend(var_list)

        #emit scope start label 
        stat_label_dir = self.emit.emitLABEL(func_frame.getStartLabel(),func_frame)
        self.emit.printout(stat_label_dir)
        [self.genInitCode(sym,MethodEnv(func_frame,current_env)) for sym in var_list]
        #read stmts
        # [stmt.accept(self,MethodEnv(func_frame, current_env)) for stmt in ctx.body[1]]
        returned= False
        for stmt in ctx.body[1]:
            stmt.accept(self,MethodEnv(func_frame, current_env))
            if isinstance(stmt,Return): returned = True
        #emit end label and end method
        end_label_dir = self.emit.emitLABEL(func_frame.getEndLabel(),func_frame)
        self.emit.printout(end_label_dir)
        if not returned:
            self.emit.printout(self.emit.emitRETURN(function_symbol.mtype.rettype, func_frame))
        end_method_dir = self.emit.emitENDMETHOD(func_frame)
        self.emit.printout(end_method_dir)
        #done!
        func_frame.exitScope()

    def opTranslate(self, op):
        if op in ['+','+.']: return '+'
        if op in ['-','-.']: return '-'
        if op in ['*','*.']: return '*'
        if op in ['\\','\\.']: return '/'
        if op in ['%']: return '%'

        if op in ['==']: return '=='
        if op in ['!=','=/=']: return '!='
        if op in ['<','<.']: return '<'
        if op in ['>','>.']: return '>'
        if op in ['<=','<=.']: return '<='
        if op in ['>=','>=.']: return '>='

        if op in ['||', '&&']: return op
    def visitBinaryOp(self, ast:BinaryOp, o):
        op = self.opTranslate(ast.op)
        frame = o.frame
        left_code, left_type = ast.left.accept(self,o)
        right_code, right_type = ast.right.accept(self,o)
        input_type = left_type #all ops works on both side of same type
        operand_code = left_code + right_code
        operation_code = None
        output_type = None

        if op in ['+','-']:
            operation_code = self.emit.emitADDOP(op,input_type,frame)
            output_type = input_type
        if op in ['*','/']:
            operation_code = self.emit.emitMULOP(op,input_type,frame)
            output_type = input_type
        if op in ['%']:
            operation_code = self.emit.emitMOD(frame)
            output_type = input_type
        if op in ['==','!=','<','>','<=','>=']:
            operation_code = self.emit.emitREOP(op,input_type,frame)
            output_type = BoolType()
        if op in ['&&']:
            result = list()
            result.append(left_code)
            result.append(self.emit.emitDUP(frame))
            shorted_label, non_shorted_label = frame.getNewLabel(),frame.getNewLabel()
            result.append(self.emit.emitIFFALSE(shorted_label,frame))
            result.append(right_code)
            result.append(self.emit.emitANDOP(frame))
            result.append(self.emit.emitGOTO(non_shorted_label,frame))
            result.append(self.emit.emitLABEL(shorted_label,frame))
            result.append(self.emit.emitPOP(frame))
            result.append(self.emit.emitPUSHICONST(0,frame))
            result.append(self.emit.emitLABEL(non_shorted_label,frame))
            output_type = BoolType()
            return (''.join(result),output_type)
        if op in ['||']:
            result = list()
            result.append(left_code)
            result.append(self.emit.emitDUP(frame))
            shorted_label, non_shorted_label = frame.getNewLabel(),frame.getNewLabel()
            result.append(self.emit.emitIFTRUE(shorted_label,frame))
            result.append(right_code)
            result.append(self.emit.emitOROP(frame))
            result.append(self.emit.emitGOTO(non_shorted_label,frame))
            result.append(self.emit.emitLABEL(shorted_label,frame))
            result.append(self.emit.emitPOP(frame))
            result.append(self.emit.emitPUSHICONST(1,frame))
            result.append(self.emit.emitLABEL(non_shorted_label,frame))
            output_type = BoolType()
            return (''.join(result),output_type)
    
        return (operand_code + operation_code, output_type)
    def visitUnaryOp(self, ast: UnaryOp, o):
        op = ast.op
        frame = o.frame

        expr_code, expr_type = ast.body.accept(self,o)
        
        operation_code = None
        input_type = expr_type
        output_type = input_type
        if op == '!':
            operation_code = self.emit.emitNOT(input_type, frame)
        if op in ['-','-.']:
            operation_code = self.emit.emitNEGOP(input_type,frame)

        return (expr_code + operation_code, output_type)
    
    def visitCallExpr(self, ast: CallExpr, o):
        name = ast.method.name
        function_sym = self.global_lookup(name)

        all_args_code = list()
        for arg in ast.param:
            arg_code, arg_type = arg.accept(self,o)
            all_args_code.append(arg_code)
            
        return (''.join(all_args_code) + self.emit.emitINVOKESTATIC(function_sym.value.value+ "/" + name,function_sym.mtype,o.frame),function_sym.mtype.rettype)
    


    def visitId(self,ctx,o):
        frame = o.frame
        is_left = o.isLeft
        symbol = None
        for scope in o.sym:
            for s in scope:
                if s.name == ctx.name: 
                    symbol = s
                    break
            if symbol: break
        
        name = symbol.name
        value = symbol.value
        var_type = symbol.mtype
        code = None
        if type(value) is Index:
            #local
            index = value.value
            if is_left:
                code = self.emit.emitWRITEVAR(name,var_type,index,frame)
            else:
                code = self.emit.emitREADVAR(name,var_type,index,frame)
        if type(value) is CName:
            #global/static
            lexeme = value.value + '/' + name
            if is_left:
                code = self.emit.emitPUTSTATIC(lexeme, var_type, frame)
            else:
                code = self.emit.emitGETSTATIC(lexeme,var_type,frame)
        
        return (code,var_type)
    
    def visitArrayCell(self, ctx: ArrayCell, o):
        result = list()
        temp_param = MethodEnv(o.frame,o.sym,False)
        array_ref_code, array_type = ctx.arr.accept(self,temp_param)
        result.append(array_ref_code)

        frame = o.frame
        current_elem_type = array_type
        for idx in ctx.idx:
            current_elem_type = current_elem_type.eleType
            idx_code, idx_type = idx.accept(self,temp_param)
            result.append(idx_code)
            if type(current_elem_type) != ArrayType: break
            load_elem_code = self.emit.emitALOAD(current_elem_type,frame)
            result.append(load_elem_code)
        is_left = o.isLeft
        if is_left:
            return (''.join(result),current_elem_type)
        else:
            load_elem_code = self.emit.emitALOAD(current_elem_type,frame)
            result.append(load_elem_code)
            return (''.join(result),current_elem_type)


    
    def visitAssign(self,ctx,o):
        #here in code gen we visit right first cause value needs to be on stack before assigning
        if isinstance(ctx.lhs, ArrayCell):
            left_code, left_type = ctx.lhs.accept(self,MethodEnv(o.frame,o.sym,True))
            right_code, right_type = ctx.rhs.accept(self,MethodEnv(o.frame,o.sym,False))
            self.emit.printout(left_code+right_code+ self.emit.emitASTORE(right_type,o.frame))
            return None
        right_code, right_type = ctx.rhs.accept(self,MethodEnv(o.frame,o.sym,False))
        left_code, left_type = ctx.lhs.accept(self,MethodEnv(o.frame,o.sym,True))

        assign_type = left_type #or right_type
        code = right_code + left_code
        self.emit.printout(code)
        return None
        

    
    def visitIf(self,ctx,o):
        #end label for end of every branch/blk
        end_label = o.frame.getNewLabel()
        for ifBlk in ctx.ifthenStmt:
            expr = ifBlk[0]
            decls = ifBlk[1]
            stmts= ifBlk[2]
            # if false go to false label
            expr_code, expr_type = expr.accept(self,o)
            false_label = o.frame.getNewLabel()
            if_false_code = self.emit.emitIFFALSE(false_label,o.frame)
            self.emit.printout(expr_code + if_false_code)
            #read code blk
            returned = self.visitCodeBlock(decls,stmts,o)
            #endblk
            if not returned:
                goto_code = self.emit.emitGOTO(end_label,o.frame)
                self.emit.printout(goto_code)
            #label 0 here
            false_label_code = self.emit.emitLABEL(false_label,o.frame)
            self.emit.printout(false_label_code)

        # else blk
        if ctx.elseStmt != ([],[]):
            self.visitCodeBlock(ctx.elseStmt[0],ctx.elseStmt[1],o)
        #final label here
        end_label_code = self.emit.emitLABEL(end_label,o.frame)
        self.emit.printout(end_label_code)
        
        return None

    
    def visitFor(self, ctx, o):
        right_code, right_type = ctx.expr1.accept(self,MethodEnv(o.frame,o.sym,False))
        left_code, left_type = ctx.idx1.accept(self,MethodEnv(o.frame,o.sym,True))
        self.emit.printout(right_code + left_code)

        frame = o.frame
        #let's go 
        frame.enterLoop()
        #begin label
        begin_label = frame.getNewLabel()
        begin_label_code = self.emit.emitLABEL(begin_label,frame)

        self.emit.printout(begin_label_code)
        #check expression
        expr_code, expr_type = ctx.expr2.accept(self,o)
        self.emit.printout(expr_code)
        #if false end loop
        end_label = frame.getBreakLabel()
        if_false_code = self.emit.emitIFFALSE(end_label,frame)
        self.emit.printout(if_false_code)
        # not false check stmt

        self.visitCodeBlock(ctx.loop[0],ctx.loop[1],o)


        continue_label= frame.getContinueLabel()
        self.emit.printout(self.emit.emitLABEL(continue_label,frame))
        #change index value 
        index_right, rtype = ctx.idx1.accept(self,MethodEnv(o.frame,o.sym,False))
        change_value,ctype = ctx.expr3.accept(self,MethodEnv(o.frame,o.sym,False))
        add_code = self.emit.emitADDOP('+',IntType(),frame)
        index_left, ltype = ctx.idx1.accept(self,MethodEnv(o.frame,o.sym,True))
        self.emit.printout(index_right+change_value+add_code+index_left)

        # done statement go to begin and check condition again

        goto_begin_code = self.emit.emitGOTO(begin_label,frame)
        self.emit.printout(goto_begin_code)

        #end label
        end_label_code = self.emit.emitLABEL(end_label,frame)
        self.emit.printout(end_label_code)

        #end here
        frame.exitLoop()

        return None

    def visitContinue(self, ctx:Continue, o):
        frame = o.frame
        continue_label = frame.getContinueLabel()
        self.emit.printout(self.emit.emitGOTO(continue_label,frame))
        
        return None 

    def visitBreak(self, ctx:Break, o):
        frame = o.frame
        continue_label = frame.getBreakLabel()
        self.emit.printout(self.emit.emitGOTO(continue_label,frame))
        
        return None 

    
    def visitReturn(self, ast:Return, o):
        expr_code, expr_type = ast.expr.accept(self, o) if ast.expr else ('', VoidType())
        self.emit.printout(expr_code + self.emit.emitRETURN(expr_type,o.frame))
        return None
        

    
    def visitDowhile(self, ctx, o):
        frame = o.frame
        #let's go 
        frame.enterLoop()
        #begin label
        begin_label = frame.getContinueLabel()
        begin_label_code = self.emit.emitLABEL(begin_label,frame)
        self.emit.printout(begin_label_code)

        #check stmt
        self.visitCodeBlock(ctx.sl[0],ctx.sl[1],o)

        #check expression
        expr_code, expr_type = ctx.exp.accept(self,o)
        self.emit.printout(expr_code)
        #if false end loop
        end_label = frame.getBreakLabel()

        if_false_code = self.emit.emitIFFALSE(end_label,frame)
        self.emit.printout(if_false_code)
        

        # done statement go to begin and check condition again
        goto_begin_code = self.emit.emitGOTO(begin_label,frame)
        self.emit.printout(goto_begin_code)
        
        #end label
        end_label_code = self.emit.emitLABEL(end_label,frame)
        self.emit.printout(end_label_code)

        #end here
        frame.exitLoop()

        return None
    
    
    def visitWhile(self,ctx,o):
        frame = o.frame
        #let's go 
        frame.enterLoop()
        #begin label
        begin_label = frame.getContinueLabel()
        begin_label_code = self.emit.emitLABEL(begin_label,frame)
        self.emit.printout(begin_label_code)
        #check expression
        expr_code, expr_type = ctx.exp.accept(self,o)
        self.emit.printout(expr_code)
        #if false end loop
        end_label = frame.getBreakLabel()

        if_false_code = self.emit.emitIFFALSE(end_label,frame)
        self.emit.printout(if_false_code)
        # not false check stmt

        self.visitCodeBlock(ctx.sl[0],ctx.sl[1],o)

        # done statement go to begin and check condition again
        goto_begin_code = self.emit.emitGOTO(begin_label,frame)
        self.emit.printout(goto_begin_code)
        
        #end label
        end_label_code = self.emit.emitLABEL(end_label,frame)
        self.emit.printout(end_label_code)

        #end here
        frame.exitLoop()

        return None
    
    def visitCallStmt(self, ast:CallStmt, o):
        """
        Find symbol, if not exist -> add, else -> just call
        """
        name = ast.method.name
        function_sym = self.global_lookup(name)

        for arg in ast.param:
            arg_code, arg_type = arg.accept(self,o)
            self.emit.printout(arg_code)
        self.emit.printout(self.emit.emitINVOKESTATIC(function_sym.value.value+ "/" + name,function_sym.mtype,o.frame))
        
        


    """NOTE: literal part"""


    def visitIntLiteral(self, ast, params):
        return (self.emit.emitPUSHICONST(ast.value,params.frame),IntType())
    def visitFloatLiteral(self, ast, params):
        return (self.emit.emitPUSHFCONST(ast.value,params.frame),FloatType())
    def visitBooleanLiteral(self, ast, params):
        return (self.emit.emitPUSHICONST(str(ast.value),params.frame),BoolType())
    
    def visitStringLiteral(self, ast, o):
        string_arg = self.emit.emitPUSHCONST('"'+ast.value+'"', StringType(), o.frame)
        return (string_arg,StringType())


    def visitArrayLiteral(self, ast, o):
        array = ast.value
        frame = o.frame
        env = o.sym
        array_type = Helper.getArrayType(ast)
        result = list()
        result.append(self.emit.emitPUSHICONST(len(array),frame))
        result.append(self.emit.emitNEWARRAY(array_type,frame))
        for index,element in enumerate(array): #for each elem
            result.append(self.emit.emitDUP(frame)) #dup the array ref
            result.append(self.emit.emitPUSHICONST(index,frame)) # push index
            elem_code, elem_type = element.accept(self,o)
            result.append(elem_code) # element code
            result.append(self.emit.emitASTORE(elem_type,frame)) # load to array cell
        return (''.join(result),array_type)






"""-------------------------type check ------------------"""

from dataclasses import dataclass
from functools import reduce

#.........................TYPE ERRORS

def printraw(obj):
    # return None
    if obj == None: return "None"
    # print(type(obj).__name__)
    if type(obj) in [int,float,bool]: return str(obj)
    if isinstance(obj,str): return repr(obj)
    if isinstance(obj,list): return '['+  ("" if not obj else reduce(lambda a,b: a + ', ' + printraw(b),obj[1:],printraw(obj[0])))+']'
    if isinstance(obj,tuple): return '('+ ("" if not obj else reduce(lambda a,b: a + ', ' + printraw(b),obj[1:],printraw(obj[0])))+')'
    #if composite
    value = list(vars(obj).values())
    name = type(obj).__name__   
    joined = reduce(lambda a,b: a + ', ' + printraw(b),value[1:],"("+printraw(value[0])) if value else "("
    return name + joined + ')'
class Kind(ABC):
    pass

class Function(Kind):
    def __str__(self):
        if printraw(self): return printraw(self)
        return "Function"

class Parameter(Kind):
    def __str__(self):
        if printraw(self): return printraw(self)
        return "Parameter"

class Variable(Kind):
    def __str__(self):
        if printraw(self): return printraw(self)
        return "Variable"

class Identifier(Kind):
    def __str__(self):
        if printraw(self): return printraw(self)
        return "Identifier"
class StaticError(Exception):
    pass

@dataclass
class Undeclared(StaticError):
    k: Kind
    n: str  # name of identifier
    
    def __str__(self):
        if printraw(self): return printraw(self)
        return  "Undeclared "+ str(self.k) + ": " + self.n

@dataclass
class Redeclared(StaticError):
    k: Kind
    n: str # name of identifier 
    
    def __str__(self):
        if printraw(self): return printraw(self)
        return  "Redeclared "+ str(self.k) + ": " + self.n

@dataclass
class TypeMismatchInExpression(StaticError):
    exp: Expr

    def __str__(self):
        if printraw(self): return printraw(self)
        return  "Type Mismatch In Expression: "+ str(self.exp)

@dataclass
class TypeMismatchInStatement(StaticError):
    stmt: Stmt

    def __str__(self):
        if printraw(self): return printraw(self)
        return "Type Mismatch In Statement: "+ str(self.stmt)

@dataclass
class TypeCannotBeInferred(StaticError):
    stmt: Stmt

    def __str__(self):
        if printraw(self): return printraw(self)
        return "Type Cannot Be Inferred: "+ str(self.stmt)

class NoEntryPoint(StaticError):
    def __str__(self):
        if printraw(self): return printraw(self)
        return "No Entry Point"

# --------------- Type Check Classes

def scope_decorator(visit_func):
    return visit_func #comment this to use
    def print_name(*arg):
        print('Begin......',visit_func.__name__,'.......\n')
        ret_val =  visit_func(*arg)
        print('End......',visit_func.__name__,'.......\n')
        return ret_val
    return print_name

class TypeCheckSymbol:
    def __init__(self,name: str, symbolType: Type, kind:Kind = Function(), value = None):
        self.name = name
        self. symbolType = symbolType
        self.kind = kind
        self.value=value
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
    
    def toSymbol(self):
        return Symbol(self.name,self.symbolType.toMtype() if isinstance(self.symbolType,FunctionType) else self.symbolType,self.value)

    def __str__(self):
        return "Symbol( " + (self.name if self.name else '') + ', ' + (type(self.symbolType).__name__ if type(self.symbolType) != FunctionType else str(self.symbolType)) + ', ' + type(self.kind).__name__+ ',' + type(self.returnType()).__name__ + ', CName:' + str(self.value.value) + ')'

@dataclass
class FunctionType:
    params:List[TypeCheckSymbol]
    rtype:Type
    #NOTE: functions are the same if same param
    def __eq__(self, other):
        return self.params == other.param_type
    def __str__(self):
        return "Function( "+ str([ (p.name if p.name else '') + ':' +type(p.returnType()).__name__ for p in self.params] if self.params else ['None']) + '---'+ type(self.rtype).__name__+' )'
    def toMtype(self):
        params = [Symbol(x.name,x.symbolType,x.value) for x in self.params]
        rtype = self.rtype
        return MType(params,rtype)
class Unknown(Type): pass  


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
            arr_type = arr_type.eleType
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
            if infer_type.dimen == symbol.symbolType.dimen:
                symbol.symbolType = infer_type
            return symbol.symbolType

        if symbol.returnType() != Unknown(): 
            return symbol.returnType()
        
        symbol.setReturnType(infer_type)

        return symbol.returnType()

#---------------------- Static Checker that returns global inferred functions + variables

class StaticChecker(BaseVisitor):
    def __init__(self,ast):
        self.libName = "io"
        self.className = "MCClass"
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
        for x in self.global_scope:
            x.value = CName(self.libName)
        return self.visit(self.ast,[self.global_scope])
    
    @scope_decorator
    def visitProgram(self,ast, env):
        #NOTE: first run to get all functions's init decl and global vars
        global_decls = [decl.accept(self,env) for decl in ast.decl]
        for x in global_decls:
            x.value = CName(self.className)
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
                prev_dim = var_type.dimen if type(var_type) == ArrayType else []
                var_type = ArrayType(var_type,[dim] + prev_dim)

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
            return TypeCheckSymbol(func_name,func_type, Function(),CName(self.className))
       
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
        if len(id_type.dimen) != len(idx): 
            # print("Array cell dim mismatch: ", len(id_type.dimen),',',len(idx))
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
        while type(arr_type.eleType) is ArrayType:
            arr_type = arr_type.eleType
        
        #NOTE: infer array element type here
        if infer_type and arr_type.eleType == Unknown():
            arr_type.eleType = infer_type
        
        return arr_type.eleType

    
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
        dim = [len(elems)] + (elem_type.dimen if type(elem_type) == ArrayType else [])
        #NOTE: we do not check for same elem type
        return ArrayType(elem_type,dim)