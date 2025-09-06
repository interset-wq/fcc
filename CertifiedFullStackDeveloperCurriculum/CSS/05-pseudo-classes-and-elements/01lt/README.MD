# Working with Pseudo-Classes and Pseudo-Elements in CSS
In these lectures, you will learn about pseudo-classes and pseudo-elements, alongside their examples and how they work.

## What Are Pseudo-classes, and How Do They Work?
Pseudo-classes are special CSS keywords that allow you to select an element based on its specific state or position. The element's state or position could include:

When it's active.
When it's being hovered over by a mouse.
When it's the first child of a parent.
When it's the last child of a parent.
When a link has been visited.
When it's disabled.
To use a pseudo-class, you add it to the selector by using a colon (:) followed by the name of the pseudo-class:

selector:pseudo-class {
  /* CSS properties */
}
Let's see how you can use a pseudo-class to represent each of the states and positions we already mentioned.

The :active pseudo-class lets you select the active state of an element, like clicking on a button:

button:active {
  background: greenyellow;
}
The :hover pseudo-class defines the hover state of an element. An example would be hovering over a button or link:

a:hover {
  text-decoration: none;
  background: crimson;
}
The :first-child pseudo-class selects an element that is the first child of its parent element. Here's an HTML example showing a div element containing multiple paragraph elements:

<div class="container">
  <p>first child</p>
  <p>second child</p>
  <p>third child</p>
  <p>last child</p>
</div>
Here's the CSS that selects the first paragraph element in that div container:

.container p:first-child {
  background: lightcoral;
  padding: 0.4rem;
}
The first paragraph element in that div will receive the lightcoral background color and padding of 0.4rem on all four sides.

The :last-child pseudo-class targets the last element that is the child of its parent. Here is an example of targeting the last paragraph element in the container div element:

.container p:last-child {
  background: lightcoral;
  padding: 0.4rem;
}
The :visited pseudo-class lets you style a link the user has already visited:

a:visited {
  color: purple;
}
The :disabled pseudo-class lets you style an interactive element in disabled mode:

button:disabled {
  background-color: lightgray;  
}
As you can see, pseudo-classes let you style elements based on user interactions, like hovering or visiting a link. This makes your website feel more interactive.

Apart from the pseudo-classes already mentioned, there are others like:

:focus
:first-of-type
:last-of-type
:nth-of-type
:modal
:enabled
:checked
:required, and more.

## What Are Examples of Element User Action Pseudo-classes?
User feedback is a crucial element of web design. For instance, it's important for users to receive visual cues when they interact with elements on a website, such as hovering over a button or clicking a link. This feedback helps users understand the state of interactive elements, like indicating whether a link has been visited or not.

User action pseudo-classes in CSS are special keywords that allow you to provide this kind of feedback without needing JavaScript or other programming languages.

These pseudo-classes include :hover, :active, :focus, and :visited, among others. They enable you to change the appearance of elements based on user interactions, improving the overall user experience.

Let's dive into some of the user action pseudo-classes we have and see how they work.

The :active pseudo-class applies styles when an element is activated by the user. For example, when the user clicks a button or a link, it provides immediate visual feedback, showing users that their actions are being recognized.

a:active {
  color: crimson;
}
The :hover pseudo-class is triggered when a user hovers over an element with their mouse or other pointing device. Developers often use it to create visual feedback for buttons, links, or any element that should respond to user attention. Here's a button a user would hover over before clicking:

<button class="btn">Hover Over Me</button>
Here's the CSS that changes the color, background color, and cursor of the button once the user hovers over it:

.btn:hover {
  background-color: darkgreen;
  color: white;
  cursor: pointer;
}
The :focus pseudo-class applies styles when an element gains focus, typically through keyboard navigation or when a user clicks into a form input. This is not just for feedback but also crucial for accessibility. It ensures that users who rely heavily on keyboards can easily identify which element they are interacting with.

Here's an input element inside a form element:

<form>
  <input type="text" />
