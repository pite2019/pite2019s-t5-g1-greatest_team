import math

class LogWriter(object):


	def __init__(self, list_data, head_text):
		#7
		#save list_data and head_text as members of this object
		# create member o_count with value None
		self.list_data = list_data
		self.head_text = head_text
		self.o_count = None

	@staticmethod
	def get_every_second_element(data):
		#1
		# return every second element (counting from index 1) from passed list
		# e.g. get_every_second_element([1,2,3,4]) == [2,4]
		pass

	@staticmethod
	def avg_every_second_element(data):
		#2
		#return the average of every second element
		#(use function get_every_second_element )
		#e.g:
		# avg_every_second_element([1,2,3,4]) == 3.0
		li = LogWriter.get_every_second_element(data)
		return sum(li)/len(li)

	@staticmethod
	def insert_data_in_text(text, data):
		
		list_as_string = str(data)
		to_find = 'list'
		index = text.find(to_find) + len(to_find)
		output = text[:index] + ' (' + list_as_string + ')' + text[index:]

		return output

	@staticmethod
	def count_o(text):
		small = text.lower()
		return small.count("o")

	def get_first_part(self):
		#5
		#append head_text (member of this object) with string
		#"_________" followed by "\n After change: \n"
		# append the output of insert_data_in_text applied
		#on head_text and list_data (members of this object).
		#Set member o_count with number of o's in contained
		# in text you created above - use count_o.
		# Return newly created text AND value of o_count
		str = ""
		str = self.head_text + "_________" + "\n After change: \n"
		str += self.insert_data_in_text(self.head_text, self.list_data)
		self.o_count = self.count_o(str)
		return (str,self.o_count)

	@staticmethod
	def what_is_added_the_meaning_of_life(add=None):
		#6
		#return square root of 42 PLUS add
		# if add is not given return 42
		#
		if add == None:
			return math.sqrt(42)
		else:
			return math.sqrt(42 + add)

	@staticmethod
	def what_is_your_quest(quest="holy grail"):
		#8
		# if the argument is not specified return "To seek the holy grail"
		# in other case append the texts "To seek the " with argument and return
		if quest == "holy grail":
			return "To seek the holy grail"
		else:
			return "To seek the " + quest

	@staticmethod
	def get_second_word(text):
		#9
		# Return the second word of text
		splitted = text.split()
		second_word = splitted[1]
		return second_word

	def o_count_is_even(self):
		if self.o_count % 2 == 0:
		    return True
		else:
		    return False
		pass

	def get_movie_reference(self):
		#11
		#this is the tough one
		#use o_count is even (use o_count_is_even())
		#If o_count is even set output of this function
		#to value of what_is_added_the_meaning_of_life applied on o_count
		#If o_count is odd setoutput to be the value of what_is_your_quest applied on
		#the second word of head_text (member of this object).
		#Lastly if o_count is higher than seven append empty line and
		#empty call of what_is_your_quest to the output.
		#Return the output
		result = "" 
		if self.o_count_is_even():
			result = self.what_is_added_the_meaning_of_life(self.o_count)
		else:
			result = self.what_is_your_quest(get_second_word(self.head_text))

		if self.o_count > 7:
			result = "\n" + self.what_is_your_quest()

		return result
		pass

	@staticmethod
	def computation(x):
		#12
		# return the the sum of:
		# x to the second power
		# square root of x
		# square root of the square root of x
		x_2nd_power = x ** 2
		x_square_root = math.sqrt(x)
		x_square_root_2 = math.sqrt(x_square_root)
		return x_2nd_power + x_square_root + x_square_root_2

	def get_second_part(self, computation=None):
		#13
		# append the:
		# - new line
		# and
		# - the value of function computation (in argument)
		# applied on number 47
		# to the output of get_movie_reference
		Ret = self.get_movie_reference() + '\n'+ str(computation(47))
		return Ret

	def combining_method(self):
		#14
		#concatenate:
		# - text output from get_first_part
		# - string "0 O 0 O 0 O 0 O 0 O 0 O"
		# - output of get_second_part applied on computation method (class member)
		#return the concatenation
		return self.get_first_part()[0] + "0 O 0 O 0 O 0 O 0 O 0 O" + self.get_second_part(self.computation)

	def __str__(self):
		return self.combining_method()

if __name__=="__main__":
	head_text ="""
	Stil liist shilts list 1ist tilst iist l1ist? 'WHAT DID THE 0NE SNO0WMAN SAY TO THE OTHER SNOWMAN? 00O0O'
	"""
	list_data = [1,2,34,4]
	test_instance = LogWriter(list_data, head_text)
	print(test_instance)

#
#examplary output is below
#
"""

Stil liist shilts list 1ist tilst iist l1ist? 'WHAT DID THE 0NE SNO0WMAN SAY TO THE OTHER SNOWMAN? 00O0O'
_________
 After change:

Stil liist shilts list ([1, 2, 34, 4]) 1ist tilst iist l1ist? 'WHAT DID THE 0NE SNO0WMAN SAY TO THE OTHER SNOWMAN? 00O0O'
0 O 0 O 0 O 0 O 0 O 0 O7.483314773547883
To seek the holy grail
22218.473985099097
"""
