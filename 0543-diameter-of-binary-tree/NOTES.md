## Use variable to store result of recursive call If need recursive call values multiple time
​
#### nonlocal
​
In Python, the nonlocal keyword is used to declare a variable in a nested function and indicate that it is not a local variable, but a variable defined in an enclosing scope. The nonlocal keyword allows you to modify variables in the nearest enclosing scope that are already defined, rather than creating a new local variable with the same name.
​
Here's an example to illustrate the usage of nonlocal:
```
def outer_function():
x = "outer"
​
def inner_function():
nonlocal x
x = "inner"
​
inner_function()
print(x)
​
outer_function()
```
​
In the above code, the variable x is defined in the outer_function(). By using the nonlocal keyword in the inner_function(), we indicate that x refers to the variable defined in the nearest enclosing scope, which is outer_function(). The assignment x = "inner" modifies the value of x in the outer function's scope. As a result, when we print x after calling inner_function(), it outputs "inner" instead of "outer".
​
Note that the nonlocal keyword can only be used within nested functions, and it is not applicable in the global scope. Additionally, if a variable with the same name does not exist in an enclosing scope, using nonlocal will result in a SyntaxError.
​