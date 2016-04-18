# History of Regular Expressions

#### A Formative Idea

Regular Expressions started in 1943 as a concept in neuroscience when Doctors Warren McCulloch and Walter Pitts published 'A logical calculus of the ideas immanent in nervous activity' in the Bulletin of Mathematical Biophysics 5:115-133. The purpose and idea of the paper was more abstract than an algebra for language, however it was incredibly influential on the field computer science. In 1956, Stephen Kleene published "Representation of events in nerve nets and finite automata" where he presented a simple algebra for expressing language. Around this time is when the term regular expression was born.<sup>[1](#References)</sup>

#### Algorithm Development

Ken Thompson published an article in the Communications of the ACM in 1968 titled "Regular Expression Search Algorithm" where he first described a compiler for regular expressions. Ken is a storied computer scientist who implemented the original Unix operating system and invented B, the predecessor to C. He is also the co-creator of Google's viral parallel computation language Go. After his 1968 paper he implemented Kleene's notation in the QED editor to do advanced pattern matching on text files. The feature also appeared in ed, the editor that led to vi. These formalizations of the idea of regular expression into a pattern matching feature were incredibly important in the formative years of regex, and we have Ken to thank.<sup>[2](#References)</sup>

#### Going Viral

When you would use Ken's regular expression feature the command would take the following form.
```
g/regular_expression/p
g - global
p - print result

in short

g/re/p
```
If you have used a Unix-like system before then you probably recognize the inspiration for the powerful `grep` command. `grep` came to Unix system in 1973, which was a formalization of the ideas and features implemented in QED and ed. It was not until 1979, though, when a fully featured implementation was brought to unix in the form of `egrep` by Alfred Aho.

The Perl programming language then came along in 1987 where Larry Wall which was a prime showcase of the power of a regular expression engine for manipulating text files integrated with a programming language. The myriad of uses and conveniences afforded by the engine brought regular expression into the limelight.<sup>[3](#References)</sup>

Since then, Kleene's algebra has been implemented in many popular programming languages. However, each implementation has slight variations, optimizations, and additional features added. It is important to understand that regular expressions are not universal, and that problems can arise from specific-implementations. We hope to teach you the general platitudes of regular expressions and the power of this pattern matching language as well as the pitfalls that language-specific implementations have.


## References

[1] - https://blog.staffannoteberg.com/2013/01/30/regular-expressions-a-brief-history/

[2] - https://en.wikipedia.org/wiki/Ken_Thompson

[3] - https://en.wikipedia.org/wiki/Perl
