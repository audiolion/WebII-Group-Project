# Java Regular Expressions
***

Java has a built in package you can import if you would like to use regular expressions.

    import java.util.regex

The package has had slight updates with newer versions of Java. Here is a quick reference of version to version differences.

#### Java 1.4
Original introduction of java.util.regex package. Need at least Java 4 to utilize the built-in regex library.

#### Java 1.5
- `LITERAL` constant added, enables literal parsing of the pattern
- `toString()` provides a string representation of the Pattern object
- `quote(String s)` method returns a literal pattern for a specified string

#### Java 1.6
- No new features added, a few bugs with edge cases were fixed

#### Java 1.7
- `UNICODE_CHARACTER_CLASS` constant added that allows for comaptibility with Unicode and POSIX character classes. Using the flag can introduce performance issues

#### Java 1.8
- Introduces `asPredicate()` and `splitAsStream(CharSequence input)` methods
  - `asPredicate()` compiles a String into a Predicate object to match to other strings
  - `splitAsStream(...)` Creates one to many streams of strings by splitting the input sequence on the regex pattern.

### Java Regex Constructs
***
Simple matching in Java can be done on Strings with the `match(String s)` method call. The `match(String s)` method puts anchor tags at the start and end of the string and does a regex matching.

    someString.match("bobcat");
    // converted to the regex pattern
    someString.match("^bobcat$");

    someString.match("[a-z]");
    someString.match("^[a-z]$");

If you want to perform a simple replace you can use the `replaceAll("regex-as-string", "replacement-string")` method. It follows the same method for regex as the `match(String s)` method. However, capturing groups can be utilized for the replacement text. Capturing groups are defined with the syntax `$digit` ala `$1` to back reference the first item group captured.

For anything more complex one must instead create a Pattern object and compile it, then a matcher object to match the pattern against a String.

    Pattern p = Pattern.compile("<regexpression>");
    Matcher m = p.matcher("<string-to-match>");
    boolean b = m.matches();

For performance reasons, if you are matching against a certain regular expression multiple times it is best to use a Pattern object. Otherwise Java will build a new compiled Pattern object each time you call a method like `match` or `replaceAll`.

The Pattern object only works with a Matcher object. The reason Java uses a matcher object is to hold a group of useful methods to get capture groups, specific matches or groups of matches and more. The matcher object can also call `replaceAll` which does the same thing as the String method, except it is faster.

One last note is that when you are using Java regex, to specify special charaters like `\s` for a space you must escape the slash. Thus you would write `\\s` to get the special identifier.
