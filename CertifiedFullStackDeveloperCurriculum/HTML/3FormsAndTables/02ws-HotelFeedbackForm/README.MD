# Build a Hotel Feedback Form

In this workshop, you will build a Hotel Feedback Form.

You will practice working with labels, inputs, fieldsets, legends, textareas and buttons.

Step 1
In this workshop, you will practice working with HTML forms by building a Hotel Feedback Form.

Start by adding the <!DOCTYPE html> followed by an html element with a lang attribute of en.

Inside your html element, add a head element.

Step 2
Inside your head element, nest a meta element with the charset attribute set to the value "UTF-8".

Below that meta element, add a title element. The title element's text should be Hotel Feedback Form.

Step 3
To prepare to create some actual content, add a body element below the head element.

Step 4
For the introductory text, you will want to display the main title followed by a short note about leaving feedback.

Inside your body element, add a header element.

Inside the header element, add an h1 element. The h1 element's text should be Hotel Feedback Form.

Below your h1 element, add a p element. The p element's text should be Thank you for staying with us. Please provide feedback on your recent stay.

Step 5
Now, it is time to add the main element which represents the main content of the page.

Step 6
In the previous lectures, you learned how to work with the form element like this:

Example Code
<form method="value-goes-here" action="url-goes-here">
  <!-- inputs go inside here -->
</form>
The action attribute is used to specify where the form data should be sent when the form is submitted.

The method attribute is used to specify the HTTP method to use when sending the form data. The most common methods are GET and POST.

NOTE: You will learn about how HTTP methods work in later modules.

Inside your main element, add a form element with an action attribute set to "https://hotel-feedback.freecodecamp.org" and a method attribute set to "POST".

Step 7
Forms consist of inputs where users can input their data. You can group related inputs together using the fieldset element.

Here is an example of using a fieldset element:

Example Code
<form action="/example-url">
  <fieldset>
  <!-- inputs go inside here-->
  </fieldset>
</form>
Inside your form element, add a fieldset element.

Step 8
When working with fieldset elements, it is common to use a caption to describe the group of inputs. You can use the legend element for this.

Here is an example of using a legend element:

Example Code
<form action="/example-url">
  <fieldset>
    <legend>Personal Information</legend>
    <!-- inputs go inside here-->
  </fieldset>
</form>
Inside your fieldset element, add a legend element with the text Personal Information.

Step 9
In the previous lectures, you learned how to associate a label element with an input like this:

Example Code
<label for="name">Name:</label>
<input type="text" id="name" name="name">
The for attribute on the label element should match the id attribute on the input element. This is known as an explicit association.

Below your legend element, add a label element with the text of Name (required):. Set its for attribute to the value of "full-name".

Then below your label element, add an input element with no attributes. In the next steps, you will add the necessary attributes.

Step 10
When a user provides their full name, the input will accept plaintext.

In the previous lectures, you learned how to work with the type attribute like this:

Example Code
<input type="text">
For your existing input element, add a type attribute set to "text".

Also give the input element an id attribute with the value of "full-name".

Step 11
The name attribute is used to identify form data after it has been submitted to the server.

Here is an example of how to use the name attribute:

Example Code
<input type="email" name="email">
Add a name attribute to the input element with the value of "name".

Step 12
In the previous lectures, you learned how to work with the placeholder and required attributes like this:

Example Code
<input type="text" placeholder="Ex. John Doe" required>
For your existing input element, add a placeholder attribute with the value of "Ex. John Doe".

Also, add the required attribute to the input element.

Step 13
Your hotel feedback form should also collect an email address from the user.

Start by adding a new label element with the text Email address (required): to the form. Your label element should have a for attribute set to the value of "email".

Step 14
Next, add an input with the type of "email" below your email label. This input should have an id attribute set to the value of "email". Also, set the name attribute to the value of "email".

This input is also required, so make sure to add the required attribute.

Finally, add a placeholder attribute set to "example@email.com".

Step 15
input elements can have a size attribute. This attribute defines the number of characters that should be visible as the user types into the input. The value of size should be a non-negative integer greater than zero. If size is not specified, or is specified with an invalid value, the input will have the default width set by the browser.

Example Code
<label for="lastName">Last Name:</label>
<input id="lastName" name="lastName" type="text" size="10" />
Give the name and email inputs a size attribute with a value of "20".

Step 16
Your hotel feedback form should have an option for users to add their age.

Start by adding a label element with the text Age (optional): to the form.

The for attribute should be set to "age".

Step 17
The number input is used to create a numeric input field.

Here is an example of a number input field:

Example Code
<input type="number" id="age" name="age" min="18" max="100">
The min and max attributes are used to set the minimum and maximum values that can be entered in the input field.

Below your label element, add an input with the type attribute set to "number" and an id of "age".

The name attribute should be set to "age", the min attribute should be set to "3" and the max attribute should be set to "100".

Step 18
The next section in the form will be responsible for asking users if they have stayed at the hotel before.

Start by adding a fieldset element.

Inside the fieldset element, add a legend element with the text of Was this your first time at our hotel?.

Step 19
If you want users to select one option from a list of options, you can use a set of radio buttons.

Here is an example of two radio buttons:

