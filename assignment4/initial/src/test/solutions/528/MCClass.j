.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
	bipush 7
	istore_1
	iload_1
	iconst_1
	if_icmpne Label3
	iconst_1
	goto Label4
Label3:
	iconst_0
Label4:
	ifle Label5
	ldc "1"
	invokestatic io/print(Ljava/lang/String;)V
	goto Label2
Label5:
	iload_1
	iconst_2
	if_icmpne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label8
	ldc "2"
	invokestatic io/print(Ljava/lang/String;)V
	goto Label2
Label8:
	iload_1
	iconst_3
	if_icmpne Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifle Label11
	ldc "3"
	invokestatic io/print(Ljava/lang/String;)V
	goto Label2
Label11:
	iload_1
	iconst_4
	if_icmpne Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label14
	ldc "4"
	invokestatic io/print(Ljava/lang/String;)V
	goto Label2
Label14:
	iload_1
	bipush 7
	if_icmpne Label15
	iconst_1
	goto Label16
Label15:
	iconst_0
Label16:
	ifle Label17
	ldc "7"
	invokestatic io/print(Ljava/lang/String;)V
	goto Label2
Label17:
	ldc "greater"
	invokestatic io/print(Ljava/lang/String;)V
Label2:
Label1:
	return
.limit stack 11
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
Label1:
	return
.limit stack 0
.limit locals 0
.end method
