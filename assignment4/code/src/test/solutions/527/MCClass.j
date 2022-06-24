.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a I
.field static b Ljava/lang/String;
.field static c F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic MCClass/c F
	ldc 5.6000
	fcmpl
	ifle Label3
	iconst_1
	goto Label4
Label3:
	iconst_0
Label4:
	ifle Label5
	getstatic MCClass/c F
	ldc 1.0000
	fadd
	putstatic MCClass/c F
	goto Label2
Label5:
Label2:
	getstatic MCClass/c F
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	getstatic MCClass/c F
	ldc 6.0000
	fcmpl
	ifge Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label9
	ldc "yes"
	invokestatic io/print(Ljava/lang/String;)V
	goto Label6
Label9:
	ldc "No"
	invokestatic io/print(Ljava/lang/String;)V
Label6:
Label1:
	return
.limit stack 5
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
