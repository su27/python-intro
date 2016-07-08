---
# Python 简介
su27
---
## What is Python?
### Python: 优雅而健壮的编程语言

- 高级
- 易学易读易维护
- 兼顾解释性和编译性的优点
- 面向对象
- 一些函数化编程的结构
- 高效快速，扩展库众多

---

## What is Python?

- 动态语言

```python
>>> a = 1
>>> a = 'asdf'
```

- 强类型语言

```python
>>> a = '1'
>>> a + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: cannot concatenate 'str' and 'int' objects
```

- 一切皆对象
  - 变量名只是一个名字，它指向一个对象
  - 赋值操作其实是绑定操作

```python
>>> (1).__class__
int
```

---

## 交互式环境

- python
- ipython
- help()
- docstring

```python
>>> help(list)

Help on class list in module __builtin__:

class list(object)
 |  list() -> new empty list
 |  list(iterable) -> new list initialized from iterable's items
 |
 |  Methods defined here:
 |
 |  __add__(...)
 |      x.__add__(y) <==> x+y
 |
 |  __contains__(...)
 |      x.__contains__(y) <==> y in x
 |
```

---

# Data Structures
---
## 数值

- int: `100` , `0x3e`
- long
    - 并不是C或者其他编译类型语言的长整型

```python
>>> import sys

>>> sys.maxint
>>> 9223372036854775807

>>> sys.maxint+1
>>> 9223372036854775808L

>>> 999999 ** 9
>>> 999991000035999916000125999874000083999964000008999999L
```

- float: `1.1`

- complex: `(9+3j)`

---

## 数值运算

- 除法

```python
>>> 5 / 2
2
>>> 5.0 / 2
2.5

>>> from __future__ import division
>>> 5 / 2
2.5
>>> 5 // 2
2
```

- 其他运算

---

## String

- 字符串是不可变的

```python
>>> s = 'python'
>>> s[0]
'p'
>>> s[0] = 'c' # TypeError
```

- 字符串的切片和成员操作

```python
>>> s = 'hello douban'
>>> s[1:5]
'ello'
>>> s[:5]
'hello'
>>> s[-6:]
'douban'

>>> 'dou' in s
True
>>> 'yah' in s
False
```

---

## String

- 字符串的连接与格式化

```python
>>> print '哈' * 5
哈哈哈哈哈

>>> '<span class="' + 'red' + '">' + 'button' + '</span>'
'<span class="red">button</span>'

>>> '<span class="%s">%s</span>' % ('red', 'button')
'<span class="red">button</span>'

>>> '{2}-{0}-{1}'.format('1', '4', '2013')
'2013-1-4'

>>> '{}:{}:{day}'.format(2009, 4, day='Sunday') # python 2.7
'2009:4:Sunday'

>>> coord = (3, 5)
>>> 'X: {0[0]};  Y: {0[1]}'.format(coord)
'X: 3;  Y: 5'

>>> coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
>>> 'Target: {latitude}, {longitude}'.format(**coord)
'Target: 37.24N, -115.81W'
```

---

## String

- 字符串的连接与格式化

```python
# 不好:

s = ''
for i in seq:
    s += chr(i)

# 好:

''.join(chr(i) for i in seq)
```

---

## String

- str:

 - `'douban.com'`
 - `'\xe8\xb1\x86\xe7\x93\xa3'`

- unicode

 - `u'\u8c46\u74e3'`

- 转换

```python
>>> '豆瓣'
'\xe8\xb1\x86\xe7\x93\xa3'

>>> '豆瓣'.decode('utf8')
u'\u8c46\u74e3'

>>> u'\u8c46\u74e3'.encode('utf8')
'\xe8\xb1\x86\xe7\x93\xa3'
```

---

## 字符串的方法

### find, index, rfind, rindex, count
### startswith, endswith, isalpha, isdigit, isalnum, islower, isupper, isspace
### encode, decode, lower, upper, strip, lstrip, rstrip, replace
### split, rsplit, splitlines
### join

---

## 容器
### tuple: `(1000001, 'ahbei')` , `(1,)`
### list: `[1, 2, 3, 4, 5]`
### dict: `{'CEO': 'ahbei', 'Team Members': ['brant', 'hongqn', ...]}`
### set: `set([1, 2, 3])`

---

## list
- 切片
- `append` , `insert` , `pop`, `remove`, `reverse` , `sort`
- `index` , `count` (没有find)
- 使用 `list` 模拟栈操作

```python
>>> stack = [3, 4, 5]
>>> stack.append(6)
>>> stack.append(7)
>>> stack
[3, 4, 5, 6, 7]
>>> stack.pop()
7
```

- 使用`list.insert`模拟队列不如 `collections.deque`

```python
>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry") # Terry arrives
>>> queue.popleft() # The first to arrive now leaves
'Eric'
```

---

## list

- 改变一个可变对象的方法，通常没有返回值

```python
>>> li = ['n', 'b', 'a']
>>> li.sort()
>>> li.reverse()
>>>

# 与不可变对象比较:
>>> 'This is it.\n'.strip().upper()
'THIS IS IT.'

# 如果想要返回:
>>> sorted(li)
['a', 'b', 'n']
```

---

## FP tools for list

### filter

```python
>>> def f(x): return x % 2 != 0 and x % 3 != 0
>>> filter(f, range(2, 25))
[5, 7, 11, 13, 17, 19, 23]
```

