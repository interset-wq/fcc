# Working with Accessible Tables and Forms

In these lectures, you will learn about how to create accessible tables and forms.

## What Are Best Practices for Tables and Accessibility?
When we see a table, we immediately start making visual associations between the data and the headers.

For example, let's say we have a table representing our pets. We have two dogs and two cats and the table is showing us their names and ages. While a sighted person may be able to understand the relationships in this table, making the connections between the values and the headers is much harder for people who use screen readers to navigate the table.

As a web developer, you are in charge of creating these associations and structuring your HTML markup in a way that is also easy for screen reader users to interpret.

So, let's see how you can create accessible tables that everyone can understand. The first best practice that we will cover is using table caption. With the caption element, you can write the caption (or title) of a table, so users, especially those who use assistive technologies, can quickly understand the table's purpose and content. You should place the caption element immediately after the opening tag of the table element. This way, screen readers and other assistive technologies can provide more context by announcing the caption before reading the content.

<table>
  <caption>Our Pets</caption>
  <!-- Table Rows and Columns -->
</table>
Now let's talk about row and column headers. Headers are special cells, typically found at the start of a row or column, that describe the type of data stored in the row or column. You can define a row or column header with the table header element, th.

For example, the code below creates a table for two pets. Every row has a row header (the name of the pet) and every column has a column header, which describes what the data in the column represents (age and type).

<table>
  <caption>Our Pets</caption>
  <thead>
    <tr>
      <!-- Column Headers -->
      <th>Name</th>
      <th>Age</th>
      <th>Type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Nora</th> <!-- Row Header -->
      <td>5</td>
      <td>Dog</td>
    </tr>
    <tr>
      <th>Gino</th> <!-- Row Header -->
      <td>2</td>
      <td>Cat</td>
    </tr>
  </tbody>
</table>
Notice that the above code has a caption element immediately after the opening table element. Then, inside the table head (thead) element, it has the column headers (Name, Age, and Type). In the second and third rows, inside the table body (tbody) element, we find the data for each one of our pets. The names of the pets are the row headers because they are inside table header elements (th).

Associating the data cells with their corresponding headers is also very important for screen readers. The scope attribute determines if a header is a row header or a column header. Screen readers may guess this correctly from the table's structure, but it's usually recommended to explicitly indicate the scope to ensure clarity.

The scope attribute has four possible values. The two you will use most often are col for column and row for row. In the code below, you can see that we added the scope attribute to the column and row headers. The three column headers (Name, Age, and Type) have a scope of col, column.

The two row headers (Nora and Gino) have a scope of row.

<table>
  <caption>Our Pets</caption>
  <thead>
    <tr>
      <!-- Now they have scope -->
      <th scope="col">Name</th>
      <th scope="col">Age</th>
      <th scope="col">Type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">Nora</th>
      <td>5</td>
      <td>Dog</td>
    </tr>
    <tr>
      <th scope="row">Gino</th>
      <td>2</td>
      <td>Cat</td>
    </tr>
  </tbody>
</table>
If a column or row header spans across multiple cells, the scope will also be applied to each one of the cells individually. Here's an example of that:

Name	Age
Dogs	Nora	5
Gino	2
Cats	Lulu	10
Elizabeth	6
In this table, the cell with Nora's age (5) will have one column header (Age) and two row headers (Dogs and Nora). Gino's age (2) will also have one column header (Age) and two row headers (Dogs and Gino).

However, some screen readers may not be able to interpret tables with complex structures, so you should also try to flatten the table as much as possible to avoid row and column headers that span across multiple cells.

Your goal should always be to make sure users can access this information, even if their screen readers can handle complex table structures.

Now, for cell width, it's recommended to avoid using fixed values. You should use relative values instead, like percentages. Also, try to avoid defining cell height. This will allow users to adjust the text size to fit their needs.

And finally, you should let the browser determine the table width whenever possible, to reduce the need for horizontal scrolling.

HTML tables are essential for presenting structured data in an accessible and understandable format. By following these accessibility guidelines, you can create tables that are easy to understand for everyone.

## Why Is It Important for Inputs to Have an Associated Label?
Labels on input fields might seem like small details, but they play a crucial role in making forms easier for everyone to use.

Labels help people with disabilities, make forms more user-friendly for everyone, and ultimately improve form conversion rates.

Let's dive into why adding labels to input elements is important for accessibility and usability.

Screen readers often rely on labels to describe the purpose of input fields. In order for this to work properly, the label must be programmatically associated with the input. While there are several ways to do that, the most common is to use the HTML label element.

Here's how to associate a label with an input:

<form>
   <label for="name">Your Name</label>
   <input type="text" id="name" />
</form>
In this example, the for attribute of the label element is associated with the id of the input element. This connection allows screen readers to announce the label when the input is in a focused state, allowing screen reader users to understand the purpose of the input.

Associating labels with all input fields also benefits SEO. With proper labels, search engines will understand the page content better, leading to a positive impact on the page search rankings.

But it is important to understand that you're making content for humans, not search engines. So, you should make sure the labels are as clear and descriptive as possible.