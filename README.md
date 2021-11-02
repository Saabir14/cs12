# wordSearch Puzzle Solver

The wordSearch puzzle solver is a project which uses C language to generate an HTML output. wordSearch searches an alphabet grid to identify if the supplied words are present in the grid. wordSearch searches the grid for these words horizontally, vertically, and even diagonally. An HTML document is created highlighting these words on the grid if they are present.

## Inputs

The user gives a minimum of 2 inputs besides 3 optional inputs.

### INPUT 1: Puzzle File

The user provides a puzzle file which is a grid of alphabets in the form of a rectangle or square which may vary in the number of rows and columns.
An error message is generated if the above conditions are not satisfied.
Charecters that are not alphabets are ignored.
Rows are separated by a line feed.
This feature allows the user to keep the Puzzle File in csv, tsv, or other file formats other than just txt.

### INPUT 2: Words / Files containing words

The user provides a set of words that are separated by a space to be searched in the grid.
The user can directly type these words following the `Puzzle File`.
Alternatively, these words can be typed in a file and provided as input, by typing the file name and path after the `Puzzle File`.
The words in the word files are separated by a character that is not an alphabet but may include numbers and newlines.
This feature can be used to hold the words in a csv, tsv, or other file formats.
This feature is extremely useful to input many words from a file rather than typing each word manually as a command argument.

### INPUT 3 (optional): `-app`

If the user wishes to append to the output file rather than overwriting it, then the user has to type `-app` as one of the command line arguments.
wordSearch will only append if the file already exists.
wordSearch will not append to a file that was not created by wordSearch itself; wordSearch will overwrite instead. This argument is not case sensitive.

### INPUT 4 (optional): `-ignorefail`

Normally, the HTML output generated is the alphabet grid with the word found being highlighted in it. However, if the word is not found, then the HTML document displays a message stating that the word is not found. If the user has a file containing many words and is unsure whether all the words will be found, then the user can type `-ignorefail` as an argument which causes the program to ignore words that are not found rather than stating that they are not found. For example, if the input includes 100 words, of which only 10 will be found in the grid. In such a case, rather than printing the 90 words that are not found, these words will be ignored. This argument is not case sensitive.

### INPUT 5 (optional): `-[File_Name]`

By default, the HTML file generated will be `out.html`. If the user wishes to name the file something else, the user can specify the file name as one of the command-line arguments. An example could be `-example.htm`. Note that the file format can be changed using the filename argument. This can be used to output an HTML document in formats other than just HTML like HTM.

## Syntax and Execution

The syntax for using wordSearch is simple.

``` bash
./wordSearch [puzzle file] [word or word file] -[output] -app -ignorefail
```

To find apple in puzzles/pApple.txt:

``` bash
./wordSearch puzzles/pApple.txt apple
```

There may be many words or word files e.g.

``` bash
./wordSearch puzzles/pTable.txt helium phosphorus potassium
```

We can also use a file consisting of words:

``` bash
./wordSearch puzzles/pTable2.csv words/wTable2.csv
```

We can also use multiple files. In this case, we use all the files given:

``` bash
./wordSearch puzzles/pTable2.csv words/wTable2.csv words/wApple.txt words/wTable.txt
```

Many words may not be found in pTable2.csv so it would be of use to ignore those failed words rather then stating them in a large HTML file. We can use the `-ignorefail` argument for that:

``` bash
./wordSearch puzzles/pTable2.csv words/wTable2.csv words/wApple.txt words/wTable.txt -ignorefail
```

If the user were to append to a preveous html document:

``` bash
./wordSearch puzzles/pApple.txt apple -app
```

## Retern Values

wordSearch can return 3 different values: 1 for syntax related errors, -1 for memory related errors and 0 for succesfull execution.

## Output

The command that is executed is displayed of at the top the html document. The html document states briefly, wether the word is found. If the word is found, the grid from the puzle file is displayed and the location of the word is neatly highlited with red borders and the letters are emphasized. At the bottom, the number of words found from the total number of words provided is displayed.
