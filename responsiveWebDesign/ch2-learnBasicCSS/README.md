# ch2 Cafe Menu

## Abstract

`CSS` tells the browser how to display your webpage. You can use `CSS` to set the color, font, size, and other aspects of HTML elements.

In this course, you'll learn CSS by designing a menu page for a cafe webpage.

CSS is the language used to style an HTML document. It describes how HTML elements should be displayed on the screen.

## Note

### style & element selector(type selector)

Until now, you've had limited control over the presentation and appearance of your content. To change that, add a `style` element within the `head` element.

You can add style to an element by specifying it in the `style` element and setting a property for it like this:

    element {
      property: value;
    }

Center the content of the `h1` element by setting its `text-align` property to the value `center`.

You now have three type selectors with the same styling. You can add the same group of styles to many elements by creating a list of selectors. Each selector is separated with commas like this:

    selector1, selector2 {
      property: value;
    }

### styles.css

You have styled three elements by writing CSS inside the style tags. This works, but since there will be many more styles, it's best to put all the styles in a separate file and link to it.

### link

Now you need to link the styles.css file, so the styles will be applied again. Inside the head element, add a `link` element. Give it a `rel` attribute with the value of `"stylesheet"` and an `href` attribute with the value of `"styles.css"`.

Note that the `link` element is a void element.

### meta

For the styling of the page to look similar on mobile as it does on a desktop or laptop, you need to add a meta element with a special content attribute.

Add the following within the head element:

    <meta name="viewport" content="width=device-width, initial-scale=1.0" />

### div

The `div` element is used mainly for design layout purposes, unlike the other content elements you have used so far. Add a `div` element inside the body element and then move all the other elements inside the new div.

Inside the opening div tag, add the `id` attribute with a value of menu.

### id selector & width

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

### margin

Next, you want to center the #menu horizontally. You can do this by setting its `margin-left` and `margin-right` properties to `auto`. Think of the `margin` as an invisible space around an element. Using these two `margin` properties, center the #menu element within the body element.

### class selector

So far you have been using type and id selectors to style elements. However, it is more common to use a different selector to style your elements.

A *class selector* is defined by a name with a dot directly in front of it, like this:

    .class-name {
      styles
    }

### background-image

Since the cafe's main product for sale is coffee, you could use an image of coffee beans as the page background.

Add a `background-image` property and set its value to `url(the url of an image)`.

### article

`article` elements commonly contain multiple elements that have related information.

### selector

The `p` elements are nested in an `article` element with the `class` attribute of item. You can style all the `p` elements nested anywhere in elements with a `class` named item like this:

    .item p { }

Using the above selector, add a `display` property with value `inline-block` so the p elements behave more like *inline elements*.