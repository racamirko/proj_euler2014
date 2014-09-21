texts = { 0 : '', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5:'five', 6:'six', 7: 'seven', 8 : 'eight', 9: 'nine',
			 10: 'ten', 11: 'eleven', 12:'twelve', 13:'thirteen', 14: 'fourteen', 15: 'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen',
			 20: 'twenty', 30: 'thirty', 40: 'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety',
			 100: 'one'+'hundred', 200:'two'+'hundred', 300:'three'+'hundred', 400:'four'+'hundred', 500:'five'+'hundred',
			 600: 'six'+'hundred', 700:'seven'+'hundred', 800:'eight'+'hundred', 900:'nine'+'hundred', 1000:'onethousand' }

def spell_out(x):
	out_spell = []
	subsum = 0
	if x > 99:
		out_spell.append(texts[x / 100 * 100])
		if x % 100 != 0:
			out_spell.append('and')
	if (x % 100) >=10 and (x%100) < 20:
		out_spell.append(texts[x % 100])
	else:
		out_spell.append(texts[(x % 100) / 10 * 10])
		out_spell.append(texts[x % 10])
	for l in out_spell:
		subsum += len(l)
	return ' '.join(out_spell), subsum

ss = 0
for x in xrange(1, 1001):
	w, l = spell_out(x)
	print("%d = %s" % (x, w))
	ss += l

print(ss)