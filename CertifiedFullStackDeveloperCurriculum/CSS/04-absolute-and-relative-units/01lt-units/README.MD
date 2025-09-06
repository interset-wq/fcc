# Working with Relative and Absolute Units, Not started
In these lectures, you will learn about relative and absolute units, and how they both impact what you see in the browser.

## What Are Absolute Units in CSS, and When Should You Use Them?
As you design your pages, you will work with different properties like widths, heights, padding, margins, and more. When you define these properties, you will need to specify the length units of measurement you want to use.

There are two types of units you can use to define these properties: relative units and absolute units. In this lecture, we will just focus on absolute units.

Absolute length units are of fixed length and are not relative to anything else. Relative means that the length is relative to something else, like the size of the screen or the size of the parent element. We will talk more about relative units in the next few lectures.

The most common absolute unit is the pixel (px). Pixels are a fixed-size unit of measurement in CSS, providing precise control over dimensions. This means that 1px is always equal to 1/96th of an inch.

It is important to note that while 1px is standardized as 1/96th of an inch for the purposes of CSS layout, the actual physical size of a pixel may differ depending on the display.

Let's take a look at an example of using pixels to set the width and height for a box:

.box {
  width: 100px;
  height: 100px;
  background-color: red;
}
In this example, we have a red box with a width and height set to 100px. The dimensions for this box will stay the same regardless of changes pertaining to the screen size.

So, if you are on a device with a small screen, the box will still be 100px wide. If you are on a large desktop screen, the box will still be 100px wide.

So, when should you use absolute units like pixels? Well, it depends on the situation. But generally you will use pixels where you need precise control over element dimensions, spacing, and layout. Sometimes you might use pixels for margins, padding, and borders.

Here is an example of using pixels to set the margin for a box:

.box {
  width: 100px;
  height: 100px;
  background-color: red;
  margin: 10px;
}
Remember that margin is the space outside of the box. So, in this example, the box will have a margin of 10px on all sides.

Other types of absolute units include the following:

The in (inches) unit, which is equal to 96px
The cm (centimeters) unit, which is equal to 25.2/64 of an inch
The mm (millimeters) unit, which is equal to 1/10th of a centimeter
The q (quarter-millimeters) unit, which is equal to 1/40th of a centimeter
The pc (picas) unit, which is equal to 1/6th of an inch
The pt (points) unit, which is equal to 1/72th of an inch
Most of these units will be used for print and not for screens.

While the most common unit you will use is pixels, it is important to know that the other absolute units exist.

## What Are Percentages in CSS, and When Should You Use Them?
Percentages in CSS are relative units that allow you to define sizes, dimensions, and other properties as a proportion of their parent element. When you use a percentage value, you're essentially saying, "Make this X% of its container."

For example, if you set width: 50% on an element, it will occupy half the width of its parent container. This makes percentages incredibly useful for creating responsive designs that adapt to different screen sizes.

Percentages are ideal for creating fluid layouts that adjust to various screen sizes. For instance, setting a container to width: 80% ensures it takes up 80% of its parent's width, regardless of the device.

Using percentages for flexible images is another common practice. By applying max-width: 100% to images, you allow them to scale down on smaller screens while maintaining their aspect ratio.

While less common, percentages can also be used for font sizes to create scalable typography. For example, font-size: 120% would make the text 20% larger than its parent's font size.

Percentages can be particularly handy for vertical centering. Here's an example of how you might use percentages with the transform property to center an element vertically:

.center-me {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);

  width: 300px;
  height: 300px;
  background-color: red;
}
This code positions the element 50% from the top of its container, then uses transform to move it back up by half its own height, effectively centering it vertically.

You will learn more about how absolute positioning and the transform properties work in more detail in future lectures.

Remember, percentages are always relative to something. For horizontal properties like width, they're relative to the parent's width. For vertical properties like height, they're usually relative to the parent's height (if specified).

However, be cautious when nesting elements with percentage-based dimensions, as this can lead to unexpected results. Also, keep in mind that percentage-based heights can be tricky if the parent doesn't have a defined height.

In summary, percentages in CSS are powerful tools for creating flexible, responsive designs. Use them when you want elements to scale proportionally to their containers or when you need layouts that adapt seamlessly to different screen sizes.

## What Are ems and rems in CSS, and When Should You Use Them?
In the previous lecture, we learned about absolute length units like pixels. While absolute units can be helpful in certain situations, there will be times when you want to use relative units.

