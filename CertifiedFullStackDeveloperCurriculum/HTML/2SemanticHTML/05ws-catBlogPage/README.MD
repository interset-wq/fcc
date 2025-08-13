# Build a Cat Blog Page

In this workshop, you will build an HTML only blog page using semantic elements including the main, nav, article and footer elements.

Step 1
In this workshop, you will practice working with semantic HTML by building a blog page dedicated to Mr. Whiskers the cat.

To begin the project, add the <!DOCTYPE html>, and an html element with a lang attribute of en.

Remember that you learned how to build a basic HTML boilerplate like this in the previous module.

Example Code
<!DOCTYPE html>
<html lang="en">
<!--all other elements go here-->
</html>

Step 2
Inside the html element, add a head element.

Step 3
Inside your head element, nest a meta element with the charset attribute set to the value "UTF-8".

Below that meta element, add a title element.

The title element's text should be Mr. Whiskers' Blog.

Step 4
To prepare creating some actual content, add a body element below the head element.

Step 5
The first section you will build out is the page header.

The header element is used to represent introductory content like page navigation and other introductory information.

Here is an example using the header element:

Example Code
<header>
  <h1>Main Page Title Goes Here</h1>
  <img src="example-logo.png" alt="Example logo" />
</header>
Inside the body element, add a header element.

Step 6
The header will be responsible for displaying main title, image and page navigation for the blog.

Inside the header element, add an h1 with the text of Welcome to Mr. Whiskers' Blog Page!.

Step 7
In this introductory content, you will want to show an image of Mr. Whiskers with a caption.

Below the h1 element, start by adding a figure element.

Inside the figure element, add an img element.

The src attribute of the img should have a value of "https://cdn.freecodecamp.org/curriculum/css-photo-gallery/1.jpg" and the alt text should have a value of "a cat peacefully sleeping".

Below your img element, add a figcaption with the text Mr. Whiskers Sleeping.

Step 8
For your blog, there should be a way for users to navigate to different sections on the page.

The nav element is used to provide navigation links to other sections in the document or other sections in the website. A lot of times you will see the nav element used for menus or table of contents.

Here is an example of using the nav element:

Example Code
<nav>
  <ul>
    <li><a href="#">Home</a></li>
    <li><a href="#about">About</a></li>
    <li><a href="#contact">Contact</a></li>
  </ul>
</nav>
Below your figure element, add a nav element with a ul element nested inside.

Inside the ul element, add three li elements.

Step 9
Inside each of the li elements, you will need to have an anchor element.

For the first anchor element, the text should be About and the href attribute value should be "#about". The hash symbol in front of the about represents an id name which be added later on in the project.

For the second anchor element, the text should be Posts and the href attribute value should be "#posts".

For the third anchor element, the text should be Contact and the href attribute value should be "#contact".

Step 10
Now that you are finished building out the page header, you will need to start adding your main content.

Below your header, add a main element.

Step 11
The first section on the page will be the about section. The section will introduce Mr. Whiskers and give users an idea of what this blog is about.

Inside your main element, add a section element with the id attribute set to "about".

Inside the section element, add an h2 with the text of About.

Step 12
Below your h2 element, add a paragraph element with the text of Hi there! I'm Jane Doe, a passionate writer who finds endless inspiration in the antics of my beloved cat, Mr. Whiskers..

Below your paragraph element, add another paragraph element with the text of His playful nature and boundless energy keeps me on my toes. I love him so much.

Step 13
Now that you have added the about section, try clicking on the About link to see the page jump down to that section.

The next section in the blog page will be a list of posts talking about Mr. Whiskers.

Add another section element with an id set to "posts".

Inside the section element, add an h2 element with the text of Posts.

Step 14
For the first blog post, you will use an article element.

The article element represents self contained content on a web page.

Example Code
<article>
  <h1>Example heading</h1>
  <p>Example article text</p>
</article>
Below the h2 element, add an article element.

Inside the article element, add an h3 element with the text Mr. Whiskers' First Day Home.

The reason an h3 is used here is that maintaining a proper structural hierarchy for heading elements is important. Since the posts subheading is an h2 element, the next level down in the hierarchy would be an h3.

Step 15
This blog post is going to contain a couple of paragraphs with lorem ipsum text.

Lorem ipsum is commonly used in web development to serve as placeholder text. It is useful when you want to focus on building out the basic structure of your web pages and not have to worry about the actual content just yet.

Here is an example of using lorem ipsum:

Example Code
<p>
  Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam
  quod, voluptates, quae, quos quibusdam dolorum quia nemo repudiandae
  quidem voluptatum quas. Quisquam quod, voluptates, quae, quos
  quibusdam dolorum quia nemo repudiandae quidem voluptatum quas.
</p>
Below your h3 element, add two paragraphs of lorem ipsum text.

Step 16
For the second blog post, you will need to add another article element.

Inside the article element, add an h3 element with the text of Mr. Whiskers' First Bath.

Below your h3 element, add two paragraphs of lorem ipsum text.

Step 17
For the third blog post, you will need to add another article element.

Inside the article element, add an h3 element with the text of Mr. Whiskers' First Birthday Party.

Below your h3 element, add two paragraphs of lorem ipsum text.

Step 18
Now that you have finished adding all of the blog posts, try clicking on the Posts link and you should see that the page jumps down to the Posts section.

The last component to add to your blog page is going to be the contact section.

Below the main element, add a footer element.

Step 19
Inside the footer element, add a section element with an id set to contact.

Inside the section element, add an h2 element with the text of Contact.

Step 20
Inside the contact section, you will want to show the blog author's contact information. You will use an address element for this.

The address element is used to represent contact information for a person or organization.

Here is an example using the address element for a physical address. The br element is used here to create a line break between the text.

Example Code
<address>
  1234 Make Believe Lane <br />
  Pretend City, USA
</address>
Below your h2 element, add an address element.

Step 21
For this step, you will need to add the phone number and email address for the blog author.

Inside the address element, add a paragraph element with the text of Phone: 555-555-5555.

Below that paragraph element, add another paragraph element with the text of Email: fake@email.com.

Step 22
To improve user experience, you will want to enhance the phone number so that users tap on it and initiate a call.

Here is how you can make phone numbers clickable:

Example Code
<a href="tel:2345678912">234-567-8912</a>
Wrap the text 555-555-5555 in an anchor element and use tel: to make it a clickable phone number.

Step 23
Similarly, users should be able to click on the email address and send an email from their default email client.

Here is how you can make email addresses clickable:

Example Code
<a href="mailto:contact@company.com">contact@company.com</a>
For this final step, wrap the text fake@email.com in an anchor element and use mailto: to make it a clickable email address.

And with those changes, your blog page is now complete.

