# Styling Lists and Links

In these lectures, you will learn the properties you need to know to effectively style lists and links, including link states like link, visited, hover, and active.

## How Do You Space List Items Using margin or line-height?
Margins and line-height are essential for spacing list items to enhance readability and visual appeal.

First, let's start spacing list items using margins!

Margins can be used to create space between list items by applying margin properties to the li elements. This method allows you to control the spacing outside each list item, effectively increasing or decreasing the gap between them.

Let's take a look at an example of an unordered list with three list items.

<ul>
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
</ul>
By default, HTML will not apply that much spacing between the list items.

To apply some spacing to the bottom of each list item, you can use the margin-bottom property like this:

li {
  margin-bottom: 40px;
}
In this example, 40px of margin will be applied to the bottom of each list item inside the unordered list.

Another way to space out list items would be to use the line-height property.

The line-height property adjusts the vertical spacing between lines of text within a single list item.

While it primarily affects the spacing between lines of text within each item, it can also indirectly influence the overall spacing between list items if the items contain only a single line of text.

If list items have multiple lines of text, the line-height will affect the spacing between those lines, but it does not directly adjust the spacing between separate list items themselves.

To control the spacing between individual list items, you would use margin or padding properties instead.

Using the same unordered list from earlier, here is an example of applying line-height to the list items:

li {
  line-height: 2; 
}
In this example, line-height: 2; sets the line height to be twice the font size, creating more vertical space within each list item.

## How Do the Different list-style Properties Work?
In CSS, the list-style property is used to control the appearance of lists on a webpage.

Whether you're working with ordered lists (ol) or unordered lists (ul), the list-style property allows you to customize how list items are displayed.

The list-style property is actually a shorthand for three other properties:

list-style-type
list-style-position
list-style-image
Each one plays a different role in defining the appearance of lists.

The list-style-type property allows you to define the type of bullet项目符号 point or number used in a list.

For unordered lists, you can choose from several bullet styles, such as discs圆盘, circles, or squares.

For ordered lists, you can use different numbering systems, like decimal十进制数, Roman numerals, or even alphabetical characters.

Here’s an example of using list-style-type:

<ul style="list-style-type: square;">
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
</ul>
In this example, the bullet points of the unordered list are changed to squares.

The list-style-type property is the most commonly used of the three, as it directly affects the appearance of the bullet or numbering style in your lists.

The list-style-position property controls the position of the bullet or number in relation to the list item’s content. There are two values you can use: inside and outside.

When you use the value outside, the bullet or number appears outside the content, which is the default behavior.

And, when you use the value inside, the bullet or number appears inside the content, which may cause the text to wrap and align with the bullet or number.

Here’s an example of using list-style-position:

<ul style="list-style-position: inside;">
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
</ul>
<ul style="list-style-position: outside;">
  <li>Item 4</li>
  <li>Item 5</li>
  <li>Item 6</li>
</ul>
In this example, both inside and outside values are provided for two different unordered list tags.

The list-style-position property can be useful when you want to control the alignment of the list content, especially in situations where you have multiple lines of text in a single list item.

The list-style-image property allows you to use an image as the bullet point for your list items. This can be useful for adding a unique visual style to your lists.

Here’s an example of using list-style-image:

<head>
  <style>
    ul {
      list-style-image: url('freeCodeCamp-logo.svg');
      list-style-position: inside;
    }
  </style>
</head>
<body>
  <ul>
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
  </ul>
</body>
In this example, the bullet points are replaced by a custom freeCodeCamp logo, adding a personalized touch to the list.

When using list-style-image, make sure the image you choose is small and appropriate for the design of your webpage. If the image is too large or complex, it can make the list harder to read.

You can combine the three properties – list-style-type, list-style-position, and list-style-image – into a single list-style shorthand property.

The order of the values in the shorthand doesn’t matter, but all three can be specified together.

Here’s an example using the shorthand property:

<ul style="list-style: square inside url('https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg');">
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
</ul>
In this example, the list items use square bullets, positioned inside the content, with a custom image as the bullet.

However, if the image is unavailable or not rendered, the square bullets will be used as a fallback.

## Why Are Default Link Styles Important for Usability on the Web?
Default link styles play a crucial role in enhancing usability and accessibility on the web.

These styles, typically blue for unvisited links and purple for visited links, have become a standard that users have come to expect and rely on when navigating websites.

The primary purpose of default link styles is to provide clear visual cues that help users distinguish between interactive and non-interactive elements on a webpage.

