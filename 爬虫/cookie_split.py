
cookies = "adh=dwa;5=dwada;dawdad=dwka;dwaddsawda=dadaw;nihao=nihao"

k = {i.split("=")[0]:i.split("=")[1] for i in cookies.split(";")}

print(k)


