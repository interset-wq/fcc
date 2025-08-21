# Introduction to ARIA,
In these lectures, you will learn about working with ARIA roles.

## What Is the Purpose of WAI-ARIA, and How Does It Work?
Making static content accessible can be relatively straightforward, but dynamic content can be more challenging. This is where WAI-ARIA comes in.

Let's look at what WAI-ARIA is, its purpose, how it works, and some examples.

WAI-ARIA stands for Web Accessibility Initiative - Accessible Rich Internet Applications. It's a specification that enhances accessibility for dynamic content and UI (User Interface) components.

Note that WCAG and WAI-ARIA are not the same. WCAG provides general guidelines for web accessibility, while WAI-ARIA offers specific rules for making dynamic and interactive content accessible for users of assistive technologies.

So, the primary purpose of WAI-ARIA is to improve accessibility for dynamic content and UI components that do not have native HTML equivalents.

WAI-ARIA works by introducing a set of attributes you can add to HTML elements to provide additional semantic information. These attributes are categorized into roles, states, and properties.

ARIA role defines the purpose of an element within a website or web app. Here is an example of setting the role to button for a div element.

<div role="button">Click Me</div>
By doing this you are indicating to assistive technology that the element is a button. Roles do not provide any functionality however. Merely giving this div a role of button will not make it act like a button. To make it look and behave like a button you would need to use CSS and JavaScript to get the desired result. It is always better to use the native button or input element with type="button" instead.

ARIA properties provide additional details about elements. For example, the aria-labelledby property lets you connect an element to a specific label:

<h2 id="header-id">About freeCodeCamp</h2>
<button id="button-id" aria-labelledby="header-id button-id">Learn More</button>
This will make the elements understandable and navigable for users of assistive technologies.

To get the best out of WAI-ARIA, try to stick with native HTML whenever possible since it generally provides more accessibility out of the box.

Use WAI-ARIA only when HTML falls short, and don’t forget to test with assistive technologies like screen readers, or have people with disabilities test your work. Also, make sure your WAI-ARIA states and properties update with the content in real time. Avoid overusing ARIA as it can be confusing many times.

## What Are ARIA Roles?
ARIA stands for Accessible Rich Internet Applications.

ARIA roles specify the semantic meaning of HTML elements. They're essential for making web content accessible to people who use assistive technologies, like screen readers.

HTML has semantic and non-semantic elements, based on whether they convey meaning about their content.

Many semantic HTML elements already have an ARIA role assigned by default. For example, the button element has a default ARIA role of button.

But non-semantic elements don't have a role. For example, screen readers will not know how to interpret the purpose of a div if you don't specify its role explicitly.

To specify the ARIA role of an element, you just need to add the role attribute, like this role="ARIA role", where value is the name of a role in the ARIA specification.

It is important to note that specifying a role on an element only does one thing: It informs assistive technology of the purpose of the element. It does not add any functionality or behavior to the element. If people expect a role to behave a certain way, it is up to you, the developer, to add that expected behavior. For example, adding a role of button to a div does not automatically make it clickable with a mouse or usable with a keyboard. It is the responsibility of the developer to add the expected behavior that allows the div to act like a button, and in most cases, it is just better to use the button element.

There are six main categories of ARIA roles:

Document structure roles
Widget roles
Landmark roles
Live region roles
Window roles
And Abstract roles
Let's take a look at them in more detail.

Document structure roles define the overall structure of the web page. With these roles, assistive technologies can understand the relationships between different sections and help users navigate the content.

However, most of the document structure roles are not used in modern web development because browsers already support equivalent semantic HTML elements, which should be prioritized whenever possible.

You should specify the roles that don't have an equivalent semantic element. For example: toolbar, tooltip, feed, math, presentation, none, and note.

There are other similar roles but these are the most commonly used ones. This is an example of a div with the math ARIA role. The div contains a mathematical equation.

<div role="math" aria-label="x squared + y squared = 3">
  x<sup>2</sup> + y<sup>2</sup> = 3
</div>
You'll also notice that the div has an aria-label attribute. The value of this attribute should be a string that represents the expression.

Widget roles define the purpose and functionality of interactive elements, like scrollbars.

Examples of widget roles include scrollbar, searchbox, separator (when focusable), slider, spinbutton, switch, tab, tabpanel, and treeitem.

Some of these roles have equivalent semantic elements. You should prioritize the semantic element over the role if there is one. For example, you should favor using the HTML button element over adding a role of button to a div.

