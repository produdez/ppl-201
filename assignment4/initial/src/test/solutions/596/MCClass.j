.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is t Z from Label0 to Label1
.var 2 is f Z from Label0 to Label1
.var 3 is x I from Label0 to Label1
.var 4 is y I from Label0 to Label1
.var 5 is z F from Label0 to Label1
.var 6 is k F from Label0 to Label1
	iconst_1
	istore_1
	iconst_0
	istore_2
	bipush 15
	istore_3
	iconst_3
	istore 4
	ldc 12.5000
	fstore 5
	ldc 4.3000
	fstore 6
	iload_3
	iload 4
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	dup
	ifle Label8
	fload 6
	fload 5
	fcmpl
	ifeq Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifgt Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	iand
	goto Label9
Label8:
	pop
	iconst_0
Label9:
	dup
	ifgt Label16
	iload_2
	ifgt Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifgt Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifgt Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ior
	goto Label17
Label16:
	pop
	iconst_1
Label17:
	dup
	ifgt Label20
	iload_1
	ifgt Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	ior
	goto Label21
Label20:
	pop
	iconst_1
Label21:
	istore_1
	iload_1
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 24
.limit locals 7
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
