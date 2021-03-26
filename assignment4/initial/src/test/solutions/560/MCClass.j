.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a [[I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_2
	anewarray [I
	dup
	iconst_0
	iconst_1
	newarray int
	dup
	iconst_0
	bipush 99
	iastore
	aastore
	dup
	iconst_1
	iconst_1
	newarray int
	dup
	iconst_0
	bipush 98
	iastore
	aastore
	putstatic MCClass/a [[I
	getstatic MCClass/a [[I
	iconst_1
	aaload
	iconst_0
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 10
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
	iconst_2
	anewarray [I
	dup
	iconst_0
	iconst_1
	newarray int
	dup
	iconst_0
	iconst_1
	iastore
	aastore
	dup
	iconst_1
	iconst_1
	newarray int
	dup
	iconst_0
	iconst_2
	iastore
	aastore
	putstatic MCClass.a [[I
Label1:
	return
.limit stack 10
.limit locals 0
.end method