Landmark roles classify and label the primary sections of a web page. Screen readers use them to provide convenient navigation to important sections of a page. You should use them sparingly to keep the overall layout simple and easy to understand. Examples of landmark roles are banner, complementary, contentinfo, form, main, navigation, region, and search. Each of these roles has a corresponding HTML equivalent, such as header, footer, aside, form, main, nav, section, and search. If you use the proper HTML elements to define the sections of your page then it is not necessary to explicitly add the role attribute to these elements.

Live region roles define elements with content that will change dynamically. This way, screen readers and other assistive technologies can announce changes to users with visual disabilities. These roles include: alert, log, marquee, status, and timer.

Window roles define sub-windows, like pop up modal dialogues. These roles include alertdialog and dialog. Please note that it is now considered a best practice to use the HTML dialog element and its associated JavaScript methods instead of manually creating a dialog.

And finally, we have abstract roles. These roles help organize the document. They're only meant to be used internally by the browser, not by developers, so you should know that they exist but you shouldn't use them on your websites or web applications.

With ARIA roles, you can create accessible and inclusive websites and web applications. They provide semantic information about the purpose and function of HTML elements.

Screen readers and other assistive technologies use this information to help users understand the content of your page and set expectations for how to use it, which helps ensure that everyone can have a great user experience.

## What Are the Roles of the aria-label and aria-labelledby Attributes?
It is important to make sure that all users, including those living with disabilities, can access websites without issues.

For people using screen readers, the aria-label and aria-labelledby attributes provide crucial information about page elements that might be unclear or invisible.

Let's look at what the aria-label and aria-labelledby attributes are and the roles they play in making the web accessible to people with visual impairments and related disabilities.

You'll notice both aria-label and aria-labelledby are prefixed with aria. So what does that mean? ARIA stands for Accessible Rich Internet Applications. It's a set of attributes prefixed with aria-, which lets developers communicate the purpose of elements to assistive technologies. The aria-label attribute is an invisible label for interactive elements. It adds a text label to an element that screen readers can read.

aria-label is especially useful for elements that do not have visible text but still need to be described by screen readers. For example, buttons with only icons often need aria-label to convey their purpose.

Here is an example:

<button aria-label="Search">
  <i class="fas fa-search"></i>
</button>
In this case, a screen reader may announce this button as Search, button, even though the button only contains an icon. The aria-label attribute tells screen readers what text to use in place of the icon.

If the button contained the text "Search" instead of an icon, then there would be no need for the aria-label attribute as the text would provide the label for the button.

For input elements, the aria-label attribute provides a label directly if there isn't a visible label associated with the input.

The aria-labelledby attribute does the exact same thing as the aria-label attribute, but instead of defining the text directly in the attribute, you use a reference to text that already exists on the page. The existing text must have an id attribute, which will be used for the reference value in the aria-labelledby attribute.

Here's an example:

<input type="text" aria-labelledby="search-btn">
<button type="button" id="search-btn">Search</button>
In this case, the text for the button is being used as the label for the search input. Screen readers will announce the input as something like Search, edit. If you later decide you want to change the button text to Find, the label for the input will automatically be updated to the new text since it is referencing the button text. Combining multiple id values into a single aria-labelledby attribute value is also possible. Here's how that works:

<div>
  <span id="volume-label">Volume</span>
  <span id="volume-details">Adjust the volume level</span>
  <input
    type="range"
    min="0"
    max="100"
    value="30"
    aria-labelledby="volume-label volume-details">
</div>
For the slider, the screen reader will look out for the content of the volume-label and volume-details elements and announce Volume Adjust the volume level.

You've seen that both aria-label and aria-labelledby attributes help screen readers understand what elements do. So, which one should you use? Since they both provide the same functionality, either can be used, but there may be a few advantages to using aria-labelledby over aria-label:

If someone is using a translation service to translate the content on your page, the text in an aria-label attribute may not always be translated.
Using aria-labelledby can also help prevent a mismatch between the visible label text and the invisible label for screen reader users since updating the visible text will automatically update the invisible label.
aria-labelledby can make it much easier to programmatically create complex invisible labels consisting of multiple sources of text.
One last note, do not use aria-label and aria-labelledby on an element at the same time. In this case, the invisible label for screen readers will always be determined by aria-labelledby and aria-label will be completely ignored.

## What Is the aria-hidden Attribute, and How Does It Work?
If you ever need to display content while at the same time hiding it from people who use assistive technology, like screen readers, you can use the aria-hidden attribute.

