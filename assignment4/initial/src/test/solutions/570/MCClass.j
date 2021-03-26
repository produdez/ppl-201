.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a [[I
.field static b [I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is c [[I from Label0 to Label1
.var 2 is d [I from Label0 to Label1
.var 3 is x I from Label0 to Label1
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
	iconst_5
	newarray int
	dup
	iconst_0
	bipush 99
	iastore
	dup
	iconst_1
	bipush 99
	iastore
	dup
	iconst_2
	bipush 99
	iastore
	dup
	iconst_3
	bipush 99
	iastore
	dup
	iconst_4
	bipush 99
	iastore
	astore_2
	bipush 50
	istore_3
	getstatic MCClass/a [[I
	iconst_0
	aaload
	iconst_0
	iaload
	getstatic MCClass/b [I
	iconst_0
	iaload
	if_icmple Label3
	iconst_1
	goto Label4
Label3:
	iconst_0
Label4:
	ifle Label5
	ldc "a>b"
	invokestatic io/print(Ljava/lang/String;)V
	goto Label2
Label5:
	ldc "b>a"
	invokestatic io/print(Ljava/lang/String;)V
Label2:
Label1:
	return
.limit stack 11
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
	iconst_2
	anewarray [I
	dup
	iconst_0
	iconst_1
	newarray int
	dup
	iconst_0
	bipush 42
	iastore
	aastore
	dup
	iconst_1
	iconst_1
	newarray int
	dup
	iconst_0
	bipush 69
	iastore
	aastore
	putstatic MCClass.a [[I
	iconst_1
	newarray int
	dup
	iconst_0
	bipush 10
	iastore
	putstatic MCClass.b [I
Label1:
	return
.limit stack 10
.limit locals 0
.end method
