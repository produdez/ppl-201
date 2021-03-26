.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a I
.field static b F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic MCClass/b F
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
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
	ldc 11.2000
	putstatic MCClass.b F
Label1:
	return
.limit stack 1
.limit locals 0
.end method
