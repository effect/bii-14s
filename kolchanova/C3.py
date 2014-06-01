#!/usr/bin/python
 
infile = open ("tower.in",'r')

inlines = infile.readlines()
#print inlines
def peop_lang(inlines):
    lang_vars = {}
    population = {}
    for someone, line in list(enumerate(inlines))[1:]:
        population[someone] = [int(x) for x in line.split()[1:]]
        for variant in population[someone]:
            lang_vars[variant] = lang_vars.get(variant, []) + [someone]
    return population, lang_vars
 
def thinker_f(start, uzd):
    uzd[start] = True
    for variant in population[start]:
        for neighbor in lang_vars[variant]:
            if not uzd[neighbor]:
                thinker_f(neighbor, uzd)

 
population, lang_vars = peop_lang(inlines)
uzd = {someone: False for someone in population.keys()}
start = 1
uzd = uzd 
thinker_f (start,uzd)

outfile =  open ("tower.out", "w")
outfile.write(str(uzd.values().count(True)))

outfile.close()
infile.close()