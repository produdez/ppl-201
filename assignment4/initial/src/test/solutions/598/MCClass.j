.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	dup
	ifgt Label5
	iconst_1
	iconst_0
	idiv
	iconst_2
	if_icmple Label3
	iconst_1
	goto Label4
Label3:
	iconst_0
Label4:
	ior
	goto Label6
Label5:
	pop
	iconst_1
Label6:
	ifle Label7
	ldc "cir-ed"
	invokestatic io/print(Ljava/lang/String;)V
	goto Label2
Label7:
Label2:
Label1:
	return
.limit stack 6
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
