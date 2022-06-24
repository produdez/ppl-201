.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a I
.field static b Ljava/lang/String;
.field static c F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	ifle Label3
	ldc "True"
	invokestatic io/print(Ljava/lang/String;)V
	goto Label2
Label3:
	ldc "false"
	invokestatic io/print(Ljava/lang/String;)V
Label2:
Label1:
	return
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
	iconst_5
	putstatic MCClass.a I
	ldc "string"
	putstatic MCClass.b Ljava/lang/String;
	ldc 5.6000
	putstatic MCClass.c F
Label1:
	return
.limit stack 1
.limit locals 0
.end method
