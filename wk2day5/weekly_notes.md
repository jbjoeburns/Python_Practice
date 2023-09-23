## Day 1: data types and variables

virtual environment
- can right click to change virtual environment
- This allows you to set up environment variables/libraries specific to certain purposes specific to certain projects
- Can also right click to change local interpreter (different python versions)

variables 
- a variable is a storage location paired with an associated symbolic name (an identifier) which contains a value
- can contain a range of data, such as integers, strings, dictionaries, lists, etc…

value
- can contain a range of data, such as integers, strings, dictionaries, lists, etc…

Operators
- symbols that execute particular mathematical/logical function
- arithmetic operators: +, -, *, /, % 
  - These are basically anything that is used in a maths operation to calculate something
- Logical/comparison operations: >, <, ==, !=, >=, <= 
  -	The operators that ask how two values relate to eachother
- Numeric types: int, float, complex
- Type of number a variable is

Strings
- Can use ‘string’ or “string”
- Double quotes are preferred because of words like let’s, but varies on a case by case basis

Slicing
- `Variable[x:y]`
- Where x is where the sliced sting starts from
- And y is where the sliced string ends
- So 3:6 would start at the 3rd character then end at the 6th (for “Hello world!” this would be “lo”)
- Can use negatives
- `Variable[z]` would give single character, where z is the index

Strip and replace
- Removes character you give it
    -	Eg. `variable.strip(‘z’)` would remove all instances of ‘z’
- Not specifying a letter will instead remove white space
- Replace can be used to replace the stripped letter instead of removing it
    -	Eg. `variable.replace(‘z’, ‘e’)`

Count
- Counts instances of character and returns number
  -	Eg. `variable.count(‘z’)`

Lower and capitalize
- Changes case
  -	`variable.lower(“WORD”)` gives you “word”
  -	`variable.capitalize(“word”)` gives you “WORD”

f-strings
- formatted stringes
- kinda works how {}s work in javascript
  - eg. `print(f”{value1} is greater than {value2} because of etc etc”)`
- can do other cool things shorthand
  -	eg. if you wanted to do something like percentage of something
  -	`print(f”you scored {score/max_score:.2%}”)`
  -	this will give you the percentage someone scored
  -	score/max_score gives score over max score
  -	.2 gives you it to 2 dp
  -	And the % tells you the remainder, but as you’re dividing to get a percentage you will have a value between 1 and 0, so the remainder is functionally the same as x100 in this situation

Boolean
- True or false
- `bool(x)`
- can also use ints 
  -	eg. `bool(0)` is false
  -	`bool(1)` is true
  -	`bool(999)` is also true because numbers greater than 0 are true
- `bool(None)` = false, but None realistically works independently of true and false
  
None
- Absence of a value, effectively the same as Null
- Proper use
  -	`z == None`	BAD FORM
  -	`z is None`	GOOD FORM
  -	None isn’t realistically equal to anything, as it’s the absence of a value

Lists
- In python, if you do the following it will replace the entry at that index and update the list
  -	`ListOne[2] = “Tomato”`
- `listOne.append(“carrot”)` adds “carrot” to the end of the list
- `listOne.extend(“carrot”, “fish”)` adds “carrot” AND “fish” to the end of the list
- `listOne.remove(“carrot”)` removes “carrot” from the list, TAKE CARE ABOUT CHANGING INDEXES
- `listOne.pop(“carrot”)` takes out “carrot” from the list and returns it, if pop is empty it just pops the last entry in the list

tuples
- Like lists but immutable
  -	`tupleExample = (“bread”, “eggs”, “milk”)`

dictionaries
- key value pairs
- Formatted like;
`dictName = {
“name”: “Joe”,
“name": "Luke”,
}`
- Can include lists as values

Sets
- Like lists, but random order
- No index
- Use curly brackets but no keys
- `setExample = {“bread”, “eggs”, “milk”}`
- mutable