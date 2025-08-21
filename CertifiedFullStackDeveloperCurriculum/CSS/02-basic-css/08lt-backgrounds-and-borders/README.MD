# Working with Backgrounds and Borders

In these lectures, you will learn about the properties and values you need to know to style backgrounds and borders of elements, alongside the accessibility considerations for backgrounds.

## How Do Background Image Size, Repeat, Position, and Attachment Work?
When working with background images in CSS, you have several properties at your disposal to control how these images are displayed.

The main properties we'll focus on are background-size, background-repeat, background-position, and background-attachment.

Let’s first take a look at the background-image property:

body {
  background-image: url("https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg");
}
The above CSS sets a cat background image for the body element.

If you want to set the size for the background image, you can use the background-size property.

You can use contain to scale the image as large as possible without cropping or stretching.

Here's an example with background-size: contain:

body {
  background-image: url("https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg");
  background-size: contain;
  min-height: 100px;
}
We are setting the min-height to 100px so the background image is visible and the layout maintains a baseline height, ensuring that even with minimal content, the design appears balanced and visually appealing.

If we change the background-size property to use the cover value, then the background image will scale to cover the entire body element while maintaining its 外观 ratio比例.

body {
  background-image: url("https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg");
  background-size: cover;
  min-height: 100px;
}
In the previous examples, you probably noticed that the background image would continuously repeat.

By default, background images repeat both horizontally and vertically to fill the entire element. However, you can control this behavior.

You can use the background-repeat property with the value set to no-repeat.

body {
  background-image: url("https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg");
  background-size: contain;
  background-repeat: no-repeat;
  min-height: 100px;
}
With the background-size set to contain and the background-repeat set to no-repeat, the image will no longer repeat on the screen.

If you wanted to repeat the background image horizontally, you can use the repeat-x value for the background-repeat property.

body {
  background-image: url("https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg");
  background-size: contain;
  background-repeat: repeat-x;
  min-height: 100px;
}
If you wanted to repeat the background image vertically, you can use the repeat-y value for the background-repeat property.

body {
  background-image: url("https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg");
  background-size: contain;
  background-repeat: repeat-y;
  min-height: 100px;
}
To position a background image on the screen, you can use the background-position property.

The background-position property allows you to set where in the element the background image appears. You can use keywords like top, bottom, left, right, and center, or specific pixel or percentage values.

Here is an example using the center and top for the background-position:

body {
  background-image: url("https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg");
  background-size: contain;
  background-repeat: no-repeat;
  background-position: center top;
  min-height: 100px;
}
This CSS code positions the background image at the center of the element horizontally and at the top vertically.

Lastly, background-attachment determines whether the background image scrolls with the content or remains fixed when the page is scrolled.

The main values are scroll (default), where the background image scrolls with the content, and fixed, where the background image stays in the same position on the screen.

Here is an example using the fixed value for the background-attachment property:

body {
  background-image: url("https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg");
  background-position: center top;
  background-attachment: fixed;
}
This CSS code sets the background image to remain fixed in place even when the page is scrolled.

If you wanted to combine a few of the properties into one line, you can do that by using the shorthand background property.

Here is an example:

body {
  background: center top fixed
    url("https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg");
}
The above example combines the background-image, background-position, and background-attachment into a single line.

By mastering these properties, you'll have great control over how background images are displayed in your web designs, allowing for more visually appealing and functional layouts.

## What Is a Background Gradient渐变色, and How Does It Work?
A background gradient in CSS is a smooth transition between two or more colors that can be applied to the background of an element. Gradients allow you to create visually appealing backgrounds without needing images.

There are two main types of gradients in CSS: linear gradients and radial辐射状的 gradients.

A linear gradient transitions colors along a straight line. You can define the direction and the colors involved.

Here is the basic syntax:

background: linear-gradient(direction, color-stop1, color-stop2, ...);
In this example, we are using the background CSS property with a value of the linear gradient.

The direction specifies the direction of the gradient. It can be an angle (such as 45deg), a keyword (such as to right, to bottom), or a side/corner.

color-stop specifies the colors and positions where the gradient transitions occur.

To better understand how linear gradients work, let's take a look at the following example:

.linear-gradient{
  background: linear-gradient(to right, red, yellow);
  height: 40vh;
}
This CSS creates a linear gradient that transitions from red on the left to yellow on the right. The gradient is applied to an element with a height of 40% of the viewport height. You'll learn more about vh units in a future lecture.

The to right direction means the gradient runs horizontally from left to right.

Another type of gradient would be the radial gradient.

A radial gradient transitions colors radiating from an origin (usually the center) outward in a circular or elliptical椭圆形的 shape.

Here is the basic syntax:

background: radial-gradient(shape size at position, color-stop1, color-stop2, ...)
On the syntax, the shape specifies the shape of gradient which could be circle or ellipse.

