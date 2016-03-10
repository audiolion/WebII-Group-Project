##### Lessons
- Lesson 1: Find letters and basics
	- Explain basic regex structure "/stuff/tail"
	- Flags look like "\" and have special meaning they go in "stuff"
	- Explain how to find any character "/a/" this example will look for a
  
- Lesson 2: Numbers and Number Specific wildcards
	- 1234
	- "/\d/" is any number 1-9
	- "/\D/" is its opposite it only grabs not numbers
	
- Lesson 3: Wildcards
	- Explain how the . works "/a../" will find add and ave and app
	- If you need to get dot use "/\./"
	
- Lesson 4: Words
	- Word "/\w/" will get whole words
	- "/\W/" is the opposite getting any not word
	
- Lesson 5: Tails
	- Explain how to search for all occurances "/a/g" this will look for every a
	- Explain how to find a whole word ex: "/the/" or all occurances "/the/g"
	- Explain how to ignore case with "/the/i" and "/THE/i"
	
- Lesson 6: Ranges
	Explain ranges "/[A-C]d/" will use the range A-C so it will find Ad, Bd, Cd and the carrot works as well, "/[^A-C]d/" will find Dd but not Ad, Bd, or Cd. THIS IS CASE SENSATIVE
	
- Lesson 7: Brackets
	- Explain how to search for array of words "/[aio]s/" will find as, is, and os
	- Explain how ^ effects brackets instead of search for these letter it means if this letter then ignore "/[^bh]og/" will ignore hog and bog but find jog
	
- Lesson 8: Heads and Tails
	- "/^stuff/" if it starts with stuff
	- "/stuff$/" if it ends with stuff
	
- Lesson 9: Logic
	- or is | so "/(I love) cats|dogs/" will return on  I love cats and I love dogs
	
- Lesson 10: Repetitions
	- "/a{2,4}/" will find aa, aaa, aaaa, and aaaa
	- "/a{3}/" will find aaa