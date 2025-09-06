# 如何写CSS样式表

## 第一步：body

- font-family 字体
- background-color 背景色
- padding 内边距
- margin 外边距 是否清除自带的margin

``` css
body {
    font-family: Arial, sans-serif;
    background-color: white;
    padding: 20px;
    margin: 0;
}
```

## 第二步 .container

- margin: 0 auto; 确保容器居中
- background-color 背景色
- padding 盒子内边距

---

- border-radious 圆角，柔化边缘
- box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); 盒子阴影 参数一水平偏移 参数二垂直偏移 参数三模糊半径 参数四阴影颜色

``` css
.container {
    max-width: 600px;
    margin: 0 auto;
    background-color: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
```

## 标题等块元素

- text-align 对齐方式

```
h1 {
    text-align: center;
}
```

## 行内元素

行内元素换行不一定要使用br，也可以将其转换为块元素

行内元素不可以设置宽度、高度、对齐方式

``` css
label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
}
```

## 行内块

input等输入控件是行内块

- width 宽度
- padding 输入框内边距
- margin 外边距 输入框与其他元素的间隔
- border 边框

---

- border-radius 圆角，柔化边缘

``` css
input,
select,
textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 15px;
    border: 1px solid #ccc;
    border-radius: 4px;
}
```

## 单选按钮和复选框

如果label设置为了块元素，可以使用display: flex;实现和行内元素类似的排版

``` css
.radio-group {
    display: flex;
    align-items: center;
    margin-top: 15px;
}
```

.radio-group是单选按钮的父元素