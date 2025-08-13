# Build a Heart Icon

In this workshop, you will practice working with SVGs by building a heart icon

Step 1
In a previous lecture, you learned about svg elements and how they're often used as icons in projects. In real-world codebases, you would typically rely on icon libraries, so you don't need to create svg elements from scratch. However, in this workshop, you'll build a heart icon to learn about the core attributes used inside an svg element.

Start by creating an svg element on the page.

Step 2
The next step is to set the width and height attributes for the svg element. As you are creating an icon, both values should be set small.

Set both values to 24.

Step 3
You are getting closer. The next thing to do is to set the viewBox attribute of the svg element. This will control how much of the image is visible. The first two numbers set the center of the image.

The following two numbers set the size of the image can we see; width followed by height.

Since here the entirety of the icon should be visible, you should set the viewBox attribute to 0 0 24 24.

Step 4
Before you begin coloring the image in, you should nest one path element inside your svg element to give the image shape.

Create a path element.

Step 5
The path element needs its shape defined. That is where the d attribute comes in. It is used to create a series of command letters and numbers that draw a shape.

These letters represent commands like move to, draw line, and close, while the numbers represent coordinates.

Set the heart shape's d attribute to M12 21s-6-4.35-9.33-8.22C-.5 7.39 3.24 1 8.4 4.28 10.08 5.32 12 7.5 12 7.5s1.92-2.18 3.6-3.22C20.76 1 24.5 7.39 21.33 12.78 18 16.65 12 21 12 21z.

Step 6
The heart icon is almost done. You just need to color it red. To do that, set the svg element's fill attribute to red.

Congrats on finishing this workshop!