### map

```python
>>> seq = range(8)
>>> def add(x, y): return x+y
>>> map(add, seq, seq)
[0, 2, 4, 6, 8, 10, 12, 14]
```

---

## 列表解析

### A.

```python
>>> squares = []
>>> for x in range(10):
...     squares.append(x ** 2)
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### B.

```python
>>> squares = map(lambda x: x ** 2, range(10))
```

### C. (list Comprehension)

```python
>>> squares = [x ** 2 for x in range(10)]
```

---

## 列表解析: 多变量及过滤条件

### exam A: flatten a list

```python
>>> vec = [[1,2,3], [4,5,6], [7,8,9]]
>>> [num for elem in vec for num in elem]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### exam B:

```python
>>> combs = []
>>> for x in [1,2,3]:
...     for y in [3,1,4]:
...         if x != y:
...             combs.append((x, y))
>>> combs
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

# 可以这样写:
>>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
```

---

## dict

```python
>>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
>>> dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'jack': 4098, 'guido': 4127}

# Dict Comprehensions
>>> {x: x ** 2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
```

- set: `d['name'] = 'Jim'`, `update`, `setdefault`
- delete: `del d['CEO']`, `pop`, `popitem`, `clear`
- get: `get`, `has_key` (deprecated), `keys`, `values`, `items`
- iter: `iterkeys`, `itervalues`, `iteritems`
- `copy`, `deepcopy`

```python
>>> Kid = {'h': '165', 'like': {'laptop': 'mac', 'book': []}}
>>> Kim = Kid.copy()
>>> Kim['like']['book'].append('LOTR')
>>> Kid['like']
{'laptop': 'mac', 'book': ['LOTR']}
```

---

## set

### set的修改:

`add`, `discard`, `remove`, `clear`, `copy`, `update`
### set的运算:

`union`(|), `difference`(-), `intersection`(*), `symmetric_difference`(^)
### 子集的判断:

`issubset`, `issuperset`, `&gt;`, `&lt;`

---

## tuple
- 元组是不可变类型

```python
# 不可赋值
>>> t = (1, 2)
>>> t[0] += 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment

# 可做dict的key
>>> d = {}
>>> d[['a']] = 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
>>> d[(1,2)] = 1
```

- mutable: list, dict, set, 类实例
- immutable: 数值类型, 字符串, tuple

---

## tuple

- 某种程度的可变

```python
>>> d = (1, ['A', 'B'])
>>> d[1].append('C')
>>> d
(1, ['A', 'B', 'C'])
```

- 单元素元组

```python
>>> type((1))
<type 'int'>
>>> type((1,))
<type 'tuple'>

>>> word = 'hello',
>>> len(word)
1
>>> word
('hello',)
```

---

## tuple

- Unpacking

```python
>>> result, = (1024,)
>>> result
1024

>>> a, b = b, a

# 注意，其他iterable也是可以unpack的
>>> a, b = range(2)
>>> a, b = xrange(2)
>>> a, b = (i for i in range(2))
>>> a, b = {"a":1, "b":2}
>>> a, b = {"a":1, "b":2}.iteritems()
```

---

## collections

Specialized container datatypes, providing
alternatives to Python’s general purpose built-in containers,
`dict`, `list`, `set`, and `tuple`.

### Counter

```python
>>> c = Counter(a=4, b=2, c=0, d=-2)
>>> d = Counter(a=1, b=2, c=3, d=4)
>>> list(c.elements())
['a', 'a', 'a', 'a', 'b', 'b']
>>> c.subtract(d)
>>> c
Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})

# An example:
>>> words = re.findall(r'\w+', open('hamlet.txt').read().lower())
>>> Counter(words).most_common(10)
[('the', 1143), ('and', 966), ('to', 762), ('of', 669), ('i', 631),
 ('you', 554),  ('a', 546), ('my', 514), ('hamlet', 471), ('in', 451)]
 ```

---

## collections
- OrderedDict

```python
>>> d = OrderedDict([('first', 1),
...                  ('second', 2),
...                  ('third', 3)])
>>> d.items()
[('first', 1), ('second', 2), ('third', 3)]
```

- deque
- defaultdict
- namedtuple


---

# Control Flow Tools
---

## 分支
- if...elif...else
- 悬挂问题

C:

```c
if (x > 0)
    if (y > 0)
        printf('both available!\n');
else
    printf('x not available!\n');
```

python:


```python
if x > 0:
    if y > 0:
        print 'both available!'
else:
    print 'x not available!'
```


---

## 分支

- `if(not)`通过计算bool()来判断，因此可以直接利用对象的bool()值

```python
toys = []
# if len(toys) == 0: 或者 if toys != [] 不好
if not toys:
    print "boring..."
```

- 三元操作 `x if condition else y`

```python
answer = 'yeah' if toys else 'no'
```

---

## 循环

- `while`
- `for i in ...`
- `break`, `continue`, `pass`, ...
- while和for都可以有else

```python
def find_cat(cat, boxes):
    for box in boxes:
        if box.isempty():
            continue
        elif cat in box:
            print "The cat is in", box
            break
    else:
        print "We have lost the cat."
```

---

## 循环

- Example A

```python
# 不好
for i in range(len(seq)):
    foo(seq[i], i)
# 好:
for i, item in enumerate(seq):
    foo(item, i)
```

- Example B

