.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a [Ljava/lang/String;
.field static b [Ljava/lang/String;

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
	iconst_0
	istore_1
	getstatic MCClass/a [Ljava/lang/String;
	iconst_0
	aaload
	invokestatic io/int_of_string(Ljava/lang/String;)I
	iconst_1
	isub
	istore_1
Label4:
	iload_1
	getstatic MCClass/a [Ljava/lang/String;
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
	getstatic MCClass/b [Ljava/lang/String;
	iload_1
	ldc "changed"
	aastore
Label2:
	iload_1
	getstatic MCClass/a [Ljava/lang/String;
	iconst_1
	aaload
	invokestatic io/int_of_string(Ljava/lang/String;)I
	iconst_1
	isub
	iadd
	istore_1
	goto Label4
Label3:
	getstatic MCClass/a [Ljava/lang/String;
	iconst_0
	aaload
	invokestatic io/print(Ljava/lang/String;)V
	getstatic MCClass/a [Ljava/lang/String;
	iconst_1
	aaload
	invokestatic io/print(Ljava/lang/String;)V
	getstatic MCClass/a [Ljava/lang/String;
	iconst_2
	aaload
	invokestatic io/print(Ljava/lang/String;)V
	getstatic MCClass/b [Ljava/lang/String;
	iconst_0
	aaload
	invokestatic io/print(Ljava/lang/String;)V
	getstatic MCClass/b [Ljava/lang/String;
	iconst_1
	aaload
	invokestatic io/print(Ljava/lang/String;)V
	getstatic MCClass/b [Ljava/lang/String;
	iconst_2
	aaload
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 5
.limit locals 2
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
	putstatic MCClass.a [Ljava/lang/String;
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
	putstatic MCClass.b [Ljava/lang/String;
Label1:
	return
.limit stack 6
.limit locals 0
.end method
