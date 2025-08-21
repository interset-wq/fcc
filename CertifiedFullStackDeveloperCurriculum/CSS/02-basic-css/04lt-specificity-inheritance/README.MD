# CSS Specificity特异性, the Cascade Algorithm, and Inheritance
In these lectures, you will learn about CSS specificity, the common selectors and their specificities, the cascade algorithm, inheritance, and more.

## What Is CSS Specificity, and the Specificity for Inline, Internal, and External CSS?
CSS specificity is a fundamental concept that determines which styles are applied to an element when multiple rules could apply.

Understanding specificity helps developers resolve conflicts between different CSS rules and ensures that the desired styles are consistently applied.

CSS specificity is calculated based on the type of selectors used.

The highest specificity is attributed to inline styles, which are applied directly to an element through the style attribute.

Following this, ID selectors like #main and #header have a high level of specificity.

Next, class selectors, attribute selectors, and pseudo-classes come into play.

Examples include class selectors such as .container and .button, attribute selectors like [type="text"], and pseudo-classes such as :hover. These have a moderate中等的 level of specificity.

Type selectors, such as div and h1, and pseudo-elements like ::before and ::after, have a lower specificity compared to the previous groups.

Finally, the universal selector, represented by an asterisk *, has the lowest specificity of all.

Specificity values are calculated as a four-part value (a, b, c, d):

a: Inline styles (1 or 0).
b: Number of ID selectors.
c: Number of class selectors, attribute selectors, and pseudo-classes.
d: Number of type selectors, pseudo-elements, and universal selectors.
Each part of the specificity value carries different weight:

Inline styles (a) have the highest weight, contributing a value of 1 to the first part of the specificity value.

ID selectors (b) carry the next highest weight, with each ID contributing 1 to the second part of the specificity value.

Class selectors, attribute selectors, and pseudo-classes (c) carry moderate weight, with each contributing 1 to the third part of the specificity value.

Type selectors and pseudo-elements (d) have the lowest weight, with each contributing 1 to the fourth part of the specificity value.

Universal selector (*): The universal selector contributes 0 to the specificity calculation and does not affect specificity. Its inclusion in a selector does not change the specificity value.

Inline CSS has the highest specificity because it is applied directly to the element. It overrides any internal or external CSS. The specificity value for inline styles is (1, 0, 0, 0).

Here is an example using inline styles for a div element.

Example Code
<div style="color: red;">This text is red.</div>
In this example, the text will always be red, regardless of any other styles applied via internal or external CSS.

Internal CSS is defined within a style element in the head section of the HTML document. It has lower specificity than inline styles but can override external styles.

The specificity value for internal styles is determined by the selectors used. For example, an ID selector within internal CSS has a specificity value of (0, 1, 0, 0).

Example Code
<head>
  <style>
    .text {
      color: blue;
    }
  </style>
</head>
<body>
  <div class="text">This text is blue.</div>
</body>
In this example, the text will be blue unless an inline style or a more specific external style is applied.

External CSS is linked via a link element in the head section and is written in separate .css files. It has the lowest specificity but provides the best maintainability for larger projects.

The specificity value for external styles is also determined by the selectors used. For example, a class selector within external CSS has a specificity value of (0, 0, 1, 0).

Example Code
<head>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div class="text">This text's color is defined in an external CSS file.</div>
</body>
In this example, the text color is defined in the styles.css file and will be applied unless overridden by internal or inline styles.

## What Is the Universal Selector, and What Is Its Specificity?
The universal selector (*) is a special type of CSS selector that matches any element in the document.

It is often used to apply a style to all elements on the page, which can be useful for resetting or normalizing styles across different browsers.

The universal selector can be used to select all elements within a specific context or globally across the entire document.

Here is an example of using the universal selector for setting the margin and padding for the entire HTML document:

Example Code
* {
  margin: 0;
  padding: 0;
}
In this code example, the * selector resets the margin and padding of all elements to zero, which is a common technique used in CSS resets.

The universal selector has the lowest specificity value of any selector. It contributes 0 to all parts of the specificity value (0, 0, 0, 0).

This means that any other selector, including type selectors, class selectors, ID selectors, and inline styles, will override the styles set by the universal selector.

Let's take a look at the following HTML and CSS example:

