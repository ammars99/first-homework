import json 
amm = {
"""1) What is the capital of France ?
a.Paris
b.Cairo
""":"a",
"""2) What is the capital of Britain ?
a.London
b.Paris
""":"a",
"""3) What is the capital of Spain ?
a.Madrid
b.Paris
""":"a",
"""4) What is the capital of Italy?
a.Rome
b.Paris
""":"a",
"""5) What is the capital of German?
a.Berlin
b.Paris
""":"a",
"""6) What is the capital of Oman ?
a.Muscat
b.Paris
""":"a",
"""7) What is the capital of China ?
a.Bekin
b.Paris
""":"a",
"""8) What is the capital of Japan?
a.Tokyo
b.Paris
""":"a",
"""9) What is the capital of Russia?
a.Moscow
b.Paris
""":"a",
"""10) What is the capital of Egypt ?
a.Cairo
b.Paris
""":"a",
"""11) What is the capital of Syria ?
a.Moscow
b.Damascus
""":"b",
"""12) What is the capital of Iran ?
a.Moscow
b.Tahran
""":"b",
"""13) What is the capital of Lebanon?
a.Moscow
b.Beirot
""":"b",
"""14) What is the capital of Iraq?
a.Moscow
b.Baghdad
""":"b",
"""15) What is the capital of Yemen?
a.Moscow
b.Sana’a
""":"b",
"""16) What is the capital of Somalia ?
a.Moscow
b.Mogadishu
""":"b",
"""17) What is the capital of Morocco?
a.Moscow
b.Elrabat
""":"b",
"""18) What is the capital of Bahrain?
a.Moscow
b.Manama
""":"b",
"""19) What is the capital of Jordan?
a.Moscow
b.Amman
""":"b",
"""20) What is the capital of Romania?
a.Moscow
b.Bucharest
""":"b",
}
ammar=json.dumps(amm)
with open("ammar.json","w")as f:
    f.write(ammar)
