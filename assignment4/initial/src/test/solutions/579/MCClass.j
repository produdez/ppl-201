.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a [[I from Label0 to Label1
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
	aload_1
	invokestatic MCClass/f([[I)V
Label1:
	return
.limit stack 11
.limit locals 2
.end method

.method public static f([[I)V
.var 0 is x [[I from Label0 to Label1
.var 1 is i I from Label0 to Label1
.var 2 is j I from Label0 to Label1
Label0:
	iconst_0
	istore_1
	iconst_0
	istore_2
	iconst_0
	istore_1
Label4:
	iload_1
	iconst_3
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
	iconst_0
	istore_2
Label9:
	iload_2
	iconst_3
	if_icmpge Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label8
	aload_0
	iload_1
	aaload
	iload_2
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label7:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label9
Label8:
Label2:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label4
Label3:
	return
Label1:
.limit stack 6
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
