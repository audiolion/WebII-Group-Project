# PHP Regular Expressions

PHP uses the [Perl Compatible Regular Expressions library](https://pcre.org) (or PCRE) to support regular expressions. This is great because the PCRE is a set of standards that follow the Perl 5 syntax and regular expression engine implementation. There are some minutiae regarding [differences from Perl 5](https://secure.php.net/manual/en/reference.pcre.pattern.differences.php) though.

PHP requires all regular expressions use the same starting and ending delimiter to encase regular expressions. The most commonly used delimiter is the '/' forward slash.

## PHP Examples

PHP utilizes the `preg_match()` function for regular expression evalutation. The syntax is as follows

		$boolean_match = preg_match($pattern, $input, $matches)

Here is a more fleshed out example

		$regex = "/(\w+) World/";
		if (preg_match($regex, "Hello to the World")) {
			echo "match found";
		}else {
			echo "no matches found";
		}

To perform global searches use the `preg_match_all()` function which takes the same parameters as `preg_match()`.

### Capturing Groups

You might have noticed in the first example we didn't provide a $matches argument. This optional argument holds the strings that are matches, and in the case that multiple matches are found is an array of the captured groups.

		$regex = "/(\d\d\d).*(\d\d\d\d)/";
		$input = "585-526-4483"
		if(preg_match_all($regex, $input, $matches)) {
			# print number of matches
			echo count($matches);

			# print first match
			echo $matches[0];
		}

### Search and Replace

Substitutions are handled by a different function called `preg_replace()`. The parameters are as follows

		$subsituted_str = preg_replace($pattern, $replacement_str, $input)

An example is as follows

		$regex = "/[-.\\s+]/";
		$input = "585-526-4483";
		# desired output = "5855264483"

		$replaced_str = preg_replace($regex, "", $input);

		echo $replaced_str;

### Splitting Strings

The method for splitting strings is `preg_split` defined as follows

		preg_split($pattern, $input, $limit=.., $flags=..)

The limit parameter is an integer that stops splitting after the limit has been reached.

Example
		
		# split string on sets of one or more space or commas
		$regex = "/[\s,]+/";
		$input = "Splitting up strings is fun, sometimes.";
		$split_str = $preg_split($regex, $input);

		echo $split_str;

		# the return value is an Array

### Regex Modifiers

If you want to perform certain operations like case insensitive searching, or multiline searches you can append these single character flags to the end of the regex pattern.

- `i` (PCRE_CASELESS) case insensitive
- `m` (PCRE_MULTILINE) modifies '^' and '$' to apply to every new line
- `s` (PCRE_DOTALL) modifies '.' to include new line characters
- `x` (PCRE_EXTENDED) whitespace is ignored inside of pattern unless escaped. Useful for adding comments inside patterns
- `S` tells php to spend extra time analyzing pattern which will increase overall performance if the pattern will be used multiple times. The analysis is only useful for non-anchored patterns that do not have a fixed starting character
- `U` (PCRE_UNGREEDY) performs an ungreedy search, which is the equivalent to using `.*?`
- `X` (PCRE_EXTRA) this modifier includes additional functionality that is not included in the Perl 5 specification and is incompatible with Perl. A common example is that a backslash in a pattern followed by a letter that has no special meaning causes an error as opposed to Perl 5 specification which would just treat the character as a literal. The purpose is to simply not use special reservations that don't have a meaning so later on if that reservation is used it won't break existing code.
-`u` (PCRE_UTF8) This modifier adds in functionality incompatible with Perl. Patterns and input strings are treated as UTF-8.

Example of using a modifier

		# add multiline and case insensitive modifiers
		$match = $preg_match("/^lazy.dog/im", $input);