# Summa-Theologica-Latin
A single .txt file that contains all of the original latin text of Summa Theologica by saint Thomas Aquinas.

#The file is pure text with no all-caps words.
#It does not include "prooemium-s" for individual parts (Prima, Prima Secundae, Secunda Secundae, Tertia).

#Between articles there is a 2 row gap.
#Between "Quaestio X"+"Prooemium" and "Articulus 1" there is a 2 row gap.
#Between the last line of an article and the next "Quastio title" there is a 2 row gap.
For example:
  Quaestio 6
  Prooemium
  ...


  Articulus 1
  ...


  Articulus 2
  ...


  Quaestio 7
  Prooemium
  ...


The workflow was mostly manual:
I used https://www.corpusthomisticum.org/ and aquinas.cc as the sources of text
The text it self came from Corpus Thomisticum, I'd manually go though pages and use ctrl+a, ctrl+c, ctrl+v into the text editor.
Then I used a simple python script to clean the text from hyperlinks and other web artifacts.

Then another phython script revealed that questions: I 71, I 72, II-II 48, II-II 80, II-II 128, II-II 143
have 0 articles. So I used aquinas.cc to add the titles "Articulus 1" manually at the correct spots.
