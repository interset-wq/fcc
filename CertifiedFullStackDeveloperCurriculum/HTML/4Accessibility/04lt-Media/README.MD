# Working with Accessible Media Elements
In these lectures, you will learn about how to create accessible links, audio and video content.

## When Is the alt Attribute Needed, and What Are Some Examples of Good Alt Text?
Alternative text, often abbreviated as alt text, is a brief text description of an image. It provides essential information about the image for users who cannot see it, such as people who use screen readers and other assistive technologies.

It's essential for making websites accessible to people with visual disabilities.

Alternative text is also used by search engines to understand images. Some browsers may also display it when an image is not loaded properly. This can happen when the image file is missing or when the user has connectivity issues. So it's helpful for many different purposes.

A person with a visual disability will not be able to know what's in the image unless it's described in the alt text. An example of bad alt text for an image of a puppy would be "A cute puppy." This text is not specific enough to convey the important details of the image, like what does the puppy look like? Where is the puppy? Are there any important objects around the puppy?

Let's improve this. An example of good alternative text would be: "A black and white puppy with an orange collar lies on its belly in the sand, looking off to the side. A bright orange ball rests near its front paws."

Here you can see this in HTML with an image element, the alt attribute, and a more detailed description:

<img src="puppy.png" alt="A black and white puppy with an orange collar lies on its belly in the sand, looking off to the side. A bright orange ball rests near its front paws." />
It is important to note that there is no one correct way to write alt text for an image. What you include in your description will depend on the context the picture is used in. For example, if the puppy picture was on a website about dog breeds, you might want to include more specifics about the physical description of the puppy and possibly ignore the fact that the puppy is at the beach playing with an orange ball. Ultimately, the alt text you use for an image should reflect the primary purpose for including the image on the page, and the information you provide should give people who can't see the image the necessary details to understand that purpose.

Here we have another example of a beautiful tropical resort. Let's describe it.

An example of bad alt text for this image would be "Resort."

This is too short and it doesn't provide enough information about the image. To improve this description, you could expand it to include the most important elements of the image:

"Tropical resort featuring a swimming pool surrounded by palm trees and bungalows."

You can use the alt attribute in HTML like this:

<img src="resort.png" alt="Tropical resort featuring a swimming pool surrounded by palm trees and bungalows." />
Now that you know what makes good and bad alt text, let's see some of the best practices.

You should try to keep alt text short. It should be detailed enough to understand the image but not so long that it becomes confusing.
You should not try to describe every little detail. Focus on the most important aspects of the image.
Generally, you don't need to start with "image of" or "picture of." You can just start the description directly.
Also, if there's similar text around the image, you don't need to write it again.
It's usually recommended to end the alt text with a period for consistency.
If the image is a link to another page, instead of describing the image itself, the alt text should describe what will happen if users click on it.
For example, if your website has a right arrow icon that takes the user to the next page, instead of writing an alt text that only says "right arrow", like in this example, where you can see the alt attribute with this description:

<a href="about.html">
  <img src="arrow-right.png" alt="Right arrow." />
</a>
You should write something like this instead, where the alt text describes what will happen if users clicks on the image. They will go to the next page.

<a href="about.html">
  <img src="arrow-right.png" alt="Go to next page." />
</a>
Only images that convey important information should have alt text. If an image is only used for decorative purposes, it should have null (empty) alt text, so it can be ignored by screen readers and other assistive technologies.

Here is an example of an empty alt attribute is empty:

<img src="decorative_image.jpg" alt="" />
Every image on your website should have an alt attribute, even if it's empty. If you omit the alt attribute completely, some screen readers will read the file name instead, which can be distracting for people who use assistive technologies, so this is not recommended.

Finally, before your website is live, you should carefully test if screen readers can read the alt text correctly.

Writing effective alt text is essential for creating accessible web content. As a web developer, by providing clear descriptions of your images, you can make sure that everyone can engage with your website in an inclusive online experience.

## What Are the Accessibility Benefits for Good Link Text, and What Are Examples of Good Link Text?
Let's take a look at the benefits of writing good link texts in the context of accessibility, and some examples of good link texts.

The first visible benefit of a good link text is that it makes it easier for everyone to find information quickly. Descriptive links help users know where they're headed and what they'll access. This ensures the user doesn't feel lost and improves the overall user experience.

