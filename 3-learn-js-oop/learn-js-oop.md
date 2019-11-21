# **JavaScript 面向对象编程学习笔记**


> **参考资料：**
>
> 1. [JavaScript 教程 | 菜鸟教程](https://www.runoob.com/js/js-tutorial.html)
> 2. [JavaScript 教程 - W3school](https://www.w3school.com.cn/js/index.asp)
> 3. [JavaScript教程 - 廖雪峰的官方网站](https://www.liaoxuefeng.com/wiki/1022910821149312)

---

#  1 JavaScript 对象概念

JavaScript的对象是一种无序的集合数据类型，它由若干键值对组成。一个对象的全部键值对由一对花括号`{}`包裹，键值对由`Key : Value`的形式组成，由`,`隔开。例如：

```js
var student = {
    name: 'Mike',
    age: 20,
    college: 'PKU',
    major: 'CS',
    class: 2,
    'favorite-sport': 'basketball'
};
```

**注意：** 最后一个键值对不需要在末尾加`,`，如果加了，有的浏览器（如低版本的IE）将报错。 

每一个键都可被是做是该对象的一个属性，JavaScript对象的所有属性都是字符串（如果属性名包含特殊字符，就必须用`''`括起来；若不含，则可以省略），不过属性对应的值可以是任意数据类型。  

## 访问属性

访问属性有两种方式：

1.  通过`.<key>`操作符访问属性

   这种方式比较常用，但这要求属性名必须是一个有效的变量名，因此这种方法无法访问包含特殊字符的属性（如上面的 `'favorite-sport'`）

   ```js
   student.age;  // 20
   student.name; // "Mike"
   ```
   
2.  通过`['key']`来访问属性

    这是访问各种属性的通用方法，可以用于访问各种类型的属性

    ```js
    student["age"]; // 20
    student["favorite-sport"]; // "basketball"
    ```

## 属性判定

访问 JavaScript 中不存在的属性不会报错，而是返回`undefined`：

```js
student.gender; // undefined
```

可以使用`in` 检测一个属性是否存在于某个对象中，返回`true`或`false`:

```js
'name' in student; // true
'gender' in student; // false
/*****************************/
 'toString' in student; // true
```

但是使用`in`判定属性归属时会包括其继承的所以属性，例如所有对象最终都会在原型链上指向`object`对象，而`toString`定义在`object`对象中，因此对任何属性使用`'toString'  in` 得到的结果都是`true`。要判断一个属性是否是某对象自身拥有的，而不是继承得到的，可以用`hasOwnProperty()`方法： 

```js
student.hasOwnProperty('name'); // true
student.hasOwnProperty('toString'); // false
```

## 修改属性

 JavaScript 的对象是动态类型，可以使用赋值语句创建一个新属性，或使用`delete`删除一个属性：

```js
student.gender = 'male'; // 新增属性 gender
'gender' in student； // true

delete student.class； // 删除属性 class
'class' in student； // false
```

---

# 2 JavaScript 标准对象







---

# 3 JavaScript 面向对象编程

