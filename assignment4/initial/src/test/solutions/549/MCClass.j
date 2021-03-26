.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a I
.field static b I
.field static c I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is x I from Label0 to Label1
.var 2 is y I from Label0 to Label1
.var 3 is z I from Label0 to Label1
	iconst_5
	istore_1
	bipush 6
	istore_2
	bipush 7
	istore_3
Label2:
	iload_3
	getstatic MCClass/a I
	if_icmple Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	getstatic MCClass/a I
	putstatic MCClass/c I
Label6:
	getstatic MCClass/c I
	iload_3
	if_icmpge Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label7
	getstatic MCClass/c I
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	getstatic MCClass/c I
	iconst_1
	iadd
	putstatic MCClass/c I
	goto Label6
Label7:
	iload_3
	iconst_1
	isub
	istore_3
	goto Label2
Label3:
	ldc "?"
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 6
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
