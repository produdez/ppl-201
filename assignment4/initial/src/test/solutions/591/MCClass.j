.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a I from Label0 to Label1
	bipush 9
	istore_1
	iload_1
	invokestatic MCClass/factorial(I)I
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 1
.limit locals 2
.end method

.method public static factorial(I)I
.var 0 is x I from Label0 to Label1
Label0:
	iload_0
	iconst_0
	if_icmpne Label3
	iconst_1
	goto Label4
Label3:
	iconst_0
Label4:
	dup
	ifgt Label7
	iload_0
	iconst_1
	if_icmpne Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ior
	goto Label8
Label7:
	pop
	iconst_1
Label8:
	ifle Label9
	iconst_1
	ireturn
Label9:
Label2:
	iload_0
	iload_0
	iconst_1
	isub
	invokestatic MCClass/factorial(I)I
	imul
	ireturn
Label1:
.limit stack 7
.limit locals 1
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
