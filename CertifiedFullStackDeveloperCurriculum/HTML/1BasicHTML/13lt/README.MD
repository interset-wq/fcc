# Working with the iframe Element

In these lectures, you will learn how to work with the iframe element which is used to embed an external site on your web page.

What Are Replaced Elements, and What Are Some Examples?
A replaced element is an element whose content is determined by an external resource rather than by CSS itself. CSS, or cascading stylesheets, is used to add styles to a web page. Common examples of replaced elements include the image, iframe, and video elements.

With replaced elements, you can control the position, or layout of an element. But your CSS cannot directly modify the content of that element. This might be easier to explain with some examples. Consider the image element, which embeds an image on your web page:

Example Code
<img src="example-img-url" alt="Descriptive text goes here">
The element itself is replaced with the external object: the image. Your CSS can control things like the positioning of the image, or apply a filter to it, but you cannot actually modify the image itself. A more robust example might be the iframe element, which embeds an external site on your web page:

Example Code
<iframe src="https://www.example.com" title="Example Site"></iframe>
Common examples for using the iframe element would be to embed Maps or YouTube videos onto the page. The element itself is replaced with the external object: the site. Your CSS can change the positioning of the embedded site, but you cannot modify the site's contents. To dive a bit further, if the embedded site has an h1 element, your CSS would not be able to style that h1 element. You cannot change the size, font color, and so on.

There are some other replaced elements, such as video, and embed. And some elements behave as replaced elements under specific circumstances. Here's an example of an input element with the type attribute set to image:

Example Code
<input type="image" alt="Descriptive text goes here" src="example-img-url">
This type of input is considered to be a replaced element, but other input types like text, or email are not replaced elements.

## How Do You Embed Videos onto Your Page Using the iframe Element?
First, what exactly is the iframe element? iframe stands for inline frame. It's an inline element used to embed other HTML content directly within the HTML page. That HTML content could be a video, map, another HTML element, or even other web pages. Here's what the syntax of the iframe element looks like:

Example Code
<iframe
  src="video-url"
  width="width-value"
  height="height-value"
  allowfullscreen
></iframe>
The src attribute specifies the URL of the page you want to embed. The width attribute specifies the width of the iframe. The height attribute specifies the height of the iframe. The allowfullscreen attribute allows the user to display the iframe in full screen mode. It's also a good practice to specify a title attribute for the iframe, as it's important for accessibility.

To embed a video within an iframe you can copy it directly from popular video services like YouTube and Vimeo, or define it yourself with the src attribute pointing to the URL of that video. Here's an example of embedding a popular freeCodeCamp course from YouTube:

Example Code
<h1>A freeCodeCamp YouTube Video Embedded with the iframe Element</h1>

<iframe
  width="560"
  height="315"
  src="https://www.youtube.com/embed/PkZNo7MFNFg?si=-UBVIUNM3csdeiWF"
  title="YouTube video player"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
  referrerpolicy="strict-origin-when-cross-origin"
  allowfullscreen
></iframe>
You can then customize the iframe to your needs or even define your own by copying the link to the YouTube video and pasting it in as the URL value. The caveat is that you must replace https://youtu.be with https://youtube.com/embed/.

youtu.be is the domain when you copy the share link and youtube.com/embed/ is the domain required for embedding videos with the iframe element. Here's an example of that:

Example Code
<iframe
  src="https://youtube.com/embed/gp5H0Vw39yw?si=Rb_2nDK6abv1iIAM"
  title="freeCodeCamp Typescript Course"
  width="500"
  height="285"
  allowfullscreen
></iframe>
Note that the video can come from anywhere. It doesn't have to come from video services like YouTube and Vimeo. Here's a video from Pixabay embedded with the iframe element:

Example Code
<h1>A Video from Pixabay Embedded with the iframe Element</h1>

<iframe
  src="https://cdn.pixabay.com/video/2022/07/24/125310-733046613_large.mp4"
  width="500"
  height="285"
></iframe>
Don't forget you can also embed a map, another web page, or direct HTML within the iframe element. Here's a map I was able to embed with the iframe element:

Example Code
<h1>A Map from Openstreetmap.org Embedded with the iframe Element</h1>

<iframe
  width="425"
  height="350"
  src="https://www.openstreetmap.org/export/embed.html?bbox=3.006134033203125%2C6.150112578753815%2C3.6357879638671875%2C6.749850810550778&amp;layer=mapnik"
  style="border: 1px solid black"
>
</iframe>
<br />
<small>
  <a href="https://www.openstreetmap.org/#map=11/6.4501/3.3210">
    View Larger Map
  </a>
</small>
If you want to embed direct HTML within the iframe element you have to use the srcdoc attribute instead of src.

