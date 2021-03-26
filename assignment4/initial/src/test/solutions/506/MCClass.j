.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a I
.field static b Ljava/lang/String;

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is b Ljava/lang/String; from Label0 to Label1
	ldc "inner_string"
	astore_1
	getstatic MCClass/a I
	invokestatic MCClass/f1(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 1
.limit locals 2
.end method

.method public static f1(I)Ljava/lang/String;
.var 0 is x I from Label0 to Label1
Label0:
	iload_0
	invokestatic io/string_of_int(I)Ljava/lang/String;
	areturn
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
	iconst_5
	putstatic MCClass.a I
	ldc "string"
	putstatic MCClass.b Ljava/lang/String;
Label1:
	return
.limit stack 1
.limit locals 0
.end method
