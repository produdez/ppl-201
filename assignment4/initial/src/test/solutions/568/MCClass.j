.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a [[I from Label0 to Label1
.var 2 is b I from Label0 to Label1
	iconst_3
	anewarray [I
	dup
	iconst_0
	iconst_3
	newarray int
	dup
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	dup
	iconst_2
	iconst_3
	iastore
	aastore
	dup
	iconst_1
	iconst_3
	newarray int
	dup
	iconst_0
	iconst_4
	iastore
	dup
	iconst_1
	iconst_5
	iastore
	dup
	iconst_2
	bipush 6
	iastore
	aastore
	dup
	iconst_2
	iconst_3
	newarray int
	dup
	iconst_0
	bipush 7
	iastore
	dup
	iconst_1
	bipush 8
	iastore
	dup
	iconst_2
	bipush 9
	iastore
	aastore
	astore_1
	bipush 100
	istore_2
	iload_2
	aload_1
	iconst_1
	aaload
	iconst_2
	iaload
	if_icmpge Label3
	iconst_1
	goto Label4
Label3:
	iconst_0
Label4:
	ifle Label5
	aload_1
	iconst_1
	aaload
	iconst_2
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	goto Label2
Label5:
	iload_2
	aload_1
	iconst_1
	aaload
	iconst_0
	iaload
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label8
	ldc "damm"
	invokestatic io/print(Ljava/lang/String;)V
	goto Label2
Label8:
	ldc "b"
	invokestatic io/print(Ljava/lang/String;)V
Label2:
Label1:
	return
.limit stack 11
.limit locals 3
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
