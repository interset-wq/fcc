# User Interface Design Fundamentals, Not started
In these lectures, you will learn about the fundamentals of user interface (UI) design. You will learn about the terms you need to know to communicate with designers, visual hierarchy, scaling, alignment, whitespace, and much more.

## What Are Common Design Terms to Help You Communicate with Designers?
As a developer, you may need to work closely with designers. If you understand basic design terminology专业术语, you'll have a shared vocabulary and you'll be able to participate in the design process more actively. This can make your workflow more efficient and result in a better user experience.

So let's dive in. We'll start with the term layout. Layout is how the visual elements are arranged on a page or screen to communicate a message. These elements may include text, images, and white space. The layout is like the blueprint of a design. Designers must consider the placement, size, and hierarchy层次结构 of each element.

The term that is closely related to layout is alignment. Alignment is how the elements are placed in relation to one another. Using alignment correctly is helpful for making the design look clean and organized. Designers create visual order by aligning elements along imaginary lines, edges, or a central point.

Great. Now let's talk about composition组合. Composition is the art of arranging elements to create a harmonious design. It determines how elements like images, text, and shapes relate to each other and contribute to the design in an artistic way. While layout mostly focuses on the placement of the elements, composition also considers the artistic impact that this placement will have in the overall design.

Composition is closely related to concepts of balance. Balance is how the visual weight is distributed within a composition. Designers aim to create an equilibrium均衡 through symmetrical对称的 or asymmetrical不对称的 arrangements. A balanced design feels harmonious.

Hierarchy is another important concept that you should know. Hierarchy establishes the order of importance of the elements in a design. It's about making sure the most important information is noticed first. You can implement a visual hierarchy with size, color, contrast, alignment, white space, and even typography字体设计.

To create clear distinctions between the elements, you can use contrast. Contrast is helpful for guiding user attention to what you want to emphasize. You can do this through variations in color, size, shape, texture, or any other visual characteristic. Strong contrast is also helpful for improving readability.

Another helpful term is white space. White Space, also known as "negative space"负空间, is the empty space in a design. It's the area surrounding the elements. You might be surprised to know that white space is not necessarily white. Actually, it can be space in any color or texture纹理. Its purpose is to improve the readability and enhance the visual hierarchy of a design.

These are general design concepts that you will find very often, but you may also find design terms that are more closely related to software development.

The user interface, also known as UI, is how humans interact with computers. A user interface includes the visual and interactive elements that users can see on their screens, like icons, images, text, menus, links, and buttons.

The user experience, also known as UX, is about how users feel when using a product or service. An application with a well-designed user experience is intuitive直观的, easy to use, efficient, accessible, and enjoyable. The user interface plays a key role in making the user experience as easy and enjoyable as possible, so they are very closely related.

These are some of the common terms that you should know to communicate with designers. With this knowledge, now you can take a more active role in the design process.

## How Do You Create Good Background and Foreground Contrast in Your Designs?
First, you may need to familiarize yourself with contrast. Contrast is the difference between two colors - or how easy it is to tell them apart.

Colors with a higher contrast will be more visually distinct, whereas colors with a lower contrast will be more visually similar. For example, black and white have a very high contrast ratio. Whereas light blue and light purple have less of a contrast.

Of course, in these examples the distinction might be made clearer because of the layout. But what about applying these colors to text? You can have the high contrast black text on a white background. And the low contrast purple text on a blue background.

But how do you determine what is a "good enough" contrast? You can't base it solely on how the text looks to you, as every user will have a different experience. Thankfully, the Web Content Accessibility Guidelines, or WCAG, provide a standard for this.

Text with a contrast ratio of 4.5:1 is considered the AA standard, which is the bare minimum you should follow to be accessible to most users. Text with a contrast ratio of 7:1 is considered the AAA standard, and ensures the best level of accessibility.

There are a number of websites that can check the contrast ratio between two colors, but most browsers will allow you to do this directly in the developer tools on your website.

Let's open the developer tools and inspect the text elements of the example site.

The black text on a white background has a contrast ratio of 21:1, which more than meets the AAA standard. The purple text on a blue background, however, has a contrast ratio of 1.48:1, which does not even meet the AA standard.

How can you fix this? Well, there are three aspects that impact the contrast ratio.

