total = int(input('Total Uang = Rp. '))
pecah = total//100000
print('Jumlah Uang Rp100.000 = ',pecah)
total = total%100000
pecah = total//50000
print('Jumlah Uang Rp50.000 = ',pecah)
total = total%50000
pecah = total//20000
print('Jumlah Uang Rp20.000 = ',pecah)
total = total%20000
pecah = total//10000
print('Jumlah Uang Rp10.000 = ',pecah)
total = total%10000
pecah = total//5000
print('Jumlah Uang Rp5.000 = ', pecah)
total = total%5000
pecah = total//2000
print('Jumlah Uang Rp2.000 = ',pecah)
total = total%2000
pecah = total//1000
print('Jumlah Uang Rp.1000 = ', pecah)