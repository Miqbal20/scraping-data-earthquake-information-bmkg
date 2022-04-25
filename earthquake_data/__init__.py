import requests
from bs4 import BeautifulSoup


def get_data_eathquake():
    try:
        content = requests.get('https://www.bmkg.go.id/gempabumi-dirasakan.html')
    except Exception:
        return None
    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')
        table = soup.find('table', {'class': 'table table-hover table-striped'})
        table_body = table.find('tbody')
        rows = table_body.find_all('tr')

        for row in rows:
            cols = row.find_all('td')

            nomor = cols[0].text
            get_tanggal = cols[1].get_text(strip=True, separator=',')
            tanggal = get_tanggal.split(',')[0]
            waktu = get_tanggal.split(',')[1]
            ls = cols[2].text.split(' ')[0]
            bt = cols[2].text.split(' ')[2]
            magnitudo = cols[3].text
            kedalaman = cols[4].text
            get_keterangan = cols[5].get_text(strip=True, separator=',')
            keterangan = get_keterangan.split(',')[0]

            data = dict()
            data['no'] = nomor
            data['tanggal'] = tanggal
            data['waktu'] = waktu
            data['ls'] = ls
            data['bt'] = bt
            data['magnitudo'] = magnitudo
            data['kedalaman'] = kedalaman
            data['keterangan'] = keterangan

            print(f"No : {data['no']}")
            print(f"Tanggal : {data['tanggal']}")
            print(f"Waktu : {data['waktu']}")
            print(f"Lokasi : LS = {data['ls']} BT = {data['bt']}")
            print(f"Magnitudo : {data['magnitudo']}")
            print(f"Kedalaman : {data['kedalaman']}")
            print(f"Keterangan : {data['keterangan']}\n")


if __name__ == "__main__":
    get_data_eathquake()
