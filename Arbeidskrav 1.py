# Arbeidskrav 1

# Variabler
km = 16_000 #km/år
trafikkforsikringsavgift = 8.38 # kr/dag
antall_år = 10 # år (antall år å sjekke)

# Variabler for elbil
el_forsikring = 5_000 # kr/år
el_drivstoffbruk = 0.2 # kWh/km
el_strømpris = 2.0 # kr/kWh
el_bomavgift = 0.1 # kr/km

# Variabler for bensinbil
bensin_forsikring = 7_500 # kr/år
bensin_drivstoffbruk = 1.0 # kr/km
bensin_bomavgift = 0.3 # kr/km


# Bruker en for løkke for å iterere over antall år
for n in range(1, antall_år + 1):
    # Variabler for begge
    antall_km = n * km # Antall km på kjørte år
    antall_dager = n * 365 # Antall dager disse år (regner ikke med skuddår)

    # El
    el_pris_forsikring = el_forsikring * n + trafikkforsikringsavgift * antall_dager # Pris for forsikring
    el_pris_drivstoff = el_drivstoffbruk * antall_km * el_strømpris # Pris for drivstoff
    el_pris_bomavgift = el_bomavgift * antall_km # Pris for bomavgift

    el_pris_total = round(el_pris_forsikring + el_pris_drivstoff + el_pris_bomavgift, 1) # Totalpris for elbil (avrundet til 1 desimal)


    # Bensin
    bensin_pris_forsikring = bensin_forsikring * n + trafikkforsikringsavgift * antall_dager # Pris for forsikring
    bensin_pris_drivstoff = bensin_drivstoffbruk * antall_km # Pris for drivstoff
    bensin_pris_bomavgift = bensin_bomavgift * antall_km # Pris for bomavgift

    bensin_pris_total = round(bensin_pris_forsikring + bensin_pris_drivstoff + bensin_pris_bomavgift, 1) # Totalpris for bensin (avrundet til 1 desimal)


    pris_differanse = round(bensin_pris_total - el_pris_total, 1) # Prisdifferanse bensin - el (avrundet til 1 desimal)

    # Print bruker , som tusenseparator for lettere lesing
    print(str(n) + '. år totalpris for elbil: ' + f'{el_pris_total:,}' + ' kr') # Print pris for elbil
    print(str(n) + '. år totalpris for bensinbil: ' + f'{bensin_pris_total:,}' + ' kr') # Print pris for bensinbil
    print(str(n) + '. år prisdifferanse: ' + f'{pris_differanse:,}' + ' kr') # Print prisdifferanse
    print() # Print newline for ryddigere output
