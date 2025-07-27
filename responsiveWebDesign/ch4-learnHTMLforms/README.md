# Learn HTML Forms by Building a Registration Form

You can use HTML forms to collect information from people who visit your webpage.

In this course, you'll learn HTML forms by building a signup page. You'll learn how to control what types of data people can type into your form, and some new CSS tools for styling your page.

## CSS相对长度单位

### vh/vw 相对于视口的高度/宽度

The `vh` unit stands for viewport height, and is equal to 1% of the height of the viewport. This makes it relative to the viewport height.

### rem 相对根元素字体像素数

如果html标签的font-size: 16px,则1rem = 16px

The `rem` unit stands for root `em`, and is relative to the font size of the `html` element.

### em 相对自身字体像素数

如果div的font-size: 16px, 则p中1em = 16px

    <div>
    <p>this is a p</p>
    </div>

### %

相对于父元素的尺寸

## form 表单标签

### form & action attribute

### method

The `method` attribute specifies how to send form-data to the URL specified in the `action` attribute. The form-data can be sent via a GET request as URL parameters (with `method="get"`) or via a POST request as data in the request body (with `method="post"`).

### fieldset 区域集合标签

### label 标记标签

用于优化input标签的交互

Following accessibility best practices, link the input elements and the label elements together using the for attribute.

Use first-name, last-name, email, and new-password as values for the respective id attributes.

### input 输入标签

Specifying the `type` attribute of an `input` element is important for the browser to know what kind of data it should expect. If the `type` is not specified, the browser will default to `text`.

Give the first two input elements a type attribute of text, the third a type attribute of email, and the fourth a type attribute of password.

The `email` type only allows emails with a`@` and a `.` in the domain. The password type obscures the `input`, and warns if the site does not use HTTPS.

The first `input` element with a type of `submit` is automatically set to submit its nearest parent `form` element.

To handle the `form` submission, after the last `fieldset` element add an `input` element with the type attribute set to `submit` and the value attribute set to Submit.

use `minlength` attribute to set the min length of the input.

With `type="password"` you can use the `pattern` attribute to define a regular expression that the password must match to be considered valid.

Add a `pattern` attribute to the password `input` element to require the `input` match: `[a-z0-5]{8,}`

Users will be allowed to choose either a Personal or Business.

To do this, within each of the first two label elements, add one `input` element with `type="radio"`.

Currently users can submit the `form` without checking the `radio` inputs. Although you previously used the `required` attribute to indicate that an input is required, it won't work in this case because adding `required` to both inputs will convey the wrong information to users.

To solve this, you can provide context of what is needed by adding a `legend` element with text Account type (required) before the `label` elements within the second `fieldset`. Then add the `checked` attribute to the Personal input to ensure the form is submitted with the required data in it.

Well, the `input` type `file` allows just that. Add a label with the text Upload a profile picture: , and nest an input accepting a file upload.

Add another label after the first, with the text Input your age (years): . Then, nest an `input` with the type of `number`.

Next, add a `min` attribute to the `input` with a value of 13 because users under the age of 13 should not register. Also, users probably will not be over the age of 120; add a `max` attribute with a value of 120.

Now, if someone tries to submit the form with values outside of the range, a warning will appear, and the form will not submit. Give it a try.

### select 选择标签 & option 选项标签

select 选项框,必须设置name属性用于提交表单

option 选项，需要嵌套在select中，每个option标签必须要有value属性，用于提交表单

Adding a dropdown to the `form` is easy with the `select` element. The `select` element is a container for a group of `option` elements, and the `option` element acts as a label for each dropdown `option`. Both elements require closing tags.

Submitting the form with an option selected would not send a useful value to the server. As such, each option needs to be given a value attribute. Without which, the text content of the option will be submitted to the server.

### textarea 文本域标签

The `textarea` element acts like an `input` element of type `text`, but comes with the added benefit of being able to receive multi-line text, and an initial number of text rows and columns.

The `textarea` appears too small. To give it an initial size, you can add the `rows` and `cols` attributes.

### placeholder 占位符属性

To give Campers an idea of what to put in their bio, the `placeholder` attribute is used. The `placeholder` accepts a text value, which is displayed until the user starts typing.

### name 

With form submissions, it is useful, and good practice, to provide each submittable element with a `name` attribute. This attribute is used to identify the element in the form submission.

Except for the two radio inputs (which you have already named), give each submittable element a unique name attribute of your choosing.

## pseudo-class class 伪类选择器

The border of the last fieldset element looks a little out of place. You can select the last element of a specific type using the last-of-type CSS pseudo-class, like this:

    p:last-of-type { }

no space between p and last-of-type

## unset

That will select the last p element. Create a new selector that targets the last fieldset element and set its border-bottom to none.

Select only the .inline elements, and give them width of `unset`. This will remove the earlier rule which set all the input elements to width: 100%.

## attribute selector 属性选择器

To style the submit button, you can use an attribute selector, which selects an element based on the given attribute value. Here is an example:

    input[name="password"]

The above selects input elements with a name attribute value of password.