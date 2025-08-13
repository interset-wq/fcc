# Understanding Nuanced Semantic Elements

In these lectures, you will learn when you should use certain semantic elements like the em element over the i element, description lists, and more.

## When Should You Use the Emphasis Element Over the Idiomatic Text Element?
These elements are very closely related to the concepts of presentational and semantic HTML. The idiomatic text element, i, was originally used for presentational purposes to display the text in italics. But now, it is frequently used for highlighting alternative voice or mood, idiomatic terms from another language, technical terms, and thoughts.

Here is example from the official HTML spec, using the i element to show an idiomatic phrase in French:

<p>There is a certain <i lang="fr">je ne sais quoi</i> in the air.</p>
The lang attribute inside the open <i> tag is used to specify the language of the content. In this case, the language would be French. The i element does not indicate if the text is important or not, it only shows that it's somehow different from the surrounding text.

If you do need to emphasize the importance of the text, you can use a similar semantic element called the emphasis element, em. This is usually recommended if you need to provide more context. You should use this element for parts of the text that require a special emphasis compared to surrounding text. It's usually limited to only a few words, because it can alter the meaning of the sentence.

This is an example of the emphasis element within a paragraph:

<p>
  Never give up on <em>your</em> dreams.
</p>
You can see the sentence Never give up on your dreams. Notice that the word your will be emphasized, because it's inside this element. In the browser you would see the word your is italicized to tell readers that this is an important word in the sentence.

Even if it looks the same when the text was inside the idiomatic text element, the semantic emphasis element conveys its meaning and importance behind the scenes.

It's important to know that these elements should not be used for presentational purposes only. If you need to display the text in italics, but the text doesn't have a special purpose, style, or meaning in the paragraph, you should use CSS instead.

## When Should You Use the Strong Element Over the Bring Attention To Element?
The "bring attention to" element, b, is commonly used to highlight keywords in summaries, or product names in reviews. Usually, browsers display this text in boldface. Here's an example using the b element to highlight product names in this review:

<p>
  We tested several products, including the <b>SuperSound 3000</b> for audio
  quality, the <b>QuickCharge Pro</b> for fast charging, and the
  <b>EcoClean Vacuum</b> for cleaning. The first two performed well, but the
  <b>EcoClean Vacuum</b> did not meet expectations.
</p>
The browser renders these parts of the text as bold text. This visual emphasis will draw readers attention to the product names.

If you need to emphasize the importance of the text, you should use the strong element instead of the b element.

strong is a semantic HTML element that emphasizes text that is crucial, or urgent. This is an example where the strong element is used to label a very important warning about the potential allergic reactions that customers may have to a product:

<p>
  <strong>Warning:</strong> This product may cause allergic reactions.
</p>
The strong element communicates that sense of urgency.

Visually both are very similar, because they are both rendered as bold by default. But their meanings are quite different. While the "bring attention to" element only draws attention to the text, without indicating the higher level of importance, the strong element does more than that. It conveys a sense of importance, or urgency. This is their main difference.

To choose between them, consider the purpose of the text and its importance within the surrounding content.

## What Are Description Lists, and When Should You Use Them?
Description lists are perfect for presenting terms and definitions in an organized and easy-to-read format, like in a glossary, or real dictionary, where you can find words with their corresponding definitions.

This is an example of a description list in HTML with two terms and their corresponding details:

<dl>
  <dt>HTML</dt>
  <dd>HyperText Markup Language</dd>
  <dt>CSS</dt>
  <dd>Cascading Style Sheets</dd>
</dl>
In this case the terms are the acronyms HTML and CSS, and the details are their expansions. The details could also be definitions, or other information related to the terms.

You will need three HTML elements to define a description list. First, the description list element, dl, which is the container for the entire list. You can see it wraps around all the other elements of the description list in the example.

Then, one description term element, dt, for each term. In this case the description list has two terms, HTML and CSS, so it has two of these elements.

And finally, after each term you will find a description details element, dd, for the description, or details associated with that term. In this example, they are Hypertext Markup Language and Cascading Style Sheets.

In the browser, you would see each term followed by its corresponding description. By default, the descriptions are slightly more indented towards the right to distinguish them visually.

But description lists are not limited to only terms and definitions. They are much more versatile than that. Here we have a recipe with two ingredients.

<dl>
  <dt>Flour</dt>
  <dd>2 cups</dd>
  <dt>Sugar</dt>
  <dd>1/2 cup</dd>
</dl>
The entire description list is within a description list element. The first ingredient, Flour, is within a description term element. Then, you can see how much of this ingredient you will need: 2 cups. This is within a description details element directly after its corresponding ingredients.

And the same structure is repeated for Sugar. In this case, the recipe has only two ingredients, but if there were more the same structure could be repeated throughout the description list.

In the browser, you would see the ingredients aligned to the left, and the measurements indented to separate them visually.

Other use cases for description lists include product specifications, frequently asked questions, contact information, and metadata. Essentially, when you have two related pieces of information in a key-value pair format, where one acts as a label, the key, and the other acts as additional related information, the value, you can use a description list.

