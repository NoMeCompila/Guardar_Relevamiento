# nro_cliente = [ "3303", "2986", "3183", "6200", "5800", "8100", "693", "700", "1480", "1920", "2023", "2193", "2279", "2500",
#                 "3431", "5100", "5200", "5500", "5700", "8700", "8800", "9070", "9080", "9170", "1916", "2241", "3414", "9130",
#                 "2987", "8200", "701", "707", "1249", "1250", "1252", "1253", "1255", "1256", "1257", "1274", "1418", "1645",
#                 "1731", "1814", "1875", "1966", "3419", "3444", "6600", "7000", "7500", "7600", "7800", "8000", "8400", "9000",
#                 "9010", "9040", "9060", "9090", "9100", "9120", "9140", "9160", "9190", "6500", "7400", "1900", "2419", "5000",
#                 "8500", "9150", "7700", "6700", "8300", "5600", "9050", "3524", "8900", "6000", "7900", "3010", "3055", "6300",
#                 "8600", "3366", "5300", "6100", "2919", "3019", "3231", "3275", "7200", "9020", "9030", "9110", "9180", "2628",
#                 "2765", "2879", "3022"]


# nueva_lista=[]
# for nro in nro_cliente:
#     nro = "C:\\" + nro + ".txt"
#     nueva_lista.append(nro)

# print(nueva_lista[0])
# #print(nro_cliente)
#from posixpath import join


import re
nro = 'C:\\3303.txt'

nro = re.findall(r'\d+', nro)

numero_cliente = "".join(nro)

print(numero_cliente)