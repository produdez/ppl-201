.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a I from Label0 to Label1
.var 2 is b I from Label0 to Label1
	bipush 88
	istore_1
	bipush 76
	istore_2
	iload_1
	iload_2
	invokestatic MCClass/gcd(II)I
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 2
.limit locals 3
.end method

.method public static gcd(II)I
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
Label0:
	iload_0
	iconst_0
	if_icmpne Label3
	iconst_1
	goto Label4
Label3:
	iconst_0
Label4:
	ifle Label5
	iload_1
	ireturn
Label5:
Label2:
	iload_1
	iconst_0
	if_icmpne Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label9
	iload_0
	ireturn
Label9:
Label6:
	iload_0
	iload_1
	if_icmpne Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ifle Label13
	iload_0
	ireturn
Label13:
Label10:
	iload_0
	iload_1
	if_icmple Label15
	iconst_1
	goto Label16
Label15:
	iconst_0
Label16:
	ifle Label17
	iload_0
	iload_1
	isub
	iload_1
	invokestatic MCClass/gcd(II)I
	ireturn
Label17:
Label14:
	iload_0
	iload_1
	iload_0
	isub
	invokestatic MCClass/gcd(II)I
	ireturn
Label1:
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
