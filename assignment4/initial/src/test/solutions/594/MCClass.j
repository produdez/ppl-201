.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is x I from Label0 to Label1
	iconst_5
	istore_1
	iload_1
	invokestatic MCClass/f(I)I
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 1
.limit locals 2
.end method

.method public static f(I)I
.var 0 is x I from Label0 to Label1
Label0:
	iload_0
	invokestatic MCClass/f1(I)I
	iconst_1
	iadd
	ireturn
Label1:
.limit stack 2
.limit locals 1
.end method

.method public static f1(I)I
.var 0 is x I from Label0 to Label1
Label0:
	iload_0
	invokestatic MCClass/f2(I)I
	iconst_1
	iadd
	ireturn
Label1:
.limit stack 2
.limit locals 1
.end method

.method public static f2(I)I
.var 0 is x I from Label0 to Label1
Label0:
	iload_0
	invokestatic MCClass/f3(I)I
	iconst_1
	iadd
	ireturn
Label1:
.limit stack 2
.limit locals 1
.end method

.method public static f3(I)I
.var 0 is x I from Label0 to Label1
Label0:
	iload_0
	iconst_1
	iadd
	ireturn
Label1:
.limit stack 2
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
