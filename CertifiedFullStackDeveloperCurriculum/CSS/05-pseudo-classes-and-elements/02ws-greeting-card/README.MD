# Design a Greeting Card, Not started
In the previous lectures, you learned how to work with the different types of pseudo-classes.

In this workshop, you will have a chance to practice what you have learned by designing a greeting card.

step1
In this workshop, you will practice working with different pseudo-classes and pseudo-elements by designing a greeting card. The HTML boilerplate has been provided for you.

Start the workshop by linking the styles.css file.

Step 2
Create a div element that has an id of greeting-card and a class of card.

Inside the div element, add an h1 with the text Happy Birthday!. Then add a paragraph element with a class called message and the text Wishing you all the happiness and joy on your special day!.

Step 3
Now it is time to style your greeting card.

Add a selector for the body element, then:

change the font-family to be Arial宋体，类似与中文宋体字 followed by the generic通用的 sans-serif无衬线字体,
give a padding on all sides of 40px,
set the text-align property to center.

Step 4
Now it's time for some color. Give the body a background-color of brown and also give the .card a background-color of white.

Step 5
Give .card a max-width of 400px, a padding of 40px on all sides, and a margin of 0 for top and bottom and auto for left and right (use the shorthand property).

Step 6
The .card element needs some more styling: add a border-radius of 10px, and a box-shadow with a value of 0 4px 8px gray.

Step 7
Now add a new div below the .message element. The new div should have a class attribute of card-links.

Step 8
Add two a elements inside the .card-links element.

The first one should have a text of Send Card, a class of send-link and an href of #send.

The second one should have a text of Share on Social Media, a class of share-link and an href of #share.

Step 9
Add two section elements, one after the other. The first should have an id of send, the second one should have an id of share.

Step 10
Add an h2 to #send that contains the text Sending your card..., then add a p element with the text Card successfully sent to your recipient!.

Step 11
Time to fill the second section!

Add an h2 element to the #share element that contains the text Sharing your card..., then add a p element with the text Your card was shared on social media!.

Step 12
Add a new selector that changes the background-color of the .card element to khaki when it is hovered over.

Step 13
The transform property can transform the element look. For example, giving it a value of scale(0.9) would make the element 10% smaller.

Example Code
p {
  transform: scale(0.9);
}
Add a transform property to the .card:hover selector and set to scale(1.1).

Step 14
When the a elements are hovered, the color of the background makes a transition to a different color. You can regulate how that transition happens with the transition property:

Example Code
a {
  transition: color 1s linear;
}
The values that the transition property accepts are, in order, the property that the transition is applied to, the duration of the transition, and then the timing.

If there are multiple properties that have a transition, you can write the values for each separated by a comma:

Example Code
p {
  transition: property1 0.1s, property2 0.6s linear;
}
If a value is omitted遗漏, like the timing for the first property, a default value is applied.

Add to the .card selector transition: transform 0.3s, background-color 0.3s ease.

Try it out, the hover transition is complete.

Step 15
You can add an emoji in front of the title using the pseudo-element ::before of the h1 element.

Create an h1::before selector, give it a content property and set its value to "🥳 " (note there is a space after the emoji).

Step 16
Now you can do something similar to add the emoji also after the title.

Create a selector that targets the pseudo-element ::after of the h1 element. Give it a content property and set its value to " 🥳" (note there is a space before the emoji).

Step 17
The .message element needs some styling. Give it:

a font-size of 1.2em,
a color of gray,
a margin-bottom of 20px.

Step 18
Add a .card-links selector, and set the margin-top property to 20px.

You can add display: flex to set an element to use flexbox弹性盒子, you will learn more about flexbox later in the course, you can consider this a small preview.

To space the two links so that they have the same space around, add a display property set to flex, and a justify-content set to space-around.

Step 19
Target the a elements inside .card-links and give them:

a text-decoration property set to none.
a font-size property set to 1em
a padding property set to 10px 20px
a border-radius property set to 5px
a color property set to white
a background-color property set to midnightblue

Step 20
Create a pseudo-class selector that targets the .card-links a elements when hovered over.

The background-color should change to orangered.

Step 21
Add a transition property to the .card-links a selector and give it a value of background-color 0.3s ease.

Step 22
Add a new selector that targets the .card-links a elements when they are active. Set the background-color to midnightblue.

Step 23
Add a new selector that targets the .card-links a elements when focused. Set the outline property to 2px solid yellow.

Step 24
Create a new selector that targets the .card-links a elements if they have already been visited. Set the property color to crimson.

Step 25
Create a selector for the section elements, and give them:

a margin property set to 20px auto,
a max-width set to 600px.
a background-color property set to whitesmoke
a padding property set to 20px
a border-radius property set to 10px

Step 26
Another value that can be used for the transform property is skewX, this function skews扭曲 the element horizontally.

Example Code
div {
  transform: skewX(7deg);
}
Add a selector that targets the section elements when hovered. Set the transform property to skewX(10deg).

Step 27
As last thing to complete this project, add a display property set to none to the section selector.

After that, create a section:target selector, and add there a display property set to block so that the section elements are visible only when the links are clicked.

