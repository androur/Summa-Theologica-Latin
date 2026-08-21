# Summa-Theologica-Latin
A single .txt file that contains all of the original latin text of Summa Theologica by saint Thomas Aquinas.

#The file is pure text with no all-caps words.
#It does not include "prooemium-s" for individual parts (Prima, Prima Secundae, Secunda Secundae, Tertia).
#53520 lines
#1579772 words

# ABOUT THE FORMAT
Text file SummaTheologica.txt contains 5 main types of lines:
  1. "Quaestio X" - X is the number of the question
  2. "Prooemium" - this one word line is always under a line type 2
  3. "Articulus X" - X is the number of the article within a question
  4. paragraph text - A line of text roughly 70 words but can be way more. Objections, replies and "sed contra" part are all individual paragraphs
  5. empty line - just ""
lines type 1, 3 and 4 depend on the actual text by Aquinas while lines type 2 and 5 can be derived from those.
In the text file SummaTheologica.txt these 5 types of lines follow predictable and useful rules:
  1. All lines type 4 have a single line type 5 right bellow.
  2. All lines type 1 have a single line type 2 right bellow.
  3. All lines types 1 and 3 have a single line type 5 right above.
Rules 1 and 3 have exceptions:
  - The text file ends with a line type 4 - line type 5 was removed bellow it.
  - The very first line of the text file begins with a line type 1 - line type 5 was removed above it.
When going from one individual part to another (line 5 of the README) a line type 1 just starts counting from 1 again, no special lines type 5 or any other type were added.

You can also check the file Example.txt, it has a real slice of the text so you can see the format without having to open the final massive file.

The workflow was mostly manual:
I used https://www.corpusthomisticum.org/ and aquinas.cc as the sources of text
The text it self came from Corpus Thomisticum, I'd manually go though pages and use ctrl+a, ctrl+c, ctrl+v into the text editor.
Then I used a simple python script to clean the text from hyperlinks and other web artifacts.
Then another python script revealed that questions: I 71, I 72, II-II 48, II-II 80, II-II 128, II-II 143
have 0 articles. So I used aquinas.cc to add the titles "Articulus 1" manually at the correct spots.
Some of those simple scripts are in the clean_summa.py file.

The file may contain errors. If you find any, we'd be thankful if you reported them to issues tab.