This distinction is fundamental to creating an intuitive直观的 and user-friendly browsing experience.

Let's consider the basic default styles for links:

a:link {
  color: blue;
  text-decoration: underline;
}

a:visited {
  color: purple;
}
These styles serve several important functions.

Firstly, the blue color for unvisited links stands out against most background colors and text, making links easily identifiable. This contrast is crucial for users to quickly scan a page and find navigational elements or important information.

The underline further emphasizes that the text is clickable, providing an additional visual cue. This is particularly helpful for users who may be colorblind or have difficulty distinguishing colors.

The change in color for visited links (typically to purple) helps users keep track of where they've been. This feature is invaluable for navigating large websites or conducting research, as it prevents users from inadvertently revisiting the same pages.

Consider this HTML example:

<p>Learn more about <a href="https://www.example.com/cats">cats</a> and <a href="https://www.example.com/dogs">dogs</a>.</p>
Without any custom CSS, most browsers will render these links in blue with an underline. After clicking on one of the links, its color will change to purple, providing immediate feedback to the user about their browsing history.

While it's common for designers to modify these default styles to match a website's aesthetic, it's crucial to maintain the core principles behind them.

If you choose to change the default styles, ensure that links are still clearly distinguishable from regular text, there's a visible difference between visited and unvisited links, and the chosen colors provide sufficient contrast with the background.

For example, you might use a custom style like this:

a:link {
  color: blue;
  text-decoration: none;
  border-bottom: 1px solid blue;
}

a:visited {
  color: purple;
  border-bottom: 1px solid purple;
}
This maintains the blue and purple color scheme while replacing the underline with a bottom border for a more modern look.

It's also important to consider the different states of links. In addition to the default and visited states, links typically have hover and active states:

a:hover {
  color: red;
}

a:active {
  color: darkorange;
}
These states provide immediate feedback to users as they interact with links, enhancing the overall usability of the site.

In conclusion, while it's possible to customize link styles, the principles behind the default styles should be maintained.

They play a crucial role in creating a usable and accessible web experience, helping users navigate and interact with content effectively.

Always prioritize clarity and user experience when designing link styles for your websites.

## How Do You Style the Different Link States?
There are different states of a link, including link, visited, hover, focus, and active. These states are important for helping users recognize links and providing clear feedback after interactions, which improves both usability and accessibility.

Styling these different link states is crucial for usability and accessibility, as it provides visual cues about the current state of the link. This helps users understand which links they have visited, which link they are interacting with, and what will happen when they click.

For users with visual impairments or cognitive disabilities, these distinct styles can make navigation much easier and more intuitive.

Additionally, clear link states enhance the overall user experience by providing immediate feedback on user interactions, reducing confusion and improving the site's navigability.

These states can be styled using something called pseudo-classes in CSS.

A pseudo-class is a keyword added to a selector that specifies a special state of the selected element.

For example, :hover can change a button's color when the user's pointer hovers over it, while :visited can change the color of a link that has already been visited.

Pseudo-classes allow you to style elements based on their state or the user's interaction with them, without the need for additional markup in your HTML.

The syntax of a pseudo-class looks something like this where A is the selector and :B is the pseudo-class:

A:B {
  property: value;
}
To better understand how to style the different link states, let's take a look at some examples.

The :link pseudo-class styles unvisited links, indicating that they are clickable.

Here is an example of targeting an anchor element and using the :link pseudo-class:

/* Normal state (unvisited link) */
a:link { 
  color: red;
}
The above example will change the link's default blue color to red when it is unvisited.

:visited styles links that have already been visited or clicked, helping users track which links they have clicked before. Here’s an example usage of :visited pseudo-class:

/* Visited link */
a:visited {
  color: green;
}
This code will color the link to green when it is clicked.

:hover changes the link's style when the user hovers over it, providing a visual cue that the link is interactive. Here’s an example usage of :hover pseudo-class:

/* Hover state */
a:hover {
  color: yellow;
}
This code will color the links to yellow when mouse is hovered over it.

:focus adds styles around the link when it is focused, such as when navigating with a keyboard, or enhancing accessibility.

Here is an example using the outline property to apply a solid orange outline when the link is focused.

/* Focus state */
a:focus {
  outline: 2px solid orange;
}
:active changes the link's styles while the link is being clicked, providing immediate feedback to the user that their action is being registered. Here’s an example usage of :active pseudo-class:

/* Active state */
a:active {
  color: pink;
}
This code example will make the link to pink color immediately when the link is clicked.

