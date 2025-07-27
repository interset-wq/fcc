# ch1 CatPhotoApp

## Abstract

HTML tags give a webpage its structure. You can use HTML tags to add photos, buttons, and other elements to your webpage.

In this course, you'll learn the most common HTML tags by building your own cat photo app.

## Note

### 文档声明

`<!DOCTYPE html>` 放在HTML文件所有代码的最前面，说明此文件是使用HTML5编写的

All pages should begin with `<!DOCTYPE html>`. This special string is known as a declaration and ensures the browser tries to meet industry-wide specifications.

`<!DOCTYPE html>` tells browsers that the document is an HTML5 document which is the latest version of HTML.

Add this declaration as the first line of the code.

### html

html是HTML文件最大的标签，除了文档声明之外，所有代码都要嵌套在html标签中

属性attributes：

- `lang` 设置网页使用的语言，请认真使用这个属性，避免浏览器总是提示翻译

Notice that the entire contents of the page are nested within an `html` element. The `html` element is the root element of an HTML page and wraps all content on the page.

You can also specify the language of your page by adding the `lang` attribute to the `html` element.

Add the `lang` attribute with the value `en` to the opening html tag to specify that the language of the page is English.

### head

直接嵌套在html内，head中所有的内容都不会在网页中显示

Notice that everything you've added to the page so far is inside the body element. All page content elements that should be rendered to the page go inside the body element. However, other important information goes inside the `head` element.

The `head` element is used to contain metadata about the document, such as its title, links to stylesheets, and scripts. Metadata is information about the page that isn't displayed directly on the page.

Add a `head` element above the `body` element.

### title

只能嵌套在head中，网页在浏览器页签上的标题

The `title` element determines what browsers show in the title bar or tab for the page.

### meta 元标签（空标签）

网页元信息，只能嵌套在head中，并且head中常常嵌套一个或多个meta

属性attributes：

- `charset` 字符编码 `charset="utf-8"`

You can set browser behavior by adding `meta` elements in the `head`.

Inside the `head` element, nest a `meta` element with an attribute named `charset`. Set to the value to `utf-8` which tells the browser how to encode characters for the page.

Note that the `meta` element is a void element.

### Comment 注释

Commenting allows you to leave messages without affecting the browser display. It also allows you to make code inactive. A comment in HTML starts with `<!--`, contains any number of lines of text, and ends with `-->`.

### h 标题标签

heading 标题

The `h1` through `h6` heading elements are used to signify the importance of content below them. The lower the number, the higher the importance, so `h2` elements have less importance than `h1` elements.

> [!NOTE]
> Only use one `h1` element per page and place lower importance headings below higher importance headings.

### p 段落标签

paragraph 段落

The `p` element is used to create a paragraph of text on websites. 

### main 主要内容标签

HTML5新特性，用于SEO优化

HTML5 has some elements that identify different content areas. These elements make your HTML easier to read and help with `Search Engine Optimization (SEO)` and accessibility.

The `main` element is used to represent the main content of the body of an HTML document. Content inside the `main` element should be unique to the document and should not be repeated in other parts of the document.

### img 图片标签（空标签）

image 图片

属性attributes：

- `src` 图片地址URL，source源
- `alt` 图片加载失败时，用于替代图片显示（加载成功时，不显示alt文字），alternate替代

You can add images to your website by using the `img` element. `img` elements have an opening tag without a closing tag. An element without a closing tag is known as a void element.

HTML attributes are special words used inside the opening tag of an element to control the element's behavior. The `src` (source) attribute in an `img` element specifies the image's URL (where the image is located).

All `img` elements should have an `alt` attribute. The `alt` (alternate) attribute's text is used for screen readers to improve accessibility and is displayed if the image fails to load.

### a 锚点标签

anchor 锚点，超链接

`a` 中可以嵌套其他标签，例如 `img`

属性attributes：

- `target` 锚点的打开方式
    - `target="_blank"` 新页签打开

You can link to another page with the anchor (`a`) element.

To open links in a new tab, you can use the `target` attribute on the anchor (`a`) element.

The `target` attribute specifies where to open the linked document. `target="_blank"` opens the linked document in a new tab or window.

Other types of content can also be turned into a link by wrapping it in anchor tags, such as `img` .

### section 分节标签

section 部分，章节 有语义使用 `section`，如果仅仅是分割不同的区域，这种语义不强的情况用 `div`

The `section` element is used to define sections in a document, such as chapters, headers, footers, or any other sections of the document. It is a *semantic element*（语义化标签） that helps with SEO and accessibility.

### ul 无序列表 & li 列表项 & ol 有序列表

- ul 无序列表 unordered list
- ol 有序列表 ordered list
- li 列表项 list item

`li` 必须要嵌套在 `ul` 或 `ol` 中

To create an unordered list of items, you can use the `ul` element.

The `li` element is used to create a list item in an ordered or unordered list.

The code for an ordered list (`ol`) is similar to an unordered list, but list items in an ordered list are numbered when displayed.

### figure 图表 & figcaption 图表标题

figure 图表（图片，视频，图表，代码块等）

figcaption 图表标题，类似与word中的题注，图表下面用于解释图表的文字

常常在 `figure` 中嵌套 `img` 和 `figcaption`

The `figure` element represents self-contained content and will allow you to associate an image with a caption.

A figure caption (`figcaption`) element is used to add a caption to describe the image contained within the figure element.

### em 强调标签

To place emphasis on a specific word or phrase, you can use the `em` element.

### strong 更强的强调

The `strong` element is used to indicate that some text is of strong importance or urgent.