The size determines the size of the gradient's ending shape which could be closest-side, closest-corner, farthest-side, farthest-corner, contain, or cover.

position determines the position of the gradient's center which could be specified using keywords (such as center, top left, bottom right) or precise values (such as 50% 50%, 10px 20px).

Lastly, color stops are a list of colors that the gradient transitions through. Each color stop can optionally include a position value (percentage or length) indicating where the color should be placed.

An example would be:

.radial-gradient{
  background: radial-gradient(circle closest-side at center, red, yellow 50%, green);
  height: 60vh;
}
This CSS creates a circular radial gradient centered in the element. It starts with red at the center, transitions to yellow at 50% of the radius, and ends with green.

The closest-side keyword makes the gradient's ending shape fit the closest side of the element. The gradient is applied to an element with a height of 60% of the viewport height.

Understanding how to work with CSS gradients can significantly enhance your designs by providing visually appealing backgrounds without the need for images.

With options like linear gradients for smooth transitions and radial gradients for circular effects, they offer both flexibility and creativity in web design.

## What Are Some Accessibility Considerations for Backgrounds?
In web design, backgrounds play a vital role in defining the overall look and feel of a webpage.

However, when designing with backgrounds, it's crucial to consider accessibility to ensure your content is usable and readable by all users, including those with visual impairments.

One of the primary accessibility concerns related to backgrounds is ensuring that there is sufficient contrast between the background and the text.

Without adequate contrast, users with visual impairments, including those with low vision or color blindness, may struggle to read the content on your page.

Contrast refers to the difference in lightness or darkness between two colors. Sufficient contrast between the background color and the text color is essential for readability.

The Web Content Accessibility Guidelines (WCAG) recommend a minimum contrast ratio of 4.5:1 for normal text and 3:1 for large text.

For example, placing white text on a light-gray background would result in poor contrast, making the text difficult to read. However, white text on a dark-blue background would provide good contrast, enhancing readability for all users.

Here’s an example of poor contrast:

<p style="color: lightgray; background-color: whitesmoke;">
   This is an example of poor contrast.
</p>
Now, here’s an example of good contrast:

<p style="color: white; background-color: darkslategray;">
  This is an example of good contrast.
</p>
Another consideration is avoiding placing text over busy or complex backgrounds, such as images or gradients with multiple colors. Busy backgrounds can make it hard to distinguish the text from the background, regardless of the contrast.

If you must use a background image, it’s a good idea to apply a semi-transparent半透明的 overlay重叠 or a solid color behind the text to make it more readable. Here's an example of how you can do this:

.background-image-text {
  background-image: url('fcc-logo.svg');
  color: white;
  padding: 20px;
  background-color: rgba(0, 0, 0, 0.75);
}
This code places a semi-transparent black overlay behind the text, improving its readability against the background image.

When designing backgrounds, avoid using color as the sole means of conveying information. For example, using just color to indicate an error or success message (such as red for error or green for success) can be problematic for users with color blindness.

In addition to color, you should use symbols or text to convey information. For example, alongside a red error message, you could use an icon or bold text to make it clear that there’s an error.

Though less common, background audio or videos can also affect accessibility.

Background music or auto-playing videos can be distracting分散注意力 for some users, particularly those with cognitive disabilities. If you include background audio, always provide a way for users to mute静音 or pause the audio.

By taking these accessibility considerations into account, you can create more inclusive designs that ensure your content is readable and usable by all users, regardless of their abilities.

## What Are the Different Ways You Can Add Borders Around Images?
In CSS, there are several ways to add borders around images, each offering different styling options and levels of control.

Let's explore some of the most common and versatile methods.

The most straightforward way to add a border to an image is by using the border property. This property is a shorthand that allows you to set the width, style, and color of the border all at once.

img {
  border: 2px solid red;
}
This CSS rule adds a 2-pixel wide, solid red border around all img elements. You can adjust the width, style (such as dashed, dotted, or double), and color to suit your design needs.

If you need more control over individual sides of the border, you can use the specific border properties for each side:

img {
  border-top: 1px solid red;
  border-right: 2px dashed green;
  border-bottom: 3px dotted blue;
  border-left: 4px double yellow;
}
This allows you to create unique border styles for each side of the image.

Another way to create a border effect is by using the outline property. While similar to border, outline doesn't affect the element's dimensions or layout:

img {
  outline: 3px solid gold;
}
This creates a gold outline around the image without changing its size or position.

If you want to create rounded corners on your border, you can use the border-radius property in conjunction结合 with border:

img {
  border: 2px solid black;
  border-radius: 10px;
}
Remember, these techniques can be combined and customized to create unique border effects. The choice of method depends on your specific design requirements and the level of complexity you need.

