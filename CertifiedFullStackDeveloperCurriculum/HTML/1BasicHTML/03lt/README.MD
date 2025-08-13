# Understanding HTML Attributes

In these lectures, you will learn more about HTML (HyperText Markup Language), a markup language for creating web pages.

You will learn about HTML's role on the web, and what HTML attributes are.

## What Role Does HTML Play on the Web?

HTML, which stands for Hypertext Markup Language, is a markup language for creating web pages. When you visit a website and see content like paragraphs, headings, links, images, and videos; that's HTML. HTML represents the content and structure of a webpage through the use of elements. Here's an example of a paragraph element:

<p>Hello</p>

Most elements will have an opening tag and a closing tag. Sometimes those tags are referred to as start and end tags. In between those two tags, you will have the content. This content can be text or other HTML elements. Both opening and closing tags start with a left angle bracket (<), and end with a right angle bracket (>), with the tag name placed between these angle brackets. Here is a closer look at just the opening and closing paragraph tags:

<p>
</p>
What distinguishes an opening tag from a closing tag is the forward slash (/) placed immediately after the left angle bracket in a closing tag. Some HTML elements do not have a closing tag. These are known as void elements. Here is an example of an image element which is a void element:

<img>
Notice that this image element does not have the closing tag and it does not have any content. Void elements cannot have any content and only have a start tag.

Sometimes you will see void elements that use a / before the > like this:

<img />
While many code formatters like Prettier, will choose to include the / in void elements, the HTML spec states that the presence of the / "does not mark the start tag as self-closing but instead is unnecessary and has no effect of any kind".

In real world development, you will see both forms so it is important to be familiar with both.

If you wanted to display an image, you will need to include a couple of attributes inside your image element. An attribute is a special value used to adjust the behavior for an HTML element. Here is an example of an image element with a src, or source, attribute:

<img src="image location" />
The src attribute is used to specify the location for that image. For image elements, it's good practice to include another attribute called the alt attribute. Here's an example of an image element with the src and alt attributes:

<img src="example-cat-img-url" alt="Cat sleeping in the grass">
The alt attribute is used to provide short, descriptive text for the images. In this case, the descriptive text is a "Cat sleeping in the grass".

So, you might be wondering if HTML by itself is enough to build a website. Well, the answer is: it depends. If you're building a small practice project that only displays text and images, HTML alone might be sufficient. However, if you're creating a modern professional website, you will need to have HTML, CSS, and JavaScript.

HTML is for the content and structure. CSS is for styling. JavaScript is for adding interactivity to your web pages. A good analogy for this is to compare HTML, CSS, and JavaScript with a complete building. HTML represents the blocks, concrete, and irons that make up the walls. It's the foundation that makes the building strong. CSS represents the interior and exterior design that makes the house look beautiful. JavaScript represents the electrical and water system that ensures uninterrupted access to water and electricity.

## What Are Attributes, and How Do They Work?
An attribute is a value placed inside the opening tag of an HTML element. Attributes provide additional information about the element or specify how the element should behave. Here is the basic syntax for an attribute:

<element attribute="value"></element>
The attribute name is followed by an equal sign (=) and a value in quotes. The value can be a string or a number, depending on the attribute.

Let's take a look at a few examples of common HTML attributes. The first example is the href attribute, which is used to specify the URL of a link:

<a href="https://www.example-website.com">Visit our website</a>
Without this attribute, the link would not work because there would be no destination URL. So you must include this href attribute to make the link functional. Other common attributes are the src, or source, and alt, or alternative, attribute - which is used to specify the source of an image and provide alternative descriptive text for the image, respectively:

<img src="image.jpg" alt="A beautiful image" />
Similar to the href attribute, the src attribute is required because it specifies the image file to be displayed. The alt attribute is not required, but it is recommended for accessibility purposes. Accessibility means making sure that everyone, including those with disabilities, can use and understand things like websites, apps, and physical spaces. You will learn more about accessibility in the upcoming lectures.

Some attributes are a little unique with their syntax like the checked attribute shown here:

<input type="checkbox" checked />
In the following example, we have an input element with the type attribute set to checkbox. Inputs are used to collect data from users, and the type attribute specifies the type of input. In this case, this input is a checkbox. You will learn more about how inputs work in the upcoming lectures. The checked attribute is used to specify that the checkbox should be checked by default. The checked attribute does not require a value. If it is present, the checkbox will be checked by default. If the attribute is not present, the checkbox will be unchecked. This is known as a boolean attribute. You will learn more about booleans in general when you get to the JavaScript section. There are several common boolean attributes you will encounter in HTML, such as disabled, readonly, and required. These attributes are used to specify the state of an element, such as whether it is disabled, read-only, or required.

HTML has many attributes that can be used to customize the behavior and appearance of elements on a webpage. Understanding how to use attributes is essential for creating interactive and accessible web content. Over the next few lectures, you will learn about more HTML attributes and how to use them effectively in your web development projects.