</form>
Here's the CSS that gives the input a solid dark green border and a border-radius when the user clicks into it:

input:focus {
  outline: 2px solid darkgreen;
  border-radius: 4px;
}
The :visited pseudo-class targets a link the user has visited. This can be useful for helping users distinguish between pages they have already visited and the ones they are yet to visit. Here is an example of changing the anchor text color to cyan when the link is visited:

a:visited {
  color: cyan;
}
The :checked pseudo-class in CSS allows you to style form elements such as checkboxes and radio buttons when they are selected (checked). This pseudo-class is useful for customizing the appearance of these elements to enhance user experience, even though browsers provide default styles for them.

Here's the kind of checkbox you usually check to agree to terms on a website:

<form>
  Agree <input class="checkbox" type="checkbox" />
</form>
Here's how you can use the :checked pseudo-class to indicate to the user that it is checked:

.checkbox:checked {
  appearance: none;
  width: 12px;
  height: 12px;
  background-color: red;
}
In this example, we are using the appearance property set to none to remove the default styling applied by the browser to checkbox inputs. When the user checks the box, it will have a background color of red.

Other examples of action pseudo-classes are:

:focus-within: for applying styles to an element when it or any of its descendants have focus.
:enabled: for targeting form buttons or other elements that are currently enabled.
:disabled: for targeting form buttons or other elements that are disabled.
:target: for applying styles to an element that is the target of a URL fragment片段 (the part of a URL after the # symbol).

## What Are Examples of Input Pseudo-classes?
The appearance and behavior of input elements matter when building web forms. A form with inputs that respond to user actions goes a long way in improving user experience, and it should not cause confusion or frustration.

CSS provides several input pseudo-classes that can make your forms more intuitive and user-friendly. Let's look at these pseudo-classes in detail.

The :focus pseudo-class allows you to target an input element when a user selects or clicks on it, drawing attention to the active input field. This helps users easily identify where they're currently typing:

input:focus {
  border: 2px solid crimson;
  outline: none;
}
As the name implies, the :hover pseudo-class is triggered when the user places the cursor over an element. It provides visual feedback before the user interacts with the input, effectively alerting them that the input is ready for action.

input:hover {
  background-color: orange;
}
In the example above, the input element background changes to an orange color when the user hovers over it, letting them know that the field is ready for interaction.

The :checked pseudo-class lets you style a radio button or checkbox differently when a user selects it. This way, the user can easily see which option they've chosen.

Here is an example:

<form>
  I have read the terms<input class="checkbox" type="checkbox">
</form>
.checkbox:checked {
  appearance: none;
  width: 12px;
  height: 12px;
  background-color: coral;
}
:required targets input elements that have the required attribute. It signals to the user that they must fill out the field to submit the form.

The HTML below has a form with two required input elements:

<form action="#">
  <label for="name">Name:</label>
  <input type="text" id="name" name="name" required />

  <label for="email">Email:</label>
  <input type="email" id="email" name="email" required />

  <label for="phone">Phone Number:</label>
  <input type="tel" id="phone" name="phone" />

  <button type="submit">Submit</button>
</form>
And this CSS applies an orange border of two pixels to the two required inputs:

input:required {
  border: 2px solid orange;
}
When validating forms, you can use the :valid pseudo-class to style the input fields that meet the validation criteria, and :invalid to style the input fields that do not meet the criteria. Typically, you will use green for a valid input and red for an invalid input.

Here is an example using the :valid pseudo-class:

input:valid {
  border-color: green;
}
Here is an example of using the :invalid pseudo-class:

input:invalid {
  border-color: crimson;
}
The :disabled pseudo-class allows you to select and style input elements that are disabled. These elements have the disabled attribute, which prevents users from interacting with them. When an input is disabled, it cannot be clicked, focused, or edited.

Here is an example of a label and a disabled input element:

<label for="name">Name:</label>
<input class="text-input" type="text" id="name" name="name" disabled />
In the CSS, we are targeting that disabled input and giving it a background color of lightgray and changing the cursor pointer to not-allowed.

.text-input:disabled {
  background-color: lightgray;
  cursor: not-allowed;
}
The cursor: not-allowed; CSS property value changes the appearance of the cursor to indicate that an action is not permitted.

When applied to an element, it shows a cursor with a circle-slash symbol (usually a circle with a diagonal line对角线 through it) to signal to users that the element is not interactive or cannot be clicked or interacted with.

Here are some other examples of input pseudo-classes and what they do:

:autofill: applies styles to input fields that the browser automatically fills with saved data.
:optional: styles input elements that are not required and can be left empty.
:in-range and :out-of-range: style elements based on whether their values are within or outside specified range constraints.

## What Are Examples of Location Pseudo-classes?
Location pseudo-classes are used for styling links and elements that are targeted within the current document. They offer a way to apply styles based on whether a link is visited or whether an element is currently in focus.

Examples of location pseudo-classes are:

:link
:visited
:any-link
:local-link
:target
:target-within
Let's take a deeper look at each of these pseudo-classes.

The :link pseudo-class allows you to target all unvisited links on a webpage. You can use it to style links differently before the user clicks on them. For example, you might want to make all unvisited links blue or your website's primary color:

a:link {
  color: magenta;
}
In this case, any link the user hasn't clicked yet will appear magenta洋红色. Once the user clicks the link, the :link style no longer applies, and the :visited pseudo-class takes over. The :visited pseudo-class comes into play after the user clicks the link, so you can use it to target links the user has already clicked.

Here is an example of changing the visited link state to the color purple:

a:visited {
  color: purple;
}
The :visited pseudo-class helps users distinguish between links they have visited and those they have not.

The :any-link pseudo-class is a combination of the :link and :visited pseudo-classes. So it matches any anchor element with an href attribute, regardless of whether it's visited or not.

Here is an example of changing the link color for the :any-link pseudo-class to crimson:

a:any-link {
  color: crimson;
}
The :local-link pseudo-class targets links that point to the same document. It can be useful when you want to differentiate internal links from external ones. Currently, no browser supports the :local-link pseudo-class.

The :target pseudo-class selects an element that matches the current URL fragment identifier, for example, #section1. It's very useful for pages with in-page navigation.

Here's an HTML example that represents an in-page navigation:

<nav id="table-of-contents">
  <ul>
    <li><a href="#section1">Introduction</a></li>
    <li><a href="#section2">Features</a></li>
  </ul>
</nav>

<section id="section1">
  <h2>Introduction</h2>
  <p>This is the introduction section.</p>
</section>

<section id="section2">
  <h2>Features</h2>
  <p>This section describes the features.</p>
</section>
Here's the CSS that uses the :target pseudo-class to style the section that matches where the user navigates to:

section:target {
  background-color: green;
  border: 2px solid green;
  padding: 10px;
}
When the user clicks on one of the navigation links, the background color for that respective section will change to green.

## What Are Examples of Tree-structural Pseudo-classes?
Tree-structural pseudo-classes allow you to target and style elements based on their position within the document tree. The document tree refers to the hierarchical structure of elements in an HTML document.

Here is a list of tree-structural pseudo-classes:

:root
:empty
:nth-child(n)
:nth-last-child(n)
:first-child
:last-child
:only-child
:nth-of-type
:first-of-type
:last-of-type
:only-of-type
Let's take a closer look at each of the tree-structural pseudo-classes, accompanied by examples.

​​The :root pseudo-class is usually the root html element. It helps you target the highest level in the document so you can apply a common style to the entire document.

:root {
  background: black;
  color: aliceblue;
}
The :root pseudo-class is also commonly used in setting CSS variables:

:root {
  --main-font: 'Arial, sans-serif';
  --primary-color: blue; 
  --secondary-color: green; 
}
With CSS variables, you get to store values and reuse them in your stylesheet. You will learn more about these later on.

Empty elements, that is, elements with no children other than white space, are also included in the document tree. That's why there's an :empty pseudo-class to target empty elements. For example, this HTML code has two empty list items:

<ul>
  <li>Item 1</li>
  <li></li> <!-- This list is empty -->
  <li>Item 2</li>
  <li></li> <!-- Another empty list -->
  <li>Item 3</li>
</ul>
With the :empty pseudo-class, you can style the empty list items differently:

:empty {
  background: black;
}
The most practical thing to do with the empty list items is probably not displaying them at all:

:empty {
  display: none;
}
:nth-child(n) allows you to select elements based on their position within a parent, while :nth-last-child(n) enables you to select elements by counting from the end. The n can be a specific number or a keyword like odd or even. This is incredibly useful in styling table cells based on position: even and odd.

Here's an HTML example of a fruit price list table:

<table>
  <tr>
    <th>Item</th>
    <th>Price</th>
  </tr>
  <tr>
    <td>Apple</td>
    <td>$1.00</td>
  </tr>
  <tr>
    <td>Banana</td>
    <td>$0.50</td>
  </tr>
  <tr>
    <td>Orange</td>
    <td>$0.80</td>
  </tr>
</table>
Here's the CSS using the :nth-child pseudo-class to target the table cells based on odd and even positions:

th,
td {
  border: 1px solid lightgray;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: orangered;
}

tr:nth-child(odd) {
  background-color: lightgreen;
}
The :first-child, :last-child, and :only-child pseudo-classes all act on items within a parent container or the entire document.

:first-child selects the first element in a parent element or the document.
:last-child selects the last element in a parent element or the document.
:only-child selects the only element in a parent element or the document.
Using the :first-child and :last-child pseudo-classes will select both Item 1 and Item 3 in this HTML:

<ul>
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
</ul>
Here's the CSS:

li:first-child {
  background-color: orangered;
}

li:last-child {
  background-color: lightgreen;
}
If you have more unordered lists on the page, you have to be more specific with the selection:

ul li:first-child {
  background-color: orangered;
}

ul li:last-child {
  background-color: lightgreen;
}
To show you how the :only-child pseudo-class works, here's an HTML example with two separate div elements:

<div class="container">
  <div>This is the only item in this container.</div>
</div>

<div class="container">
  <div>This is one of two items in this container.</div>
  <div>Here is the second item.</div>
</div>
Using the :only-child pseudo-class ensures only the div element with a single child is selected:

.container div:only-child {
  border: 2px solid crimson;
  padding: 10px;
  background-color: lightblue;
}
The :first-of-type and :last-of-type pseudo-classes select the first and last occurrence of a specific element type within its parent. They are useful for applying unique styles to the first or last instance of that element type among its siblings.

In the HTML below, :first-of-type and :last-of-type applies to the first element and last element within the section element:

<section>
  <h2>Introduction</h2>
  <p>This is the first paragraph in the first section</p>
  <p>This is the second paragraph in the first section</p>
</section>
<section>
  <h2>Details</h2>
  <p>This is the first paragraph in the second section.</p>
  <p>This is the second paragraph in the second section.</p>
</section>
Here's the CSS:

section p:first-of-type {
  background-color: lightgreen;
}

section p:last-of-type {
  background-color:lightblue;
}
:nth-of-type(n) allows you to select a specific element within its parent based on its position among siblings of the same type. For instance, in the HTML below, :nth-of-type(2) targets the second element in the container:

<div class="container">
  <p>First paragraph</p>
  <h2>First heading</h2>
  <p>Second paragraph</p>
  <p>Third paragraph</p>
  <h2>Second heading</h2>
</div>
Here's the CSS:

p:nth-of-type(2) {
  color: red;
  font-weight: bold;
}
:only-of-type selects an element if it's the only one of its type within its parent. This can be useful for emphasizing single items or ensuring that they are styled differently when they’re not part of a group.

In the HTML below, there are two div elements with one having a single element:

<div class="container">
  <p>The only paragraph</p>
</div>

<div class="container">
  <p>The first paragraph</p>
  <p>The second paragraph</p>
</div>
Here's the CSS that only applies to the first container:

p:only-of-type {
  border: 4px solid green;
}

## What Are Examples of Functional Pseudo-classes?
Functional pseudo-classes allow you to select elements based on more complex conditions or relationships. Unlike regular pseudo-classes which target elements based on a state, for example, :hover, :focus, functional pseudo-classes accept arguments within parentheses, hence the name "functional pseudo-classes".

Examples of functional pseudo-classes are:

:is()
:where()
:has()
:not()
Let's take a deeper look at each of these functional pseudo-classes with examples.

The :is() pseudo-class is useful when you want to style a group of elements that share some, but not all, characteristics. For example, you might want to style different types of buttons on your website, including button elements, links styled as buttons, and input elements with types submit and reset. Here's an HTML example representing that:

<button>Click Me</button>
<a href="#" class="button">Click Me Too</a>
<input type="submit" value="Submit" />
<input type="reset" value="Reset" />
Without the :is() function, you would have to write a complex selector like this:

button,
a.button,
input[type='submit'],
input[type='reset'] {
  background-color: darkblue;
  color: white;
  border: 1px solid darkblue;
  padding: 10px 20px;
  text-decoration: none;
  border-radius: 5px;
  cursor: pointer;
  display: inline-block;
  margin: 5px;
  font-size: 16px;
  text-align: center;
}

button:hover,
a.button:hover,
input[type='submit']:hover,
input[type='reset']:hover {
  background-color: lightblue;
  border-color: lightblue;
}
With the :is() function, you can write a more compact and understandable selector like this:

:is(button, a.button, input[type='submit'], input[type='reset']) {
  background-color: darkblue;
  color: white;
  border: 1px solid darkblue;
  padding: 10px 20px;
  text-decoration: none;
  border-radius: 5px;
  cursor: pointer;
  display: inline-block;
  margin: 5px;
  font-size: 16px;
  text-align: center;
}

:is(button, a.button, input[type='submit'], input[type='reset']):hover {
  background-color: blue;
  border-color: blue;
}
The :where() pseudo-class functions similarly to :is(), but it doesn't increase the specificity of your selectors. This makes it ideal for applying styles without affecting the specificity of other rules.

For example, you can use the :where() function to apply zero margin and padding to heading elements. This ensures that the reset won't interfere with more specific styles you might apply later. Here's the HTML for that:

<h1>Page Title</h1>
<h2>Subtitle</h2>
<h3>A point</h3>
And this is the CSS:

:where(h1, h2, h3) {
  margin: 0;
  padding: 0;
}
Styling a parent element based on its children's states was previously challenging until the :has() pseudo-class was introduced. It allows you to apply styles to a parent element based on the presence or state of its child elements.

For example, the CSS below will only apply to any article element that has an h2 in it:

article:has(h2) {
  border: 2px solid hotpink;
}
Here's the HTML for that:

<article>
  <h2>Subheading</h2>
  <p>Lorem ipsum dolor sit amet.</p>
</article>

<article>
  <h3>A point</h3>
  <p>Lorem ipsum dolor sit amet.</p>
  <p>Lorem ipsum dolor sit amet.</p>
</article>
The :not() pseudo-class is ideal for situations where you want to apply styles to a group of elements, excluding one or more specific exceptions. In the CSS below, any button that is not a primary button will have a grey background:

button {
  padding: 10px 20px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  border: none;
  color: white;
}

button.primary {
  background-color: deepskyblue;
}

button:not(.primary) {
  background-color: grey;
}
Here's the HTML for the buttons:

<button class="primary">Primary Button</button>
<button class="secondary">Secondary Button</button>
<button class="danger">Another Secondary Button</button>

## What Are Pseudo-elements, and How Do They Work?
One of the most interesting aspects of CSS is the use of pseudo-elements. In this context, "pseudo" means "not real", so pseudo-elements are virtual or synthetic合成的 elements that don't directly match any actual HTML elements. They allow you to style specific parts of an element or insert content without adding extra HTML.

To apply a pseudo-element, attach it to the original element's selector using a double colon (::). Note that the selector can be any type, such as a class or ID selector. Here's what the basic syntax of pseudo-elements looks like:

selector::pseudo-element {
  property: value;
}
This double colon is what distinguishes pseudo-elements from pseudo-classes, which use a single colon.

Pseudo-elements allow you to style specific parts of an element's content or insert content before or after it, but they cannot exist independently. The element to which a pseudo-element is attached is called its originating element.

Let's start by looking at examples for the ::before and ::after pseudo-elements. As their names suggest, ::before lets you insert content just before the element's content while ::after lets you insert content after it.

Here is an example of a button element:

<button class="cta-button">Learn More</button>
In the CSS, we will use absolute positioning and the ::before pseudo-element to add a star before the button's Learn More text. You will learn more about absolute positioning in future lectures.

.cta-button {
  background-color: lightseagreen;
  color: white;
  border: none;
  padding: 10px 20px;
  cursor: pointer;
  position: relative;
}

.cta-button::before {
  content: "⭐";
  position: absolute;
  left: 3px;
  top: 8px;
  font-size: 0.75rem;
}
The content property is used to represent the content you wish to add before the button text. In this example, we are adding a star. You'll notice that you can not only insert content but also style it. Here's an example of the ::after pseudo-element with the same button:

.cta-button {
  background-color: orange;
  border: none;
  padding: 10px 30px;
  cursor: pointer;
  position: relative;
}

.cta-button::after {
  content: '➡️';
  position: absolute;
  right: 5px;
  bottom: 6px;
  font-size: 1.125rem;
  transition: transform 0.3s ease;
}
In the ::after pseudo-element, the transition property is used to animate changes over 0.3 seconds with an easing effect, creating a smooth and gradual transformation rather than a sudden one. You will learn more about the transition property in future lectures.

You can also attach a pseudo-class to the content you insert into another content with the ::before and ::after pseudo-elements. For example, a hover state for the content. Here's an example:

.cta-button {
  background-color: orange;
  border: none;
  padding: 10px 30px;
  cursor: pointer;
  position: relative;
}

.cta-button::after {
  content: "➡️";
  position: absolute;
  right: 5px;
  bottom: 6px;
  font-size: 1.125rem;
  transition: transform 0.3s ease;
}

.cta-button:hover::after {
  transform: translateX(2px);
}
With transform: translateX(2px) in the hover state, the content gets pushed to the right by 2px any time the user hovers on the button. The transition property in the ::after itself ensures the process takes 0.3s.

That's what the transform property does – it allows you to rotate旋转, skew偏移, scale, or translate平移 an element in a particular direction. You will learn more about that in future lectures.

In the next example, we will look at the ::first-letter pseudo-element. The ::first-letter pseudo-element targets the first letter of an element's content, allowing you to style it. Here's an example of some paragraph text:

<p>freeCodeCamp lets you learn to code without having to pay.</p>
If we want to style the first letter, we can use the ::first-letter pseudo-element like this:

p::first-letter {
  font-size: 4rem;
}
In the last example, we will look at is the ::marker pseudo-element which lets you select the marker, bullet or numbering of list items for styling. The ::marker pseudo-element offers a way to enhance your website's brand identity by customizing list markers to match your color scheme.

Here's an example of an unordered list and an ordered list:

<ul>
  <li>Unordered list item 1</li>
  <li>Unordered list item 2</li>
  <li>Unordered list item 3</li>
  <li>Unordered list item 4</li>
</ul>

<ol>
  <li>Ordered list item 1</li>
  <li>Ordered list item 2</li>
  <li>Ordered list item 3</li>
  <li>Ordered list item 4</li>
</ol>
To change the list item's marker color and size, you can use the ::marker pseudo-element like this:

li::marker {
  color: crimson;
  font-size: 1.5em;
  font-weight: bold;
}
In this lecture, we have covered only a few pseudo-elements. But there are many more like the ::placeholder, ::spelling-error and ::selection that I encourage you to explore on your own.

