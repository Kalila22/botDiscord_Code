import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

def random_emoji():
    emojis = ["😀", "😂", "😍", "😎", "🥳", "🤩", "😺"]
    return random.choice(emojis)

def get_fakta():
    fakta_list = [
        "🌍Sekitar 8 juta ton sampah plastik masuk ke laut setiap tahun.",
        "♻️Mendaur ulang 1 ton kertas dapat menyelamatkan sekitar 17 pohon.",
        "💧Kurang dari 1% air di Bumi dapat langsung digunakan sebagai air minum.",
        "🌳Satu pohon dewasa dapat membantu menyerap karbon dioksida (CO₂) dan menghasilkan oksigen.",
        "🐢Hewan laut seperti penyu sering mengira kantong plastik adalah ubur-ubur sehingga dapat membahayakan mereka."
    ]
    return random.choice(fakta_list)

def get_tips():
    tips_list = [
        "🌱Bawa tumbler sendiri agar mengurangi penggunaan botol plastik sekali pakai.",
        "🛍️Gunakan tas belanja kain daripada kantong plastik saat berbelanja.",
        "🚲Jika jaraknya dekat, berjalan kaki atau bersepeda untuk membantu mengurangi polusi udara.",
        "♻️Pisahkan sampah organik dan anorganik agar lebih mudah didaur ulang.",
        "💡Matikan lampu dan alat elektronik saat tidak digunakan untuk menghemat energi."
    ]
    return random.choice(tips_list)

def get_recycle():
    recycle_list = [
        "♻️ Daur ulang botol plastik menjadi pot tanaman atau tempat pensil.",
        "📰 Gunakan kembali kertas yang masih kosong di salah satu sisinya untuk mencatat.",
        "🥫 Kaleng bekas dapat dijadikan tempat alat tulis atau pot kecil.",
        "🛍️ Gunakan kembali tas belanja kain agar mengurangi penggunaan kantong plastik.",
        "🍶 Botol kaca bekas dapat dimanfaatkan sebagai vas bunga atau wadah penyimpanan."
    ]
    return random.choice(recycle_list)

def get_laut():
    laut_list = [
        "🌊Sekitar 8 juta ton sampah plastik masuk ke laut setiap tahun.",
        "🐠Sampah plastik dapat melukai atau membunuh hewan laut seperti ikan, penyu, dan paus.",
        "🪸Terumbu karang merupakan rumah bagi ribuan spesies laut, tetapi dapat rusak akibat pencemaran dan perubahan iklim.",
        "🛢️Tumpahan minyak di laut dapat mencemari air dan membahayakan kehidupan hewan laut.",
        "💙Laut menghasilkan lebih dari 50% oksigen yang kita hirup, sehingga menjaga kebersihannya sangat penting."
    ]
    return random.choice(laut_list)
