.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a [I from Label0 to Label1
.var 2 is b [I from Label0 to Label1
	iconst_1
	newarray int
	dup
	iconst_0
	iconst_1
	iastore
	astore_1
	iconst_1
	newarray int
	dup
	iconst_0
	iconst_2
	iastore
	astore_2
	aload_1
	aload_2
	invokestatic MCClass/f1([I[I)V
	aload_1
	iconst_0
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	aload_2
	iconst_0
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 6
.limit locals 3
.end method

.method public static f1([I[I)V
.var 0 is x [I from Label0 to Label1
.var 1 is y [I from Label0 to Label1
.var 2 is temp [I from Label0 to Label1
Label0:
	iconst_1
	newarray int
	dup
	iconst_0
	iconst_0
	iastore
	astore_2
	aload_0
	astore_2
	aload_1
	astore_0
	aload_2
	astore_1
	return
Label1:
.limit stack 5
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
