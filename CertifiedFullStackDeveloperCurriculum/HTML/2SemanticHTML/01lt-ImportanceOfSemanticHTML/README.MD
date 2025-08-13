# Importance of Semantic HTML

In these lectures, you will learn about semantic HTML and why you should care about it, semantic elements, how semantic HTML differs from presentational HTML, and more.

## Why Should You Care About Semantic HTML?
Semantics are the meaning of words, or phrases, in a language. In HTML, which is a language, elements have their own semantic meaning too. In fact, you can think of your HTML document like you would a text document. And much like a text document, you might have headings, images, bold text, and other formatting.

The semantic meaning of an element refers to what special information that element conveys. The semantic meaning of a p element, for example, is a paragraph of text:

<p>
  Let me tell you about my fantastic holiday in Paris.
  I saw the impressive Eiffel Tower up close!
</p>
Most elements have semantic meaning. The div element is one of the very few that does not. But why is this important?

First and foremost, using proper semantic HTML will ensure the best experience for users with assistive technology like screen readers. But also, semantic HTML can improve your search rankings. This is referred to as search engine optimization, or SEO.

Finally, using correct semantic elements can improve your development experience. Rather than having to sift through a bunch of developments to find your navigation bar, you can edit the nav element directly and know what you're changing. Throughout this section, you will learn more about these topics, how to use semantic elements, and why semantic HTML is so important.

## Why is it Important to Have Good Structural Hierarchy?
The most important aspect of creating a structural hierarchy is the proper use of heading elements. Heading elements are numbered as h1, h2, h3, and so on. These numbers represent the heading level for that element.

Much like a text document, you do not want to use heading levels in the incorrect order. Your h1 element is your top-level heading. You will rarely have more than one of these on a page, and it should typically come before all of your content.

Your h2 element is your subheading. It should always come after your h1 and might come after some introductory text. Unlike an h1 element, you can have multiple h2 elements on your page. You'll often do this to delineate different sections of content.

Following the pattern, your h3 element should always come after an h2 element. That is, you should never skip directly from h1 to h3. You can, however, have multiple heading elements at the same level. For example, this code is correct:

<div>
  <section>
    <h1>freeCodeCamp</h1>
    <h2>Learn Front-End Development</h2>
    <h2>Learn Back-End Development</h2>
  </section>
</div>
But this code would not be correct, because h3 comes before h2:

<div>
  <section>
    <h1>freeCodeCamp</h1>
    <h3>Learn Front-End Development</h3>
    <h2>Learn Back-End Development</h2>
  </section>
</div>
It may be tempting to use a specific heading element because of its styling, such as h1 for large text:

<article>
  <p>
    Here is some
    <h1>Large Text</h1>
  </p>
</article>
Instead, you should choose the appropriate element for your document structure and use CSS to achieve the styling you'd like.

Using the right hierarchy is important for accessibility. Assistive technologies, like screen readers, rely on the structure of a web page to determine how to parse and announce that web page to the user. Using an h3 element after an h1 might cause a screen reader user to believe they have accidentally skipped over important content, due to the lack of an h2 element.

Proper structure is also important for SEO. Search engines use automation to parse the content of your web page and determine when and where it should show up in results. If your structure is malformed, search engines may not be able to rank you very well in the relevant search results.

Finally, depending on how incorrect your structure is, your HTML may not even be technically valid. When this happens, the web browser has to effectively guess what you meant to do. And what it guesses might not even be what you want at all.

As you have learned today, there are many reasons to use the proper structural hierarchy for your page. Keep this in mind as you build new projects.

## What Is the Difference Between Presentational and Semantic HTML?
Presentational HTML focuses on the appearance and style of the content. In the early days of HTML, developers would use elements like the center, big, and font elements. But in modern web development you shouldn't use these types of elements, because of their limitations and negative impact on accessibility and maintainability.

Many presentational HTML elements are deprecated, which means that they are outdated and no longer recommended. There are better ways to get the same results. However, it is helpful to know that they exist, so we'll take a look at some examples.

The font element is a deprecated element used to set the font size and color of the text. Here's an example of a font element:

<font size="5" color="blue">This text is blue and large.</font>
This example sets the color of the text to blue and the size to a value of 5. The range for the size attribute is from 1 to 7, with 1 being the smallest and 7 being the largest. The default value is 3, if you don't set the value explicitly.

While this element still works, you should not use it because the font size and color should always be set in CSS, not in HTML.

The center element is another deprecated element that is used to center the content horizontally within its container. Here's an example of the center element that contains text and a paragraph element:

<center>
  This text is centered.
  <p>HTML is awesome.</p>
</center>
In the browser, you would see all of the content within the center element centered horizontally.

And next, we have the big element. This is another deprecated presentational HTML element that makes the enclosed text one level bigger than its surrounding text. Here we have an example that defines a paragraph with two parts:

<p>
  This text has a normal font size.
  <big>This text is larger.</big>
</p>
The first part has normal sized text, while the second part enclosed within the big element will be displayed in a larger font size. In the browser, you would see the text within the big element looks larger compared to the surrounding text.

However, remember that font size should always be set with CSS, so you should not use this element in modern HTML.

These were examples of presentational HTML elements. But all of them are deprecated and no longer recommended. So what should you use instead? Let's see.

Semantic HTML is now the recommended practice. It describes the content of the elements, so it's much easier to read, understand, and maintain.

Search engines can easily understand your website when you use semantic HTML. It's also helpful for accessibility purposes, because screen readers need semantic information to describe what's on the web page.

Examples of semantic HTML elements include:

The header element for defining the header of the document, or section.
The navigation section element, nav, for sections with navigation links.
The section element for grouping related information.
The figure element for illustrations and diagrams.
This is an example of a header element that contains a navigation section element:

<header>
  <nav>
    <a href="#">Home</a>
    <a href="#">About</a>
    <a href="#">Contact</a>
  </nav>
</header>
The semantic elements clearly show their purpose within the HTML structure. There are many different semantic HTML elements. You will definitely find one that fits the needs of your project.

Great work. Now you know the difference between presentational and semantic HTML: semantic HTML describes the content, while presentational HTML focuses on the appearance.