In this lecture, we will learn about two relative units: ems and rems.

em units are relative to the font size of the element. If you are using ems for the font-size property, the size of the text will be relative to the font size of the parent element.

To better understand how this works, let's take a look at an example:

<p class="para">I am a paragraph element</p>

<div class="blue-box"></div>
For the HTML, we have a paragraph and div element. The paragraph element has a class of para, and the div element has a class of blue-box.

Here is the accompanying CSS:

.para {
  font-size: 20px;
  margin-bottom: 1.5em;
  border: 2px solid red;
}

.blue-box {
  background-color: blue;
  color: white;
  padding: 10px;
}
For the para class, we set the font-size to 20px and the margin-bottom to 1.5em. This means that the margin will be 1.5 times the font size of the paragraph element. 1.5em results in 30 pixels of margin at the bottom of the paragraph. We have also set a border of 2px solid red so you can see the margins better.

For the blue-box class, we set the background color to blue, the text color to white, and the padding to 10px on all four sides.

From the example, there'll be a clear space between the bottom of the paragraph element and the blue box.

So what happens if we remove the font-size property from the para class?

Well, the bottom margin will be relative to the font size of the parent element. In this case, the parent element is the body element, which has a default font size of 16px.

Good use cases for ems would be when you are working with modular模块化的 components like buttons or cards. By using em units, you can ensure that all aspects of the component (such as padding, margin, and borders) scale proportionally with the font size, keeping consistent proportions.

So, up until this point, we have been setting the font size for an element using pixels. But that does present some challenges for users.

Inside your browser settings, you can control the default font size.

For those with visual impairments, they may increase the font size to make it easier to read. But if you are setting pixels for the font sizes in your web designs, the text will not scale proportionally with the rest of the content.

One way to address this issue is to use rem units for typography. A rem unit is relative to the font size of the root element, which is the html element.

By default, the font size of the html element is 16px. If the user increases the font size in their browser settings, the font size of the html element will increase, and all rem units will scale proportionally.

Here is an example of using the rem unit for the font size instead of pixels:

.para {
  font-size: 1.2rem;
  margin-bottom: 1.5em;
  border: 2px solid red;
}
By setting the font size to 1.2rem, the font size of the paragraph element will be 1.2 times the font size of the root element. If the user hasn't changed the default font size, the font size of the paragraph element will be 19.2px because it is 1.2 times 16px.

So when should you use rem units? rem units are preferred over pixels for typography because they scale proportionally with the user's browser settings. This makes your content more accessible to users with visual impairments.

rem units can also help maintain consistent spacing and layout across different elements.

## What Are vh and vw Units, and When Should You Use Them?
In CSS, vh and vw are viewport-relative units that allow you to size elements based on the dimensions of the browser window. These units are particularly useful for creating responsive designs that adapt to different screen sizes.

vh stands for "viewport height," and 1vh is equal to 1% of the viewport's height.

Similarly, vw stands for "viewport width," and 1vw is equal to 1% of the viewport's width.

This means that if you set an element's height to 100vh, it will occupy the full height of the viewport, regardless of the actual pixel dimensions of the device.

These units are especially handy when you want to create full-screen layouts or elements that maintain a specific proportion of the screen.

For example, you might want to use them to create a hero section that always fills the entire screen:

.hero {
  height: 100vh;
  width: 100vw;
}
This CSS ensures that the hero section will always be exactly the size of the viewport, regardless of the device's screen size.

vh and vw units can also be used for typography to create responsive text sizes. For instance:

h1 {
  font-size: 5vw;
}
This will set the font size of h1 elements to 5% of the viewport width, allowing the text to scale smoothly with the browser window size.

One of the advantages of vh and vw units is that they respond to changes in the viewport size in real-time. This means that if a user resizes their browser window, elements sized with these units will adjust accordingly without needing to reload the page. However, it's important to use these units judiciously明智的. Setting font sizes solely with vw units, for example, can lead to text becoming too small on narrow screens or too large on wide screens.

Another consideration is that on mobile devices, the viewport height can change when the browser's address bar appears or disappears, which can cause unexpected layout shifts if you're using vh units extensively大规模的.

