zwembad_meters = 8*3*1.5
zwembad_uitgraven = zwembad_meters*25
zwembad_afvoeren = zwembad_meters*32.5
zwembad_voorijkosten = 250 + round(zwembad_meters * 2.05)
zwembad_totaal = round(zwembad_uitgraven + zwembad_afvoeren + zwembad_voorijkosten)

print(f"Offerte van een zwembed van 8x3x1.5 meter (inhoud {zwembad_meters} m3)")
print(f"Uitgraven : €{zwembad_uitgraven} ")
print(f"Afvoeren Grond : €{zwembad_afvoeren} ")
print(f"Voorrijkosten : €{zwembad_voorijkosten} ")
print(f"Totaal : €{zwembad_totaal} ")