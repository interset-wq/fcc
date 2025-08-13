# Working with Text and Time Semantic Elements

In this lecture, you will learn about the importance of semantics in conveying meaning for text and time-related content including the time, blockquote elements and more.

How Do Block and Inline Quotes Work in HTML?
In HTML, quoted elements are used to distinguish quoted text from the surrounding content. This gives the quoted text a format that is easy to identify.

You should use the block quotation element for representing a section quoted from another source. It's mainly used for extended quotations. If the source of the quote has an address, you can cite it with the cite attribute. The value of this attribute should be a valid URL. This is an example of a quote within a block quotation element:

<blockquote cite="https://www.freecodecamp.org/news/learn-to-code-book/">
  "Can you imagine what it would be like to be a successful developer? To have built software systems that people rely upon?"
</blockquote>
This element has a cite attribute. The value of the cite attribute is the URL of the source. While this attribute doesn't change the presentation of the block quote, it's very helpful for giving screen readers and search engines more information about the quote. In the browser, you'll see that the text is slightly indented.

If you want to start and end the block quote with quotation marks, you may need to write them explicitly within the text. You can write the text directly within the block quotation element, like I just did, or wrap it within one or more paragraph elements. This is helpful when the text has multiple paragraphs, but you want to keep them within the same block quote. Here's an example with four paragraphs:

<blockquote cite="https://www.freecodecamp.org/news/learn-to-code-book/">
  <p>Build your projects. Show them to your friends. Build projects for your friends.</p>
  <p>Build your network. Help the people you meet along the way. What goes around comes around. You'll get what's coming to you.</p>   
  <p>It is not too late. Life is long.</p>
  <p>You will look back on this moment years from now and be glad you made a move.</p>
</blockquote>
All the paragraphs are contained within the same block quotation element, so they are part of the same quotation. You can see that the element has a cite attribute with the URL of the source. In the browser, you'll see that the four paragraphs are aligned relative to each other, but they are indented relative to their container.

So far I've been using the cite attribute to attribute the source of the quotation, but the attribute doesn't really show the source to the user. It only works behind the scenes.

If you want to attribute the source visually, you can add a citation element, cite, outside of the block quotation element. This is different from the cite attribute. The citation element is an HTML element that you can use to mark up the title of a referenced creative work like a book article, song, film, website, or research paper. Here's an example:

<div>
  <blockquote cite="https://www.freecodecamp.org/news/learn-to-code-book/">
    Can you imagine what it would be like to be a successful developer? To have built software systems that people rely upon?
  </blockquote>
  <p>—Quincy Larson, <cite>How to Learn to Code and Get a Developer Job [Full Book].</cite></p>
</div>
The block quotation element contains quoted text. Below the element you can see a paragraph element with the name of the author, followed by a citation element. The citation element contains the title of the book where the quotation came from.

If you go to the browser, now the source will be clearly visible and see that the quote comes from a book written by Quincy Larson. The title of this book is How to Learn to Code and Get a Developer Job.

You should use block quotes like these for long quotations from other sources. But sometimes you will only need to quote a few words within a larger paragraph.

That's exactly what the inline quotation element is for. It's for short inline quotations from other sources. Most modern browsers will add quotation marks around the inline quote automatically when you use this element. This is an example:

<p>
  As Quincy Larson said,
  <q cite="https://www.freecodecamp.org/news/learn-to-code-book/">
    Momentum is everything.
  </q>
</p>
You can see a paragraph element that contains text. Part of the text is an inline quote, because it's within the inline quotation element. You can also add a cite attribute to attribute the source.

This works exactly the same as it did with the block quotation element. There won't be any visual changes, but it will give screen readers and search engines more information about the quote.

In the browser, you'll see that the quoted text is part of the paragraph and it's surrounded by quotation marks. Most modern browsers will add these quotation marks automatically.

What's the difference between block quotes and inline quotes? You should use block quotes for extended quotations from other sources and inline quotes for short quotations from other sources that should be part of existing paragraphs.

## How Do You Display Abbreviations and Acronyms in HTML?
An abbreviation is a shortened form of a word. For example, "Dr" followed by a period, is an abbreviation for the word "doctor".