In summary, vh and vw units are powerful tools for creating responsive layouts and elements that adapt to the viewport size. They're particularly useful for full-screen sections, maintaining aspect ratios, and creating smoothly scaling designs. However, they should be used thoughtfully and often in combination with other CSS techniques to ensure the best user experience across all devices.

## What Is the calc() Function, and How Does It Work?
With the calc() function, you can perform calculations directly within your stylesheets to determine property values dynamically. This means that you can create flexible and responsive user interfaces by calculating dimensions based on the viewport size or other elements.

calc() is a CSS function. You'll learn more about functions when you start learning about JavaScript, but in this lecture, you're going to learn the basics that you need to know to understand how calc() works.

A function is a block of code that performs a specific task. Some functions are already defined in CSS, so you can use them directly and pass any necessary values to them to customize how their tasks will be performed.

In the world of programming, when we run the task performed by a function, we say that we "call" the function. The values that we pass into the function are known as arguments.

Like you can see in the code below, to call a function, you write its name followed by the arguments within parentheses, separated by commas. There shouldn't be a space between the name of the function and the opening parenthesis:

function(argument1, argument2, argument3)
A function may only need one value to know what to do. In that case, it will only take one argument. That's what happens with the calc() function. It takes one argument because it needs to know what to calculate.

For this, you pass something called an expression as an argument. An expression is a combination of values and operators that produces a result.

This is how you can call the calc() function. You write the name calc, followed by parentheses, and within the parentheses, you write the expression:

calc(expression)
The expression is evaluated to calculate the final result. "Evaluated" just means that the values and operators are converted into a single value behind the scenes. The result is assigned to the CSS property where the calculation is being made.

You can perform calculations on values that represent length, angle, time, percentages, numbers, and colors. You can also combine different units like pixels, percentages, and ems.

With numbers, all the values in the expression, also called the operands操作数, must have their corresponding units, like px, em, and percentage (%). Depending on the operator, different operands may have different units.

You can use the addition (+), subtraction (-), multiplication (*), and division (/) operators in the expression.

If there are multiple operands and operators, calc() will follow the standard operator precedence优先级 rule. You can also add parentheses to establish the order of the operations if needed.

In the example below, you can see a div with the text Hello, World!:

<div>Hello, World!</div>
Using the CSS type selector for selecting the div, you can style it with white text and a dark blue background:

div {
  color: white;
  background-color: #1b1b32;
  width: calc(50% - 20px);
}
What's new here is that the width is calculated dynamically. Notice how we are calling the calc() function and passing an expression as an argument. The expression has two operands with different units and one operator, the subtraction operator.

Percentage is a relative unit. The value (50%) will be determined by the width of the parent container. Then, 20px is subtracted from the value. The result of this expression will determine the width of the div.

The width of the div is approximately half the total width of its container, and if you resize the parent container, the width will be recalculated automatically.

That's the key advantage of using calc(). You can determine the value of a CSS property dynamically based on different aspects of the application or viewport.

The expression can also contain CSS functions and variables if you need to use them in your calculations. You'll learn more about CSS variables in the next lectures.

Great. Now that you know about the basics of the calc() function, let's cover some of its best practices.

First, you must surround the addition (+) and subtraction (-) operators with whitespace.

For example, the expression below would not be a valid expression because the subtraction operator is immediately before the second operand.

calc(100% -30px)
The subtraction (-) operator must be surrounded by whitespace, like this. Adding the whitespace will create a valid expression.

calc(100% - 30px)
This is not necessary for the multiplication and division operators but it's highly recommended.

You can also nest calc() function calls if you need to perform calculations and use those results in other calculations.

Also, if you use the value zero to represent length in the expression that you pass into the calc() function, you must include the units. For example, this expression would not be valid:

calc(100% - 0)
You would need to add the units, like px.

calc(100% - 0px)
You should also know that currently, if you use the multiplication or division operators, one of the operands has to be unitless. For the division operator, specifically the right operand has to be unitless. This would not be a valid expression because both operands have units (pixels). One of the operands, either 5 or 50, must be unitless:

calc(5px * 50px)
You would need to omit删去 the units in one of them. Both of these alternatives would be valid:

calc(5 * 50px)
calc(5px * 50)
And this is an example with the division operator. This would not be a valid expression since they both have units:

calc(50% / 5%)
You should remove the unit from the right operand when you have the division operator:

calc(50% / 5)
The calc() function can be very helpful for you as a web developer. With this function, you can set property values dynamically to create flexible and responsive designs.

