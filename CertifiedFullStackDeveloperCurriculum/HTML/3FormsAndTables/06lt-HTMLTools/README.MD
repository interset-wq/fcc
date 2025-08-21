# Working with HTML Tools

In these lectures, you will learn about HTML tools and how they let you write better code. These tools include HTML validators, DOM Inspector, and the browser developer tools.

## What Is an HTML Validator, and How Can It Help You Debug Your Code?
HTML is a very forgiving language – elements still render even when you make mistakes, like forgetting to include a closing tag.

Let's say you have an h2 element without a closing tag:

<h1>Article Topic</h1>
<h2>Subheading 1 </h2>
<h2>Subheading 2 </h2>

<!-- This h2 does not have a closing tag -->
<h2>Subheading 3
The h2 without a closing tag will still render fine. This happens because browsers use a parsing algorithm that handles common errors and tries to render HTML as closely as possible to the author's intention.

But this could backfire sometimes. Let's add a few paragraphs under the existing heading 2 tags in the code:

<h1>Article Topic</h1>
<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Maiores, nisi.</p>

<h2>Subheading 1 </h2>
<p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. At, doloremque.</p>

<h2>Subheading 2 </h2>
<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Unde, placeat.</p>

<!-- This h2 does not have a closing tag -->
<h2>Subheading 3
<p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Tempore, illum.</p>
As a result, the paragraph element under the h2 without a closing h2 tag renders as heading 2. This is why you need an HTML validator.

An HTML validator is a tool that checks the validity of your HTML code against the standard HTML specifications. It helps you identify errors and warnings in your HTML code, ensuring your web pages are correctly structured and compliant with web standards.

Using an HTML validator benefits not only you and your future code reviews, but also anybody else going through your code, such as your teammates and open-source contributors.

There are several HTML validators out there you can use. The most widely accepted one is the w3.org markup validation service.

When you visit the site validator.w3.org, you can click on the Validate by Direct Input button and paste in your HTML code.

When you click on the Check button, then a list of results will display with the errors that need to be fixed.

Another HTML validator that you can use is jsonformatter.org.

You can copy and paste your HTML code inside the first editor, and when you click on the Validate button, it will show you any errors you have in your code.

## How to Use the DOM Inspector and DevTools to Debug and Build Your Projects
When you are building out your projects, you will frequently run into issues where your programs are not working as expected.

Programmers often refer to issues as bugs. The process of finding and fixing these bugs is known as debugging.

To debug your code, you will need to use some tools provided by your browser.

Two important tools to use would be the DOM inspector and developer tools.

The DOM inspector allows you to inspect the HTML structure of the page you are on.

The DOM stands for Document Object Model. It is a tree-like structure that represents the elements on a page. You will learn more about the DOM in later modules.

The developer tools allow you to inspect the HTML, CSS, and JavaScript of the page you are on.

Let's take a look at an HTML example that contains a small bug in the anchor element:

<a href="https://www.freecodecamp.org/larn/">freeCodeCamp curriculum</a>
When you click on the link, it will lead to a 404 page. A 404 page is an error page that appears when a user tries to access a webpage that doesn't exist on the server.

The intent is for the link to lead to the freeCodeCamp curriculum.

To see what the issue might be, you can use the developer tools.

To open the developer tools in your browser, you can right-click on the page and select Inspect.

You can also use Control Shift I on your PC keyboard or Command Option I on your Mac.

When you open developer tools in Google Chrome, you'll see a number of tabs. The first tab is called the Elements tab. This tab shows you the HTML structure of the page you are on.

The second tab is called the Console tab. This tab shows you any errors that might be occurring on the page.

In the situation where you have a broken link, you can check the console to see the error messages for that broken link. The common message that continues to display for the broken link is the 404 error. The 404 error indicates that the page is not found.

This lets us know that the issue is with the URL in the anchor element. When you inspect the href value you will see there is a typo.

Right now the console message shows /larn against a 404, but the correct URL should be /learn. When the link is corrected, then it will work as expected.

You will learn more about working with the developer tools throughout the certification, but this is just a short example on how it can help you debug your code.