```python
# 不好:
for i in xrange(len(seq1)):
    foo(seq1[i], seq2[i])
# 好:
for i, j in zip(seq1, seq2):
    foo(i, j)

for i, j in itertools.izip(seq1, seq2):
    foo(i, j)
```

---

## 异常

- 所有异常都是`Exception`的子类
    - 除了`KeyboardInterrupted`和`SystemExit`
    - `ValueError`, `KeyError`, etc...

```python
try:
    do_something()
except KeyError:
    handle_key_error()
except Exception, e:
    import traceback
    traceback.print_exc()
finally:
    release_resources()
```

- `raise`

---

## 异常

- 不要做这样的事情

```python
try:
    do_something()
except:
    pass
```

---

# Modules
---

### A module is a file containing Python definitions and statements.

```python
# fibo.py
author = 'su27'
_AUTHOR_AGE = 27
def fib(n): # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print b,
        a, b = b, a+b
```

- import modules to use

```python
>>> import fibo
>>> fibo.fib(1000)
1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
>>> fibo.author
'su27'
>>> fibo.__name__
'fibo'
```

---

## 名称空间与作用域

### Local, Global, 与 Built-ins 名称空间

### 自由区隔的名字空间

```python
def foo():
    pass
foo.__doc__ = '呀，刚才忘了加上doc字符串'
foo.version = 0.2
```

### import即是把名字导入当前的名称空间

---

## import的方式

```python
>>> import fibo
>>> from fibo import fib, author

>>> from fibo import * # 绝大多数情况下要避免这样用
>>> author
'su27'
>>> _AUTHOR_AGE
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name '_AUTHOR_AGE' is not defined
```

### Note: import的时候, 被import的模块代码将被执行

---

# Functions

---

## python中的函数

- 关键字参数和默认参数

```python
def net_conn(host, port=80):
    print "connect to %s:%s" % (host, port)

>>> net_conn('douban', 8080)
>>> net_conn(port=8080, host='douban')
```

- 默认参数要在关键字参数前面

```python
>>> net_conn(host='douban', 8080)
  File "<stdin>", line 1
SyntaxError: non-keyword arg after keyword arg
```

---

## 可变对象不能做参数默认值

```python
>>> def hero_string(heroes=[]):
...     heroes.append("me")
...     return ', '.join(heroes)

>>> hero_string(['batman'])
'batman, me'

>>> hero_string(['batman', 'superman'])
'batman, superman, me'

>>> hero_string()
'me'

>>> hero_string()
'me, me'

>>> hero_string()
'me, me, me'
```

---

## 哪些调用是错的？

```python
def net_conn(scheme, host='douban', port=80):
    print "connect to %s://%s:%s" % (scheme, host, port)

>>> net_conn('http', 'douban', host='8080')

>>> net_conn('douban', scheme='http', port=8080)

>>> net_conn(port=8080, host='douban', 'http')

>>> net_conn(port=8080, host='douban', scheme='http')

>>> net_conn(scheme='http', 'douban', port='8080')

>>> net_conn('http', port='8080')

>>> net_conn('http', 'douban')

>>> net_conn('http', 'douban', 8080, 'tcp')
```

---

## 哪些调用是错的？

```python
def net_conn(scheme, host='douban', port=80):
    print "connect to %s://%s:%s" % (scheme, host, port)

>>> net_conn('http', 'douban', host='8080')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: net_conn() got multiple values for keyword argument 'host'

>>> net_conn('douban', scheme='http', port=8080)
  File "<stdin>", line 1
TypeError: net_conn() got multiple values for keyword argument 'scheme'

>>> net_conn(port=8080, host='douban', 'http')
  File "<stdin>", line 1
SyntaxError: non-keyword arg after keyword arg

>>> net_conn(port=8080, host='douban', scheme='http')
connect to http://douban:8080
```

---

## 哪些调用是错的？

```python
def net_conn(scheme, host='douban', port=80):
    print "connect to %s://%s:%s" % (scheme, host, port)

>>> net_conn(scheme='http', 'douban', port='8080')
  File "<stdin>", line 1
SyntaxError: non-keyword arg after keyword arg

>>> net_conn('http', port='8080')
connect to http://douban:8080

>>> net_conn('http', 'douban')
connect to http://douban:80

>>> net_conn('http', 'douban', 8080, 'tcp')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: net_conn() takes at most 3 arguments (4 given)
```

---

## 可变长度的参数

```python
>>> def f(x, *args, **kwargs):
...     print 'x:', x, 'args:', args, 'kwargs:', kwargs
...
>>> f(1)
x: 1 args: () kwargs: {}

>>> f(1, 2, 3)
x: 1 args: (2, 3) kwargs: {}

>>> f(1, 2, n=3)
x: 1 args: (2,) kwargs: {'n': 3}
```

---

## 匿名函数与lambda

- lambda [_arg1_[, _arg2_, ..., _argN_]]: _expression_

```python
>>> sorted([('Bo', 24), ('Yi', 23), ('Si', 31)], key=lambda p: p[1])
[('Yi', 23), ('Bo', 24), ('Si', 31)]

>>> map((lambda x: x+' me'), ['love', 'hate', 'kill'])
['love me', 'hate me', 'kill me']

>>> reduce((lambda x,y: x+y), range(10))
45

# but this is faster:
>>> from operator import add
>>> reduce(add, range(10))
```

