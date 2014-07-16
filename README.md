# fibonacci_message_encoding

## Idea
Using the Fibonacci sequence, a secret string is embedded in a listing
of words such that the secret string is not directly retrievable from
the listing.

Example: inmates passing secret messages between prisons use a code so
that the guards who read the messages are not able to see the secret
messages.

This entails that the sender and receiver place letters at certain
positions in the messages. This is effectively what we are doing, but
we will use the Fibonacci sequence as our determining position.

## Requirements
- Database of words [extremely large]
- Secret string to embed in a message
- Initial *m_0* value for beginning the Fibonacci sequence

## Algorithms

### Encode
1. Split the secret into characters
2. Generate Fibonacci values *v_m_n* using *m_0*
3. For each character *c_n*:
    1. Pick a word *w_n* such that character *c_n* is at 
       position *p* where
       
           p = (v - 1) mod s
       
       where
       - v = *v_m_n*
       - s = length of *w_n*
4. Append word to message

### Decode
1. Split the message into words
2. Generate Fibonacci values *v_m_n* using *m_0*
3. For each word *w_n*:
    1. Find the character *c_n*** at position *p* where
       
           p = (v - 1) mod s
       
       where
       - v = *v_m_n*
       - s = length of *w_n*
4. Append character to secret

## Todo
1. Elaborate on how the letter is encoded if the Fibonacci value
   is larger than the length of the word used.
2. Improve code, error handling, etc


## Examples

### Example 1
#### Encode
Given:

- secret := "**run**"
- *m_0* := 0

| n        | 0   | 1   | 2   |
|----------------------------|
| string   | 'r' | 'u' | 'n' |
| *v_m_n*  | 1   | 1   | 2   |
| p        | 0   | 0   | 1   |
| w_n      | w_0 | w_1 | w_2 |

- w_0: character 'r' at position 0
- w_1: character 'u' at position 0
- w_2: character 'n' at position 1

Many words will satisfy these conditions, therefore I will 
arbitrarily pick words that satisfy these conditions.

- w_0: "rain"
- w_1: "unnerve"
- w_2: "unnerve"

It is possible that a word can be used more than once using this
algorithm. We could have also chosen a different choice of words:

- w_0: "raise"
- w_1: "user"
- w_2: "unbecoming"

The second choice will be used in the decode


#### Decode
Given:

- message := "raise user unbecoming"
- *m_0* := 0

| n        | 0       | 1      | 2            |
|--------------------------------------------|
| words    | 'raise' | 'user' | 'unbecoming' |
| *v_m_n*  | 1       | 1      | 2            |
| p        | 0       | 0      | 1            |
| c_n      | c_0     | c_1    | c_2          |

- c_0: position 0 of w_0
- c_1: position 0 of w_1
- c_2: position 1 of w_2

Looking up the characters in the words gives:

- c_0: 'r'
- c_1: 'u'
- c_2: 'n'

Joined, we get our secret, "**run**".



