.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a I
.field static b I
.field static c I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	iconst_1
	invokestatic MCClass/f1(II)V
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public static f1(II)V
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
Label0:
	iload_0
	iload_1
	if_icmple Label3
	iconst_1
	goto Label4
Label3:
	iconst_0
Label4:
	ifle Label5
	ldc "a"
	invokestatic io/print(Ljava/lang/String;)V
	goto Label2
Label5:
	ldc "b"
	invokestatic io/print(Ljava/lang/String;)V
Label2:
	return
Label1:
.limit stack 3
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
	iconst_1
	putstatic MCClass.a I
	iconst_2
	putstatic MCClass.b I
	iconst_3
	putstatic MCClass.c I
Label1:
	return
.limit stack 1
.limit locals 0
.end method