### form 表单标签 & input 输入标签（空标签，行内元素） & button 按钮标签（行内元素） & fieldset 分组标签 & label 标记标签

#### form 表单

form 表单 用于收集用户信息

属性attributes：

- `action` 表单提交的url

The `form` element is used to get information from a user like their name, email, and other details.

The `action` attribute indicates where form data should be sent.

#### input 输入标签（空标签，行内元素）

input 输入 它的行为会随着 `type` 属性值的变化而变化

属性attributes：

- `type` 类型 控制input的行为
    - `type="text"` 默认值，文本输入框
    - type="radio" 单选按钮，单选按钮必须使用 `name` 属性和 `value` 属性，并且同一组的所有单选按钮 `name`的属性值必须相同，每个单选按钮的value属性值互不相同
    - type="password" 密码输入框
    - type="checkbox" 复选框，和单选按钮类似，必须使用 `name` 属性和 `value` 属性，并且同一组的所有复选框 `name`的属性值必须相同，每个单选按钮的value属性值互不相同，二者唯一的区别就是单选按钮只能选中一个选项，而复选框可以选中多个选项
- `name` 必须有这个属性，提交表单时需要这个属性
- `value` 必须有这个属性，提交表单时需要这个属性,提交时name和value属性值会作为?之后参数名值对
- `placeholder` 占位符，提示表单要输入的内容，常配合文本输入框使用
- `required` 将这个input设置为必填项，这个标签不需要值
- `checked` 配合单选按钮或复选框使用，将某个选项设置为默认选中，这个标签不需要值

The `input` element allows you several ways to collect data from a web form. Like img elements, `input` elements are a void element and do not need closing tags.

There are many kinds of inputs you can create using the `type` attribute. You can easily create a password field, reset button, or a control to let users select a file from their computer.

Create a text field to get text input from a user by adding the type attribute with the value `text` to the input element.

In order for a form's data to be accessed by the location specified in the `action` attribute, you must give the text field a `name` attribute and assign it a value to represent the data being submitted.

`placeholder` text is used to give people a hint about what kind of information to enter into an input.

To prevent a user from submitting your form when required information is missing, you need to add the `required` attribute to an input element.

here's no need to set a value to the `required` attribute. Instead, just add the word `required` to the input element, making sure there is space between it and other attributes.

When elements have multiple attributes, the order of the attributes doesn't matter.

Notice that both `radio` buttons can be selected at the same time. To make it so selecting one `radio` button automatically deselects the other, both buttons must have a `name` attribute with the same value.

If you select the Indoor radio button and submit the form, the form data for the button is based on its `name` and `value` attributes. Since your radio buttons do not have a `value` attribute, the form data will include `indoor-outdoor=on`, which is not useful when you have multiple buttons.

Add a `value` attribute to both radio buttons. For convenience, set the button's `value` attribute to the same `value` as its `id` attribute.

Forms commonly use checkboxes for questions that may have more than one answer. The `input` element with a `type` attribute set to `checkbox` creates a checkbox.

There's another way to associate an `input` element's text with the element itself. You can nest the text within a `label` element and add a `for` attribute with the same value as the `input` element's `id` attribute.

Add the `name` attribute with the value to the checkbox `input` element.

While you won't notice this in the browser, doing this makes it easier for a server to process your web form, especially when there are multiple checkboxes.

Like radio buttons, form data for selected checkboxes are `name` / `value` attribute pairs. While the `value` attribute is optional, it's best practice to include it with any checkboxes or radio buttons on the page.

Add a `value` attribute to each checkbox. For convenience, set each checkbox's `value` attribute to the same `value` as its `id` attribute.

In order to make a checkbox checked or radio button selected by default, you need to add the `checked` attribute to it.

There's no need to set a value to the `checked` attribute. Instead, just add the word `checked` to the input element, making sure there is space between it and other attributes.


#### button 按钮标签（行内元素）

button 按钮 创建一个可以点击的按钮，用于提交表单，点击按钮，表单就被提交到action指定的网址了

属性attributes：

- `type` 类型，和input类似，控制按钮的行为
    - `type="submit"` 默认值，提交按钮

The `button` element is used to create a clickable button.

both `input` and `button` elements are *inline elements*, which don't appear on new lines.

The button you added will submit the form by default. However, relying on default behavior may cause confusion. Add the `type` attribute with the value `submit` to the button to make it clear that it is a submit button.

You can use radio buttons for questions where you want only one answer out of multiple options.

#### label 标记标签

label 标记 用于将文字与 `input` 绑定，优化交互体验

属性attributes：

- `for` 用于绑定 `input`，使用这个属性时，需要绑定的input必须设置id属性，`for` 的属性值必须和要绑定的input的 `id` 的属性值相同

`label` elements are used to help associate the text for an `input` element with the `input` element itself (especially for assistive technologies like screen readers).

The `id` attribute is used to identify specific HTML elements. Each `id` attribute's value must be **unique** from all other `id` values for the entire page.

#### fieldset 分组标签

fieldset 区域集合 类似于tkinter中的LabelFrame

caption 表格标题标签

caption需要嵌套在fieldset或表格中，作为fieldset或表格的标题

The `fieldset` element (like LabelFrame of tkinter) is used to group related inputs and labels together in a web form. `fieldset` elements are block-level elements, meaning that they appear on a new line.

The `legend` element acts as a caption for the content in the `fieldset` element. It gives users context about what they should enter into that part of the form.

### footer 页脚标签

The `footer` element is used to define a footer for a document or section. A `footer` typically contains information about the author of the document, copyright data, links to terms of use, contact information, and more.

After the `main` element, add a `footer` element.

