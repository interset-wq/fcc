# Working with Specialized Semantic Elements

In this lecture, you will learn about specialized semantic elements like u, s, code elements and more.

## How Do You Display Mathematical Equations and Chemical Formulas in HTML?
The superscript element is used to display a piece of text as a superscript. A superscript is a symbol or letter printed above the normal line of text.

Here is an example using the superscript element to illustrate exponents:

<p>2<sup>2</sup> (2 squared) is 4.</p>
In this example, the number 2 is wrapped in sup tags to represent the superscript inside the paragraph. In the browser, you would see that the second number 2 is smaller and slightly higher than the first number 2.

Common use cases for the superscript element would include exponents, superior lettering, and ordinal numbers. Here is an example using the superscript element for superior lettering:

<p>
  Monseigneur is often written as <strong>M<sup>gr</sup></strong>.
</p>
Superior lettering refers to letters written in superscript, usually to indicate abbreviations. The letters g and r are wrapped inside superscript tags to illustrate the abbreviation in this example.

It is important to note that the superscript element should only be used for typographical reasons. If you want style a piece of text with a raised baseline, then you should use CSS instead of the superscript element.

To represent chemical equations inside HTML, you would use the subscript element. This element uses a subscript which displays a lowered baseline using smaller text.

Here is an example of using the subscript element to show the chemical representation for carbon dioxide.

<p>CO<sub>2</sub></p>
The number two is wrapped inside sub tags to illustrate that the character should be a subscript.

Common use cases for the subscript element include chemical formulas, footnotes, and variable subscripts.

## How Do You Represent Computer Code in HTML?
The inline code element is used to represent short snippets of code inside text. Common use cases for the code element would be for technical articles and documentation pages.

Here is an example of using the code element to show a CSS code snippet:

<p>
  To set the text color to blue in CSS, use the following code:
  <code>color: blue;</code>
</p>
In this example, the CSS color property is used to set the text color to blue. By wrapping this code snippet inside <code> tags, it communicates to the browser that the text is a piece of inline code.

The browser will apply default styles for content inside of the code element. The default styling is a monospaced font.

The code element is meant to represent a single line of code. If you want to represent multiple lines of code, you will need to place a code element inside a preformatted text element.

The preformatted text element is used to represent preformatted text. Here is an example of using the preformatted text element to show a CSS declaration:

<pre>
  <code>
    body {
      color: red;
    }
  </code>
</pre>
When using the pre element, you will need to be mindful of spacing because it will display exactly as written inside the HTML document.

In the browser, you will see that the code is indented several spaces to the right. If you were to change the indentation in the code example, then you will see a difference in indentation on the screen.

When it comes to including code examples inside your HTML document, you should use the code element for short inline examples.

If you need to display longer code snippets, then you will need to use the pre and code elements.

## What Are the U, S, and Ruby Elements Used For, and How Do They Work?
The unarticulated annotation element, or u element for short, is used to represent inline text that has non-textual annotation applied.

Here is an example of using the u element to highlight various spelling errors:

<p>
  You can use the unarticulated annotation element to highlight
  <u>inccccort</u> <u>spling</u> <u>issses</u>.
</p>
In the example, the words incorrect, spelling, and issues are misspelled. The default styling for the u element is a black underline underneath the text.

In HTML4, the u element was used for styling purposes. But in HTML5, the u element should only be used to indicate that text has non-textual annotation applied.

If you want to style a piece of text with an underline, you should use CSS instead of HTML.

The strikethrough element, or s element for short, should be used to represent when text is no longer accurate or relevant. Here is an example of using the s element to show the cancellation of an activity:

<p><s>Tomorrow's hike will be meeting at noon.</s></p>

<p>Due to unforeseen weather conditions, the hike has been canceled.</p>
In this example, the first sentence is crossed out because the hike was canceled due to weather reasons.

The s element should never be used to just to show changes to a document. More appropriate elements in that case would be the deleted text element and the inserted text element.

The ruby element represents small text shown above or below the main text. It is typically used to show the pronunciation of East Asian characters. Here is the ruby element example from the MDN web docs page:

<ruby> 明日 <rp>(</rp><rt>Ashita</rt><rp>)</rp> </ruby>
The rp element, or ruby fallback parenthesis element, is used as a fallback for browsers lacking support for displaying ruby annotations.

The rt element, or ruby text element, is used to indicate text for the ruby annotation. This text is usually used for pronunciation, or translation details in East Asian typography.

While the ruby element can be used for other types of annotations, the most common use case is for East Asian typography.

