# Working With Forms

In these lectures, you will learn about forms, the role of labels, inputs and buttons in creating forms, client-side form validation, and form states.

## How Do Forms, Labels, and Inputs Work in HTML?
The form element in HTML is used to gather user information, such as names and email addresses. Here is an example of a form element:

<form action="url-goes-here">
  <!-- input elements go here -->
</form>
The action attribute specifies where the form data will be sent upon submission. To collect specific information, like names and email addresses, you would use the input element. Here is an example of using an input element:

<form action="">
  <input type="text" />
</form>
input elements are void elements and do not have closing tags. The type attribute defines the data type expected from the user. In this case, the data would be plaintext. To add a label for the input, you would use a label element. Here is an example of using a label element with the text of Full Name::

<form action="">
  <label>
    Full Name:
    <input type="text" />
  </label>
</form>
By nesting an input inside a label element, you create an implicit association between the label and the input field. The term "implicit" refers to something that is understood or inferred without needing to be explicitly stated or defined with additional attributes or elements. To explicitly associate a label with an input, you can use the for attribute. Here is an example of using the for attribute for an email address label:

<form action="">
  <label for="email"> Email Address: </label>
  <input type="email" id="email" />
</form>
When using an explicit association, the values for the for attribute and id need to be the same. In this case, the values are both set to email. The email type in the input provides basic validation for correctly formatted email addresses. If you want to show additional hints to the users about the expected input, you can use the placeholder attribute. Here is an example using the placeholder attribute inside the email input:

<form action="">
  <label for="email"> Email Address: </label>
  <input type="email" id="email" placeholder="Ex. example@email.com" />
</form>
For the placeholder text, you want to provide helpful short text to show the format and type of data you expect from your users. In this case, the placeholder text, Ex. example@email.com, shows the user that they must enter a correctly formatted email address.

## What Are the Different Types of Buttons, and When Should You Use Them?
The button element is used to perform a particular action when it is activated. Here is an example of a button element with the button text of Start Game.

<button>Start Game</button>
Other examples of using the button element include submitting a form, showing a modal, or toggling a side menu open and closed. The button element has a type attribute which controls the behavior of the button when it is activated. The first possible value for the type attribute would be the button type. Here is an example of using the button element with the button type and a text of Show Alert:

<button type="button">Show Alert</button>
By default, the button will not do anything when activated. However, you can add some JavaScript code to make the button interactive, such as showing an alert in this case. Another possible value for the type attribute is the submit value. Here is an example of using a button element with the submit type:

<form action="">
  <label for="email">Email address:</label>
  <input type="email" id="email" name="email" />
  <button type="submit">Submit form</button>
</form>
Inside this form element, there is a label and input element for the user's email address. When the user clicks on the submit button, their data will be sent to the server and will be processed. The third possible value for the type attribute is the reset value. Here is an example of a form element with reset and submit buttons:

<form action="">
  <label for="email">Email address:</label>
  <input type="email" id="email" name="email" />
  <button type="reset">Reset form</button>
  <button type="submit">Submit form</button>
</form>
In this modified example, a label and input element are used to collect the user's email address. When the user clicks on the reset button, then it will clear out all of their input data. It is important to note that reset buttons are usually not the best idea because they could lead to users accidentally resetting their data. Also, multiple buttons in your form could clutter up the user interface.

Another way to create buttons in HTML is to use the input element. The input element also has a type attribute with the possible values of submit, reset, and button. Here is an example of using the input element with the type set to button:

<input type="button" value="Show Alert" />
The value attribute is used to show the button text. So, what is the difference between using the input and button elements? input elements are void elements, which means they cannot have child nodes, such as text, and can only have a start tag. On the other hand, the button element offers more flexibility because you can nest text, images, and icons inside it.

## What Is Client-Side Form Validation in HTML Forms, and What Are Some Examples?
When a user fills out a form on your website, it is important that they fill out all of the necessary information in the correct format. HTML form controls, like inputs, have a lot of built-in validation that you can use to check for invalid data. This will help ensure that the user fixes these mistakes before the information is submitted and processed by the server.

The term "client-side" refers to everything that happens on the user's computer or device, like the part of a website or app you interact with directly. This includes the layout, design, and any interactive features.

The term "server-side" refers to everything that happens on the server, the computer, or system, that hosts the website or app. This includes processing data, running applications, and handling requests that come from the user's device.

While client-side validation is important, you also need server-side validation for added security. Malicious users can bypass client-side checks, so robust server-side measures are essential. You'll learn more about this in a later module. For now, let's take a look at some examples of client-side form validation.

One common example of built-in form validation is to use the required attribute in inputs. The required attribute specifies that the user needs to fill out that portion of the form before it gets submitted. Here is an example of using the required attribute in an email input:

<form action="">
  <label for="email">Email Address (Required field):</label>
  <input required type="email" name="email" id="email" />
  <button type="submit">Submit Form</button>
</form>
When the user clicks on the Submit Form button without supplying an email address, they will be alerted that the field is required and the form will not be submitted. Each browser will have its own set of styles for showing this alert message.

Another advantage of using the email input, is that email inputs have some basic validation to ensure correctly formatted email addresses. For example, if you type in random words and click submit, then the browser will show an alert that an @ sign is missing. It is important to note that browsers only check for basic validation for standard email addresses. It is up to you to add additional layers of validation, which you will learn about in later modules.

Other forms of validation for email inputs are to use the minlength and maxlength attributes. Here is an example using the extra validation:

<form action="">
  <label for="email">Email Address (Required field):</label>
  <input
    required
    type="email"
    name="email"
    id="email"
    minlength="4"
    maxlength="64"
  />
  <button type="submit">Submit Form</button>
</form>
The minlength and maxlength attributes are used to set the minimum and maximum length in characters for the email input. If you don't include the minimum length or exceed the max length of characters, the browser will show an alert message.

## What Are the Different Form States, and Why Are They Important?
In HTML, form controls, like inputs, can be in different stages or conditions like a focused state, readonly state, or disabled state.

The first state would be considered the default state. The default state of an email address input is a blank input. That is what the email input looks like when it is first rendered on the page. At this point, the user has not input any information.

When the user clicks on a form control or selects it with the keyboard's tab key, then that means it is in the focused state. When an input is in the focused state, most browsers will show a blue highlighted border around the input. But you can choose to add additional styles in CSS.

Another form state is the disabled state. This state shows users that an input cannot be focused or activated. To disable an input, you can add the disabled boolean attribute to the element like this:

<input disabled type="email" name="email" id="email" />
If the user tries to click on the input, then the focus will not be enabled. Similar to the focused state, you can choose to add additional styles for the disabled state using CSS.

Another type of form state is the readonly state. This is when a form control, like an input, is not editable by the user. Here is an example of setting an email input to read only:

<input
  readonly
  type="email"
  name="email"
  id="email"
  value="example@email.com"
/>
The value attribute is used to set the value shown inside the input field. If you tried to click on the input, you would not be able to edit the existing value.

A key difference between the disabled state and readonly state is that readonly can be focused while the disabled state cannot.

Understanding the different form states is important because they ensure a smooth user experience by providing clear feedback and guidance while handling errors.