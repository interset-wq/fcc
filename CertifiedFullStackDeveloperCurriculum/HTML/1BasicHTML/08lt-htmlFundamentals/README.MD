# HTML Fundamentals

In these lectures, you will learn about HTML fundamentals like the div element, the id and class attributes, the HTML boilerplate, HTML entities, and more.

## What are Div Elements and When Should You Use Them?

Now that we understand what HTML is, let's move onto the fun stuff! I am going to look at the Content Division Element - or in other words, the div:

<div></div>
I like to think of the div as a beautiful being that can be anything you want it to be. We can give a div a height, we can give it a width, and we can give it a background color using CSS - or in other words styling, which we will cover in lectures coming up.

We can also use it in a very basic form without styling, to hold other elements together. So for example, we can create a div and put a heading in it, and put a paragraph in it, and now these two elements will be grouped together:

<div>
  <h1>I am a heading</h1>
  <p>I am a paragraph</p>
</div>
Just be aware that there might be better elements to use when grouping these together. You might choose a section element, for example:

<section>
  <h1>I am a heading</h1>
  <p>I am a paragraph</p>
</section>
This is because the section element has semantic meaning. Semantics are the meaning of words or phrases in a language. In HTML, which is a language, elements have their own semantic meaning too. So, this means if you use a section element, the browser will pick up its semantic meaning and understand to treat this as a section - on desktops, mobiles, you name it. 

We will dive into this topic further later on. For now, just know that the div, does not have this. It's like a mysterious ghost. Let's see what else we can do to a div, in the next lecture.

## What Are IDs and Classes, and When Should You Use Them?

The id attribute adds a unique identifier to an HTML element. In this example, there is an h1 element with an id of title:

<h1 id="title">Movie Review Page</h1>
You can reference the id name of title within your JavaScript or CSS. Here's a CSS example referencing the id of title to change the text color to red:

