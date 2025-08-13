# Understanding the HTML Boilerplate

In these lectures, you will learn about the HTML boilerplate which is a ready-made template for your webpages.

You will learn how to work with the link element, meta element and more.

## What Is the Role of the Link Element in HTML, and How Can It Be Used to Link to External Stylesheets?

Let's learn about the link element, and how to use it to link to external stylesheets.

The link element is used to link to external resources like stylesheets and site icons. Here is the basic syntax for using the link element for an external CSS file:

<link rel="stylesheet" href="./styles.css" />
The rel attribute is used to specify the relationship between the linked resource and the HTML document. In this situation, we need to specify that this linked resource is a stylesheet.

It is considered best practice to separate your HTML and CSS in different files. Developers will use the link element for their external CSS file instead of writing everything in the HTML document.

The href attribute is used to specify the location of the URL for the external resource.

The dot followed by a forward slash in the example tells the computer to look in the current folder, or directory, for the styles.css file.

The link element should be placed inside the head element as seen in the following example:

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Examples of the link element</title>
  <link rel="stylesheet" href="./styles.css" />
</head>
Often times you will see multiple link elements inside a professional codebase that link to different stylesheets, fonts, and icons. Here is an example of using the link element to link to an external Google Font called Playwright Cuba:

<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link
  href="https://fonts.googleapis.com/css2?family=Playwrite+CU:wght@100..400&display=swap"
  rel="stylesheet"
/>
Google Fonts are a set of free and open source custom fonts that you can use inside any project. You can choose which fonts you would like to use and Google will provide you with the necessary HTML and CSS code. In this example, the preconnect value for the rel attribute tells the browser to create an early connection to the value specified in the href attribute. This is done to speed up loading times for these external resources.

Another common use case for the link element is to link to icons. Here is an example of linking to a favicon:

<link rel="icon" href="favicon.ico" />
A favicon, which is short for favorite icon, is a small icon typically displayed in the browser tab next the site title. A lot of websites will use a favicon to display their brand icon.

## What Is an HTML Boilerplate, and Why Is It Important?

Let's learn about the HTML boilerplate.

What is the HTML boilerplate, you ask? It's like a ready-made template for your webpages. Think of it as the foundations of a house. A boilerplate includes the basic structure and essential elements every HTML document needs. It saves you time and helps ensure your pages are set up properly. Here is an example:

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta
       name="viewport"
       content="width=device-width, initial-scale=1.0" />
    <title>freeCodeCamp</title>
    <link rel="stylesheet" href="./styles.css" />
  </head>
  <body>
  </body>
</html>
Let's break down the key parts of this boilerplate. First, there is the DOCTYPE declaration:

<!DOCTYPE html>
It tells browsers which version of HTML you're using. Next, comes the html tag:

<!DOCTYPE html>
<html lang="en">
  <!--All other elements go inside here-->
</html>
This wraps around all your content, and can specify the language of your page. Inside the html tag, you'll find two main sections - a head, and a body:

<!DOCTYPE html>
<html lang="en">
  <head>
    <!--Important metadata goes here-->
  </head>
  <body>
    <!--Headings, paragraphs, images, etc. go inside here-->
  </body>
</html>
The head section contains important behind-the-scenes information:

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Document Title Goes Here</title>
  <link rel="stylesheet" href="./styles.css" />
</head>
Your site's metadata, contained in meta elements, has details about things like character encoding, and how websites like Twitter should preview your page's link. Your site's title, found in the title element, determines the text that appears in the browser tab or window. Finally, you'll typically link your page's external stylesheets in the head section using link elements.

The body section is where all your content goes:

<body>
  <h1>I am a main title</h1>
  <p>Example paragraph text</p>
</body>
Now, why is a boilerplate important? It ensures your pages are structured correctly and work well across different browsers. Using a boilerplate helps you avoid common mistakes and follow best practices. It's a great starting point for any web project. Remember, you can customize your own boilerplate to fit your needs. As you gain experience, you might add your own preferred elements or meta tags. As you continue to improve your personal boilerplate, you'll find that it saves you time when starting new projects.

Next time you start a new HTML file, consider using a boilerplate. It will definitely give you a solid foundation to build on.

## What Is UTF-8 Character Encoding, and Why Is It Needed?

What is UTF-8 character encoding, and why is it needed?

UTF-8, or UCS Transformation Format 8, is a standardized character encoding widely used on the web. Character encoding is the method computers use to store characters as data. Essentially, all text on a web page is a sequence of characters stored as one or more bytes. In computing, a byte is a unit of data consisting of 8 bits, or binary digits. UTF-8 supports every character in the Unicode character set - and this includes characters and symbols from all writing systems, languages, and technical symbols. Here is an example of using the meta element with the charset attribute to set the character encoding to UTF-8:

<meta charset="UTF-8" />
By setting the character encoding to UTF-8, it will ensure that the accented "e" character (é) is displayed correctly on the page. Here is an extended code example of using the UTF-8 character encoding:

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Examples of the UTF-8 encoding</title>
  </head>
  <body>
    <p>Café</p>
  </body>
</html>
For each new project you create, you should include this meta element with the charset attribute set to UTF-8.