# Python Regular Expressions
***

## Language Specific Implementation Differences
Python has a fairly powerful library called `re` that supports the regular expression implementation very well. There are three main features missing from the library:

- Atomic Groupings
- Possessive Quantifiers
- Unicode Properties

### Atomic Groupings
Atomic grouping syntax is simply a way of reducing computation time in certain scenarios and preventing a couple of specific edge case traps that can greatly impede regex performance. Atomic groupings stop the regex engine from backtracking to a capture group and trying new branches off of it. The atomic group solidifies the first match of the capture group and does not allow backtracking to the tokens in the group. All this being said, there are workarounds to do atomic grouping in python if you really want to.


### Possessive Quantifiers
Possessive quantifiers are similar to atomic groups in that they do not give up matches as the regex engine backtracks to greedily look for other matches. Again this helps with certain edge cases of catastrophic backtracking and you can use the workaround for atomic grouping in python to accomplish the same goal. Essentially, possessive quantifiers are just a little syntactic sugar that allow you to not fiddle around with atomic groupings.

### Unicode Properties
Unicode is a mapping of all characters, drawings, and marks using in languages throughout history. Unicode has been popular because software and websites now must support multiple languages and by using unicode you don't need to worry about making sure all the language specific glyphs and characters are included. However, the cost is that unicode characters are not always supported by popular libraries. In this case, Python's `re` library does not use a unicode library for its engine. There is an option flag you can set to force unicode rendering but you will need to consult the documentation to see how interactions change when working with unicode.

## Python Regular Expression Example

The following is a simple script that shows how one can interact with the `re` library.

		import re

		text = "Hello World!"
		match = re.search(r"[a-zA-Z].[a-zA-Z]!)

		print match	# evaluates to true

		text = "When a dog jumps he says Hello World!"
		match = re.search(r"[a-zA-Z].[a-zA-Z]!)
		
		if(match)
			print "Match found at index %s, %s" % (match.start(), match.end())

			# match.group(index) allows us to extract capture groups
			# match.group(0) gives the fully qualified string
			# match.group(1) gives the first capture group, match.group(2) the second...
			# match.group() defaults to match.group(0)

			print "Group 0: %s" % (match.group(0))
			print "Group 1: %s" % (match.group(1))
		else:
			print "No matches found"

This gives a taste of how re works. There are some other handy functions that you you will likely find yourself using.
		
		# find and replace
		import re

		text = "Substitute out yacks from sentences"
		
		# re.sub(regex, replacement, text)
		text_subbed = re.sub(r"(yacks), "animals", text)
		
		# using a regex multiple times in a row? use re.compile
		# regex_compiled = re.compile(regex, flags=..)
		regex_compiled = re.compile(r"[a-zA-Z0-9]")
		match = regex_compiled.search("Broski!!1!")

		# want to do a global search use regex.findAll()

		print regex_compiled.findAll(text)
		# returns all matches found

		# splitting a string
		re.split(pattern, stringToSplit, maxSplitNumber=0, flags=..)

There are a set of constant flags that exist to set certain modifiers.

- re.DOTALL - flag expands the '.' character to match new line characters as well
- re.MULTILINE - flag modifies '^' and '$' to look for matches at the start of new lines or at the end of where a new line character is. This is opposed to simply matching at the start of end of the entire text, as is the default behavior.
- re.UNICODE sets up different behavior for dealing with unicode characters, refer to the [documentation](https://docs.python.org/2/library/re.html#regular-expression-syntax) for specifics.
- re.LOCALE flag reverts the unicode setting
- re.IGNORECASE performs a case insensitive search
- re.DEBUG displays information about the compiled expression
- re.VERBOSE allows you to write expressions in a more readable format

		expr = re.compile(	r"""	\d+ # match digits
									- 	# match hyphen
									\d+ # match digits
							""", flags=re.VERBOSE)
	Note the extra quotes for each additional line, this is required for proper compilation.

For more examples [visit python's `re` page](https://docs.python.org/2/library/re.html#examples)