#title {
  color: red;
}
The hash symbol (#) in front of title, tells the computer you want to target an id with that value. id names should not be used more than once, and they should always be unique. Another thing to note about id values, is that they cannot have spaces in them. Here is an example of applying the words main and heading to an id attribute value:

<h1 id="main heading">Main heading</h1>
Browsers will see this space as part of the id which will lead to unwanted issues when it comes to styling and scripting. id attribute values should only contain letters, digits, underscores, and dashes.

In contrast to the id attribute, the class attribute value does not need to be unique and can contain spaces. Here is an example of applying a class called box to a div element:

<div class="box"></div>
If you wanted to add multiple class names to an element, you can do so by separating the names by a space. Here is an updated example applying multiple classes to a div element:

<div class="box red-box"></div>
To apply a set of styles to that box class, you can reference that class inside your CSS. Here is an example of setting width, height, and border properties to the element with the class name of box:

.box {
  width: 200px;
  height: 200px;
  border: 2px solid black;
}
The dot symbol (.) in front of box, tells the computer you want to target a class with that value. When the code runs, it will search through all of your HTML document to find all elements with that class name and apply those styles.

So, to recap, when should you use an id versus a class? Classes are best used when you want to apply a set of styles to many elements. If you want to target a specific element, it is best to use id because those values need to be unique.

## What Are HTML Entities, and What Are Some Common Examples?
An HTML entity, or character reference, is a set of characters used to represent a reserved character in HTML. In this example, there is a paragraph element with an image element nested inside:

<p>This is an <img /> element</p>
The text on the screen should say This is an <img/> element. However, the text currently says This is an element. This is happening because when the HTML parser sees the less than (<) symbol followed by an HTML tag name, it interprets that as an HTML element.

To fix this issue, you can use HTML entities. Here is an updated example using the correct HTML entities for the less than and greater than (>) symbols.

<p>This is an &lt;img /&gt; element</p>
These types of character references are known as named character references. Named references start with an ampersand sign (&) and end with a semicolon (;). By using a named character reference, the HTML parser will not confuse this with an actual HTML element. Here is what the updated paragraph element looks like on the page: This is an <img/> element. Now, users will be able to see the entire image element syntax as you intended it.

Another type of character reference would be the decimal numeric reference. Here is an example of using the decimal numeric reference for the less than symbol:

&#60;
This character reference starts with an ampersand sign and hash symbol (#), followed by one or more decimal digits, followed by a semicolon.

The last type of character reference would be the hexadecimal numeric reference. Here is an example of using the hexadecimal numeric reference for the less than symbol:

&#x3C;
This character reference starts with an ampersand sign, hash symbol, and the letter x. Then it is followed by one or more ASCII hex digits and ends with a semicolon.

So what are some other examples of using HTML entities? Well, you often see them used for symbols like the copyright symbol (©), quotes ("), trademark symbol (™), and the ampersand sign.

## What Is the Role of the Script Element in HTML, and How Can It Be Used to Link to External JavaScript Files?
The script element is used to embed executable code. Most developers will use this to execute JavaScript code. JavaScript is used to add interactivity to your web pages. Common examples of using JavaScript include interactive games, image sliders, and dynamic forms that validate user input in real-time. Here is an example of using the script element in an HTML document:

<body>
  <script>
    alert("Welcome to freeCodeCamp");
  </script>
</body>
In this example, we have an alert to display the message Welcome to freeCodeCamp. When the page first loads, the alert will pop up. Then the user can click on the OK button to dismiss the message.

While you can technically write all of your JavaScript code inside the script tags, it is considered best practice to link to an external JavaScript file instead. Here is an example of using the script element to link to an external JavaScript file:

<script src="path-to-javascript-file.js"></script>
The src attribute is used here to specify the location for that external JavaScript file. src stands for "source". The reason why it is not encouraged to place all of your JavaScript inside the HTML document is because of separation of concerns. Separation of concerns is a design principle where you separate your programs into distinct sections and have each section address a separate concern. In this case, we want to separate our JavaScript code from our HTML code.

## What Is the Role of the Meta Description, and How Does It Affect SEO?
SEO, or Search Engine Optimization, is a practice that optimizes web pages so they become more visible and rank higher on search engines. One way to improve your site's SEO, is to provide a short description for the web page using the meta element. Here is an example of using the meta element to set a page description for a gardening site:

<meta
  name="description"
  content="Discover expert tips and techniques for gardening in small spaces, choosing the right plants, and maintaining a thriving garden."
/>
By setting the name attribute to description, it ensures that browsers, search engines, and other web tools correctly interpret this metadata. The content attribute is where you will place your description. It is recommended that you keep your descriptions short and concise. This is because search engines will often truncate the description based on the results page layout.

Similar to other types of meta elements, the meta description will not be visible on the web page itself. One place where the page description can be found is in the search engine results page snippet. Here are some examples of page result snippets for freeCodeCamp's subreddit and GitHub repositories:

r\FreeCodeCamp: This is the official subreddit for the freeCodeCamp.org community. Learn to
code for free together with millions of other people...
Our full-stack web development and machine learning curriculum is completely free and self-
paced. We have thousands of interactive coding challenges to help you...
In the examples, each of the page descriptions are located just beneath the site links. Within a couple of seconds, users can get a general sense of what the page is about and decide to click on the links for more information.

Even though meta descriptions won't directly affect a site's ranking on search engine, having a strong description could result in more traffic to your website.

## What Is the Role of Open Graph Tags, and How Do They Affect SEO?
The open graph protocol enables you to control how your website's content appears across various social media platforms, such as Facebook, LinkedIn, and many more. By setting these open graph properties, you can entice users to want to click and engage with your content. You can set these properties through a collection of meta elements inside your HTML head section.

The first important OG property to include would be the title. Here is an example of setting the OG title for the freeCodeCamp homepage:

<meta content="freeCodeCamp.org" property="og:title" />
For the property attribute, you will need to specify that it is og:title. The content attribute is where you will write the title you want displayed for social media sites.

The next important OG property would be the type. Here is an example of using the OG type for the freeCodeCamp homepage:

<meta property="og:type" content="website" />
The type property is used to represent the type of content being shared on social media. Examples of this content include articles, websites, videos, or music.

The third important OG property would be the image. Here is an example of setting the OG image for the freeCodeCamp homepage:

<meta
  content="https://cdn.freecodecamp.org/platform/universal/fcc_meta_1920X1080-indigo.png"
  property="og:image"
/>
In this example, the open graph image is pointing to the freeCodeCamp logo. All of these images should be high quality with good dimensions and ratios. Most social media platforms will include criteria for image requirements to help you ensure that your content displays well on their site. For example, the developers.facebook.com documentation page states:

"use images that are at least 1200 by 630 pixels for the best display on high resolution devices. At the minimum, you should use images that are 600 by 315 pixels to display link page posts with larger images."

The fourth important OG property would be the url. Here is an example of setting the OG url for the freeCodeCamp homepage:

<meta property="og:url" content="https://www.freecodecamp.org" />
There are many more OG properties that you can set, like description, audio, video and locale. However, the open graph url, image, type, and title are the most important ones to include.

So how do these open graph properties affect Search Engine Optimization? When your content is shared on social media, well-crafted OG properties can enhance the appearance for your content in users' feeds. This can lead to higher click-through rates which could signal to search engines that your content is relevant and engaging.