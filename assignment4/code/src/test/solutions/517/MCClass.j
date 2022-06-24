.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a F
.field static b F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is t Z from Label0 to Label1
	iconst_1
	istore_1
	getstatic MCClass/a F
	getstatic MCClass/b F
	fcmpl
	ifle Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	invokestatic MCClass/f(Z)V
	getstatic MCClass/a F
	getstatic MCClass/b F
	fcmpl
	ifge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	invokestatic MCClass/f(Z)V
	getstatic MCClass/a F
	getstatic MCClass/b F
	fcmpl
	ifeq Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	invokestatic MCClass/f(Z)V
	getstatic MCClass/a F
	getstatic MCClass/b F
	fcmpl
	iflt Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	invokestatic MCClass/f(Z)V
	getstatic MCClass/a F
	getstatic MCClass/b F
	fcmpl
	ifgt Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	invokestatic MCClass/f(Z)V
Label1:
	return
.limit stack 12
.limit locals 2
.end method

.method public static f(Z)V
.var 0 is x Z from Label0 to Label1
Label0:
	iload_0
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	return
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
	ldc 1.6000
	putstatic MCClass.a F
	ldc 0.4000
	putstatic MCClass.b F
Label1:
	return
.limit stack 1
.limit locals 0
.end method