Example Code
<input type="radio" id="yes" name="first-time">
<label for="yes">Yes</label>
<input type="radio" id="no" name="first-time">
<label for="no">No</label>
In this example, the radio buttons are grouped together by using the same name attribute value. This means that only one radio button can be selected at a time.

Below your legend element, add a label element with the text Yes and a for attribute set to "yes-option".

Below your label element, add a radio button with the id set to "yes-option", and the name attribute set to "hotel-stay".

Step 20
Below your first radio button, add another label element with the for attribute set to "no-option". The text for the label should be No.

Below your second label element, add a radio button with the id set to "no-option", and the name attribute set to "hotel-stay".

When you are finished, you can now try out the radio buttons by selecting one option at a time.

Step 21
The next section of the form will ask users why they chose that particular hotel. Users will have the opportunity to select multiple options.

Start by adding another fieldset element.

Inside the fieldset element, add a legend element with the text Why did you choose to stay at our hotel? (Check all that apply).

Step 22
When you want a user to select multiple options from a list, you can use checkboxes.

Here is an example of how to work with checkboxes dealing with food options:

Example Code
<fieldset>
  <legend>Food Options</legend>
  <label for="pizza">Pizza</label>
  <input type="checkbox" id="pizza" name="food" value="pizza">
  <label for="burger">Burger</label>
  <input type="checkbox" id="burger" name="food" value="burger">
</fieldset>
The value attribute is used to specify the value that will be sent to the server when the form is submitted.

Below your legend element, add a label element with the text of Social Media Ads. The for attribute should be set to "ads".

Below your label element, add a checkbox input with the id, name and value attributes set to "ads".

Step 23
Add another label with the text of Personal Recommendation. The for attribute should be set to "recommendation".

Below the label element, add another checkbox input with the id, name and value attributes set to "recommendation".

Step 24
Next, add another label element with the text of Location and the for attribute set to "location".

For the checkbox input, the id, name and value attributes should be set to "location".

Below that input element, add another label element with the text of Reputation and the for attribute set to "reputation".

For the checkbox input, the id, name and value attributes should be set to "reputation".

Step 25
To make a checkbox input checked by default, you can add the checked attribute.

Here is an example of using the checked attribute:

Example Code
<input checked type="checkbox" id="checked" name="checked">
Add the checked attribute to the checkbox input with the id of "reputation" to make it checked by default.

Step 26
For the final label and input inside this fieldset, you will add a label element with the text of Price and the for attribute set to "price".

The checkbox input should have the id, name and value attributes set to "price".

Now you can test out your form by selecting the various checkboxes.

Step 27
The next section of the form will provide users with the ability to leave a rating for the hotel.

Start by adding a new fieldset element with a legend element nested inside. The legend should have the text Ratings.

Below the legend element, add a label element with the text How was the service?. The for attribute should be set to "service".

Step 28
When you want users to make selections from a dropdown menu, you can use the select and option elements.

Here is an example of using the select and option elements to create a dropdown for different cities:

Example Code
<label for="city">Choose a City: </label>
<select id="city" name="city">
  <option value="new-york">New York</option>
  <option value="los-angeles">Los Angeles</option>
  <option value="chicago">Chicago</option>
  <option value="miami">Miami</option>
</select>
Start by adding a select element with the name and id attributes set to "service".

Step 29
Inside your select element, add the following five option elements with these corresponding values for the option text and value attribute:

Value Attributes:

poor
satisfactory
good
very-good
excellent
Option Element Text:

Poor
Satisfactory
Good
Very Good
Excellent

Step 30
To make an option selected by default, you can add the selected attribute to the option element you want to be selected.

Here is an example using the selected attribute:

Example Code
<option selected value="amazing">Amazing</option>
Inside your select element, add the selected attribute to the option element with the value of "excellent".

Step 31
Your hotel feedback form should also give users the ability to rate the food.

Start by adding a label element with the text of How was the food?. That label element should have a for attribute set to "food".

Below your label element, add a select element with an id and name set to "food".

Step 32
Inside your select element, add the following five option elements with these corresponding values for the option text and value attribute:

Value Attribute:

poor
satisfactory
good
very-good
excellent
Option Text:

Poor
Satisfactory
Good
Very Good
Excellent
Don't forget to add the selected attribute to the option element with the value of "excellent".

Step 33
The last section of the form will allow users to provide any additional feedback they like about the hotel.

Start by adding a label element with the text of Other Comments? and a for attribute set to "comments".

Step 34
If you want users to have more space to write their comments, you can use a textarea element.

The textarea element is a multi-line text input control that allows users to enter text that is longer than a single line. It can be used to create a comment box, a message input, or other text input that requires multiple lines.

Here's an example of a textarea element:

Example Code
<textarea id="comments" name="comments" rows="4" cols="50"></textarea>
The rows attribute is used to specify the visible height of the textarea, and the cols attribute is used to specify the visible width of the textarea.

Below your label element, add a textarea element. In the next step, you will add the necessary attributes.

Step 35
For your textarea element, add an id and name attribute with the value of "comments".

For the cols attribute set the value to 30 and for the rows attribute set the value to 10.

Step 36
For the last step in the hotel feedback form workshop, you will need to add a submit button to the form.

Remember that you learned how to work submit buttons in the previous lectures.

Add a button element with the type attribute set to "submit" and the text content set to Submit.

And with that, your hotel feedback form is complete!