# Learn How to Work with Numbers and Strings by Implementing the Luhn Algorithm通过卢恩算法学习数字和字符串

The Luhn Algorithm is widely used for error-checking in various applications, such as verifying credit card numbers.

By building this project, you'll gain experience working with numerical computations and string manipulation.

The Luhn algorithm is as follows:

- From the right to left, double the value of every second digit; if the product is greater than 9, sum the digits of the products.
- Take the sum of all the digits.

    Part of the algorithm is to double every second digit, starting from the right. If the result of doubling the number is greater than or equal to 10, add the two digits together. For example, if the digit is 6, double it to get 12. Add 1 and 2 together to get 3. 

- If the sum of all the digits is a multiple of 10, then the number is valid; else it is not valid.

Assume an example of an account number "7992739871" that will have a check digit added, making it of the form 7992739871x:

Account number      7   9  9  2  7  3  9   8  7  1  x
Double every other  7  18  9  4  7  6  9  16  7  2  x
Sum 2-char digits   7   9  9  4  7  6  9   7  7  2  x

## `<class 'str'>`

### .maketrans

Python comes with built-in classes that can help us with string manipulation. One of them is the `str` class. It has a method called `maketrans` that can help us create a translation table. This table can be used to replace characters in a string:

    str.maketrans({'t': 'c', 'l': 'b'})

view it as a bulit-in function.

The above, when called on a string, will replace all t characters with c and all l characters with b.

Defining the translation does not in itself translate the string. The translate method must be called on the string to be translated with the translation table as an argument:

    my_string = "tamperlot"
    translation_table = str.maketrans({'t': 'c', 'l': 'b'})
    translated_string = my_string.translate(translation_table)

### slice

You have accessed elements (characters) of a string before, using the index operator `[]`. You can also use the index operator to access a range of characters in a string with `string[start:stop:step]`:

    my_string = 'camperbot'
    my_string[0:6] == 'camper' # True
    my_string[0:6:3] == 'cp' # True

Where start is the starting index (inclusive), stop is the ending index (exclusive), and step is the amount of characters to skip over. If not specified, step is default to 1.