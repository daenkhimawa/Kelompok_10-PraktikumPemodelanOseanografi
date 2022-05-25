Panduan Penggunaan Script

Untuk menggunakan script ini diperlukan library python berupa numpy untuk melakukan perhitungan dan matplotlib. Selanjutnya diperlukan data nilai kedalaman, temperatur, dan salinitas dengan format (".txt"). Data tersebut dimasukan dalam script pada bagian:
f = open (path_data)
Kemudian terdapat label temperatur, kedalaman, dan salinitas yang dapat diubah nama labelnya apabila diinginkan.
Pada bagian paling akhir dari script terlihat bahwa script ini akan disimpan di enviroment python di komputer masing-masing dengan nama "Tugas Pendahuluan.jpg" dengan dpi sebesar 300.
Nama dan dpi dapat diubah apabila diinginkan.

---------------------------------------------------------------------------

Persamaan Adveksi-Difusi atau yang biasa disebut dengan persamaan transport adalah persamaan matematis yang didesain untuk mempelajari fenomena transpor polutan. Persamaan Adveksi-Difusi merupakan salah satu persamaan differensial yang merepresentasikan sirkulasi aliran air di estuari dengan variabel C (Konsentrasi garam) sebagai fungsi ruang dan waktu. Dalam pemodelan matematika sering sekali kita mendapati persamaan-persamaan differensial yang rumit untuk diselesaikan secara analitis. Tetapi dalam menyelesaikan persamaan persamaan differensial ini tidak hanya dilakukan secara analitis, terdapat juga penyelesaian secara numerik. Metode numerik adalah teknik dimana permasalahan matematika diformulasikan sehingga dapat diselesaikan dengan operasi aritmatika dan logika. Perkembangan komputer dengan waktu komputasi yang semakin cepat, membuat pemodelan matematika semakin banyak diminati, dengan penerapan metode-metode numerik yang mempermudah dalam menyelesaikan persamaan-persamaan matematis pada model matematika yang telah dibuat. 

Persamaan Adveksi 1D :
![image](https://user-images.githubusercontent.com/105977853/169846115-f5ebf363-8827-4260-b5f6-b25377d75351.png)
Keterangan :
F = konsentrasi suatu zat terlarut
t = waktu 
U = kecepatan 
X = arah sumbu horizontal 

Metode Pendekatan dalam Pemodelan Numerik 
Secara umum, terdapat 2 pendekatan, yaitu eksplisit dan implisit. Perbedaan dari eksplisit dan implisit yaitu :
Eksplisit :
1.	Terdapar stabilitas hitungan
2.	Penyelesaian lebih mudah
3.	Simulasi lebih lama 
Implisit :
1.	Tidak terdapat hitungan
2.	Penyelesaian lebih rumit
3.	Simulasi lebih cepat  

Terdapat beberapa metode analisis numerik untuk menyelesaikan persmaan differensial, yaitu FTCS, Leapfrog (CTCS), dan Upstream. 

FTCS (Forward in Time Central in Space)
Metode FTCS merupakan gabungan dari pendekatan beda hingga yakni turunan pertama terhadap waktu dengan beda maju dan turunan kedua terhadap ruang dengan beda tengah sehingga Solusi FTCS termasuk ke dalam solusi solusi stabil bersyarat dengan syarat kestabilan.
Rumus :
![image](https://user-images.githubusercontent.com/105977853/169846421-d64276a3-7374-4251-ad5c-fa170cabaa3b.png)
![image](https://user-images.githubusercontent.com/105977853/169846485-49ef26fa-39cf-4afe-8a2a-fe022f1c19c2.png)

Leapfrog 
Metode beda hingga ini merupakan perluasan dari metode beda tengah ( Central Difference ) terhadap ruang dan waktu. Menurut Røed (2017), skema Leapfrog didapatkan dari turunan dari deret taylor, ini adalah skema yang konsisten. Leapfrog ini akan konsisten apabila nilai dari C≤1. Dengan nilai C adalah sebagai berikut :
![image](https://user-images.githubusercontent.com/105977853/169846585-94f1e6f8-eccc-491d-b6ea-70e723c0234d.png)
![image](https://user-images.githubusercontent.com/105977853/169846622-b053e8e1-fba4-40b1-9594-9ead61cb3b84.png)

Upstream 
Upstream ini merupakan skema yang digunakan untuk melengkapi ketidaksempurnaan dari metode Leapfrog. Karena, nilai konsentrasi dalam computer manjadi negatif, walaupun konsentrasinya positif. Untuk itu metode Upstream ini dibuat untuk model positif dari konsentrasi dialam yang merujuk ke lautan. Metode ini menggunakan pendekatan beda maju untuk turunan waktu, sedangkan untuk turunan terhadap ruang dilakukan dengan melihat arah kecepatan u. jika u > 0 maka turunan terhadap ruang menggunakan pendekatan beda mundur. Sebaliknya jika u < 0 maka digunakan pendekatan beda maju.
Stabilitas sama dengan skema Leapfrog
![image](https://user-images.githubusercontent.com/105977853/169846759-25aa51fa-d1e5-45b1-b739-19d1de7c6ba2.png)

Diskritisasi 
Proses Transformasi variabel numerik menjadi selang nilai atau diskrit
*Selang nilai dapat berupa beda maju, mundur, ataupun tengah(center) pada variabel waktu(time) dan tempat(space)
1.	FTCS (Forward Time Center Space)
2.	Leapfrog (Center Time Center Space)
3.	Upstream(Forward Time, bisa forward space atau back space. Tergantung nilai kecepatan(u))
![image](https://user-images.githubusercontent.com/105977853/169846899-3980c434-bc6c-450f-b2ea-bfdf3b3db775.png)
jika u > 0 maka turunan terhadap ruang menggunakan pendekatan beda mundur. Sebaliknya jika u < 0 maka digunakan pendekatan beda maju.
