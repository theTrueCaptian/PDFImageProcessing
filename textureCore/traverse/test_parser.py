'''

'''
from parser import *

dictionary_name = "university_name"

# match := regular_expression
check(test("[A-Z]+[a-z]+"), 			[{"attribute":"regular_expression", "attribute_index":0, "expected":"[A-Z]+[a-z]+"}])
check(test("[A-EA]"), 					[{"attribute":"regular_expression", "attribute_index":0, "expected":"[A-EA]"}])
check(test("[A-D]*"), 					[{"attribute":"regular_expression", "attribute_index":0, "expected":"[A-D]*"}])
check(test("[A-D]{3}"), 				[{"attribute":"regular_expression", "attribute_index":0, "expected":"[A-D]{3}"}])
check(test("X[A-C]{3}Y"), 				[{"attribute":"regular_expression", "attribute_index":0, "expected":"X[A-C]{3}Y"}])
check(test("X[A-C]{3}\("), 				[{"attribute":"regular_expression", "attribute_index":0, "expected":"X[A-C]{3}\("}])
check(test("X\d"), 						[{"attribute":"regular_expression", "attribute_index":0, "expected":"X\d"}])
check(test("foobar\d\d"), 				[{"attribute":"regular_expression", "attribute_index":0, "expected":"foobar\d\d"}])
check(test("foobar{2}"), 				[{"attribute":"regular_expression", "attribute_index":0, "expected":"foobar{2}"}])
check(test("foobar{2,9}"), 				[{"attribute":"regular_expression", "attribute_index":0, "expected":"foobar{2,9}"}])
check(test("fooba[rz]{2}"), 			[{"attribute":"regular_expression", "attribute_index":0, "expected":"fooba[rz]{2}"}])
check(test("(foobar){2}"), 				[{"attribute":"regular_expression", "attribute_index":0, "expected":"(foobar){2}"}])
check(test("([01]\d)|(2[0-5])"), 		[{"attribute":"regular_expression", "attribute_index":0, "expected":"([01]\d)|(2[0-5])"}])
check(test("([01]\d\d)|(2[0-4]\d)|(25[0-5])"), [{"attribute":"regular_expression", "attribute_index":0, "expected":"([01]\d\d)|(2[0-4]\d)|(25[0-5])"}])
check(test("[A-C]{1,2}"), 				[{"attribute":"regular_expression", "attribute_index":0, "expected":"[A-C]{1,2}"}])
check(test("[A-C]{0,3}"), 				[{"attribute":"regular_expression", "attribute_index":0, "expected":"[A-C]{0,3}"}])
check(test("[A-C]\s[A-C]\s[A-C]"), 		[{"attribute":"regular_expression", "attribute_index":0, "expected":"[A-C]\s[A-C]\s[A-C]"}])
check(test("[A-C]\s?[A-C][A-C]"), 		[{"attribute":"regular_expression", "attribute_index":0, "expected":"[A-C]\s?[A-C][A-C]"}])
check(test("[A-C]\s([A-C][A-C])"), 		[{"attribute":"regular_expression", "attribute_index":0, "expected":"[A-C]\s([A-C][A-C])"}])
check(test("[A-C]\s([A-C][A-C])?"), 	[{"attribute":"regular_expression", "attribute_index":0, "expected":"[A-C]\s([A-C][A-C])?"}])
check(test("[A-C]{2}\d{2}"), 			[{"attribute":"regular_expression", "attribute_index":0, "expected":"[A-C]{2}\d{2}"}])
check(test("@|TH[12]"), 				[{"attribute":"regular_expression", "attribute_index":0, "expected":"@|TH[12]"}])
check(test("@(@|TH[12])?"), 			[{"attribute":"regular_expression", "attribute_index":0, "expected":"@(@|TH[12])?"}])
check(test("@(@|TH[12]|AL[12]|SP[123]|TB(1[0-9]?|20?|[3-9]))?"), [{"attribute":"regular_expression", "attribute_index":0, "expected":"@(@|TH[12]|AL[12]|SP[123]|TB(1[0-9]?|20?|[3-9]))?"}])
check(test("@(@|TH[12]|AL[12]|SP[123]|TB(1[0-9]?|20?|[3-9])|OH(1[0-9]?|2[0-9]?|30?|[4-9]))?"), [{"attribute":"regular_expression", "attribute_index":0, "expected":"@(@|TH[12]|AL[12]|SP[123]|TB(1[0-9]?|20?|[3-9])|OH(1[0-9]?|2[0-9]?|30?|[4-9]))?"}])
check(test("(([ECMP]|HA|AK)[SD]|HS)T"), [{"attribute":"regular_expression", "attribute_index":0, "expected":"(([ECMP]|HA|AK)[SD]|HS)T"}])
check(test("[A-CV]{2}"), 				[{"attribute":"regular_expression", "attribute_index":0, "expected":"[A-CV]{2}"}])
check(test("A[cglmrstu]|B[aehikr]?|C[adeflmorsu]?|D[bsy]|E[rsu]|F[emr]?|G[ade]|H[efgos]?|I[nr]?|Kr?|L[airu]|M[dgnot]|N[abdeiop]?|Os?|P[abdmortu]?|R[abefghnu]|S[bcegimnr]?|T[abcehilm]|Uu[bhopqst]|U|V|W|Xe|Yb?|Z[nr]"), [{"attribute":"regular_expression", "attribute_index":0, "expected":"A[cglmrstu]|B[aehikr]?|C[adeflmorsu]?|D[bsy]|E[rsu]|F[emr]?|G[ade]|H[efgos]?|I[nr]?|Kr?|L[airu]|M[dgnot]|N[abdeiop]?|Os?|P[abdmortu]?|R[abefghnu]|S[bcegimnr]?|T[abcehilm]|Uu[bhopqst]|U|V|W|Xe|Yb?|Z[nr]"}])
check(test("(a|b)|(x|y)"), 				[{"attribute":"regular_expression", "attribute_index":0, "expected":"(a|b)|(x|y)"}])
#check(test("(a|b) (x|y)"), 				[{"attribute":"regular_expression", "attribute_index":0, "expected":"(a|b) (x|y)"}])

