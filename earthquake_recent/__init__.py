import requests
from bs4 import BeautifulSoup


def extraction_data():
    try:
        content = requests.get('https://www.bmkg.go.id/')
    except Exception:
        return None
    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')
        get_data_gempa = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        ul = get_data_gempa.find_all('ul')

        for res in ul:
            li = res.find_all('li')
            tanggal = li[0].text.split(', ')[0]
            waktu = li[0].text.split(', ')[1]
            magnitudo = li[1].text
            kedalaman = li[2].text
            ls = li[3].text.split(' - ')[0]
            bt = li[3].text.split(' - ')[1]
            pusat = li[4].text
            keterangan = li[5].text

            data = dict()
            data['tanggal'] = tanggal
            data['waktu'] = waktu
            data['magnitudo'] = magnitudo
            data['kedalaman'] = kedalaman
            data['lokasi'] = {"ls": ls, "bt": bt}
            data['pusat'] = pusat
            data['keterangan'] = keterangan
            return data
    else:
        return None


def show_data(result):
    if result is None:
        print("Tidak ada data gempa terkini")
        return

    print(f"\nTanggal : {result['tanggal']}")
    print(f"Waktu : {result['waktu']}")
    print(f"Magnitudo : {result['magnitudo']}")
    print(f"Kedalaman : {result['kedalaman']}")
    print(f"Lokasi : LS = {result['lokasi']['ls']} BT = {result['lokasi']['bt']}")
    print(f"Pusat Gempa : {result['pusat']}")
    print(f"Keterangan : {result['keterangan']}")


if __name__ == "__main__":
    data = extraction_data()
    show_data(data)
