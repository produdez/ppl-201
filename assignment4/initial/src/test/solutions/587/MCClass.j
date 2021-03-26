.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
	bipush 10
	istore_1
	iload_1
	invokestatic MCClass/f1(I)V
Label1:
	return
.limit stack 1
.limit locals 2
.end method

.method public static f1(I)V
.var 0 is x I from Label0 to Label1
.var 1 is i I from Label0 to Label1
Label0:
	iconst_0
	istore_1
	iconst_0
	istore_1
Label4:
	iload_1
	iload_0
	if_icmpgt Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
.var 2 is j I from Label7 to Label8
Label7:
	iconst_0
	istore_2
	iload_0
	iload_1
	isub
	istore_2
Label11:
	iload_2
	iconst_0
	if_icmplt Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label10
	iload_2
	iload_0
	iload_1
	isub
	iconst_2
	idiv
	if_icmpne Label15
	iconst_1
	goto Label16
Label15:
	iconst_0
Label16:
	ifle Label17
	goto Label9
	goto Label14
Label17:
Label14:
	iload_2
	iconst_2
	irem
	iconst_0
	if_icmpne Label19
	iconst_1
	goto Label20
Label19:
	iconst_0
Label20:
	ifle Label21
	iload_2
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	goto Label18
Label21:
	iload_2
	ineg
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label18:
Label9:
	iload_2
	iconst_1
	ineg
	iadd
	istore_2
	goto Label11
Label10:
	iload_1
	iload_0
	iconst_2
	idiv
	if_icmpne Label23
	iconst_1
	goto Label24
Label23:
	iconst_0
Label24:
	ifle Label25
	goto Label3
	goto Label22
Label25:
Label22:
Label8:
Label2:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label4
Label3:
	return
Label1:
.limit stack 12
.limit locals 3
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
