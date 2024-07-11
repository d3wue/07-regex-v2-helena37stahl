import re


reg = re.compile("(Prof\. |Dr\. )*([A-Z][a-z]+) ([A-Z\.a-z]*) ?([A-Z][a-z]+)(, (PhD|MSC|Duke of Manchester|KG|KT|PC|ADC))*")

#Slash um echten punkt zu escapen
#? das z.B. Leerezichen optional ist
#* steht für beliebig oft
#| oder
#^damit muss der string anfangen
#$ damit muss der String aufhören
m = reg.match("Uwe Meier")
if m:
    print(m.group(0))
else:
    print(m)
m = reg.match("Prof. Dr. Chris C Schmidt")
if m:
    print(m.group(0))
else:
    print(m)
m = reg.match("Hanna J Gruber, PhD")
if m:
    print(m.group(0))
else:
    print(m)
m = reg.match("Hanna J. Gruber, PhD")
if m:
    print(m.group(0))
else:
    print(m)
m = reg.match("Hanna Jana Gruber, PhD, MSc")
if m:
    print(m.group(0))
else:
    print(m)
m = reg.match("Dr. Uwe Meier, MSc")
if m:
    print(m.group(0))
else:
    print(m)
m = reg.match("Dr. Alfred Nobel, PhD, PhD, PhD, MSc")
if m:
    print(m.group(0))
else:
    print(m)
m = reg.match("Dr. Dr. Dr. Theodore Hesburgh, PhD, PhD, PhD, MSc")
if m:
    print(m.group(0))
else:
    print(m)
m = reg.match("Albert KD Klein, PhD, PhD, PhD, MSc")
if m:
    print(m.group(0))
else:
    print(m)
m = reg.match("Prince William, Duke of Manchester, KG, KT, PC, ADC")
if m:
    print(m.group(0))
else:
    print(m)
