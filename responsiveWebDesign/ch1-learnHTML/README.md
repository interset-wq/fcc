# ch1 CatPhotoApp

## Abstract

HTML tags give a webpage its structure. You can use HTML tags to add photos, buttons, and other elements to your webpage.

In this course, you'll learn the most common HTML tags by building your own cat photo app.

## Note

### h

The `h1` through `h6` heading elements are used to signify the importance of content below them. The lower the number, the higher the importance, so h2 elements have less importance than h1 elements.

> [!NOTE]
> Only use one `h1` element per page and place lower importance headings below higher importance headings.

### p

The `p` element is used to create a paragraph of text on websites. 

### Commenting

Commenting allows you to leave messages without affecting the browser display. It also allows you to make code inactive. A comment in HTML starts with `<!--`, contains any number of lines of text, and ends with `-->`.

### main

HTML5 has some elements that identify different content areas. These elements make your HTML easier to read and help with `Search Engine Optimization (SEO)` and accessibility.

The `main` element is used to represent the main content of the body of an HTML document. Content inside the `main` element should be unique to the document and should not be repeated in other parts of the document.

### img

You can add images to your website by using the `img` element. `img` elements have an opening tag without a closing tag. An element without a closing tag is known as a void element.

HTML `attributes` are special words used inside the opening tag of an element to control the element's behavior. The `src` (source) attribute in an `img` element specifies the image's URL (where the image is located).

All `img` elements should have an `alt` attribute. The `alt` (alternate) attribute's text is used for screen readers to improve accessibility and is displayed if the image fails to load.

### a

You can link to another page with the anchor (`a`) element.

To open links in a new tab, you can use the `target` attribute on the anchor (a) element.

The `target` attribute specifies where to open the linked document. `target="_blank"` opens the linked document in a new tab or window.

Other types of content can also be turned into a link by wrapping it in anchor tags, such as `img` .

### section

The `section` element is used to define sections in a document, such as chapters, headers, footers, or any other sections of the document. It is a semantic element that helps with SEO and accessibility.

### ul & li & ol

To create an unordered list of items, you can use the `ul` element.

The `li` element is used to create a list item in an ordered or unordered list.

The code for an ordered list (`ol`) is similar to an unordered list, but list items in an ordered list are numbered when displayed.

### figure & figcaption

The `figure` element represents self-contained content and will allow you to associate an image with a caption.

A figure caption (`figcaption`) element is used to add a caption to describe the image contained within the figure element.

### em

To place emphasis on a specific word or phrase, you can use the `em` element.

### strong

The `strong` element is used to indicate that some text is of strong importance or urgent.

### form & input & button $ fieldset

The `form` element is used to get information from a user like their name, email, and other details.

The `action` attribute indicates where form data should be sent.

The `input` element allows you several ways to collect data from a web form. Like img elements, `input` elements are a void element and do not need closing tags.

There are many kinds of inputs you can create using the `type` attribute. You can easily create a password field, reset button, or a control to let users select a file from their computer.

Create a text field to get text input from a user by adding the type attribute with the value `text` to the input element.

In order for a form's data to be accessed by the location specified in the `action` attribute, you must give the text field a `name` attribute and assign it a value to represent the data being submitted.

`placeholder` text is used to give people a hint about what kind of information to enter into an input.

To prevent a user from submitting your form when required information is missing, you need to add the `required` attribute to an input element.

here's no need to set a value to the `required` attribute. Instead, just add the word `required` to the input element, making sure there is space between it and other attributes.

The `button` element is used to create a clickable button.

both `input` and `button` elements are *inline elements*, which don't appear on new lines.

The button you added will submit the form by default. However, relying on default behavior may cause confusion. Add the `type` attribute with the value `submit` to the button to make it clear that it is a submit button.

You can use radio buttons for questions where you want only one answer out of multiple options.

`label` elements are used to help associate the text for an `input` element with the `input` element itself (especially for assistive technologies like screen readers).

The `id` attribute is used to identify specific HTML elements. Each `id` attribute's value must be **unique** from all other `id` values for the entire page.

When elements have multiple attributes, the order of the attributes doesn't matter.

Notice that both `radio` buttons can be selected at the same time. To make it so selecting one `radio` button automatically deselects the other, both buttons must have a `name` attribute with the same value.

If you select the Indoor radio button and submit the form, the form data for the button is based on its `name` and `value` attributes. Since your radio buttons do not have a `value` attribute, the form data will include `indoor-outdoor=on`, which is not useful when you have multiple buttons.

Add a `value` attribute to both radio buttons. For convenience, set the button's `value` attribute to the same `value` as its `id` attribute.

The `fieldset` element (like LabelFrame of tkinter) is used to group related inputs and labels together in a web form. `fieldset` elements are block-level elements, meaning that they appear on a new line.

The `legend` element acts as a caption for the content in the `fieldset` element. It gives users context about what they should enter into that part of the form.

Forms commonly use checkboxes for questions that may have more than one answer. The `input` element with a `type` attribute set to `checkbox` creates a checkbox.

There's another way to associate an `input` element's text with the element itself. You can nest the text within a `label` element and add a `for` attribute with the same value as the `input` element's `id` attribute.

Add the `name` attribute with the value to the checkbox `input` element.

While you won't notice this in the browser, doing this makes it easier for a server to process your web form, especially when there are multiple checkboxes.

Like radio buttons, form data for selected checkboxes are `name` / `value` attribute pairs. While the `value` attribute is optional, it's best practice to include it with any checkboxes or radio buttons on the page.

Add a `value` attribute to each checkbox. For convenience, set each checkbox's `value` attribute to the same `value` as its `id` attribute.

In order to make a checkbox checked or radio button selected by default, you need to add the `checked` attribute to it.

There's no need to set a value to the `checked` attribute. Instead, just add the word `checked` to the input element, making sure there is space between it and other attributes.

### footer

The `footer` element is used to define a footer for a document or section. A footer typically contains information about the author of the document, copyright data, links to terms of use, contact information, and more.

After the `main` element, add a `footer` element.

### head

Notice that everything you've added to the page so far is inside the body element. All page content elements that should be rendered to the page go inside the body element. However, other important information goes inside the `head` element.

The `head` element is used to contain metadata about the document, such as its title, links to stylesheets, and scripts. Metadata is information about the page that isn't displayed directly on the page.

Add a `head` element above the `body` element.

### title

The `title` element determines what browsers show in the title bar or tab for the page.

### html

Notice that the entire contents of the page are nested within an `html` element. The `html` element is the root element of an HTML page and wraps all content on the page.

You can also specify the language of your page by adding the `lang` attribute to the `html` element.

Add the `lang` attribute with the value `en` to the opening html tag to specify that the language of the page is English.

### `<!DOCTYPE html>`

All pages should begin with `<!DOCTYPE html>`. This special string is known as a declaration and ensures the browser tries to meet industry-wide specifications.

`<!DOCTYPE html>` tells browsers that the document is an HTML5 document which is the latest version of HTML.

Add this declaration as the first line of the code.

### meta

You can set browser behavior by adding `meta` elements in the `head`.

Inside the `head` element, nest a `meta` element with an attribute named `charset`. Set to the value to `utf-8` which tells the browser how to encode characters for the page.

Note that the `meta` element is a void element.