.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static f([II)[I
.var 0 is a [I from Label0 to Label1
.var 1 is n I from Label0 to Label1
Label0:
	aload_0
	iload_1
	sipush 888
	iastore
	aload_0
	areturn
Label1:
.limit stack 3
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a [I from Label0 to Label1
	bipush 6
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
	dup
	iconst_3
	iconst_4
	iastore
	dup
	iconst_4
	iconst_5
	iastore
	dup
	iconst_5
	bipush 6
	iastore
	astore_1
	aload_1
	iconst_1
	iconst_2
	iadd
	iconst_3
	iconst_2
	idiv
	iadd
	bipush 101
	iadd
	aload_1
	iconst_3
	iaload
	bipush 6
	imul
	isub
	bipush 6
	irem
	invokestatic MCClass/f([II)[I
	aload_1
	iconst_3
	iaload
	bipush 6
	irem
	sipush 999
	iastore
	aload_1
	iconst_0
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	aload_1
	iconst_1
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	aload_1
	iconst_2
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	aload_1
	iconst_3
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	aload_1
	iconst_4
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	aload_1
	iconst_5
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
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
Label1:
	return
.limit stack 0
.limit locals 0
.end method