You just need to add it to the HTML element that you want to hide and set its value to true, like you can see over here: aria-hidden="true".

This attribute hides the element and all of its children from the accessibility tree, while keeping them visible on the page. Common use cases include:

Icons and images that only have a decorative purpose.
Duplicated content.
It is important to remember that aria-hidden only hides content from assistive technology, such as screen readers. If the content should be hidden from everyone, then you should not use aria-hidden to hide it. For example, a hamburger menu that is currently collapsed must be hidden from all keyboard users, not just screen reader users. In this case you could set the CSS display property to none on the menu to remove it from the DOM when it is collapsed.

You should never use aria-hidden to hide an element that is focusable with the keyboard. The aria-hidden attribute only removes the element from the accessibility tree. It does not remove it from the DOM. Thus, it will still be possible for screen reader users to tab to the element, but their screen reader will not announce the element, effectively causing them to focus on "nothing".

Here's an example where we hide an icon from the accessibility tree by adding the aria-hidden attribute with a value of true.

We only keep the text exposed to assistive technologies to avoid any confusion that may arise from the redundancy of having both an icon and text for the same purpose.

<button>
  <i class="fa-solid fa-gear" aria-hidden="true"></i>
  <span class="label">Settings</span>
</button>
You do not need to use aria-hidden when:

The HTML element already has a hidden attribute.
The element or the element's ancestor is already hidden with display: none.
The element or the element's ancestor is already hidden with visibility: hidden.
In these three cases, the element is already removed from the DOM and thus hidden from the accessibility tree, so the aria-hidden attribute is not necessary.

As with using any ARIA attributes, you should always test with assistive technologies, and preferably having people with disabilities test your work, to make sure that it's easy to understand, even with these hidden elements.

You should also know that setting aria-hidden to false will not expose the element to assistive technologies if any of its parents has this attribute set to true.

The aria-hidden attribute is used to hide elements from people who use assistive technology, such as screen reader users.

While it can be helpful for hiding purely decorative elements and duplicated content, it should be used sparingly to avoid hindering accessibility.

In general, all content and functionality available on the page should also be available to people using assistive technology. The use case for aria-hidden is very narrow and should be limited primarily to making the experience cleaner for screen reader users by removing purely decorative or duplicate information. Do not use aria-hidden to hide content that you don’t think screen reader users would be interested in. Screen reader users deserve to have access to all information on the page.

By following these best practices and testing the user experience, you can create inclusive online experiences for everyone.

## What Is the aria-describedby Attribute, and How Does It Work?
The aria-describedby attribute is used to provide additional information about an element to screen reader users by referencing existing content on the page. It creates a programmatic association between the element and the content (technically referred to as an accessible description), which screen readers can use to inform users of the additional information when they interact with the element.

The most common use for aria-describedby is to associate instructions and error messages with form inputs. Due to the various methods screen reader users have for navigating a page, they may miss these messages when navigating between inputs. Using aria-describedby helps ensure that they will hear them.

Let's take a look at a few examples to understand how it works. In this first example, we have a form element that accepts a password:

<form>
  <label for="password">Password:</label>
  <input type="password" id="password" aria-describedby="password-help" />
  <p id="password-help">Your password must be at least 8 characters long.</p>
</form>
We are using a label element for the Password text and associating that with the password input field.

We also have a paragraph element that describes the password requirements. We are using the aria-describedby attribute to associate the password input field with the password requirements in the paragraph element. When a screen reader user interacts with this input, their screen reader will announce the name of the input (Password) and may then also announce the password requirements. This is not an absolute guarantee however as some screen readers may not automatically announce the additional content, or may only announce it in specific circumstances. This is not uncommon. Each screen reader is different and handles ARIA attributes in their own way. This does not negate the use of aria-describedby, as it will benefit screen reader users in general.

Another good use case for the aria-describedby attribute is when you have a delete button. Here is an example of a delete button followed by a message describing what will happen when the button is clicked:

<button aria-describedby="delete-message">Delete</button>

<p id="delete-message">Warning! All deletions are permanent.</p>
Just like in the earlier example, we associate the delete button with the message using the aria-describedby attribute. The id value and the value of the aria-describedby attribute must match.

The aria-describedby attribute is a powerful attribute that can be used to help ensure that additional information about an element is provided to screen reader users when they interact with the element. It is most commonly used to associate instructions and error messages with form inputs in order to reduce the chance that screen reader users will miss these messages as they navigate the form.

