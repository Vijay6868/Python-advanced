# Programming challenge for comprehensions

import string
import pprint


test_str = "2 apples, 9 oranges?, 4 pears, Mike's 1 egg, Jane's 2 kiwis, $50!"

# YOUR CODE HERE
l = len(test_str)

#count the number of charachters 
nums = len([c for c in test_str if c.isnumeric])

#coutn the punctuation charachters
punct = len([c for c in test_str if c in string.punctuation])

#count the unique charachters
unique = "".join({c for c in test_str if c.isalpha()})
# print the data
str_data = {"length: ":l,
            "numeric count: ":nums,
            "punctuation count: ":punct,
            "unique: ":unique,
            "unique count: ":len(unique)
}
pprint.pp(str_data)

