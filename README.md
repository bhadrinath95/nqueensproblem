# nqueensproblem

In this Django project, we will give integer value as an input for board size. 
The resultant output for N Queens Problem is displayed in screen.

## N Queens Problem

The N Queen is the problem of placing N chess queens on an N×N chessboard so that no two queens attack each other.

Eg: For 4 Queen problem.

```bash
{ 0,  1,  0,  0}
{ 0,  0,  0,  1}
{ 1,  0,  0,  0}
{ 0,  0,  1,  0}
```

## Backtracking Algorithm

* The idea is to place queens one by one in different columns, starting from the leftmost column. 
* When we place a queen in a column, we check for clashes with already placed queens. 
* In the current column, if we find a row for which there is no clash, we mark this row and column as part of the solution. 
* If we do not find such a row due to clashes then we backtrack and return false.

## Chess Board

### CSS Attributes used for chess pieces

* To create a Chessboard with Chess pieces we first need to know their unicode or HTML equivalent codes.
* There are around 12 Symbols that are needed to create a Chessboard in HTML.
* These symbols are available in Unicode range U+2654 to U+265F.

1. White Chess King ♔
Unicode : U+2654
HTML Code : &#9812;

2. Black Chess King ♚
Unicode : U+265A
HTML Code : &#9818;


3. White Chess Queen ♕
Unicode : U+2655
HTML Code : &#9813;

4. Black Chess Queen ♛
Unicode : U+265B
HTML Code : &#9819;


5. White Chess Rock ♖
Unicode : U+2656
HTML Code : &#9814;


6. Black Chess Rock ♜
Unicode : U+265C
HTML Code : &#9820;


7. White Chess Bishop ♗
Unicode : U+2657
HTML Code : &#9815;


8. Black Chess Bishop ♝
Unicode : U+265D
HTML Code : &#9821;


9. White Chess Knight ♘
Unicode : U+2658
HTML Code : &#9816;


10. Black Chess Knight ♞
Unicode : U+265E
HTML Code : &#9822;


11. White Chess Pawn ♙
Unicode : U+2659
HTML Code : &#9817;


11. Black Chess Pawn ♟
Unicode : U+265F
HTML Code : &#9823;

### CSS Attributes used for chess pieces arrangement

```html
<!-- 1st -->
<div class="white">&#9820;</div>
<div class="black">&#9822;</div>
<div class="white">&#9821;</div>
<div class="black">&#9819;</div>
<div class="white">&#9818;</div>
<div class="black">&#9821;</div>
<div class="white">&#9822;</div>
<div class="black">&#9820;</div>
<!-- 2nd -->
<div class="black">&#9821;</div>
<div class="white">&#9821;</div>
<div class="black">&#9821;</div>
<div class="white">&#9821;</div>
<div class="black">&#9821;</div>
<div class="white">&#9821;</div>
<div class="black">&#9821;</div>
<div class="white">&#9821;</div>
<!-- 7th -->
<div class="white">&#9817;</div>
<div class="black">&#9817;</div>
<div class="white">&#9817;</div>
<div class="black">&#9817;</div>
<div class="white">&#9817;</div>
<div class="black">&#9817;</div>
<div class="white">&#9817;</div>
<div class="black">&#9817;</div>
<!-- 8th -->
<div class="black">&#9814;</div>
<div class="white">&#9816;</div>
<div class="black">&#9815;</div>
<div class="white">&#9813;</div>
<div class="black">&#9812;</div>
<div class="white">&#9815;</div>
<div class="black">&#9816;</div>
<div class="white">&#9814;</div>
```

## Referene

See 
1. Chessboard with pieces using pure HTML and CSS: http://code2care.org/pages/chessboard-with-pieces-using-pure-html-and-css/
2. N Queen Problem using Backtracking: https://www.geeksforgeeks.org/n-queen-problem-backtracking-3/
