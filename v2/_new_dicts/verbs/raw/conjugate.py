from pattern.en import conjugate
# conjugate(verb, 
# ...     tense = "past",           # INFINITIVE, PRESENT, PAST, FUTURE
# ...    person = 3,                # 1, 2, 3 or None
# ...    number = "singular",       # SG, PL
# ...      mood = "indicative",     # INDICATIVE, IMPERATIVE, CONDITIONAL, SUBJUNCTIVE
# ...    aspect = "imperfective",   # IMPERFECTIVE, PERFECTIVE, PROGRESSIVE 
# ...   negated = False)            # True or False

# #infinitive:
# conjugate(verb, tense = "infinitive")

# #gerund:
# conjugate(verb, tense = "present", aspect = "progressive")

# #past:
# conjugate(verb, tense = "past")

# #3rdPerson:
# conjugate(verb, tense = "present", person = 3)

def inf(verb):
	return conjugate(verb, tense = "infinitive")

def gerund(verb):
	return conjugate(verb, tense = "present", aspect = "progressive")

def past(verb):
	return conjugate(verb, tense = "past")

def third(verb):
	return conjugate(verb, tense = "present", person = 3)


