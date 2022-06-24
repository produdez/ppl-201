.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static b [[[Ljava/lang/String;

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a [[[Ljava/lang/String; from Label0 to Label1
.var 2 is i I from Label0 to Label1
	iconst_3
	anewarray [[Ljava/lang/String;
	dup
	iconst_0
	iconst_1
	anewarray [Ljava/lang/String;
	dup
	iconst_0
	iconst_1
	anewarray java/lang/String
	dup
	iconst_0
	ldc "1"
	aastore
	aastore
	aastore
	dup
	iconst_1
	iconst_1
	anewarray [Ljava/lang/String;
	dup
	iconst_0
	iconst_1
	anewarray java/lang/String
	dup
	iconst_0
	ldc "2"
	aastore
	aastore
	aastore
	dup
	iconst_2
	iconst_1
	anewarray [Ljava/lang/String;
	dup
	iconst_0
	iconst_1
	anewarray java/lang/String
	dup
	iconst_0
	ldc "3"
	aastore
	aastore
	aastore
	astore_1
	iconst_0
	istore_2
	aload_1
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_0
	aaload
	invokestatic io/int_of_string(Ljava/lang/String;)I
	iconst_1
	isub
	istore_2
Label4:
	iload_2
	aload_1
	iconst_2
	aaload
	iconst_0
	aaload
	iconst_0
	aaload
	invokestatic io/int_of_string(Ljava/lang/String;)I
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
	getstatic MCClass/b [[[Ljava/lang/String;
	iload_2
	aaload
	iconst_0
	aaload
	iconst_0
	ldc "changed"
	aastore
Label2:
	iload_2
	aload_1
	iconst_1
	aaload
	iconst_0
	aaload
	iconst_0
	aaload
	invokestatic io/int_of_string(Ljava/lang/String;)I
	iconst_1
	isub
	iadd
	istore_2
	goto Label4
Label3:
	aload_1
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_0
	aaload
	invokestatic io/print(Ljava/lang/String;)V
	aload_1
	iconst_1
	aaload
	iconst_0
	aaload
	iconst_0
	aaload
	invokestatic io/print(Ljava/lang/String;)V
	aload_1
	iconst_2
	aaload
	iconst_0
	aaload
	iconst_0
	aaload
	invokestatic io/print(Ljava/lang/String;)V
	getstatic MCClass/b [[[Ljava/lang/String;
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_0
	aaload
	invokestatic io/print(Ljava/lang/String;)V
	getstatic MCClass/b [[[Ljava/lang/String;
	iconst_1
	aaload
	iconst_0
	aaload
	iconst_0
	aaload
	invokestatic io/print(Ljava/lang/String;)V
	getstatic MCClass/b [[[Ljava/lang/String;
	iconst_2
	aaload
	iconst_0
	aaload
	iconst_0
	aaload
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 17
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
	iconst_3
	anewarray [[Ljava/lang/String;
	dup
	iconst_0
	iconst_1
	anewarray [Ljava/lang/String;
	dup
	iconst_0
	iconst_1
	anewarray java/lang/String
	dup
	iconst_0
	ldc ""
	aastore
	aastore
	aastore
	dup
	iconst_1
	iconst_1
	anewarray [Ljava/lang/String;
	dup
	iconst_0
	iconst_1
	anewarray java/lang/String
	dup
	iconst_0
	ldc ""
	aastore
	aastore
	aastore
	dup
	iconst_2
	iconst_1
	anewarray [Ljava/lang/String;
	dup
	iconst_0
	iconst_1
	anewarray java/lang/String
	dup
	iconst_0
	ldc ""
	aastore
	aastore
	aastore
	putstatic MCClass.b [[[Ljava/lang/String;
Label1:
	return
.limit stack 17
.limit locals 0
.end method
