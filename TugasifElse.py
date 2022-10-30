# untuk mendapat nilai_rata_rataA  nilai_rata_ratarata rata mulai 90 ~ 100
# untuk mendapat nilai_rata_rataB  nilai_rata_ratarata rata mulai 80 ~ 89
# untuk mendapat nilai_rata_rataC  nilai_rata_ratarata rata mulai 70 ~ 79
# untuk mendapat nilai_rata_rataD  nilai_rata_ratarata rata mulai 60 ~ 69
# untuk mendapat nilai_rata_rataE  nilai_rata_ratarata rata kurang dari 60

# matematika
# english
# b indo
# pkn
# biologi
# fisika

# 1. buat variable mata pelajaran
matematika = int(input('Matematika : '))
english = int(input('English :'))
b_indonesia = int(input('Indonesia :'))

# 2.biar nilai rata rata (mat + indo)/5 
nilai_rata_rata = (matematika + english + b_indonesia) / 3
print(f'Nilai rata rata (nilai_rata_rata) ') 

if (nilai_rata_rata >= 90 and nilai_rata_rata <= 100):
    print(f'Nilai {nilai_rata_rata} mendapatkan A')
elif (nilai_rata_rata >= 80 and nilai_rata_rata < 90):
    print(f'Nilai {nilai_rata_rata} mendapatkan B')
elif (nilai_rata_rata >= 70 and nilai_rata_rata < 80):
    print(f'Nilai {nilai_rata_rata} mendapatkan C')
elif (nilai_rata_rata >= 60 and nilai_rata_rata < 70):
    print(f'Nilai {nilai_rata_rata} mendapatkan D')
elif (nilai_rata_rata < 60):
    print(f'Nilai {nilai_rata_rata} mendapatkan E')
else:
    print(f'Nilai {nilai_rata_rata} Tidak dalam Rentang')
    
# total = 5 + 6 + 2
# print(f'Total {total} ') 

# 3.nilai rata rata  di selection