The first is the hue色调, which represents the general color type, like red, blue, orange. Let's shift to a hue that is further away from blue. In this case, let's use red.

Unfortunately, this change only brought the contrast ratio to 1.49:1, which means you need to change the saturation饱和度, or the "amount" of color present. Let's increase the amount of red in the text. That brings us much closer to the goal, with a 3.54:1 contrast ratio.

However, you can potentially get even closer by changing the last value, which is lightness. Lightness represents how much white is present in the color.

Let's decrease the lightness of the red. Now there is a much darker red against the light blue background, which brings the contrast ratio to 10.34:1.

You could continue to adjust the colors to find the balance between the visual effect you want and an accessible contrast ratio. But it is important to remember that accessibility should always take precedence优先.

## What Is the Importance of Good Visual Hierarchy in Design?
Visual hierarchy refers to the way you layout and display the content of your page to guide the viewer's attention.

A strong hierarchy can provide a clear path for the eye to follow, ensuring that the information you convey is consumed in the order that you intended.

Let's consider a basic page layout in which the HTML for the page is semantically correct, but the styling applied does not create a strong visual hierarchy.

If the font size isn't distinct, there is no visible indication of the document flow, although things are separated by headings.

To create a visual hierarchy, you should apply different font sizes to the heading tiers. You could also use something like a "callout标注 box" to highlight a specific section.

Visual hierarchy can also help increase your user conversion. For example, you can take advantage of the callout box to further draw attention to a Call to Action (CTA) button.

With the CTA button being visually tied to the work history section, it guides the user to the vital information and the action you want them to take based on that information.

Finally, your visual hierarchy can be important for conveying other components, like a navigation bar or a footer.

This makes it easier for your users to find the essential information that they may be looking for.

## How Does Scale缩放比例 Work in Design?
The "scale" of something refers to its size.

When you're looking at scaling in your web design, you're looking at the size relationships between different elements, and how these elements might adapt to different screen sizes.

Using the correct scale for your elements plays an important role in visual hierarchy. Larger elements will draw more attention, which can guide your users through the content in the way that you want.

For example, the visual separation between a heading and a paragraph draws your reader’s attention, but the scale should be appropriate to get an eye-catching text that pulls your reader to that section.

Scale doesn't apply just to text, though. It's also important for images. And while the scale of a banner image might make sense for a desktop layout, it might be too large on a mobile layout.

By scaling an image down to a more appropriate ratio, you can keep the visual impact while ensuring the information on the site is visible.

Scale is also important for interactivity, and the ability to actually use your website. If the text in a navigation bar is not at an appropriate scale, mobile phone users will have a hard time tapping on the links.

And if you scale it appropriately, you end up with links that are not only easier to read, but easier to click on for your mobile users.

There are many ways that scale is important in your designs. We've covered the basics, so you should now have a fundamental understanding of its importance.

## How Does Alignment Work in Design?
When you are designing web pages, it is important to create cohesive有结合力的 and visually appealing designs. One way to achieve this is through the use of alignment.

Alignment is the process of arranging text and images in a way that creates a visual connection between elements.

It helps to create a sense of order and organization on the page, making it easier for users to navigate and understand the content.

There are several types of alignment you can use, but the basic ones are:

left alignment
center alignment
right alignment
justified alignment
vertical alignment
Left, right, and center alignments are all subtypes of horizontal alignment, while vertical alignment is used to align elements along a vertical axis.

Let's take a closer look at each type of alignment and how you can use them in your designs.

Left alignment is commonly used with text where each element is aligned to the left margin. Aligning all of the headings and paragraphs on a web page to the left margin makes it easier for the user to read and follow the content.

The opposite of left alignment is right alignment, where each element is aligned to the right margin. This is often used on websites to display additional content like promotional推销的 banners or advertisements.

For example, an ad that is aligned to the right margin makes it stand out from the rest of the content on the page but doesn't distract the user from the main content.

Center alignment is where elements are centered on the page. This is often used for headings, logos, and other important elements that you want to draw attention to.

Justified alignment is when text is aligned to both the left and right margins. This is typically used for descriptive passages or articles, and creates a clean and professional look.

The last type of alignment is vertical alignment, which is used to align elements along a vertical axis.

