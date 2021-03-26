.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a I from Label0 to Label1
.var 2 is b I from Label0 to Label1
.var 3 is c I from Label0 to Label1
	iconst_1
	istore_1
	iconst_2
	istore_2
	iconst_3
	istore_3
	iload_1
	iload_2
	iadd
	iload_3
	iadd
	iconst_3
	if_icmple Label3
	iconst_1
	goto Label4
Label3:
	iconst_0
Label4:
	ifle Label5
	iload_1
	iload_2
	iadd
	iconst_2
	if_icmple Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label9
	iload_1
	iconst_1
	if_icmple Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ifle Label13
	ldc "a"
	invokestatic io/print(Ljava/lang/String;)V
	goto Label10
Label13:
	iload_2
	iconst_1
	if_icmple Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label16
	ldc "b"
	invokestatic io/print(Ljava/lang/String;)V
	goto Label10
Label16:
	ldc "nei"
	invokestatic io/print(Ljava/lang/String;)V
Label10:
	goto Label6
Label9:
Label6:
	goto Label2
Label5:
Label2:
Label1:
	return
.limit stack 9
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
