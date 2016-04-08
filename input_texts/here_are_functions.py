def ucfirst(source):
	return source[0].upper() + source[1:]

def human_join(parts, conj):
	if len(parts) == 1:
		return parts[0]
	elif len(parts) == 0:
		return ""
	first_part = ", ".join(parts[:-1])
	whole_thing = first_part + " " + conj+ " " + parts[-1]
	return whole_thing

def restaurant(building="House", foodstuff="Pancakes"):
	return "International " + building + " of " + foodstuff