Vertical alignment can be used, for example, for a contact form on a website. Aligning all of the form inputs like the name, email, and message fields along a vertical axis makes it easier for the user to fill out the form.

By using different types of alignment, you can create a sense of order and organization on the page that makes it easier for users to navigate and understand the content.

## What Is the Importance of Whitespace in Design?
White space refers to any type of space around elements like images, text, and buttons. White space is important in design because it helps to create a balance between the elements on the page.

Let's take a look at some examples of how white space can be used effectively in design.

For example, let's consider a call-to-action (CTA) button. CTAs are used to encourage users to take a specific action like signing up for a newsletter简讯 or making a purchase.

By using white space effectively, we can help to make a CTA button more prominent and encourage users to click on it.

Now let's take a closer look at the different types of white space.

This first example uses both macro巨大的 and active white space. Macro white space is the space between larger elements like images, text blocks, and buttons.

Active white space is the space that is intentionally created to help guide the user's eye and draw attention to certain elements on the page.

In contrast to active white space, there is also passive white space. Passive white space is the space that is left over after all the elements on a page have been placed.

Another type of whitespace would be micro white space. This is the space between individual characters in a line of text.

Micro white space is important because it helps to improve readability and legibility易读性, making it easier for users to scan and understand the content.

When designing your web pages, you always want to be mindful of the law of proximity接近. This law states that elements that are close together are perceived as being related, while elements that are far apart are perceived as being unrelated.

You can use white space to help group related elements together and help navigate users through the content on your page.

## What Are Best Practices for Working with Images in Your Designs?
Adding images to your websites is a great way to engage your users and increase the visual appeal of your site. But there are a few things to consider when working with images in your designs.

The first thing to consider is creating responsive images. Responsive images are images that scale to fit the size of the screen they are being viewed on. This is important because it ensures that your images look good on all devices, from desktops to mobile phones.

Another thing to consider is the resolution分辨率 for images. Higher quality images with better resolution have more pixels per inch. Pixels are small squares that make up an image.

Pixels per inch, or PPI, is the number of pixels in one inch of an image. The higher the PPI, the better the image quality.

You want to make sure that your images are high quality and look good on all devices. This means that you should use high resolution images that are optimized for the web.

Another thing to consider is the size of your images and how they fit within the spaces in the layout. You want to make sure that your images are the right size and are not too large or too small.

Using large images that are meant to fit in smaller spaces in the design can slow down your website and make it harder for users to load your site. You want to make sure that your images are the right size and are optimized for the web.

When it comes to image placement, you want to think about balance, hierarchy, and alignment to help ensure your images are optimized for the web.

Balance is the distribution of visual weight in a design. You want to make sure there is a good balance between text and images on the site so it creates a harmonious design.

Hierarchy is the order in which elements are viewed on a page. You want to make sure that images that align with important content are placed higher than images that are less important.

Alignment is the placement of elements in relation to each other. You want to make sure that your images are aligned with the text and other elements on your site so that it creates a cohesive有结合力的 design.

The last thing to consider is accessibility for images. You want to make sure that your images are accessible to all users, including those with visual impairments. This means that you should use alt text for your images so that screen readers can read the text to users who are visually impaired.

## What Is Progressive渐进的 Enhancement?
Progressive enhancement is a design approach that ensures all users, regardless of browser or device, can access the essential content and functionality of an application.

It focuses on delivering a core experience that works for everyone, while offering extra features and improvements to users with more advanced browsers or better internet connections.

The progressive enhancement approach lives by these core principles:

All core content and basic functionality should be accessible on all browsers
All advanced layouts should be provided through external CSS stylesheets
All advanced functionality should be provided through external JavaScript files
A user's browser preferences should be respected
Using a progressive enhancement approach makes your applications more accessible because all core content and functionality should not be blocked in unsupported environments.

In terms of speed, a progressive enhancement approach can also help improve the performance of your applications.

Those users that are working with slower internet connection speeds will still be able to access the content because the browser will download the necessary resources first.

When it comes to SEO, progressive enhancement can also help improve the visibility of your applications.

Search engines will be able to crawl爬取 the content of your applications because the core content is available in the initial HTML response.

While some have criticized this approach deeming认为 that it is not always realistic for applications that rely heavily on JavaScript for their functionality, it is still a good practice to follow when building applications.