---

## Decorator

### Case A

```python
def my_songs(request):
    if request.user:
        songs = request.user.songs
        return render_songs_list(songs=songs)
    else:
        raise NotLoginError()
```

### 重构

```python
@require_login
def my_songs(request):
    songs = request.user.songs
    return render_songs_list(songs=songs)
```


---

### Case B

```python
MCKEY_SONGS = 'songs:%s'

def get_songs(user_id):
    mckey = MCKEY_SONGS % user_id
    songs = mc.get(mckey)
    if songs is None:               # "if not songs"?
        rows = store.execute('select id from user_song '
                             'where user_id=%s', user_id)
        songs = [id for id, in rows]
        mc.set(mckey, songs, ONE_DAY)
    return songs
```

### 重构

```python
@cache(MCKEY_SONGS, ONE_DAY)
def get_songs(user_id):
    rows = store.execute('select id from user_song '
                         'where user_id=%s', user_id)
    return [id for id, in rows]
```

---

## How to write a decorator(case A)

```python
def require_login(func):
    def _(request, *args, **kwargs):
        if request.user:
            return func(request, *args, **kwargs)
        raise NotLoginError()
    return _


@require_login
def my_songs(request):
    return render_songs_list(request.user.songs)
```

---

## decorator做了什么

```python
@f
def func(): pass
```

### 等效于

```python
def func(): pass
func = f(func)
```

---

## How to write a decorator(case B)

```python
def cache(key, expire=0):
    def cached_func(original_func):
        def _(*args, **kw):
            mckey = key % args
            result = mc.get(mckey)
            if result is None:
                result = original_func(*args, **kw)
                mc.set(mckey, result, expire)
            return result
        return _
    return cached_func


@cache(MCKEY_SONGS, ONE_DAY)
def get_songs(user_id):
    rows = store.execute('select id from user_song '
                         'where user_id=%s', user_id)
    return [id for id, in rows]
```

---

## 带参数的decorator做了什么

```python
@f(arg)
def func(): pass
```

### 等效于

```python
def func(): pass
func = f(arg)(func)
```

---

## Another way(callable object)

```python
class cache(object):
    def __init__(self, key, expire=0):
        self.key = key
        self.expire = expire

    def __call__(self, original_func):
        def cached_func(*args, **kw):
            mckey = self.key % args
            result = mc.get(mckey)
            if result is None:
                result = original_func(*args, **kw)
                mc.set(mckey, result, expire)
            return result
        return cached_func
```

---

# Iterators
---

## Functional Programming

- 不进行状态改变，而是在函数间传递数据流.
- 不产生副作用。但python程序员没那么极端。
- 在python中，可以编写函数来接收和返回对象实例，通过这种方式来结合OO和FP。

- 函数式风格的理论上与实践上的好处：
  - Formal provability
  - Modularity
  - Ease of debugging and testing
  - Composability

---

## 迭代器

### 什么是迭代器？迭代器用起来是什么感觉？

```python
for element in [1, 2, 3]:
    print element

for key in {'one':1, 'two':2}:
    print key

for key, value in {'one':1, 'two':2}.items():
    print key, value

for char in "123":
    print char

for line in open("myfile.txt"):
    print line
```

---

## for在这里做了什么?

- 调用了iter()方法，得到一个对象
- 对该对象反复调用next()方法
- 直到next()方法抛出一个异常

```python
>>> s = 'abc'
>>> it = iter(s)
>>> it
<iterator object at 0x00A1DB50>
>>> it.next()
'a'
>>> it.next()
'b'
>>> it.next()
'c'
>>> it.next()
Traceback (most recent call last):
    File "<stdin>", line 1, in ?
        it.next()
StopIteration
```

---

## for是“iteration sugar”

- 原始用法

```python
it = iter(something)
while 1:
    try:
        item = it.next()
    except StopIteration:
        break
    process(item)
```

- 使用 for

```python
for item in something:
    process(item)

```

---

## Iterator是什么？

- 一个`iterator`(迭代器)描述了一个数据流。
- `iterator`支持`next()`方法，返回其描述的数据流的下一个元素。
- 如果能从一个对象中得到它的`iterator`，就说这个对象能被迭代(`iterable`)。

---

## 写一个Iterator

```python
class Reverse:
    """一个迭代器，逆序返回给定序列中的元素"""

    def __init__(self, data):
        if not hasattr(data, '__len__') or not hasattr(data, '__getitem__'):
            data = list(data)
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

>>> rev = Reverse('spam')
>>> iter(rev)
<__main__.Reverse object at 0x00A1DB50>
>>> for char in rev:
...     print char
```

---

## 生成器

- 生成器是一种简单创建迭代器的特殊函数。生成器执行后返回的是一个迭代器。
- 执行到`yield`的时候，其运行状态会被挂起，下次调用`next()`时恢复执行。

```python
def reverse(data):

    for char in data[::-1]:
        yield char

>>> for char in reverse('AI'):
...     print char
I
A
```

---

- 生成器可以有一个不带参数的return，表示数据流的结束，跟执行到底效果一样。
- 生成器可以接受传入值。
- 不同于一般函数，生成器可以从多个不同位置开始运行、结束运行和挂起。

例子：生成从x个元素的列表中选k个的所有可能组合

```python
>>> list(gcomb([1, 2, 3, 4], 2))
[[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
```

--

