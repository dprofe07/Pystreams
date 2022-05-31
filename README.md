# Pystreams

This library allows users use C++ syntax in python

In C++ you can write:

```cpp
cout << "Hello, world!";
int a; 
cin >> a;
```

Now you can do the same thing in Python:

```python
pout << "Hello, world!"
a = 10000
pin >> a
```

To convert values to types you can use that syntax:

```python
a = 10000
pin >> int >> a
```

Also you can use functions instead of types (any callable object):

```python
a = 10000
pin >> print >> a # It will print anything you enter
print(a) # None
```


> *You shouldn't use 0 in line `a = 10000` because:*
> 
> ```python
> a = 10000
> b = 10000
> print(a is b)
> # False
> ```
> 
> *But*
> 
> ```python
> a = 0
> b = 0
> print(a is b) 
> # True
> ```
    
> *Warning: this code will work only in global scope. 
> To use pin in functions/methods/modules you should use Pointers*
> 
> Code in functions can look like that:
>
> ```python
> def nextValue():
>     a = 10000
>     pin >> Pointer(a, locals())
>     return a
> ```

As a bonus, you can use Pointers in Python code:

```python
a = Pointed()
ptr = Pointer(a, vars())
```

That's all! Now ptr is pointing to a variable. You can edit it:

```python
ptr.obj = 123
print(a)
# 123
```

You can read value:

```python
a = 'Hello, world!'
print(+ptr) # Unary '+' or '-' return ptr.obj
# Hello, world!
```