Example Code
<head>
  <style>
    * {
      color: blue;
    }
    p {
      color: red;
    }
    .highlight {
      color: green;
    }
    #unique {
      color: purple;
    }
  </style>
</head>
<body>
  <p id="unique" class="highlight">This text has multiple styles applied.</p>
</body>
The universal * selector sets the text color to blue for all elements.

However, the p type selector overrides this by setting the text color to red specifically for p elements.

If an element has the highlight class, the class selector takes precedence, changing the text color to green.

Finally, the #unique ID selector, which has the highest specificity, will override all others, setting the text color to purple.

## What Is the Specificity for Type Selectors?
Type selectors, also known as element selectors, target elements based on their tag name.

These selectors are fundamental in CSS and allow you to apply styles to all instances of a specific HTML element.

Type selectors are straightforward to use and are written simply as the tag name of the element you want to style.

Here is an example of a type selector targeting all paragraph elements on the page:

Example Code
p {
  color: blue;
}
In this example, all p elements will have their text color set to blue.

Type selectors have a relatively low specificity compared to other selectors. The specificity value for a type selector is (0, 0, 0, 1).

This means that type selectors will be overridden by class selectors, ID selectors, and inline styles, but can still apply styles unless those higher-specificity rules are present.

Let's take a look at an example where the class selectors will override the styles of the type selector.

Here is an example with two paragraph elements:

Example Code
<p class="para">I am a paragraph</p>
<p class="para">Here is another paragraph</p>
Both paragraph elements have a class called para.

Inside the CSS file, the type selector targets paragraphs, and the class selector targets elements with the para class.

Example Code
p {
  color: blue;
}

.para {
  color: red;
}
All paragraphs on the page with the class of para will have the text color set to red instead of blue because class selectors have a higher specificity than type selectors.

## What Is the Specificity for Class Selectors?
Class selectors are a key part of CSS, allowing developers to target multiple elements with the same class attribute and apply consistent styling.

This makes them highly versatile万用的 and efficient for applying styles across a website.

Class selectors are defined by a period (.) followed by the class name. They can be applied to any element in the HTML document.

Here is an example using a class selector:

Example Code
.highlight {
  color: green;
}
In this example, any element with the class highlight will have its text color set to green.

Class selectors have a higher specificity than type selectors but lower than ID selectors and inline styles.

The specificity value for a class selector is (0, 0, 1, 0). This means that class selectors can override type selectors, but they can be overridden by ID selectors and inline styles.

Class selectors can be combined with other selectors to create more specific rules.

Here is an example combining a paragraph type selector with a class selector:

Example Code
p.highlight {
  font-weight: bold;
}
This rule applies only to p elements that also have the highlight class, making their text bold.

## What Is the Specificity for ID Selectors?
ID selectors are among the most powerful selectors in CSS, allowing developers to apply styles to specific elements with unique identifiers.

This makes them highly effective for targeting individual elements that need unique styling.

ID selectors are defined by a hash symbol (#) followed by the ID name. They should be unique within an HTML document, meaning no two elements should share the same ID.

Here is an example using an ID selector:

Example Code
#unique {
  color: purple;
}
In this example, the element with the ID unique will have its text color set to purple.

ID selectors have a very high specificity, higher than type selectors and class selectors, but lower than inline styles. The specificity value for an ID selector is (0, 1, 0, 0).

This means that ID selectors can override class selectors and type selectors but can be overridden by inline styles.

## What Is the important Keyword, and What Are the Best Practices for Using It?
The !important keyword in CSS is used to give a style rule the highest priority, allowing it to override any other declarations for a property.

When used, it forces the browser to apply the specified style, regardless of the specificity of other selectors.

Let's say you have an HTML paragraph element with inline styles like this:

Example Code
<p class="para" style="background-color: lightblue; color: black;">
  This is a paragraph.
</p>
In this example, the paragraph element has a background color set to lightblue and a text color set to black.

The CSS file applies the following styles to the paragraph element:

Example Code
.para {
  background-color: black;
  color: white;
}
Since inline styles have a higher precedence than class, ID and type selectors, the black background color and white text color will not be applied to that paragraph element.

To override those inline styles, you can use the !important keyword like this:

Example Code
.para {
  background-color: black !important;
  color: white !important;
}
The !important keyword is used after the CSS value and before the semicolon.

