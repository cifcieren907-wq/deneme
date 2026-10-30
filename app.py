import streamlit as st

# Sayfa Yapılandırması
st.set_page_config(
    page_title="Gelişmiş Fortran Eğitimi", page_icon="💻", layout="centered"
)

st.title("💻 İleri Düzey Fortran Eğitim Platformu")
st.write(
    "Fortran'ın sayısal hesaplama, matris işlemleri, sayısal türev ve dizi"
    " yönetimini içeren "
    "kapsamlı eğitim modülüne hoş geldin! Aşağıdan incelemek istediğin konuyu"
    " seçebilirsin."
)

st.divider()

# Kullanıcıya Konu Seçimi Sunma
secim = st.radio(
    "**Hangi konuyu incelemek istiyorsun?**",
    [
        "1. Do Döngüsü (Do Loop Temelleri)",
        "2. Döngüler ile Matris Yazdırma ve İşlemleri",
        "3. İleri, Geri ve Ortalama Türev Hesabı",
        "4. Belirli Aralıkta Fonksiyon Değerlerini Hesaplama",
        "5. Parametre (`parameter`) ve Boyut (`dimension`) Mantığı",
    ],
)

st.divider()

# Seçilen Konuya Göre Detaylı İçerik Gösterme
if "Do Döngüsü" in secim:
  st.subheader(" 1. Do Döngüsü (Do Loop Temelleri)")
  st.write(
      "Fortran'da tekrarlı işlemleri gerçekleştirmek için `do` döngüsü"
      " kullanılır. Standart döngünün yanı sıra **adım (step)** miktarı"
      " belirleyebilir, döngüleri **iç içe (nested)** yazabilir veya"
      " koşullu durumlarda döngüyü erkenden sonlandırabilirsiniz."
  )

  st.markdown("#### Örnek 1: Klasik Artış ve Adımlı Döngü")
  st.code(
      """
integer :: i, j

! 1'den 10'a kadar 1'er artan döngü
print *, "--- 1'er Artış ---"
do i = 1, 10
    print *, "Sayı: ", i
end do

! 2'den 10'a kadar 2'şer artan döngü (Çift sayılar)
print *, "--- 2'şer Artış ---"
do j = 2, 10, 2
    print *, "Çift sayı: ", j
end do
    """,
      language="fortran",
  )

  st.markdown("#### Örnek 2: Geriye Doğru (Azalan) Döngü")
  st.code(
      """
integer :: k
! 10'dan 1'e doğru geriye sayım
do k = 10, 1, -1
    print *, "Geri sayım: ", k
end do
print *, "Kalkış! "
    """,
      language="fortran",
  )

elif "Matris" in secim:
  st.subheader(" 2. Döngüler ile Matris Yazdırma ve İşlemleri")
  st.write(
      "Matrisler, çok boyutlu verileri saklamak için kullanılan temel yapı"
      " taşlarıdır. Fortran'da 2 boyutlu matrisleri işlemek için **iç içe iki"
      " `do` döngüsü** (`nested loops`) kullanılır: dıştaki döngü satırları"
      " (`i`), içteki döngü sütunları (`j`) tarar."
  )

  st.code(
      """
integer, parameter :: satir = 3, sutun = 3
integer :: i, j
real, dimension(satir, sutun) :: matris

! 1. Adım: Matrise değer atama (Örn: Çarpım tablosu mantığı)
do i = 1, satir
    do j = 1, sutun
        matris(i, j) = real(i * j)
    end do
end do

! 2. Adım: Matrisi ekrana düzenli bir şekilde yazdırma
print *, "--- 3x3 Matris Çıktısı ---"
do i = 1, satir
    ! Her satırı yan yana yazdırmak için modern Fortran formatı
    print '(3F6.1)', (matris(i, j), j = 1, sutun)
end do
    """,
      language="fortran",
  )
  st.info(
      "💡 **İpucu:** `(3F6.1)` kalıbı, her satırda 3 adet ondalıklı sayının 6"
      " karakter genişlikte ve virgülden sonra 1 basamakla yazdırılmasını"
      " sağlar."
  )

