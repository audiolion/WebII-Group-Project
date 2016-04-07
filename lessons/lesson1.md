## Lesson 1 - Introduction to Regex

#### What are Regular Expressions
Regular Expressions, often shortened to Regex, are an algebra designed to match and identify a sequence of characters. Regular expressions are often seen as daunting because a regular expression in code often looks like complete gibberish.
```
/\s+[a-zA-Z\d]{3}.*/
```
But this is no different from any other symbolic language, like seeing the mathematical equation for the fundamental theorem of calculus.

![F(x) = integral a to b of f(t) dt](http://latex.codecogs.com/png.latex?F(x)&amp;space;=&amp;space;\\int_{a}^{b}f(t)dt)

To anyone who has never been exposed to mathematical symbols this is as incomprehensible as the regular expression above.

However regular expressions are much easier to understand than mathematics. The symbolic language is much smaller and each symbol has an exact meaning. When broken down symbol by symbol we can easily figure out what is going on.
```
/     # begin regular expression
\s    # match a whitespace character
+     # match one or more whitespace characters
[     # set of characters to match
a-z   # any character a to z
A-Z   # any character A to Z
\d    # any digit
]     # end set of characters to match
{3}   # match three characters in the previous set
.*    # match zero to any number of characters afterwards
/     # end regular expression
```
When broken down like this the regular expression is much more readable, because we are looking at each symbol individually and describing it. The regular expression above matches any number of proceeding whitespace characters and then three alphabet or alphanumeric characters and it doesn't care what comes after that.

Learning regular expressions is just a matter of learning the symbolic language, a few of the constructs and their applications, and practicing.

#### Applications of Regular Expressions

Regular expressions have a wide array of uses, the basic scenarios are:
- Parsing text for certain patterns (form data entry validation)
- Extracting text (data mining)
- Replacing text (find and replace)

These three scenarios come up often when programming and while we can get away with exact matching in many cases, the reason regex exists is because we needed a solution for more complex scenarios.

#### Regex 101

While each programming language will have it's own syntax for how to produce regular expressions, the defacto standard is Perl. Perl has a very powerful and complete implementation of regular expressions and we will be using Perl regex syntax in our definitions.

In Perl any regular expression begins with '/' and terminates with '/'.

Let's begin by implementing some very simple regular expressions. We have a string that we are trying to match.
```
15 Grumpy wizards make toxic brew for the evil Queen and Jack.
```
If we wanted to know if this string contained alphanumerics, how would we do this?

```
/.*[0-9].*/
```

Breaking this down
```
/     # begin
.*    # match any number of characters
[0-9] # match a digit
.*    # match any number of characters
/     # end
```

Quite simply we are looking for a digit surrounded by any number of characters. Now we could also have used the digit syntax `\d` instead of `[0-9]` and it would have been fine. `\d` is potentially dangerous though as it can match digits in unicode which you weren't expecting to, so `[0-9]` is more explicit and defined.

You might also ask, why did we not just use
```
/[0-9]/
```
why the `.*` before and after? Well if we did not include those wildcard zero to infinity identifiers we would only match a single digit, in this case `1`, and not the entire string. If the goal is to find strings with alphanumerics in them, we would miss out on the entire string.

Now lets try to match strings that contain the word `Queen`.
```
/Queen/
```
This would be the simple exact match of a word. Let's say we want to match `queen` or `Queen` though, how would we do that?

We can match different sets by separating them with the `|` character.

```
/Queen|queen/
```

The `|` pipe acts like a boolean OR operator. Thus is matches either representation of queen. It is best practice to surround expressions like this with parenthesis `(Queen|queen)` so that if you have other elements to your regular expression it correctly groups these elements together.

```
/(Queen|queen)/
```

Now let's say we just want to match the word `queen`, we don't care if it any of the letters are capitalized or not, this request is represented in the idea of 'ignore case' which is specified by adding an `i` at the end of our regular expression.

```
/queen/i
```

In the above example it wouldn't matter if the text was written as 'qUeen', 'Queen', or 'quEEN' or any combination of cases (fun aside, how many possible combinations are there?).

#### Wildcards

Wildcards are an important concept in regex because often we don't care what character comes at a certain position in the string. Formally, the wildcard character is `.`, which means match any single character. We can combine the operators `+` and `*` with the `.` to match many wildcard characters. Specifically `*` matches 0 or more of the previous regex symbol, and `+` matches 1 or more of the previous symbol. The distinction is important if we want to ensure at least one character is in the position or not. For completeness's sake, `.+` is equivalent to `.*.` or `..*` to make sure it is at least one character and then zero or more, but `.+` is cleaner, more readable and more efficient. Let's try a few examples.

```
15 Grumpy wizards make toxic brew for the evil Queen and Jack.
```

How would we match the word Jack followed by one or more characters?

```
/Jack.+/
```
How about the letter b with three characters after it?
```
/b.../
```
If we want a specified number just repeat the `.` wildcard that many times.

How about the letter t followed by the letter c three characters after it?

```
/t...c/
```

In this way we can match and literal text in any combination of pattern we want.

#### Putting it all together

Ok, recapping what we have learned
- Start and end a regular expression with `/`
- Ignore case with an i proceeding the terminating `/`, `/hello/i`
- Wildcards are represented with the `.` character
- Match any number of characters, *one* or more of the proceeding character with the `+`
- Match any number of characters, *zero* or more of the proceeding character with the `*`
- Use the boolean OR operator to match sets of expressions with the `|` and surround with parenthesis to group

Let's try to write a regular expression that matches an alphanumeric followed by the words 'make' and then the word 'evil' or the word 'Queen', finally match the letter 'a' with any character before it and precisely three characters after it.

```
15 Grumpy wizards make toxic brew for the evil Queen and Jack.
```

Answer
```
/[0-9].*make.*(evil|Queen).+a.../

# breakdown

/       # begin
[0-9]   # any digit
.*      # zero or more characters until
make    # the word make
.+      # one or more characters until
(       # group
  evil  # evil
  |     # OR
  Queen # queen
)       # end group
.*      # zero or more characters until
a       # a character
...     # three wildcard characters
/       # end
```
