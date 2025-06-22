# Learn CSS Colors by Building a Set of Colored Markers

Selecting the correct colors for your webpage can greatly improve the aesthetic appeal to your readers.

In this course, you'll build a set of colored markers. You'll learn different ways to set color values and how to pair colors with each other.

## margin 外边距

When the shorthand `margin` property has two values, it sets `margin-top` and `margin-bottom` to the first value, and `margin-left` and `margin-right` to the second value. top/bottom left/right

复合属性 `margin` 有两个值时，第一个值表示上下外边距(margin-top/margin-bottom),第二个值表示左右外边距(margin-left/margin-right)，简记为 **上下 左右**

## padding 内边距

just like `margin`

## multiple classes 多个类名

If you add multiple classes to an HTML element, the styles of the first classes you list may be overridden by later classes.

当一个HTML元素有多个类名的时候，后面的类名会覆盖第一个类名的样式

## Color 颜色表示法

### RGB 常用

    rgb(red, green, blue)

In this project, you'll work with the RGB model. This means that colors begin as black, and change as different levels of red, green, and blue are introduced. Each red, green, and blue value is a number from 0 to 255. 0 means that there's 0% of that color, and is black. 255 means that there's 100% of that color.

primary color

- black rgb(0, 0, 0)
- red rgb(255, 0, 0)
- pure green rgb(0, 255, 0) / #00FF00
- green rgb(0, 127, 0)
- blue rgb(0, 0, 255)

secondary color

- yellow rgb(255, 255, 0)
- cyan rgb(0, 255, 255)
- magenta rgb(255, 0, 255)

tertiary color

- orange rgb(255, 127, 0)
- spring green rgb(0, 255, 127)
- violet rgb(127, 0, 255)
- chartreuse green rgb(127, 255, 0)
- azure rgb(0, 127, 255)
- rose rgb(255, 0, 127)

A color wheel is a circle where similar colors, or hues, are near each other, and different ones are further apart. For example, pure red is between the hues rose and orange.

Two colors that are opposite from each other on the color wheel are called complementary colors. If two complementary colors are combined, they produce gray. But when they are placed side-by-side, these colors produce strong visual contrast and appear brighter.

### HEX 十六进制颜色 常用

    hsl(240, 100%, 50%)

A very common way to apply color to an element with CSS is with hexadecimal or hex values. While hex values sound complicated, they're really just another form of RGB values.

Hex color values start with a # character and take six characters from 0-9 and A-F. The first pair of characters represent red, the second pair represent green, and the third pair represent blue. For example, `#4B5320`.

With hex colors, 00 is 0% of that color, and FF is 100%. So #00FF00 translates to 0% red, 100% green, and 0% blue, and is the same as rgb(0, 255, 0).

### CMYK 印刷颜色表示法

use red, black, yellow and so on to discribe colors.

### HSL 色调饱和度亮度表示法

    hsl(240, 100%, 50%)

The HSL color model, or hue, saturation, and lightness, is another way to represent colors.

The CSS hsl function accepts 3 values: a number from 0 to 360 for hue, a percentage from 0 to 100 for saturation, and a percentage from 0 to 100 for lightness.

If you imagine a color wheel, the hue red is at 0 degrees, green is at 120 degrees, and blue is at 240 degrees.

Saturation is the intensity of a color from 0%, or gray, to 100% for pure color. You must add the percent sign % to the saturation and lightness values.

Lightness is how bright a color appears, from 0%, or complete black, to 100%, complete white, with 50% being neutral.

##  linear-gradient 渐变色

You've learned a few ways to set flat colors in CSS, but you can also use a color transition, or gradient, on an element.

A gradient is when one color transitions into another. The CSS `linear-gradient` function lets you control the direction of the transition along a line, and which colors are used.

通过 `linear-gradient` 设置渐变色

One thing to remember is that the `linear-gradient` function actually creates an image element, and is usually paired with the `background` property which can accept an image as a value.

The `linear-gradient` function is very flexible -- here is the basic syntax you'll use in this tutorial:


    linear-gradient(gradientDirection, color1, color2, ...);

gradientDirection is the direction of the line used for the transition. color1 and color2 are color arguments, which are the colors that will be used in the transition itself. These can be any type of color, including color keywords, hex, rgb, or hsl.

You won't see gradient yet because the linear-gradient function needs at least two color arguments to work.

```css
.red {
  background: linear-gradient(90deg, rgb(255, 0, 0), rgb(0, 255, 0), rgb(0, 0, 255));
}
```

Color-stops allow you to fine-tune where colors are placed along the gradient line. They are a length unit like px or percentages that follow a color in the linear-gradient function.

For example, in this red-black gradient, the transition from red to black takes place at the 90% point along the gradient line, so red takes up most of the available space:

    linear-gradient(90deg, red 90%, black);

```css
.red {
  background: linear-gradient(180deg, rgb(255, 0, 0) 75%, rgb(0, 255, 0), rgb(0, 0, 255));
}
```

`180deg` means vertical, `90deg` means horizonal

## opacity 不透明度

Opacity describes how opaque, or non-transparent, something is. For example, a solid wall is opaque, and no light can pass through. But a drinking glass is much more transparent, and you can see through the glass to the other side.

With the CSS `opacity` property, you can control how opaque or transparent an element is. With the value `0`, or 0%, the element will be completely transparent, and at `1.0`, or 100%, the element will be completely opaque like it is by default.

## alpha channel

Another way to set the opacity for an element is with the alpha channel. Similar to the opacity property, the alpha channel controls how transparent or opaque a color is.

### rgba 加上不透明度的rgb表示法

You're already familiar with using the rgb function to set colors. To add an alpha channel to an rgb color, use the rgba function instead.

The rgba function works just like the rgb function, but takes one more number from 0 to 1.0 for the alpha channel:

    rgba(redValue, greenValue, blueValue, alphaValue);

You can also use an alpha channel with hsl and hex colors.

    rgb(255, 255, 255, 50%)

## border-left-width

## border-left-style

## border-left

The border-left shorthand property lets you to set the left border's width, style, and color at the same time.

Here is the syntax:

    border-left: width style color;

## box-shadow

the last thing you'll do is add a slight shadow to each marker to make them look even more realistic.

The `box-shadow` property lets you apply one or more shadows around an element. Here is basic syntax:

    box-shadow: offsetX offsetY color;

Here's how the offsetX and offsetY values work:

both `offsetX` and `offsetY` accept number values in px and other CSS units
a positive offsetX value moves the shadow right and a negative value moves it left
a positive offsetY value moves the shadow down and a negative value moves it up
if you want a value of zero (0) for any or both offsetX and offsetY, you don't need to add a unit. Every browser understands that zero means no change.
The height and width of the shadow is determined by the height and width of the element it's applied to. You can also use an optional spreadRadius value to spread out the reach of the shadow. More on that later.

Notice that the edges of the shadow are sharp. This is because there is an optional blurRadius value for the box-shadow property:

    box-shadow: offsetX offsetY blurRadius color;

If a blurRadius value isn't included, it defaults to 0 and produces sharp edges. The higher the value of blurRadius, the greater the blurring effect is.

But what if you wanted to expand the shadow out further? You can do that with the optional spreadRadius value:

    box-shadow: offsetX offsetY blurRadius spreadRadius color;

Like blurRadius, spreadRadius defaults to 0 if it isn't included.

