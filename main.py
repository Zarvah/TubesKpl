from flask import *
app = Flask(__name__)

#table driven
#digunakan untuk pencarian turnamen bedasarkan nama game
game = {
    "Counter Strike: Global Offensive": {
        "jadwal": "Selasa, Rabu, Kamis (April 2022 - Mei 2022)",
        "jenis": "FPS",
        "gambar": "csgo.jpg"
    },
    "Valorant": {
        "jadwal": "Jumat - Minggu (Maret 2022 - Mei 2022)",
        "jenis": "FPS",
        "gambar": "valorant.jpg"
    },
    "Overwatch": {
        "jadwal": "Kamis, Jumat (Mei 2022 - Juni 2022)",
        "jenis": "FPS",
        "gambar": "overwatch.jpg"
    },
    "Dota 2": {
        "jadwal": "Senin, Sabtu, Minggu (April 2022 - Juni 2022)",
        "jenis": "MOBA",
        "gambar": "dota2.jpeg"
    },
    "League of Legends": {
        "jadwal": "Senin - Rabu (Februari 2022 - April 2022)",
        "jenis": "MOBA",
        "gambar": "lol.jpg"
    },
    "Heroes of the Storm": {
        "jadwal": "Senin, Kamis, Jumat, Minggu (Maret 2022 - April 2022)",
        "jenis": "MOBA",
        "gambar": "hots.jpg"
    },
    "PUBG Battlegrounds": {
        "jadwal": "Jumat, Minggu (Mei 2022 - Juli 2022)",
        "jenis": "Survival - TPS",
        "gambar": "pubg.jpg"
    },
    "Fortnite": {
        "jadwal": "Jumat - Minggu (April 2022 - Juli 2022)",
        "jenis": "Survival - TPS",
        "gambar": "fortnite.jpg"
    },
    "Rainbow Six Siege": {
        "jadwal": "Rabu, Jumat (Mei 2022 - Juni 2022)",
        "jenis": "FPS",
        "gambar": "rainbow.jpg"
    },
    "Apex Legends": {
        "jadwal": "Selasa - Kamis (April 2022 - Mei 2022)",
        "jenis": "Survival",
        "gambar": "apex.jpg"
    },
    "Destiny 2": {
        "jadwal": "Kamis, Jumat (April 2022)",
        "jenis": "FPS",
        "gambar": "destiny2.jpg"
    },
    "Rocket League": {
        "jadwal": "Jumat (Juni 2022 - Agustus 2022)",
        "jenis": "Racing - Football (Sports)",
        "gambar": "rocket.jpg"
    },
    "World of Tanks": {
        "jadwal": "Rabu (Mei 2022)",
        "jenis": "TPS - Driving",
        "gambar": "wot.jpg"
    },
    "Hearthstone": {
        "jadwal": "Selasa, Kamis (April 2022 - Mei 2022)",
        "jenis": "Strategi",
        "gambar": "hearthstone.jpg"
    },
    "Dead by Daylight": {
        "jadwal": "Senin (Juni 2022)",
        "jenis": "Survival",
        "gambar": "deadbydaylight.jpg"
    },
    "RF Online": {
        "jadwal": "Rabu - Jumat (Mei 2022 - Agustus 2022)",
        "jenis": "MMORPG",
        "gambar": "rf.jpg"
    },
    "Monster Hunter": {
        "jadwal": "Kamis - Sabtu (Juni 2022 - Juli 2022)",
        "jenis": "MMORPG",
        "gambar": "mh.jpg"
    },
    "Among Us": {
        "jadwal": "Minggu (Juli 2022)",
        "jenis": "Survival",
        "gambar": "amongus.jpg"
    },
    "Call of Duty Cold War": {
        "jadwal": "Sabtu, Minggu (Juli 2022 - September 2022)",
        "jenis": "FPS",
        "gambar": "cod.jpg"
    },
    "PES": {
        "jadwal": "Kamis - Minggu (Mei 2022 - Juni 2022)",
        "jenis": "Football (Sports)",
        "gambar": "pes.jpg"
    },
}

@app.route('/')
def cari():
    query = request.args.get('query')
    data = game
    if query != None:
        #menyaring data agar nama game sesuai dengan kata kunci pencarian
        data = {k:v for (k,v) in data.items() if query.lower() in k.lower()}
    return render_template('cari.html', data=data, query=query, datacount=len(data))

@app.route('/gambar_game/<filename>')
def gambar_game(filename):
	return send_file('/static/assets/images/'+filename, attachment_filename=filename)

app.run(debug = False, threaded=True)