```python
def gcomb(x, k):

    if k == 0:
        yield []

    elif k <= len(x):
        first, rest = x[0], x[1:]

        # 第一个元素要么选，要么不选
        for c in gcomb(rest, k-1):
            c.insert(0, first)
            yield c

        for c in gcomb(rest, k):
            yield c

```

---

## 生成器表达式

- 把列表解析的方括号换成圆括号，就是生成器表达式，它返回一个迭代器。
- 迭代器按需计算数据，而列表解析需要一次性把所有数据实体化。
  处理无限长度或海量数据时，生成器表达式更佳。

```python
>>> sum(x * y for x,y in zip(xvec, yvec)) # dot product
260

>>> page = ('this is a big dog', 'this is a small cat')

# List comprehension to set
>>> words = set([word for line in page for word in line.split()])

# Set comprehension
>>> words = {word for line in page for word in line.split()}

# Generator expression to set
>>> words = set(word for line in page for word in line.split())

>>> words
set(['a', 'this', 'big', 'is', 'dog', 'cat', 'small'])
```

---

## tools for iterable

### any / all
- any([0, 1, 0]) => True
- all([1, 1, 0]) => False

### itertools
- itertools.count() => 0, 1, 2, ...
- itertools.cycle([1, 2]) => 1, 2, 1, 2, ...
- itertools.chain([1, 2], ('a', 'b')) => 1, 2, 'a', 'b'
- map的iter版：itertools.imap
- filter的iter版：itertools.ifilter
- zip的iter版：itertools.izip
- more...


---

### Examples of functional programming
## from the "Fun Tests"
# A recursive Sieve of Eratosthenes generator

---

```python
>>> def firstn(g, n):
...     return [g.next() for i in xrange(n)]
```

---

```python
>>> def firstn(g, n):
...     return [g.next() for i in xrange(n)]

>>> def intsfrom(i):
...     while 1:
...         yield i
...         i += 1

>>> firstn(intsfrom(5), 7)
[5, 6, 7, 8, 9, 10, 11]
```

---

```python
>>> def firstn(g, n):
...     return [g.next() for i in xrange(n)]

>>> def intsfrom(i):
...     while 1:
...         yield i
...         i += 1

>>> def exclude_multiples(n, ints):
...     for i in ints:
...         if i % n:
...             yield i

>>> firstn(exclude_multiples(3, intsfrom(1)), 6)
[1, 2, 4, 5, 7, 8]
```

---

```python
>>> def firstn(g, n):
...     return [g.next() for i in xrange(n)]

>>> def intsfrom(i):
...     while 1:
...         yield i
...         i += 1

>>> def exclude_multiples(n, ints):
...     for i in ints:
...         if i % n:
...             yield i

>>> def sieve(ints):
...     prime = ints.next()
...     yield prime
...     not_divisible_by_prime = exclude_multiples(prime, ints)
...     for p in sieve(not_divisible_by_prime):
...         yield p

>>> primes = sieve(intsfrom(2))

>>> firstn(primes, 16)
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
```

---

# generate all integers of the form
##    `2**i * 3**j  * 5**k`
# in increasing order
## (i, j, k >= 0)

---

```python
>>> def times(n, g):
...     for i in g:
...         yield n * i

>>> firstn(times(10, intsfrom(1)), 10)
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
```

---

```python
>>> def times(n, g):
...     for i in g:
...         yield n * i

>>> def merge(g, h):
...     ng = g.next()
...     nh = h.next()
...     while 1:
...         if ng < nh:
...             yield ng
...             ng = g.next()
...         elif ng > nh:
...             yield nh
...             nh = h.next()
...         else:
...             yield ng
...             ng = g.next()
...             nh = h.next()
```

---

```python
>>> def times(n, g):
...     for i in g:
...         yield n * i

>>> def merge(g, h):
...     ng = g.next()
...     nh = h.next()
...     while 1:
...         if ng < nh:
...             yield ng
...             ng = g.next()
...         elif ng > nh:
...             yield nh
...             nh = h.next()
...         else:
...             yield ng
...             ng = g.next()
...             nh = h.next()

>>> def m235():
...     yield 1
...     me_times2 = times(2, m235())     # works, but inefficient
...     me_times3 = times(3, m235())
...     me_times5 = times(5, m235())
...     for i in merge(merge(me_times2,
...                          me_times3),
...                    me_times5):
...         yield i

>>> result = m235()
>>> print firstn(result, 15)
[1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24]
```

---

## Use itertools.tee to get the internal uses of m235 to share a single generator
```python
>>> from itertools import tee
>>> def m235():
...     def _m235():
...         yield 1
...         for n in merge(times(2, m2),
...                        merge(times(3, m3),
...                              times(5, m5))):
...             yield n
...     m1 = _m235()
...     m2, m3, m5, mRes = tee(m1, 4)
...     return mRes


>>> it = m235()
>>> print firstn(it, 15)
[1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24]
```

---

# Fibonacci generator

---

```python
>>> def fib():
...
...     def _isum(g, h):
...         while 1:
...             yield g.next() + h.next()
...
...     def _fib():
...         yield 1
...         yield 2
...         fibTail.next() # throw first away
...         for res in _isum(fibHead, fibTail):
...             yield res
...
...     realfib = _fib()
...     fibHead, fibTail, fibRes = tee(realfib, 3)
...     return fibRes


>>> firstn(fib(), 16)
[1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]
```

