# ch2 Cafe Menu

## Abstract

`CSS` tells the browser how to display your webpage. You can use `CSS` to set the color, font, size, and other aspects of HTML elements.

In this course, you'll learn CSS by designing a menu page for a cafe webpage.

CSS is the language used to style an HTML document. It describes how HTML elements should be displayed on the screen.

## Note

### style 样式标签 

在html中的css代码一般放在 `style` 标签中， `style` 标签要嵌套在 `head` 标签中

Until now, you've had limited control over the presentation and appearance of your content. To change that, add a `style` element within the `head` element.

### element selector(type selector) 元素选择器

You can add style to an element by specifying it in the `style` element and setting a property for it like this:

    element {
      property: value;
    }

Center the content of the `h1` element by setting its `text-align` property to the value `center`.

You now have three type selectors with the same styling. You can add the same group of styles to many elements by creating a list of selectors. Each selector is separated with commas like this:

    selector1, selector2 {
      property: value;
    }

### styles.css 外部样式表

You have styled three elements by writing CSS inside the style tags. This works, but since there will be many more styles, it's best to put all the styles in a separate file and link to it.

### link 链接标签（空标签）

`link` 标签需要嵌套在 `head` 标签中

    <link href="styles.css" rel="stylesheet"/>

Now you need to link the styles.css file, so the styles will be applied again. Inside the head element, add a `link` element. Give it a `rel` attribute with the value of `"stylesheet"` and an `href` attribute with the value of `"styles.css"`.

Note that the `link` element is a void element.

### meta 元标签

For the styling of the page to look similar on mobile as it does on a desktop or laptop, you need to add a meta element with a special content attribute.

Add the following within the head element:

    <meta name="viewport" content="width=device-width, initial-scale=1.0" />

### div 分块标签

division 分区，分割 主要用于布局

The `div` element is used mainly for design layout purposes, unlike the other content elements you have used so far.

Inside the opening div tag, add the `id` attribute with a value of menu.

### id selector & width ID选择器

The goal now is to make the `div` not take up the entire width of the page. The CSS `width` property is perfect for this.

You can use the id selector to target a specific element with an `id` attribute. An id selector is defined by placing the hash symbol `#` directly in front of the element's `id` value. For example, if an element has the `id` of cat then you would target that element like this:

    #cat {
      width: 250px;
    }

> [!WARNING]
> No space between `#` and id selector.

### comments

Like this:

    /* comment here */

### px & %

Now it's easy to see that the text is centered inside the #menu element. Currently, the width of the #menu element is specified in pixels (`px`).

Change the width property's value to be 80%, to make it 80% the width of its parent element (body).

### margin 外边距

Next, you want to center the #menu horizontally. You can do this by setting its `margin-left` and `margin-right` properties to `auto`. Think of the `margin` as an invisible space around an element. Using these two `margin` properties, center the #menu element within the body element.

使用 `margin` 将某元素居中：

    #menu {
      margin: 0 auto;
    }

### class selector 类选择器

So far you have been using type and id selectors to style elements. However, it is more common to use a different selector to style your elements.

A *class selector* is defined by a name with a dot directly in front of it, like this:

    .class-name {
      styles
    }

> [!NOTE]
> There is no space between `.` and class-name

### background-image

Since the cafe's main product for sale is coffee, you could use an image of coffee beans as the page background.

Add a `background-image` property and set its value to `url(the url of an image)`.

设置背景图片：

    body {
      background-image: url(the url of an image)
    }

### article 文章标签

`article` 内部通常嵌套多个具有相关信息的标签

`article` elements commonly contain multiple elements that have related information.

### class-type selector 复合选择器

The `p` elements are nested in an `article` element with the `class` attribute of item. You can style all the `p` elements nested anywhere in elements with a `class` named item like this:

    .item p { }

Using the above selector, add a `display` property with value `inline-block` so the p elements behave more like *inline elements*.

### padding 内边距

You can give your menu some space between the content and the sides with various `padding` properties.

- `padding-left`
- `padding-right`
- `padding-top`
- `padding-bottom`

if 4 sides have the same padding, only use `padding`

### max-width

Add a `max-width` property to the menu class with a value of 500px to prevent it from growing too wide.

### font-family

You can change the `font-family` of text, to make it look different from the default font of your browser. Each browser has some common fonts available to it.

Change all the text in your body, by adding a `font-family` property with the value `sans-serif`无衬线字体（微软雅黑等笔画无粗细变化的字体）. This is a fairly common font that is very readable.

You can add a fallback value for the `font-family` by adding another font name separated by a comma `, `. Fallbacks are used in instances where the initial is not found/available.

Add the fallback font `serif`衬线字体（宋体等） after the Impact font.

### font-style

Italicize the Est. 2020 by creating an established class selector and giving it a `font-style` property of `italic`.

### font-size

### hr 水平线标签

horizontal rule 水平线

You can use an `hr` element to display a divider between sections of different content.

The default properties of an `hr` element will make it appear as a thin light grey line. You can change the height of the line by specifying a value for the `height` property.

Notice the grey color along the edges of the line. Those edges are known as borders. Each side of an element can have a different color or they can all be the same.

Make all the edges of the hr element the same color as the background of it using the `border-color` property.

Notice how the thickness of the line looks bigger? The default value of a property named `border-width` is 1px for all edges of `hr` elements. By changing the border to the same color as the background, the total height of the line is 5px (3px plus the top and bottom border width of 1px).

Change the `height` property of the hr to 2px, so the total height of it becomes 4px.

### pseudo-selector 伪类选择器

You change the properties of a link when the link has actually been visited by using a pseudo-selector that looks like 

    a:visited { 
      propertyName: propertyValue; 
    }

You change the properties of a link when the mouse hovers over them by using a pseudo-selector that looks like 

    a:hover { 
      propertyName: propertyValue; 
    }

You change the properties of a link when the link is actually being clicked by using a pseudo-selector that looks like 

    a:active { 
      propertyName: propertyValue; 
    }

> [!NOTE]
> no space