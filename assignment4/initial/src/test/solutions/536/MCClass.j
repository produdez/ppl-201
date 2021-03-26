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
	putstatic MCClass/a I
Label4:
	getstatic MCClass/a I
	iconst_5
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
	getstatic MCClass/a I
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label2:
	getstatic MCClass/a I
	iconst_1
	iadd
	putstatic MCClass/a I
	goto Label4
Label3:
Label1:
	return
.limit stack 4
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
