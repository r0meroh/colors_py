# colors_py
Simple program that uses turtle framework to create on screen graphics.

Two libraries were imported to make up this small program.
A pen object is created and is reponsible for creating the shapes in a window.


![import Statements](https://github.com/r0meroh/colors_py/blob/master/images/colorsPyimportStatements.png)


The turtle library utilizes actual strings for the color declarations.

![string of colors](https://github.com/r0meroh/colors_py/blob/master/images/Screenshot%20from%202019-10-16%2008-25-10.png)

A while loop runs the program until the user closes the window. The program creates circles in random locations within a determined 
pixel area and also randomly chooses the colors from the "colors" list.

At the end of the loop, after the circle is created, the pen object lifts up to allow a different circle to be created once the loop reiterates.
![while Loop](https://github.com/r0meroh/colors_py/blob/master/images/clolorsWhileLoop.png)

The loop only exits when the user closes the window. This is done with the "done()" function.

![window loop](https://github.com/r0meroh/colors_py/blob/master/images/colorsNameofColors.png)

The circles are set to appear relatively fast to emulate a "kaleidoscope" like effect.
Here is how it loops within one second of the loop executing.

![initial loop](https://github.com/r0meroh/colors_py/blob/master/images/colorsInitial.png)

Here is another screenshot after the loop is given several seconds to run.

![later loop](https://github.com/r0meroh/colors_py/blob/master/images/colorsLater.png)
