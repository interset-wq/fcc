# Working with Images and SVGs

In these lectures, you will learn how to work with SVGs and learn about techniques for optimizing your images.

## What Are Common Ways to Optimize Media Assets?

There are three tools to consider when using media, such as images, on your web pages: the size, the format, and the compression.

Let's talk about the size of your images first. When you are building a website, you'll often style images to display in a specific size. For example, you might have an image display at a 640x480 resolution. 640 represents the width while 480 represents the height in pixels. When preparing your image you want to scale it to a 640x480 size to match that styling. If you serve an image that is 1920x1080 but you are styling it to be much smaller, you're requiring your users to download unnecessary data. A smaller resolution results in a smaller file size.

The next thing to consider is your file format. Two of the most common file formats are PNG and JPG, but these are no longer the most ideal formats for serving images. Unless you need support for older browsers, you should consider using a more optimized format, like WEBP or AVIF.

Finally, you can run compression algorithms on your images. A compression algorithm is used to reduce the size for files or data. There are options like pngcrush to compress your images locally, or you can use online compression tools. However, it's worth noting that specific file formats, such as JPG, are not lossless. Lossless means that the original data can be perfectly reconstructed from the compressed data. If you try to compress a JPG image, it will result in a degraded quality. You should keep all these things in mind when selecting images for your web pages.

## What Are the Different Types of Image Licenses, and How Do They Work?
Images are considered intellectual property, this means that they are protected by copyright regulations, most often belonging to the creator. By default, images are released as all rights reserved. The creator, or publisher sometimes, holds all copyright for the image.

This means that you cannot use them in your web page unless you do one of three things: obtain written permission from the copyright holder, purchase a license from the copyright holder, or incorporate the image in a way that falls under fair use.

That third point is a bit tricky. Fair use requires that your use of the image is both limited and transformative. Some examples of fair use would be to comment on or review the art or create a parody of the image.

Some images might be released under a permissive license, like a Creative Commons license, or the BSD license that freeCodeCamp uses. These images are available for use in your website, but you'll need to read the license to understand the rules you need to follow when using these images. For example, you might be required to make your website open source, or you may not be permitted to modify the image in any way.

Finally, some images may be released to the public domain. An image under the public domain has no copyright attached to it and is free to be used without any restrictions. Images licensed specifically under the Creative Commons 0 license are considered public domain.

Most search engines will allow you to filter image results by a license. There are also sites like Pixabay and Unsplash, which offer free-to-use images. Always be mindful of the copyright and licensing when you use an image in your website.

## What Are SVGs, and When Should You Use Them?
First, you need to understand how images work. Common image formats like PNG and JPG are classified as raster formats. This essentially means that they are pixel-based, with the data tracking the color value in each pixel.

A large downside of raster based images is that they do not upscale well. If you've ever tried to make a PNG larger, you may have seen that it becomes pixelated, or blurry.

An SVG is a different kind of image. SVG stands for a scalable vector graphic. A vector graphic tracks data based on paths and equations to plot points, lines, and curves. What this really means is that a vector graphic, like an SVG, can be scaled to any size without impacting the quality.

SVGs specifically have the added benefit of storing data in XML. This means you can use them directly in your code as raw HTML with the svg element. It also means you can programmatically change the color of the image.

So when would you want to use an SVG? A great use case is for icons. If you want to create custom bullet points, or add icons to your links to represent social media platforms, using SVGs is the best approach. One of the most popular icon libraries, Font Awesome, uses SVG images for their icons. SVGs are also great for webpage logos, because they scale perfectly. They allow you to adapt your layout to any responsive design you need. Next time you have an SVG locally, try opening it with a text editor and playing with the code.

