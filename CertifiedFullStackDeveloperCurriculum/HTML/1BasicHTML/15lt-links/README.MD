# Working with Links

In these lectures, you will learn about links, the target attribute, different link states, absolute, and relative paths, and more.

## What Are the Different Target Attribute Types, and How Do They Work?
You may have seen the target attribute on anchor elements, or links. This important attribute tells the browser where to open the URL for the anchor element:

<a href="https://freecodecamp.org" target="_blank">Visit freeCodeCamp</a>
There are four important possible values for this attribute. Note that each value is preceded by an underscore.

The first value is _self, which is the default value. This opens the link in the current browsing context. In most cases, this will be the current tab or window.

The second value is _blank, which opens the link in a new browsing context. Typically, this will open in a new tab. But some users might configure their browsers to open a new window instead.

The third value is _parent, which opens the link in the parent of the current context. For example, if your website has an iframe, a _parent value in that iframe would open in your website's tab/window, not in the embedded frame.

The fourth value is _top, which opens the link in the top-most browsing context - think "the parent of the parent". This is similar to _parent, but the link will always open in the full browser tab/window, even for nested embedded frames.

There is a fifth value, called _unfencedTop, which is currently used for the experimental FencedFrame API. At the time of this lecture, you probably won't have a reason to use this one yet.

Selecting the right target value to control where your users end up is an important consideration when creating a website.

## What Is the Difference Between Absolute and Relative Paths?
A path is a string that specifies the location of a file or directory in a file system. In web development, paths let developers link to resources like images, stylesheets, scripts, and other web pages. There are absolute and relative paths - both are essential when specifying file locations within a file system. Let's look at the two so you can decide which one of them to use and when.

An absolute path is a complete link to a resource. It starts from the root directory, includes every other directory, and finally the filename and extension. The "root directory" refers to the top-level directory or folder in a hierarchy.

An absolute path also includes the protocol - which could be http, https, and file and the domain name if the resource is on the web. Here's an example of an absolute path that links to the freeCodeCamp logo:

<a href="https://design-style-guide.freecodecamp.org/img/fcc_secondary_small.svg">
  View fCC Logo
</a>
In this example, the protocol is https, the domain name is design-style-guide.freecodecamp.org, and the filename is fcc_secondary_small.svg.

Now, what if the resource you want to link to using an absolute path is on your local machine? Here's how to link to the about.html file with an absolute path:

<p>
  Read more on the
  <a
    href="/Users/user/Desktop/fCC/script-code/absolute-vs-relative-paths/pages/about.html"
    >About Page</a
    >
</p>
It looks like this because we are going into a folder called Users, then into a folder called user, then into a folder called Desktop, then into a folder called fCC, then into a folder called script-code, then into a folder called absolute-vs-relative-paths, then into a folder called pages to finally get the about.html file.

Here's what the absolute URL looks like in the browser address bar:

file:///Users/user/Desktop/fCC/script-code/absolute-vs-relative-paths/pages/about.html
The URL includes the protocol, file://. It also include the path, which looks like this: /Users/user/Desktop/fCC/script-code/absolute-vs-relative-paths/pages/, and represents the series of folders that lead to the file. And finally, it also includes the about.html, which is the filename and the extension.

Now, lets look at the relative path. A relative path specifies the location of a file relative to the directory of the current file. It does not include the protocol or the domain name, making it shorter and more flexible for internal links within the same website. Here's an example of linking to the about.html page from the contact.html page, both of which are in the same folder:

<p>
  Read more on the
  <a href="about.html">About Page</a>
</p>
So imagine you are on the contact.html page, and because the about.html page is in the same place, you simply get the filename. This is an example of using a relative file path.

So, which should you use and when; an absolute path or a relative path? Here are the rules you should follow:

Use absolute paths when linking to a resource hosted on an external website.

Use absolute paths when you need the link to a page or resource to work consistently regardless of the document location within the site.

Use relative paths when linking to resources within the same website.

Use relative paths if you want to keep your code cleaner and easier to maintain during development.

Use relative paths during local testing to ensure links work without an internet connection.

## What Is the Difference Between Slashes, a Single Dot, and Double Dot in Path Syntax?
You may have seen links like /public/logo.png, ./script.js, or ../styles.css before. But what do these special types of links mean? These are called file paths. There are three key syntaxes to know. First is the slash, which can be a backslash (\) or forward slash (/) depending on your operating system. The second is the single dot (.). And finally, we have the double dot (..).

The slash is known as the "path separator". It is used to indicate a break in the text between folder or file names. This is how your computer knows that naomis-files/ points to a directory of that same name, while naomis/files/ points to a files directory in the naomis directory.

A single dot points to the current directory, and two dots point to the parent directory. You will typically see a single dot used to ensure that the path is recognized as a relative path. Remember that you learned in a previous lecture about relative versus absolute paths before.

Double dots, however, are much more common to access files outside of the current working directory.

For example, given this file tree:

my-app/
├─ public/
│  ├─ favicon.ico
│  ├─ index.html
├─ src/
│  ├─ index.css
│  ├─ index.js
If your public/index.html file needed to load the favicon.ico file, you would use a relative path with a single dot to access the current directory: ./favicon.ico. If your public/index.html file needed to load the index.css file, you would use a relative path with double dots to navigate to the parent my-app directory first, then to the src directory, and finally to your file: ../src/index.css.

What Are the Different Link States, and Why Are They Important?
You may have seen a link on a web page become purple after you click it. This is because the state of the link has changed, so different styling gets applied. There are five different states a link can be in.

The first is the default state, which is :link. This state represents a link which the user has not visited, clicked, or interacted with yet. You can think of this state as providing the base styles for all links on your page. The other states build on top of it.

The second state is :visited, which applies when a user has already visited the page being linked to. By default, this turns the link purple - but you can leverage CSS to provide a different visual indication to the user. This is helpful to let someone know they have already read a portion of your documentation. Or, that the site is one they can trust because they have used it before.

The third state is :hover. This state applies when a user is hovering their cursor over a link. This state is helpful for providing extra attention to a link, to ensure a user actually intends to click it.

Then we have :focus. This state applies when we focus on a link.

And finally, we have :active. This state applies to links that are being activated by the user. This typically means clicking on the link with the primary mouse button by left clicking, in most cases. This state can be helpful for showing a user that the element they clicked on is interactive.

When you use these states to style your links, there is a specific order you need to write your CSS in: link, visited, hover, focus, then active.

You should now know how to give links in your page your own personal flair, while still providing the important information a user needs about the state of each link.