---

# >>> import this

---
# Beautiful is better than ugly.
---
```python
halve_evens_only = lambda nums: map(lambda i: i/2, filter(lambda i: not i%2, nums))

#-----------------------------------------------------------------------

def halve_evens_only(nums):
    return [i/2 for i in nums if not i % 2]

#-----------------------------------------------------------------------

def halve(nums):
    return [i / 2 for i in nums]

def evens_only(nums):
    return [i for i in nums if not i % 2]

def halve_evens_only(nums):
    return halve(evens_only(nums)
```
---
# Explicit is better than implicit.
---
```python
from corelib.consts import *

#-----------------------------------------------------------------------

from corelib.consts import (K_SAYING, K_NOTE, K_PHOTO, K_TOPIC,
                            K_ONLINE_EVENT, K_PHOTO_ALBUM, K_GROUP)

#-----------------------------------------------------------------------

import corelib.consts import consts
consts.K_SAYING
```
---
```python
from os import *
print getcwd()

#-----------------------------------------------------------------------

import os
print os.getcwd()
```
---
```python

def f(dryrun):
    if not dryrun:
        print 'run'

f(False)

#-----------------------------------------------------------------------

def f(dryrun):
    if not dryrun:
        print 'run'

dryrun = False
f(dryrun)
```
---
```python

def _underlying_print_something(target=sys.stdout):
    print >> target, 'something'

_underlying_print_something()

#-----------------------------------------------------------------------

def _underlying_print_something(target=sys.stdout):
    print >> target, 'something'

_underlying_print_something(sys.stdout)

#-----------------------------------------------------------------------

def _underlying_print_something(target):
    print >> target, 'something'

def _underlying_print_something_to_stdout():
    return _underlying_print_something(sys.stdout)

_underlying_print_something_to_stdout()
```
---
# Simple is better than complex.
---
```python
# 不好::

    for i in xrange(len(seq)-1, -1, -1):
        foo(seq[i])

# 好::

    for i in reversed(seq):
        foo(i)

    for i in seq[::-1]:
        foo(i)
```
---
# Simple is better than complex.
# Complex is better than complicated.
---
```python
counter = 0
while counter < 5:
    print counter
    counter += 1

#-----------------------------

for i in xrange(5):
    print i
```
(http://stackoverflow.com/questions/228181/zen-of-python)
---
```python

# 不好::

    for i in xrange(len(seq1)):
        foo(seq1[i], seq2[i])

# 好::

    for i, j in zip(seq1, seq2):
        foo(i, j)

    for i, j in itertools.izip(seq1, seq2):
        foo(i, j)
```
```python

# 不好::

    lst = []
    for i in seq:
        lst.append(foo(i))

# 好::

    lst = [foo(i) for i in seq]

    for x in (foo(i) for i in seq):
        bar(x)
```
---
```python
def store(weight, temperature, color):
    import sqlalchemy
    import sqlalchemy.types as sqltypes

    db = create_engine(
        'mysql://user:password@localhost/db?charset=utf8&use_unicode=1')
    db.echo = False
    metadata = sqlalchemy.MetaData(db)
    table = sqlalchemy.Table('measurements', metadata,
        sqlalchemy.Column('id', sqltypes.Integer, primary_key=True),
        sqlalchemy.Column('weight', sqltypes.Float),
        sqlalchemy.Column('temperature', sqltypes.Float),
        sqlalchemy.Column('color', sqltypes.String(32)),
        )
    table.create(checkfirst=True)

    for measurement in measurements:
        i = table.insert()
        i.execute(weight=weight, temperature=temperature, color=color)
```
---
```python
def store(measurements):
    import MySQLdb
    db = MySQLdb.connect(user='user', passwd="password", host='localhost', db="db")

    c = db.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS measurements
                 id int(11) NOT NULL auto_increment,
                 weight float,
                 temperature float,
                 color varchar(32)
                 PRIMARY KEY id
                 ENGINE=InnoDB CHARSET=utf8""")

    for measurement in measurements:
        c.execute("INSERT INTO measurements (weight, temperature, color) "
                  "VALUES (%s, %s, %s)",
                  (weight, temperature, color))
```

(http://artifex.org/~hblanks/talks/2011/pep20_by_example.html)
---
# Flat is better than nested.
---
```python
def identify(animal):
    if animal.is_vertebrate():
        noise = animal.poke()
        if noise == 'moo':
            return 'cow'
        elif noise == 'woof':
            return 'dog'
    else:
        if animal.is_multicellular():
            return 'Bug!'
        else:
            if animal.is_fungus():
                return 'Yeast'
            else:
                return 'Amoeba'
```
---
```python
def identify(animal):
    if animal.is_vertebrate():
        return identify_vertebrate()
    else:
        return identify_invertebrate()

def identify_vertebrate(animal):
    noise = animal.poke()
    if noise == 'moo':
        return 'cow'
    elif noise == 'woof':
        return 'dog'

def identify_invertebrate(animal):
    if animal.is_multicellular():
        return 'Bug!'
    else:
        if animal.is_fungus():
            return 'Yeast'
        else:
            return 'Amoeba'
```
---
# Sparse is better than dense.
---
```python
""" Parse an HTTP response object, yielding back new requests or data. """

#-----------------------------------------------------------------------

def process(response):
    selector = lxml.cssselect.CSSSelector('#main > div.text')
    lx = lxml.html.fromstring(response.body)
    title = lx.find('./head/title').text
    links = [a.attrib['href'] for a in lx.find('./a') if 'href' in a.attrib]
    for link in links:
        yield Request(url=link)
    divs = selector(lx)
    if divs: yield Item(utils.lx_to_text(divs[0]))

#-----------------------------------------------------------------------

def process(response):
    lx = lxml.html.fromstring(response.body)

    title = lx.find('./head/title').text

    links = [a.attrib['href'] for a in lx.find('./a') if 'href' in a.attrib]
    for link in links:
        yield Request(url=link)

    selector = lxml.cssselect.CSSSelector('#main > div.text')
    divs = selector(lx)
    if divs:
        bodytext = utils.lx_to_text(divs[0])
        yield Item(bodytext)
```
---
# Readability counts.
---
![no pep8, no soup](static/image/no-pep8-no-soup.jpg)
---
```python
# 不好::

    if x != []:
        do_something()

# 好::

    if not x:
        do_something()
```
```python
# 不好::

    for i in range(len(seq)):
        foo(seq[i], i)

# 好::

    for i, item in enumerate(seq):
        foo(item, i)
```

---

# Special cases aren't special enough to break the rules.

--

# Although practicality beats purity.

---

# Special cases aren't special enough to break the rules.

* A string of length 1 is not special enough to deserve a dedicated char type.

# Although practicality beats purity.

* That's why we have the chr() and ord() builtins.

---

# Errors should never pass silently.

--

# Unless explicitly silenced.

---

```python
""" Import whatever json library is available. """

try:
    import json

except ImportError:

    try:
        import simplejson as json

    except:
        print 'Unable to find json module!'
        raise
```

- One more thing: fail early, fail loudly

---

# In the face of ambiguity, refuse the temptation to guess.

---

```python
if not a and b:
    assert not a
    assert b

# -------------------

if b and not a:
   pass
```

---

# There should be one -- and preferably only one -- obvious way to do it.

---

# Although that way may not be obvious at first unless you're Dutch.

---

```python
def fibonacci_generator():
    prior, current = 0, 1
    while current < 100:
        yield prior + current
        prior, current = current, current + prior

sequences = [
    range(20),
    {'foo': 1, 'fie': 2},
    fibonacci_generator(),
    (5, 3, 3),

for sequence in sequences:
    for item in sequence: # all sequences iterate the same way
        pass
```

---

# Now is better than never.

--

# Although never is often better than *right* now.

---

```python
def deprecated_func():
    raise DeprecationWarning
```

```python
from __future__ import print_function

print(b'Hello, bytes!')
print(u'Hello, unicodes!')
```

---

# If the implementation is hard to explain, it's a bad idea.

---

# If the implementation is easy to explain, it may be a good idea.

---

```python
import xml.dom.minidom

document = xml.dom.minidom.parseString(
    '''<menagerie><cat>Fluffers</cat><cat>Cisco</cat></menagerie>''')
menagerie = document.childNodes[0]

for node in menagerie.childNodes:
    if node.childNodes[0].nodeValue== 'Cisco' and node.tagName == 'cat':
        return node

# -----------------------------------------------

import lxml

menagerie = lxml.etree.fromstring(
    '''<menagerie><cat>Fluffers</cat><cat>Cisco</cat></menagerie>''')

for pet in menagerie.find('./cat'):
    if pet.text == 'Cisco':
        return pet
```

---

# Namespaces are one honking great idea -- let's do more of those!

---

```python
def chase():
    import menagerie.models.cat as cat
    import menagerie.models.dog as dog

    dog.chase(cat)
    cat.chase(mouse)
```

---

## 随机调查：如果只能选一条，你认为最重要的是什么

- py: Readability counts.
- Davies: KISS.
- xyb: Simple is better than complex.
- hongqn: Readability counts.
- su27: KISS.

---

# KISS
#### Keep It Simple and Stupid!

---

## 一个故事

```python
def get_picture():
    return hasattr(self, 'picture') and self.picture or default_picture
```

---

```python
def get_picture():
    return hasattr(self, 'picture') and self.picture or default_picture

# wait, it should be...
def get_picture():
    return (hasattr(self, 'picture') and [self.picture] or [default_picture])[0]
```

---

```python
def get_picture():
    return hasattr(self, 'picture') and self.picture or default_picture

# wait, it should be...
def get_picture():
    return (hasattr(self, 'picture') and [self.picture] or [default_picture])[0]

# why not
def get_picture():
    return self.picture if hasattr(self, 'picture') else default_picture

# then unittest failed...LOL
```

---

```python
def get_picture():
    return hasattr(self, 'picture') and self.picture or default_picture

# wait, it should be...
def get_picture():
    return (hasattr(self, 'picture') and [self.picture] or [default_picture])[0]

# why not
def get_picture():
    return self.picture if hasattr(self, 'picture') else default_picture

# then unittest failed...LOL

# is this better than the original one?
def get_picture():
    return self.picture if (hasattr(self, 'picture') and
                            self.picture) else default_picture

# and this?
def get_picture():
    return getattr(self, 'picture', None) or default_picture
```

---

# About Class

---

## Subclassing

### old-style class的诡异行为
```python
>>> class Base:
...     def say(self):
...         print 'base'
...
>>> class Base1(Base):
...     pass
...
>>> class Base2(Base):
...     def say(self):
...         print 'base2'
...
>>> class MyClass(Base1, Base2):
...     pass
...
>>> m = MyClass()
>>> m.say()
base
```

---

### MRO用于解决复杂继承关系中的method查找问题(new-style class)
```
                          6
                         ---
Level 3                 | O |                  (more general)
                      /  ---  \
                     /    |    \                      |
                    /     |     \                     |
                   /      |      \                    |
                  ---    ---    ---                   |
Level 2        3 | D | 4| E |  | F | 5                |
                  ---    ---    ---                   |
                   \  \ _ /       |                   |
                    \    / \ _    |                   |
                     \  /      \  |                   |
                      ---      ---                    |
Level 1            1 | B |    | C | 2                 |
                      ---      ---                    |
                        \      /                      |
                         \    /                      \ /
                           ---
Level 0                 0 | A |                (more specialized)
                           ---
```
- http://www.python.org/download/releases/2.3/mro/

---

- super并没有调用到“父类方法”，而是调用了MRO中的下一个方法。
- 例如，Y是X的子类，`super(Y, obj).foo()`会在`obj.__class__.__mro__`中，
  紧接着Y查找到X的foo方法进行调用。

```python
>>> class A(object):
...     def __init__(self):
...         print "A"
...         super(A, self).__init__()
...
>>> class B(object):
...     def __init__(self):
...         print "B"
...         super(B, self).__init__()
...
>>> class C(A,B):
...     def __init__(self):
...         print "C"
...         A.__init__(self)
...         B.__init__(self)
...

>>> print "MRO:", [x.__name__ for x in C.__mro__]
MRO: ['C', 'A', 'B', 'object']
>>> C()
C A B B
<__main__.C object at 0xc4910>
```

---

- 不要混用old-style和new-style class
- 尽量避免多重继承
- 父类和子类中要用super就全用super
- super的其他一些问题(http://fuhm.net/super-harmful)

---

- 在python中，私有属性并不能用一般的方式实现

```python
>>> class MyClass(object):
...     __secret_value = 1
...
>>> instance_of = MyClass()
>>> instance_of.__secret_value
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'MyClass' object has no attribute '__secret_value'

>>> dir(MyClass)
['_MyClass__secret_value', '__class__', '__delattr__', '__dict__',
'__doc__', '__getattribute__', '__hash__', '__init__', '__module__',
'__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
'__str__', '__weakref__']
>>> instance_of._MyClass__secret_value
1
```

- 私有行为可以用descriptor和property的方式实现

---

## Descriptors

- descriptor用来自定义你希望对象在读写属性时发生的事情。

```shell
>>> class UpperString(object)

...     def __init__(self):
...         self._value = ''

...     def __get__(self, instance, klass):
...         return self._value

...     def __set__(self, instance, value):
...         self._value = value.upper()
...
>>> class MyClass(object):
...     attribute = UpperString()
...
>>> instance_of = MyClass()
>>> instance_of.attribute
''
>>> instance_of.attribute = 'my value'
>>> instance_of.attribute
'MY VALUE'
```

---

## Properties

```python
>>> class MyClass(object):
...     def __init__(self):
...         self._my_secret_thing = 1
...
...     def _i_get(self):
...         return self._my_secret_thing
...
...     def _i_set(self, value):
...         self._my_secret_thing = value
...
...     def _i_delete(self):
...         print 'ouch!'
...
...     my_thing = property(_i_get, _i_set, _i_delete,
...                         'the thing')
...
>>> help(MyClass())
Help on MyClass in module __main__ object:
class MyClass(__built-in__.object)
  | Methods defined here:
  |
  | __init__(self)
  |
  | -------------------------------------------
  | Data descriptors defined here:
  | ...
  | my_thing
  |     the thing
```

---

### `__getattr__()` 和 `__getattribute__`

- `__getattr__`方法是在属性不能从实例的`__dict__`或它的类的`__dict__`，
  或它的祖先的`__dict__`中找到的时候，才被调用。但`__getattribute__`无论何种情况，
  都会被调用。

- 两者都被定义了的话，除非`__getattribute__`引发`AttributeError`，或者显式调用，
  否则`__getattr__`不会被调用。

---

### `__getattribute__`中属性查找的顺序

- 类属性
- data descriptor
- 实例属性
- non-data descriptor
- 此时`__getattribute__`会抛出`AttributeError`，如果有`__getattr__`，则会调用之，
  否则错误将会抛给用户。

---

## Meta

### The `__new__` Method

- 当对象创建时永远会调用`__new__`，不论`__init__`是否被调用。
- `__new__`在`__init__`之前被调用。
- 用来检查对象的初始化情况，或进行一些更底层的初始化工作。

---

## the Black Magic: Meta Programming

- 如果你不知道它是干什么的，那你用不到它。*(by hongqn)*

### The `__metaclass__` Method

- Just as regular classes act as templates for producing instances,
  metaclasses act as templates for producing classes.

- 虽然meta-programming十分强大，但绝大部分情况下不会用到，因为在oop中，
  class自己一般不会扮演实例的角色。而且它使class设计晦涩难懂。

- 适用的情况一般是，在类代码的设计阶段，并不能精确预知这个类需要做的所有事情，比如：

  - 模块被不同的应用调用时
  - 运行时可能面对的未知情况


---
# The End