Now the paragraph element will have those black and white colors applied because the inline styles are being overridden with the use of the !important keyword.

The !important keyword in CSS is used to give a style rule the highest priority, effectively overriding other declarations, including those with higher specificity and inline styles.

However, the !important keyword does not change the specificity of the CSS selector itself. It simply ensures that the rule with !important is applied, even if there are other conflicting rules with higher specificity.

Another appropriate use case for the !important keyword is to override styles from third-party libraries or frameworks when you do not have control over the original CSS.

However, overusing the !important keyword can lead to difficulties in maintaining and debugging your CSS, as it breaks the natural cascading of styles and can lead to unintended consequences.

So, it is best to use the !important keyword sparingly节约地.

## How Does the Cascade Algorithm Work at a High Level?
The Cascade Algorithm is the process the browser uses to decide which CSS rules to apply when there are multiple styles targeting the same element. It ensures that the most appropriate styles are used, based on a set of well-defined rules.

The process begins with relevance. The browser first filters all the CSS rules to find those that actually apply to the element in question. This includes matching selectors and considering media queries查询 that might be in effect.

A media query is a CSS technique used to apply styles based on the characteristics of the device or viewport, such as its width, height, or orientation.

Next, the algorithm considers origin and importance. CSS can come from different sources: the browser’s default styles (user-agent), styles set by the user, and styles written by the author (you).

Following the consideration of origin, the algorithm then evaluates the importance of each rule, giving priority to rules marked with !important, which override other rules regardless of their source.

After filtering by origin and importance, the algorithm looks at specificity. When two rules from the same origin and importance level apply, the rule with the higher specificity will be applied.

Specificity is a measure of how targeted a selector is, with more specific selectors taking precedence优先 over more general ones.

Finally, if everything else is equal, the order of appearance comes into play. When two rules have the same specificity, the one that appears last in the CSS will be applied.

This is why the order in which you write your styles can sometimes affect the outcome.

Let's take a look at an example.

Here we have a single paragraph element on the page:

Example Code
<p>example paragraph</p>
Inside the CSS, we have two rules each targeting the paragraph element.

Example Code
p {
  color: blue;
}

p {
  color: green; 
}
The first rule sets all paragraph elements to the text color of blue while the second rule sets all paragraph elements to the text color of green.

So which color will be applied? The color green will be applied to the paragraph elements.

By considering relevance, origin and importance, specificity, scope作用域, and order of appearance, the Cascade Algorithm ensures that your CSS behaves predictably, allowing you to design more complex and nuanced细致的 web pages.

## How Does Inheritance Work with CSS at a High Level?
Inheritance is a key concept in CSS that determines how styles are passed down from parent elements to their child elements.

Just like in the real world, where children often inherit traits特征 from their parents, in CSS, certain properties can be inherited by child elements from their parent elements.

This allows for a more efficient way to apply consistent styling across an entire document.

In CSS, not all properties are inherited by default. For example, properties like color, font-family, and line-height are inherited. This means that if you set the text color on a parent element, all of its child elements will inherit that color unless you specifically override it.

For instance, consider the following example where a parent div element has its color set using an inline style, and the child p element inherits that color:

Example Code
<div style="color: blue;">
  This is the parent element.
  <p>This is the child element inheriting the color.</p>
</div>
In this case, both the parent div and the child p will display their text in blue because the color is inherited.

On the other hand, properties like margin, padding, border, and background are not inherited by default. If you want a child element to inherit these styles, you need to explicitly set them, either directly on the child element or by using the inherit keyword.

The inherit keyword can be used to force inheritance of a property from a parent element, even if that property is not normally inherited.

For example, if you want a specific child element to have the same padding as its parent, you can set padding: inherit on the child element:

Example Code
<div style="padding: 20px;">
  This is the parent element with padding.
  <p style="padding: inherit;">This is the child element inheriting the padding.</p>
</div>
In this case, the child p element will inherit the 20px of padding from its parent div element.

Inheritance is especially useful for maintaining consistency and reducing redundancy冗余度 in your stylesheets.

Instead of writing the same style rule for multiple elements, you can define it once on a parent element, and the child elements will inherit it. This can make your CSS more concise and easier to manage.

However, it’s important to remember that inheritance only works in one direction – from parent to child. If you override a style on a child element, it won’t affect the parent element.

