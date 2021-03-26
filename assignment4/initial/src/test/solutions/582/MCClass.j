.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a Ljava/lang/String; from Label0 to Label1
.var 2 is b Ljava/lang/String; from Label0 to Label1
	ldc "a"
	astore_1
	ldc "b"
	astore_2
	aload_1
	aload_2
	invokestatic MCClass/f1(Ljava/lang/String;Ljava/lang/String;)V
	aload_1
	invokestatic io/print(Ljava/lang/String;)V
	aload_2
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 2
.limit locals 3
.end method

.method public static f1(Ljava/lang/String;Ljava/lang/String;)V
.var 0 is x Ljava/lang/String; from Label0 to Label1
.var 1 is y Ljava/lang/String; from Label0 to Label1
.var 2 is temp Ljava/lang/String; from Label0 to Label1
Label0:
	ldc ""
	astore_2
	aload_0
	astore_2
	aload_1
	astore_0
	aload_2
	astore_1
	return
Label1:
.limit stack 1
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