An acronym is a word formed from the initial letters of a phrase, with each letter representing the first letter of a word in that phrase. HTML is an example of an acronym. It stands for HyperText Markup Language.

By taking the first letters of each word H, T, M, and L, you get the acronym HTML. They are both very helpful for writing more concise text, especially when they are well-known and easy to understand in a given context.

If you need to display abbreviations and acronyms in HTML, the abbreviation element is exactly what you're looking for. You should always explain their full meaning when you use them for the first time. Then you can use the abbreviation element to highlight them and provide more details.

Here's an example where you can see a paragraph with the sentence HTML is the foundation of the web:

<p><abbr>HTML</abbr> is the foundation of the web.</p>
The acronym HTML is within an abbreviation element. In the browser, you'll see that nothing has really changed. It still looks like normal text. The abbreviation element is providing helpful context behind the scenes, but users will still see the acronym as normal text.

If you want to help users understand what this acronym means, you can show its full form with the title attribute.

The title attribute is optional, but if you decide to include it, it must be a human readable description of the abbreviation, or acronym.

Let's take the same example as before, but add the title attribute. It will be HyperText Markup Language, the expanded form of the acronym:

<p><abbr title="HyperText Markup Language">HTML</abbr> is the foundation of the web.</p>
Usually, the style of the abbreviation element will change when you add this attribute. The specific style will depend on the browser. Some browsers may display a dotted underline, while others may convert the contents to small caps, or even assign certain default styles, such as a dotted underline. When the user hovers over the acronym with the mouse, the full form is displayed as a tooltip.

While you don't necessarily need to use the abbreviation element for every abbreviation, or acronym on your web page, it's recommended for those that might be unclear and those that might need additional context.

You should use your best judgment to find the right balance between information and presentation to avoid cluttering the text while being clear and concise.

## How Do You Display Addresses in HTML?
The contact address element is used to represent contact information for a section on a web page. The address element is versatile and can be used for business pages, author pages, personal sites, and more.

When it comes to building out your website's contact sections, you should use the semantic address element over a generic element like a div.

Here is an example of using the address element for a company contact page:

<address>
  <h2>Company Name</h2>
  <p>
    1234 Elm Street<br />
    Springfield, IL 62701<br />
    United States
  </p>
  <p>Phone: <a href="tel:+15555555555">+1 (555) 555-5555</a></p>
  <p>Email: <a href="mailto:contact@company.com">contact@company.com</a></p>
</address>
In this example, there is the company name, physical address, phone, and email information. For the physical address, the line break element, br, is used to show the division between the street name, city, and country.

For the phone number, we have an anchor element with the href value set for telephone numbers. The tel:+ value inside the href attribute creates a clickable link to initiate a phone call on certain devices that support that.

For the email address, another anchor element is used with the href value set to a mailto link. mailto links are used in HTML documents to allow users to open a new email within their preferred email client.

One of the downsides of using a mailto link is that users often perceive it as spam. Unfortunately, a lot of spammers will use this option to send emails to users. So just keep that in mind when you're using it.

## How Do You Display Times and Dates in HTML?
The time element is used to represent a specific moment in time.

Here is an example using the time element to represent twenty hundred hours, or eight PM in the evening.

<p>The reservations are for <time datetime="20:00">20:00 </time></p>
The datetime attribute is used to translate dates and times into a machine-readable format.

This is important, because it helps with search engine results and helps the browser process date and time information more effectively.

The value for the datetime attribute must be either a valid year, valid month, valid time, local date, global date, or valid duration string.

Here is another example of using the time element to represent a particular date:

<p>
  The graduation will be on <time datetime="2024-06-15T15:00">June 15</time>
</p>
The value for the datetime attribute is in the ISO 8601 format. ISO 8601 is an international standard to represent dates and times.

The first part of that value is the year, month and day. The capital T in the value is a separator between the date and time.

The fifteen hundred hours would be three PM in the afternoon.

Whenever you need to represent events, publication dates, or appointments, it is best to use the time element.

