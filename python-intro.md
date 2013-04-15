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
template: inverse

# Data Structures
---
## Data Structures
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
## Data Structures

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
## Data Structures

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
## Data Structures

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
## Data Structures

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
## Data Structures

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

## Data Structures

## 字符串的方法

### find, index, rfind, rindex, count
### startswith, endswith, isalpha, isdigit, isalnum, islower, isupper, isspace
### encode, decode, lower, upper, strip, lstrip, rstrip, replace
### split, rsplit, splitlines
### join

---
## Data Structures

## 容器
### tuple: `(1000001, 'ahbei')` , `(1,)`
### list: `[1, 2, 3, 4, 5]`
### dict: `{'CEO': 'ahbei', 'Team Members': ['brant', 'hongqn', ...]}`
### set: `set([1, 2, 3])`
---
## Data Structures

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
## Data Structures
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
## Data Structures
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
## Data Structures
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
## Data Structures
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
## Data Structures
### dict

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
## Data Structures
## set

### set的修改:

`add`, `discard`, `remove`, `clear`, `copy`, `update`
### set的运算:

`union`(|), `difference`(-), `intersection`(*), `symmetric_difference`(^)
### 子集的判断:

`issubset`, `issuperset`, `&gt;`, `&lt;`
---
## Data Structures
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
## Data Structures
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
## Data Structures
## tuple

- Unpacking

```python
>>> result, = (1024,)
>>> result
1024

>>> a, b = b, a
```
---
## Data Structures
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
## Data Structures
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
template: inverse

# Control Flow Tools
---
## Control Flow Tools
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
## Control Flow Tools
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
## Control Flow Tools
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
## Control Flow Tools
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
## Control Flow Tools
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
## Control Flow Tools
## 异常

- 不要做这样的事情

```python
try:
    do_something()
except:
    pass
```
---
template: inverse

# Modules
---
## Modules
### A module is a file containing Python definitions and statements.

```python
# fibo.py
author = 'su27'
_author_age = 27
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
## Modules
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
## Modules
### import的方式

```python
>>> import fibo
>>> from fibo import fib, author

>>> from fibo import * # 绝大多数情况下要避免这样用
>>> author
'su27'
>>> _author_age
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name '_author_age' is not defined
```

### Note: import的时候, 被import的模块代码将被执行
---
template: inverse

# Iterators
---
## Iterators
## 迭代器

- 迭代器用起来是什么感觉？

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

- `xrange`和`range`
- `iterkeys`, `iteritems`

---
## Iterators
## 迭代器

- for在这里做了什么?

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
## Iterators

- 一个`iterator`描述了一个数据流。
- `iterator`支持`next()`方法，返回其描述的数据流的下一个元素。
- 如果能从一个对象中得到它的`iterator`，就说这个对象能被迭代(`iterable`)。
- 写一个:

```python
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    def __iter__(self):
        return self
    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data [self.index]

>>> rev = Reverse('spam')
>>> iter(rev)
<__main__.Reverse object at 0x00A1DB50>
>>> for char in rev:
...     print char
```
---
## Iterators
## Generators
## 生成器
- 生成器是一种简单创建迭代器的特殊函数。生成器执行后返回的是一个迭代器。
- 执行到yield的时候，其运行状态会被挂起，下次调用next()时恢复执行。

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
## Iterators
## Generators

- 生成器可以有一个不带参数的return，表示数据流的结束，跟执行到底效果一样。
- 生成器可以接受传入值。
- 不同于一般函数，生成器可以从多个不同位置开始运行、结束运行和挂起。

```python
def gcomb(x, k):  # 生成元素列表x中选k个的所有可能组合
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


>>> list(gcomb([1, 2, 3, 4], 2))
[[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
```
---
## Iterators
## Generators
## Generator Expressions
### 生成器表达式
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
## Iterators
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
- ...
---
template: inverse

# Functions
---
## Functions
### python中的函数

```python
def foo(value):
    return value, value % 2
```

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
## Functions

- 可变对象不能做参数默认值

```python
>>> def hero_string(heroes=[]):
   ....:     heroes.append("me")
   ....:     return ', '.join(heroes)

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
## Functions
### 哪些调用是错的？

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
## Functions
### 哪些调用是错的？

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
## Functions
### 哪些调用是错的？

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
## Functions
### 可变长度的参数
 - 用一个元组接受可变长默认参数

```python
def func(arg1, arg2, *rest):
    print 'arg1:', arg1
    print 'arg2:', arg2
    for arg in rest:
        print 'extra arg:', arg
```

 - 用一个字典接受可变长关键字参数

```python
def func(arg1, arg2, **rest):
    print 'arg1:', arg1
    print 'arg2:', arg2
    for arg in rest:
        print 'extra arg: %s=%s' % (arg, rest[arg])
```

---
## Functions
### 可变长度的参数

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
## Functions
### 匿名函数与lambda
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
## Functions
## Decorator

- Case A

```python
def my_songs(request):
    if request.user:
        songs = request.user.songs
        return render_songs_list(songs=songs)
    else:
        raise NotLoginError()
```

- 重构

```python
@require_login
def my_songs(request):
    songs = request.user.songs
    return render_songs_list(songs=songs)
```

---
## Functions
## Decorator

- Case B

```python
MCKEY_SONGS = 'songs:%s'

def get_songs(user_id):
    songs = mc.get(MCKEY_SONGS % user_id)
    if songs is None:               # "if not songs"?
        rows = store.execute('select id from user_song '
                             'where user_id=%s', user_id)
        songs = [id for id, in rows]
        mc.set(MCKEY_SONGS, songs, ONE_DAY)
    return songs
```

- 重构

```python
@cache(MCKEY_SONGS, ONE_DAY)
def get_songs(user_id):
    rows = store.execute('select id from user_song '
                         'where user_id=%s', user_id)
    return [id for id, in rows]
```

---
## Functions
## Decorator

- How to write a decorator(case A)

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

- decorator做了什么


```python
@f
def func(): pass
```


```python
def func(): pass
func = f(func)
```
---
## Functions
## Decorator

- How to write a decorator(case B)

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

- 带参数的decorator做了什么


```python
@f(arg)
def func(): pass
```

```python
def func(): pass
func = f(arg)(func)
```
---
## Functions
## Decorator

- Another way(callable object)

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
