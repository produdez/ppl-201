.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a I
.field static b I
.field static c I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a I from Label0 to Label1
.var 2 is b I from Label0 to Label1
.var 3 is c I from Label0 to Label1
.var 4 is i I from Label0 to Label1
.var 5 is j I from Label0 to Label1
	iconst_5
	istore_1
	iconst_5
	istore_2
	bipush 15
	istore_3
	iconst_0
	istore 4
	iconst_0
	istore 5
	iload_1
	iconst_5
	isub
	istore 4
Label4:
	iload 5
	iload_2
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
	iload 4
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	iload 5
	iconst_2
	iadd
	istore 5
Label2:
	iload 4
	iload_3
	bipush 14
	isub
	iadd
	istore 4
	goto Label4
Label3:
Label1:
	return
.limit stack 5
.limit locals 6
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
	iconst_1
	putstatic MCClass.a I
	iconst_2
	putstatic MCClass.b I
	iconst_3
	putstatic MCClass.c I
Label1:
	return
.limit stack 1
.limit locals 0
.end method
