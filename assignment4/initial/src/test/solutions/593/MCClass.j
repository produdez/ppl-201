.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is x I from Label0 to Label1
	iconst_3
	istore_1
	iload_1
	invokestatic MCClass/f1(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 1
.limit locals 2
.end method

.method public static f1(I)Ljava/lang/String;
.var 0 is z I from Label0 to Label1
Label0:
	iload_0
	iconst_1
	if_icmpne Label3
	iconst_1
	goto Label4
Label3:
	iconst_0
Label4:
	ifle Label5
	ldc "1"
	areturn
Label5:
	iload_0
	iconst_2
	if_icmpne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label8
	ldc "2"
	areturn
Label8:
	iload_0
	iconst_3
	if_icmpne Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifle Label11
	ldc "3"
	areturn
Label11:
	ldc "noshit"
	invokestatic io/print(Ljava/lang/String;)V
	ldc ""
	areturn
Label2:
	ldc "Done"
	areturn
Label1:
.limit stack 11
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
