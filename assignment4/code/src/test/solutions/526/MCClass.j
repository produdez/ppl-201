.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a I
.field static b Ljava/lang/String;
.field static c F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic MCClass/a I
	iconst_5
	if_icmplt Label3
	iconst_1
	goto Label4
Label3:
	iconst_0
Label4:
	dup
	ifle Label7
	getstatic MCClass/a I
	bipush 10
	if_icmpgt Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	iand
	goto Label8
Label7:
	pop
	iconst_0
Label8:
	ifle Label9
	bipush 6
	putstatic MCClass/a I
	goto Label2
Label9:
	getstatic MCClass/a I
	bipush 7
	if_icmpne Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label12
	bipush 7
	putstatic MCClass/a I
	goto Label2
Label12:
	bipush 10
	putstatic MCClass/a I
Label2:
	getstatic MCClass/a I
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 7
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
