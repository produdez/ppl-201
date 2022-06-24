.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a [I from Label0 to Label1
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
	astore_1
	aload_1
	invokestatic MCClass/f([I)[I
	astore_1
	aload_1
	iconst_0
	iaload
	invokestatic MCClass/f1(I)V
	aload_1
	iconst_1
	iaload
	invokestatic MCClass/f1(I)V
	aload_1
	iconst_2
	iaload
	invokestatic MCClass/f1(I)V
Label1:
	return
.limit stack 5
.limit locals 2
.end method

.method public static f([I)[I
.var 0 is x [I from Label0 to Label1
Label0:
	aload_0
	iconst_0
	aload_0
	iconst_0
	iaload
	iconst_1
	iadd
	iastore
	aload_0
	iconst_1
	aload_0
	iconst_1
	iaload
	iconst_2
	iadd
	iastore
	aload_0
	iconst_2
	aload_0
	iconst_2
	iaload
	iconst_3
	iadd
	iastore
	aload_0
	areturn
Label1:
.limit stack 4
.limit locals 1
.end method

.method public static f1(I)V
.var 0 is temp I from Label0 to Label1
Label0:
	iload_0
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	return
Label1:
.limit stack 1
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
Label1:
	return
.limit stack 0
.limit locals 0
.end method
