.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a [Ljava/lang/String; from Label0 to Label1
.var 2 is b [Ljava/lang/String; from Label0 to Label1
.var 3 is i I from Label0 to Label1
	iconst_3
	anewarray java/lang/String
	dup
	iconst_0
	ldc "1"
	aastore
	dup
	iconst_1
	ldc "2"
	aastore
	dup
	iconst_2
	ldc "3"
	aastore
	astore_1
	iconst_3
	anewarray java/lang/String
	dup
	iconst_0
	ldc ""
	aastore
	dup
	iconst_1
	ldc ""
	aastore
	dup
	iconst_2
	ldc ""
	aastore
	astore_2
	iconst_0
	istore_3
	aload_1
	iconst_0
	aaload
	invokestatic io/int_of_string(Ljava/lang/String;)I
	iconst_1
	isub
	istore_3
Label4:
	iload_3
	aload_1
	iconst_2
	aaload
	invokestatic io/int_of_string(Ljava/lang/String;)I
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
	aload_2
	iload_3
	ldc "changed"
	aastore
Label2:
	iload_3
	aload_1
	iconst_1
	aaload
	invokestatic io/int_of_string(Ljava/lang/String;)I
	iconst_1
	isub
	iadd
	istore_3
	goto Label4
Label3:
	aload_1
	iconst_0
	aaload
	invokestatic io/print(Ljava/lang/String;)V
	aload_1
	iconst_1
	aaload
	invokestatic io/print(Ljava/lang/String;)V
	aload_1
	iconst_2
	aaload
	invokestatic io/print(Ljava/lang/String;)V
	aload_2
	iconst_0
	aaload
	invokestatic io/print(Ljava/lang/String;)V
	aload_2
	iconst_1
	aaload
	invokestatic io/print(Ljava/lang/String;)V
	aload_2
	iconst_2
	aaload
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 7
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