elif "Türev" in secim:
  st.subheader(" 3. İleri, Geri ve Ortalama Türev Hesabı")
  st.write(
      "Sayısal analizde bilgisayarlar analitik türev (formül türevi) yerine"
      " **Sonlu Farklar (Finite Differences)** yöntemini kullanır. $h$ adımı"
      " ne kadar küçük olursa, sonuç gerçek türeve o kadar yaklaşır."
  )

  st.markdown(
      "- **İleri Türev (Forward):** $\\frac{f(x+h) - f(x)}{h}$"
      "<br>- **Geri Türev (Backward):** $\\frac{f(x) - f(x-h)}{h}$"
      "<br>- **Ortalama/Merkezi Türev (Central):** $\\frac{f(x+h) - f(x-h)}{2h}$"
      " *(En hassas sonuçtur)*",
      unsafe_allow_html=True,
  )

  st.code(
      """
! f(x) = x^2 fonksiyonunun x = 3.0 noktasındaki türevi (Analitik sonucu: 6.0)
real :: x, h
real :: ileri_turev, geri_turev, merkez_turev

x = 3.0
h = 0.0001 ! Çok küçük bir adım boyutu

! Formüllerin Fortran karşılığı:
ileri_turev  = (((x + h)**2) - (x**2)) / h
geri_turev   = (x**2 - ((x - h)**2)) / h
merkez_turev = (((x + h)**2) - ((x - h)**2)) / (2.0 * h)

print *, "Gerçek Değer (Analitik): 6.0"
print *, "İleri Türev Sonucu    : ", ileri_turev
print *, "Geri Türev Sonucu     : ", geri_turev
print *, "Merkezi Türev Sonucu  : ", merkez_turev
    """,
      language="fortran",
  )

elif "Fonksiyon" in secim:
  st.subheader(" 4. Belirli Aralıkta Fonksiyon Değerlerini Hesaplama")
  st.write(
      "Bir mühendislik probleminde, belirli bir sınır aralığında ($x_{min}$"
      " ile $x_{max}$ arası) bir fonksiyonun davranışını gözlemlemek için"
      " döngü kullanılır. Adım sayısı ($n$) belirlenerek her adımda $x$"
      " değeri güncellenir ve $f(x)$ hesaplanır."
  )

  st.code(
      """
! f(x) = sin(x) fonksiyonunun [0, 3.14] aralığında değerler tablosu
real :: baslangic, bitis, adim_boyutu, x, fx
integer :: i, n

baslangic = 0.0
bitis = 3.14159
n = 5 ! Aralık kaç parçaya bölünecek?
adim_boyutu = (bitis - baslangic) / real(n)

print *, "    x    |    f(x) = sin(x)"
print *, "--------------------------"

do i = 0, n
    x = baslangic + real(i) * adim_boyutu
    fx = sin(x)
    print '(F6.2, " | ", F10.4)', x, fx
end do
    """,
      language="fortran",
  )

elif "Parametre" in secim:
  st.subheader(" 5. Parametre (`parameter`) ve Boyut (`dimension`) Mantığı")
  st.write(
      "* **`parameter`**: Kodun hiçbir yerinde **değiştirilemeyen sabitleri**"
      " tanımlar (Örn: Pi sayısı, ışık hızı veya maksimum dizi boyutu)."
      " Program güvenliği sağlar.\n* **`dimension`**: Bellekte oluşturulacak"
      " dizilerin veya matrislerin **kaç elemanlı olacağını** derleyiciye"
      " bildirir."
  )

  st.code(
      """
! Sabit tanımlamaları (parameter)
real, parameter :: pi = 3.1415926535
integer, parameter :: MAX_OGRENCI = 50

! Boyut tanımlamaları (dimension)
real, dimension(MAX_OGRENCI) :: notlar        ! 1 boyutlu dizi (Vektör)
real, dimension(10, 10) :: sinif_matrisi      ! 2 boyutlu matris

print *, "Matematiksel Pi Sabiti:", pi
print *, "Maksimum Öğrenci Kapasitesi:", MAX_OGRENCI
print *, "Oluşturulan dizinin boyutu:", size(notlar)
    """,
      language="fortran",
  )

st.success(
   
)
