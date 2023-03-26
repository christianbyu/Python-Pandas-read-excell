import pandas as pd
data = pd.read_excel(io='./data/Mahasiswa.csv' ,dtype={'No. NIM':int,'Nama':object,'Jurusan':object,'Kampus':object})
print(data)