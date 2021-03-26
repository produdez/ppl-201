.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a [[[[I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_3
	anewarray [[[I
	dup
	iconst_0
	iconst_2
	anewarray [[I
	dup
	iconst_0
	iconst_1
	anewarray [I
	dup
	iconst_0
	iconst_1
	newarray int
	dup
	iconst_0
	bipush 7
	iastore
	aastore
	aastore
	dup
	iconst_1
	iconst_1
	anewarray [I
	dup
	iconst_0
	iconst_1
	newarray int
	dup
	iconst_0
	bipush 8
	iastore
	aastore
	aastore
	aastore
	dup
	iconst_1
	iconst_2
	anewarray [[I
	dup
	iconst_0
	iconst_1
	anewarray [I
	dup
	iconst_0
	iconst_1
	newarray int
	dup
	iconst_0
	bipush 9
	iastore
	aastore
	aastore
	dup
	iconst_1
	iconst_1
	anewarray [I
	dup
	iconst_0
	iconst_1
	newarray int
	dup
	iconst_0
	bipush 10
	iastore
	aastore
	aastore
	aastore
	dup
	iconst_2
	iconst_2
	anewarray [[I
	dup
	iconst_0
	iconst_1
	anewarray [I
	dup
	iconst_0
	iconst_1
	newarray int
	dup
	iconst_0
	bipush 11
	iastore
	aastore
	aastore
	dup
	iconst_1
	iconst_1
	anewarray [I
	dup
	iconst_0
	iconst_1
	newarray int
	dup
	iconst_0
	bipush 12
	iastore
	aastore
	aastore
	aastore
	putstatic MCClass/a [[[[I
	getstatic MCClass/a [[[[I
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_0
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	getstatic MCClass/a [[[[I
	iconst_2
	aaload
	iconst_1
	aaload
	iconst_0
	aaload
	iconst_0
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 29
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
	iconst_3
	anewarray [[[I
	dup
	iconst_0
	iconst_2
	anewarray [[I
	dup
	iconst_0
	iconst_1
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
	aastore
	dup
	iconst_1
	iconst_1
	anewarray [I
	dup
	iconst_0
	iconst_1
	newarray int
	dup
	iconst_0
	iconst_2
	iastore
	aastore
	aastore
	aastore
	dup
	iconst_1
	iconst_2
	anewarray [[I
	dup
	iconst_0
	iconst_1
	anewarray [I
	dup
	iconst_0
	iconst_1
	newarray int
	dup
	iconst_0
	iconst_3
	iastore
	aastore
	aastore
	dup
	iconst_1
	iconst_1
	anewarray [I
	dup
	iconst_0
	iconst_1
	newarray int
	dup
	iconst_0
	iconst_4
	iastore
	aastore
	aastore
	aastore
	dup
	iconst_2
	iconst_2
	anewarray [[I
	dup
	iconst_0
	iconst_1
	anewarray [I
	dup
	iconst_0
	iconst_1
	newarray int
	dup
	iconst_0
	iconst_5
	iastore
	aastore
	aastore
	dup
	iconst_1
	iconst_1
	anewarray [I
	dup
	iconst_0
	iconst_1
	newarray int
	dup
	iconst_0
	bipush 6
	iastore
	aastore
	aastore
	aastore
	putstatic MCClass.a [[[[I
Label1:
	return
.limit stack 29
.limit locals 0
.end method
