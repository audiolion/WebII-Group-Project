# JavaScript Regular Expressions

## Language Specific Differences

JavaScript implements the ECMA-262 standard for regular expressions. This standardization borrows from Perl's regular expression syntax but is ultimately a subset of Perl's functionality. Many of the more advanced features were left out of the standard:

- Lookbehind is not supported
- Atomic Grouping is not supported
- Possessive Quantifiers are not supported
- No Unicode support (workarounds exist for single character matching)
- No named capturing groups
- Mode Modifiers are not supported
- No conditionals
- Comments cannot be included in regex

## Using the RegExp methods on the String class
JavaScripts String class has a few simple methods for performing basic find and replace functions. Namely, `str.match(/regex/)` and `str.replace(/regex/, "replacement string")`.

Example
		
		var str = "lazy dogs and sky pie";
		if(str.match(/lazy.*pie/)){
			console.log("match found");
		}

		var replace = str.replace(/and/, "eat");
		console.log(replace);
		// logs "lazy dogs eat sky pie"

## Using the RegExp Object

More formally there is a RegExp object which can be created. This is similar to compiling a regular expression and provides perfmance advantages if you want to do multiple searches. The RegExp object also allows you to extract capture groups.

		var regex = "/and/";
		var re = new RegExp(regex);

		var str = "lazy dogs and sky pie";
		str = str.replace(re, "eat");

		// capture groups
		matches = re.exec(str);

		console.log(matches);
		// logs array of matches

### Replacements with Capture Groups

Using the RegExp object, capture groups, and backreferences we can replace certain parts of text. JavaScript does not support named capture groups, so capturing groups are simply given number assignments starting at $1 and going up to $99. A quick note on backreferences, if there are less than 10 matches $10 is treated as a backrefence to $1 with a literal 0 after it, if there are more than 9 it is treated as the backreference to $10.

When dealing with capturing groups `$&` will reinsert the regex matched, `$\`` will insert text to the left of the regex matched, while `$'` will insert the text to the right of the regex matched. These are useful if you are trying to grab certain parts of the text.


