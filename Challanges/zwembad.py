zwembad_breedte = float(input("Geef de breedte van het zwembad in: "))
zwembad_lengte = float(input("Geef de lengte van het zwembad in: "))
zwembad_hoogte = float(input("Geef de hoogte van het zwembad in: "))



zwembad_meters = zwembad_lengte*zwembad_breedte*zwembad_hoogte
zwembad_uitgraven = zwembad_meters*25
zwembad_afvoeren = zwembad_meters*32.5
zwembad_voorijkosten = 250 + round(zwembad_meters * 2.05)
zwembad_vierkante_meters = zwembad_lengte*zwembad_breedte 
zwembad_beton_tegels = round(zwembad_vierkante_meters *zwembad_lengte * zwembad_hoogte*200 )
zwembad_totaal = round(zwembad_uitgraven + zwembad_afvoeren + zwembad_voorijkosten + zwembad_beton_tegels)

print(f"Offerte van een zwembed van {zwembad_breedte}bij {zwembad_lengte} bij {zwembad_hoogte} meter (inhoud {zwembad_meters} m3)")
print(f"Uitgraven : €{zwembad_uitgraven} ")
print(f"Afvoeren Grond : €{zwembad_afvoeren} ")
print(f"Voorrijkosten : €{zwembad_voorijkosten} ")
print(f"Beton + tegel ({zwembad_vierkante_meters}m2) : €{zwembad_beton_tegels} ")
print(f"Totaal : €{zwembad_totaal} ")