For those using screen readers, a clear and descriptive link text is a must. Screen readers read the link text aloud, so a text like "Read our accessibility guide" is way better than "Click here."

Making link text clear and descriptive isn't just beneficial for those living with visual impairments. Descriptive links also help people with cognitive disabilities by providing clear context.

Here are some best practices to keep in mind while writing link texts:

Make sure links are visually distinct by using underlining and other visual cues, so users can easily identify and navigate them.
Avoid generic link texts like "here", "click here", and "more-info" as they don't provide any useful information.
Aim for concise and descriptive link texts, ideally between 2-5 words, that convey the link's purpose.
Avoid jargon and abbreviations that users may not understand.
Focus on the destination, not the action. For example, "user behavior results", instead of "click here to read more".
Don’t repeat the same link text for different destinations.
Place links in a way that they make sense within the surrounding text. For example, "for more details, visit our events page" instead of "Click here for more".
Here are some examples of good link texts for specific use cases, compared to less helpful ones. Let's say you want to link to a page providing details about an event like this:

<a href="webinar-details-link">Details</a>
Details is vague and doesn’t provide specific information about what the user will find if they click the link. Without additional context, users might not know if the link leads to details about a webinar, a product, a policy, or something else.

Now, here is an example of good link text:

<a href="webinar-details-link">
  Get details about our upcoming webinar
</a>
This link text gives users context about the content they will find, making it easier to decide whether they want to click on it. It reduces ambiguity by specifying that the link is related to a webinar.

Here is an another example linking to a post in a blog:

<a href="/blog-post-link">Read more</a>
The link text Read more is not ideal in terms of accessibility because it lacks context.

Here is a better link text example:

<a href="/blog-post-link">
   Read our latest blog post on web accessibility
</a>
This updated link text provides users with a clearer idea of what to expect and why they might want to click the link, which is particularly important for those using screen readers.

Let's take a look at one more example. Let's say you want to provide more information about a certain topic:

<a href="/link-to-topic">More info</a>
More info is also vague and can be problematic for accessibility. It doesn't provide specific details about the link's destination, which can be confusing for users relying on screen readers or those who might be navigating the site in a non-linear way.

Here is a better example for link text:

<a href="/link-to-topic">
   Learn more about our accessibility efforts
</a>
This updated link text is better because it clearly describes what the user will find if they click the link. Users can immediately understand that the link leads to information about your accessibility efforts.

## What Are Good Ways to Make Audio and Video Content Accessible?
Multimedia, especially video, has become the go-to format for sharing information online.

With this surge in content, there's a growing need to ensure everyone can access and enjoy video and audio content online, irrespective of their abilities or environment.

Making your audio and video content accessible isn't just a nice-to-have, it's essential for reaching a wider audience. Let's look at some inexpensive ways to make your video and audio content more accessible.

A video is not just about visuals but also audio, so the first thing you should consider doing is adding captions or subtitles to your video content.

Captions provide the text version of spoken words and important non-verbal sounds, like music or laughter, synchronized with the video.

Subtitles on the other hand are essential for people who don't understand the language you're speaking. This helps not only people who are deaf or hard of hearing but also those watching videos in noisy or quiet environments.

To add captions or subtitles to your video or audio content, you can use the track element inside your video or audio element:

<!-- Video -->
<video controls src="video.mp4">
  <track
    src="captions.vtt" 
    kind="captions"
    srclang="en"
    label="English" 
  />
</video>

<!-- Audio -->
<audio controls src="audio.mp3">
  <track
    src="captions.vtt"
    kind="captions"
    srclang="en"
    label="English"
  />
</audio>
The kind attribute is used to tell the track element how it should be used. Valid values for the kind attribute include captions, subtitles, chapters, and metadata.

The srclang attribute represents the language for the track content. The label attribute is a descriptive title for the text track that browsers use to identify and display it in the list of available text tracks.

Another important thing to consider is providing a transcript for your audio and video content. A transcript is a text version of all the spoken words in your audio or video. Unlike captions, transcripts don’t need to be synchronized with the media. Transcripts are useful for deaf people and those hard of hearing. They're also beneficial for people who prefer reading instead of watching or listening. Transcripts also make your content searchable, allowing users to quickly find specific parts of your audio or video. If you have a video or audio on a website, you can simply add the transcript below the audio or video:

<audio controls>
  <source src="audio.mp3" />
  Your browser does not support the audio element.
</audio>

<!-- Transcript -->
<h3>Transcript</h3>
<p>
  [Speaker 1]: Welcome to the tutorial on making accessible content
</p>
<p>
  [Speaker 2]: Today, we'll cover captions, transcripts, and more.
</p>

<!-- Rest of transcript -->
If you're publishing videos on a video-sharing platform like YouTube or Vimeo, they have automatic captions and transcripts for videos. But if you're not satisfied, you can use services like veed.io, Rev, Amara, and Descript.

Other ways to make your video and audio content accessible include:

Adding a sign language overlay for videos for deaf people and those hard of hearing.
Providing volume and speed controls.
Ensuring good contrast for on-screen text.
Offering multiple formats.

## What Are Some Ways to Make Web Applications Keyboard Accessible?
Many users rely on keyboards instead of mice due to physical disabilities, repetitive strain injuries, or personal preference. This includes users of screen readers and those who may not have a working mouse. Keyboard accessibility ensures these users can navigate web applications effectively without barriers.

Let's look at some practical techniques you can employ to make web applications keyboard accessible.

Many users rely on the Tab key to move through interactive elements on a webpage. By default, browsers let users tab through elements like links, buttons, and form fields in the order they appear in the HTML. This is called the natural tab order.

Sometimes, you may want to adjust which elements are focusable or change their focus order. The tabindex attribute allows you do this.

Here is the basic syntax:

<element tabindex="number">Element Text</element>
The value of tabindex determines how the element behaves in keyboard navigation:

tabindex="0": Adds the element to the natural tab order. For example:

<button>First</button>
<div tabindex="0">Second</div>
<a href="#">Third</a>
Tabbing will move focus from the button to the div, then to the link, following their order in the HTML.

tabindex="-1": Makes an element focusable programmatically. This is useful for managing focus in elements that are not normally focusable, such as headings, containers, dialogs, or error messages:

<p tabindex="-1">Sorry, there was an error with your submission.</p>
In this example, the paragraph is not part of the normal tab order, so users cannot reach it by pressing the Tab key. However, if you set focus to this element via a script, the message will be brought to the user's attention. You'll learn more about this technique in JavaScript lectures.

tabindex greater than 0: Sets a custom tab order, so elements with lower positive values are focused first:

<input tabindex="2">
<input tabindex="1">
<input tabindex="3">
In this example, tabbing will focus the input with tabindex="1" first, then 2, then 3, regardless of their order in the HTML.

Custom positive values are sometimes used in complex widgets, such as a toolbar where you want a specific navigation order. However, this approach is discouraged because it can make navigation confusing and hard to maintain, especially as the page grows or changes.

accesskey is another attribute you can use to make your web project keyboard accessible. It allows you to define a key that focuses on or activates a particular element:

<button accesskey="s">Save</button>
<button accesskey="c">Cancel</button>
<a href="index.html" accesskey="h">Home</a>
In the above code:

accesskey="s" assigns the key S to the Save button. On most browsers, pressing ALT + S (on Windows) and CTRL + Option + S (on Mac) will activate this button.
accesskey="c" sets the key C to the Cancel button, allowing users to activate it using ALT + C (Windows) and CTRL + Option + C (Mac).
accesskey="h" assigns the key H to the Home link, allowing users to navigate to the homepage using ALT + H (Windows) and CTRL + Option + H (Mac).
Please note that the exact key combination to activate the accesskey might vary depending on the browser and operating system. It's typically ALT + Specified Key on Windows and CTRL + Option + Specified Key on Mac.

Another way to make the keyboard accessible in your apps is to make sure you provide clear focus indicators. If you feel the default browser focus indicator is not enough, you can override it by targeting the focus state of the element.

Here is an example of styling the focus state for an HTML element:

element:focus {
  outline: 2px solid #005fcc;
}
The outline property is used to define the outline around the element. This example sets the outline to a solid blue line with 2 pixels set for the thickness. The focus indicator should be styled in a way that makes it obvious which element currently has focus. In order to be accessible, the indicator must have a minimum color contrast of at least 3:1 with the background color it covers.

You should also avoid keyboard traps, which occur when a user cannot move focus away from a certain element in components like modals and popups.