# match := is
check(test("is(Person)"), 				[{"attribute":"isEntity", "attribute_index":0, "expected":"is"}, {"attribute":"isEntity", "attribute_index":2, "expected":"Person"}])

# match := in
check(test("in("+dictionary_name+")"), 	[{"attribute":"inDict", "attribute_index":0, "expected":"in"}, {"attribute":"inDict", "attribute_index":2, "expected":dictionary_name}])
# match := permute(rule*)
# match := rule*
'''
#----------------------------------------------------------------
# match := regular_expression  		box := part
check(test("[A-Z]+[a-z]+ from page"), 		[{"attribute":"regular_expression", "attribute_index":0, "expected":"[A-Z]+[a-z]+"}, {"attribute":"box", "attribute_index":0, "expected":"page"}])
check(test("[A-Z]+[a-z]+ from section"),	[{"attribute":"regular_expression", "attribute_index":0, "expected":"[A-Z]+[a-z]+"}, {"attribute":"box", "attribute_index":0, "expected":"section"}])
check(test("[A-Z]+[a-z]+ from group"), 		[{"attribute":"regular_expression", "attribute_index":0, "expected":"[A-Z]+[a-z]+"}, {"attribute":"box", "attribute_index":0, "expected":"group"}])
check(test("[A-Z]+[a-z]+ from paragraph"), 	[{"attribute":"regular_expression", "attribute_index":0, "expected":"[A-Z]+[a-z]+"}, {"attribute":"box", "attribute_index":0, "expected":"paragraph"}])
check(test("[A-Z]+[a-z]+ from lines"), 		[{"attribute":"regular_expression", "attribute_index":0, "expected":"[A-Z]+[a-z]+"}, {"attribute":"box", "attribute_index":0, "expected":"lines"}])
check(test("[A-Z]+[a-z]+ from heading"), 	[{"attribute":"regular_expression", "attribute_index":0, "expected":"[A-Z]+[a-z]+"}, {"attribute":"box", "attribute_index":0, "expected":"heading"}])
check(test("[A-Z]+[a-z]+ from title"), 		[{"attribute":"regular_expression", "attribute_index":0, "expected":"[A-Z]+[a-z]+"}, {"attribute":"box", "attribute_index":0, "expected":"title"}])
check(test("[A-Z]+[a-z]+ from line"), 		[{"attribute":"regular_expression", "attribute_index":0, "expected":"[A-Z]+[a-z]+"}, {"attribute":"box", "attribute_index":0, "expected":"line"}])


# match := regular_expression  		box := part operator+regex
check(test("[A-Z]+[a-z]+ from page after regex"), 	[{"attribute":"regular_expression", "attribute_index":0, "expected":"[A-Z]+[a-z]+"}, {"attribute":"part", "attribute_index":0, "expected":"page"},{"attribute":"box_expression", "attribute_index":0, "expected":"after"}, {"attribute":"box_expression", "attribute_index":1, "expected":"regex"}])
test("[A-Z]+[a-z]+ from page before regex ")

test("[A-Z]+[a-z]+ from page within regex")
test("[A-Z]+[a-z]+ from page contains regex")
test("[A-Z]+[a-z]+ from section after regex")
test("[A-Z]+[a-z]+ from section before regex ")
test("[A-Z]+[a-z]+ from section within regex")
test("[A-Z]+[a-z]+ from section contains regex")
test("[A-Z]+[a-z]+ from group after regex")
test("[A-Z]+[a-z]+ from group before regex ")
test("[A-Z]+[a-z]+ from group within regex")
test("[A-Z]+[a-z]+ from group contains regex")
test("[A-Z]+[a-z]+ from paragraph after regex")
test("[A-Z]+[a-z]+ from paragraph before regex ")
test("[A-Z]+[a-z]+ from paragraph within regex")
test("[A-Z]+[a-z]+ from paragraph contains regex")
test("[A-Z]+[a-z]+ from lines after regex")
test("[A-Z]+[a-z]+ from lines before regex ")
test("[A-Z]+[a-z]+ from lines within regex")
test("[A-Z]+[a-z]+ from lines contains regex")
test("[A-Z]+[a-z]+ from heading after regex")
test("[A-Z]+[a-z]+ from heading before regex ")
test("[A-Z]+[a-z]+ from heading within regex")
test("[A-Z]+[a-z]+ from heading contains regex")
test("[A-Z]+[a-z]+ from title after regex")
test("[A-Z]+[a-z]+ from title before regex ")
test("[A-Z]+[a-z]+ from title within regex")
test("[A-Z]+[a-z]+ from title contains regex")
test("[A-Z]+[a-z]+ from line after regex")
test("[A-Z]+[a-z]+ from line before regex ")
test("[A-Z]+[a-z]+ from line within regex")
test("[A-Z]+[a-z]+ from line contains regex")
# match := regular_expression  		box := part operator+box*
# match := regular_expression  		box := part between*

#----------------------------------------------------------------
# match := regular_expression 		box := part n
test("[A-Z]+[a-z]+ from page 1")
test("[A-Z]+[a-z]+ from section 1")
test("[A-Z]+[a-z]+ from group 1")
test("[A-Z]+[a-z]+ from paragraph 1")
test("[A-Z]+[a-z]+ from lines 1")
test("[A-Z]+[a-z]+ from heading 1")
test("[A-Z]+[a-z]+ from title 1")
test("[A-Z]+[a-z]+ from line 1")
# match := regular_expression 		box := part n operator_regex
test("[A-Z]+[a-z]+ from page 1 after regex")
test("[A-Z]+[a-z]+ from page 1 before regex ")
test("[A-Z]+[a-z]+ from page 1 within regex")
test("[A-Z]+[a-z]+ from page 1 contains regex")
test("[A-Z]+[a-z]+ from section 1 after regex")
test("[A-Z]+[a-z]+ from section 1 before regex ")
test("[A-Z]+[a-z]+ from section 1 within regex")
test("[A-Z]+[a-z]+ from section 1 contains regex")
test("[A-Z]+[a-z]+ from group 1 after regex")
test("[A-Z]+[a-z]+ from group 1 before regex ")
test("[A-Z]+[a-z]+ from group 1 within regex")
test("[A-Z]+[a-z]+ from group 1 contains regex")
test("[A-Z]+[a-z]+ from paragraph 1 after regex")
test("[A-Z]+[a-z]+ from paragraph 1 before regex ")
test("[A-Z]+[a-z]+ from paragraph 1 within regex")
test("[A-Z]+[a-z]+ from paragraph 1 contains regex")
test("[A-Z]+[a-z]+ from lines 1 after regex")
test("[A-Z]+[a-z]+ from lines 1 before regex ")
test("[A-Z]+[a-z]+ from lines 1 within regex")
test("[A-Z]+[a-z]+ from lines 1 contains regex")
test("[A-Z]+[a-z]+ from heading 1 after regex")
test("[A-Z]+[a-z]+ from heading 1 before regex ")
test("[A-Z]+[a-z]+ from heading 1 within regex")
test("[A-Z]+[a-z]+ from heading 1 contains regex")
test("[A-Z]+[a-z]+ from title 1 after regex")
test("[A-Z]+[a-z]+ from title 1 before regex ")
test("[A-Z]+[a-z]+ from title 1 within regex")
test("[A-Z]+[a-z]+ from title 1 contains regex")
test("[A-Z]+[a-z]+ from line 1 after regex")
test("[A-Z]+[a-z]+ from line 1 before regex ")
test("[A-Z]+[a-z]+ from line 1 within regex")
test("[A-Z]+[a-z]+ from line 1 contains regex")
# match := regular_expression 		box := part n operator_box*
# match := regular_expression 		box := part n between*

#----------------------------------------------------------------
# match := regular_expression 		box := part n to m
test("[A-Z]+[a-z]+ from page 1 to 3")
test("[A-Z]+[a-z]+ from section 1 to 3")
test("[A-Z]+[a-z]+ from group 1 to 3")
test("[A-Z]+[a-z]+ from paragraph 1 to 3")
test("[A-Z]+[a-z]+ from lines 1 to 3")
test("[A-Z]+[a-z]+ from heading 1 to 3")
test("[A-Z]+[a-z]+ from title 1 to 3")
test("[A-Z]+[a-z]+ from line 1 to 3")
# match := regular_expression 		box := part n to m operator_regex
test("[A-Z]+[a-z]+ from page 1 to 3 after regex")
test("[A-Z]+[a-z]+ from page 1 to 3 before regex ")
test("[A-Z]+[a-z]+ from page 1 to 3 within regex")
test("[A-Z]+[a-z]+ from page 1 to 3 contains regex")
test("[A-Z]+[a-z]+ from section 1 to 3 after regex")
test("[A-Z]+[a-z]+ from section 1 to 3 before regex ")
test("[A-Z]+[a-z]+ from section 1 to 3 within regex")
test("[A-Z]+[a-z]+ from section 1 to 3 contains regex")
test("[A-Z]+[a-z]+ from group 1 to 3 after regex")
test("[A-Z]+[a-z]+ from group 1 to 3 before regex ")
test("[A-Z]+[a-z]+ from group 1 to 3 within regex")
test("[A-Z]+[a-z]+ from group 1 to 3 contains regex")
test("[A-Z]+[a-z]+ from paragraph 1 to 3 after regex")
test("[A-Z]+[a-z]+ from paragraph 1 to 3 before regex ")
test("[A-Z]+[a-z]+ from paragraph 1 to 3 within regex")
test("[A-Z]+[a-z]+ from paragraph 1 to 3 contains regex")
test("[A-Z]+[a-z]+ from lines 1 to 3 after regex")
test("[A-Z]+[a-z]+ from lines 1 to 3 before regex ")
test("[A-Z]+[a-z]+ from lines 1 to 3 within regex")
test("[A-Z]+[a-z]+ from lines 1 to 3 contains regex")
test("[A-Z]+[a-z]+ from heading 1 to 3 after regex")
test("[A-Z]+[a-z]+ from heading 1 to 3 before regex ")
test("[A-Z]+[a-z]+ from heading 1 to 3 within regex")
test("[A-Z]+[a-z]+ from heading 1 to 3 contains regex")
test("[A-Z]+[a-z]+ from title 1 to 3 after regex")
test("[A-Z]+[a-z]+ from title 1 to 3 before regex ")
test("[A-Z]+[a-z]+ from title 1 to 3 within regex")
test("[A-Z]+[a-z]+ from title 1 to 3 contains regex")
test("[A-Z]+[a-z]+ from line 1 to 3 after regex")
test("[A-Z]+[a-z]+ from line 1 to 3 before regex ")
test("[A-Z]+[a-z]+ from line 1 to 3 within regex")
test("[A-Z]+[a-z]+ from line 1 to 3 contains regex")
# match := regular_expression 		box := part n to m operator_box*
# match := regular_expression 		box := part n to m between*
#----------------------------------------------------------------


test("is(Person) from title #1 after Education")
'''
