.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a F from Label0 to Label1
.var 2 is b F from Label0 to Label1
.var 3 is c F from Label0 to Label1
	ldc 1.2000
	fstore_1
	ldc 1.8000
	fstore_2
	ldc 5.0000
	fstore_3
	fload_3
	fload_2
	fmul
	fload_1
	fdiv
	fload_1
	fsub
	fload_1
	fneg
	fsub
	fload_3
	fadd
	fstore_3
	fload_3
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 2
.limit locals 4
.end method

.method public <init>()V
.var 0 is this LMCClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public <clinit>()V
Label0:
Label1:
	return
.limit stack 0
.limit locals 0
.end method
