# single line string
name = "Mohammad Arsalan Rajput";

# multiline string 
greet = """In most languages like PHP and Python and others that have an exponentiation operator (**), 
 the exponentiation operator is defined to have
 a higher precedence than unary operators such as unary + and unary -,
 but there are a few exceptions.
 For example, in Bash the ** operator is defined to have a lower precedence than unary operators.
 In JavaScript, it is impossible to write an ambiguous exponentiation expression, 
 i.e. you cannot put a unary operator """;

print(greet[0]) # output H
print(greet[0:3]) # output Hel
print(greet[0:-1]) # output Hello Worl

print(greet.split(" "));
print(greet.upper());
print(greet.capitalize());
print(greet.count("a"));
print(greet.index("P"));