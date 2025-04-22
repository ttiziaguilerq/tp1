beneficiario = str(input("Ingrese el nombre y apellido del beneficiario: "))
codigo = input("Ingrese el codigo: ")
monto_nominal = int(input("Ingrese el monto nominal: "))

if "ARS" in codigo:
    moneda = "ARS"
    monto_base = monto_nominal - ((monto_nominal * 5) / 100)
    monto_base = round(monto_base, 2)

elif "USD" in codigo:
    moneda = "USD"
    monto_base = monto_nominal - ((monto_nominal * 7) / 100)
    monto_base = round(monto_base, 2)

elif "EUR" in codigo:
    moneda = "EUR"
    monto_base = monto_nominal - ((monto_nominal * 7) / 100)
    monto_base = round(monto_base, 2)

elif "GBP" in codigo:
    moneda = "GBP"
    monto_base = monto_nominal - ((monto_nominal * 9) / 100)
    monto_base = round(monto_base, 2)

elif "JPY" in codigo:
    moneda = "JPY"
    monto_base = monto_nominal - ((monto_nominal * 9) / 100)
    monto_base = round(monto_base, 2)

else:
    moneda = "Moneda no autorizada"
    monto_base = 0

if monto_base > 500000:
    monto_final = monto_base-((monto_base * 21) / 100)
    monto_final = round(monto_final, 2)
else:
    monto_final = monto_base
    monto_final = round(monto_final, 2)

print("Beneficiario:", beneficiario)
print("Moneda:", moneda)
print("Monto base (descontadas las comisiones):", monto_base)
print("Monto final (descontados los impuestos):", monto_final)
