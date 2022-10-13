zwembad_meters = 8*3*1.5
zwembad_uitgraven = zwembad_meters*25
zwembad_afvoeren = zwembad_meters*32.5
zwembad_totaal = round(zwembad_uitgraven + zwembad_afvoeren)

print(f"Offerte van een zwembed van 8x3x1.5 meter (inhoud {zwembad_meters} m3)")
print(f"Uitgraven : €{zwembad_uitgraven} ")
print(f"Afvoeren Grond : €{zwembad_afvoeren} ")
print(f"Totaal : €{zwembad_totaal} ")