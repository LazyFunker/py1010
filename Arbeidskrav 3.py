# Arbeidskrav 3

# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# del a

# Les excel filen inn i en panda dataframe
df = pd.read_excel('support_uke_24.xlsx')

# Lag arrayene med pandas
u_dag = df['Ukedag'].values
kl_slett = df['Klokkeslett'].values
varighet = df['Varighet'].values
score = df['Tilfredshet'].values


# del b

# Unike navn
x = pd.unique(u_dag)
# Antall unike navn, usortert
y = pd.Series(u_dag).value_counts(sort=False)

# Plot søylediagram
plt.grid()
plt.bar(x, y)
plt.show()


# del c

# Lag det til en timedelta med pandas
td = pd.to_timedelta(varighet)
# Sorter verdiene
td = td.sort_values()

# Første i sorterte arrayet gir korteste
kort = td[0]
# kort gir:
# 0 days 00:00:59
# -5: gir 5 siste (00:59) mm:ss

# Siste i sorterte arrayet gir lengste
lang = td[-1]
# 0 days 00:11:28
# Samme som over

print('Den korteste samtalen i uke 24 var: ' + str(kort)[-5:])
print('Den lengste samtalen i uke 24 var: ' + str(lang)[-5:])


# del d

gjennomsnitt = td.mean()
# gjennomsnitt gir:
# 0 days 00:06:40.009216589
# ..........X-->X..........
# 10 til 15 fjerner unødvendig tidsdata
print('Gjennomsnittlig samtaletid i uke 24 var: ' + str(gjennomsnitt)[10:15]) # Behold minutt og sekund i stringen


# del e

# sorter med pandas, og søk igjennom
dt = pd.to_timedelta(kl_slett).sort_values()

fra_8 = dt.searchsorted(['08:00:00', '10:00:00'])
fra_10 = dt.searchsorted(['10:00:00', '12:00:00'])
fra_12 = dt.searchsorted(['12:00:00', '14:00:00'])
fra_14 = dt.searchsorted(['14:00:00', '16:00:00'])

# Tuple, sluttindex - startindex gir antall
antall_fra_8 = fra_8[1] - fra_8[0]
antall_fra_10 = fra_10[1] - fra_10[0]
antall_fra_12 = fra_12[1] - fra_12[0]
antall_fra_14 = fra_14[1] - fra_14[0]

x = [antall_fra_8, antall_fra_10, antall_fra_12, antall_fra_14]
y = ['08:00 - 10:00', '10:00 - 12:00', '12:00 - 14:00', '14:00 - 16:00']

# Plot pie, med prosenter
plt.pie(x, labels=y, autopct='%1.0f%%')
plt.show()


# del f

# Bruk pandas series
num = pd.Series(score).sort_values()
# Trenger [a, b + 1] for å søke etter a -> b
negativ = num.searchsorted([1, 7])
neutral = num.searchsorted([7,9])
positiv = num.searchsorted([9,11])

# Tuple, sluttindex - startindex gir antall
antall_negativ = negativ[1] - negativ[0]
antall_neutral = neutral[1] - neutral[0]
antall_positiv = positiv[1] - positiv[0]

# Totale tilbakemeldinger
antall_total = antall_negativ + antall_neutral + antall_positiv

# Regn om til prosent med 1 desimal
prosent_negativ = np.round(antall_negativ / antall_total * 100, 1)
prosent_positiv = np.round(antall_positiv / antall_total * 100, 1)

# NPS = % positive kunder - % negative kunder
NPS = prosent_positiv - prosent_negativ

print('NPS\'en for supportavdelingen er: ' + str(NPS) + ' %')
