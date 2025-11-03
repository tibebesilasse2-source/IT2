import http.client

conn = http.client.HTTPSConnection("imdb-top-1000-movies-series.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "44a76a64d7msh81286dc50b51c1ep1d64c1jsn369a3da51ab2",
    'x-rapidapi-host': "imdb-top-1000-movies-series.p.rapidapi.com"
}

conn.request("GET", "/byrating", headers=headers)

res = conn.getresponse()
data = res.read()

print("🧾 API Response:")
print(data.decode("utf-8"))
