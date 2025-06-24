# IntelliJ - Fix
1. Project Structure
2. Modules
3. +
4. Import Module
5. Gleicher Ordner
6. Maven
7. Apply


# Implementierung
## TestCases
### If Tests

``` Java
if (true) {
	return 1;
} else return 2;
```
Wird im AST Absichtlich mit
``` 
thenBranch=[Block[statements=[ReturnStmt[value=LiteralExpr[value=1]]]]],
elseBranch=[ReturnStmt[value=LiteralExpr[value=2]]]]]
```
berechnet.

---
`{ }` um die Pfade sorgt dafür, dass diese als Block erkannt werden.  Nur ohne Klammern wird ein einzelnes Statement auch als solches erkannt. 


## AST
### IfStmnt
Erwartet aktuell Liste von Statements, lieber mit einzelnem Statement konstruieren dass evtl Block und der wiederum viele Statements enthält.

Besser? :
Oder lieber immer einen Block übergeben der beliebig viele Statements enthält?

### AssignmentStmtExpr
Was macht das Attribut Varname?

TestCasesAST Zeile 125
``` Java
// int x = 5;  
// x = true; // Typen-Mismatch  
methodBody.add(new LocalVarDeclStmt(ValType.INTEGER, "x", new LiteralExpr(5)));  
methodBody.add(new AssignmentStmtExpr(null, new VarExpr("x"), new LiteralExpr(true)));
```

