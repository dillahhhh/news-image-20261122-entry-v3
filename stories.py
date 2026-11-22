# Data — 34 berita dunia, 22 November 2026. Satu kartu = satu berita.
# Ditulis segar dari riset berita hari ini; judul dan isi diparafrase sendiri.
# Cerita 0 = utama, 1-3 = sekunder, 4-33 = grid.

STORIES = [
    {
        "tag": "IKLIM",
        "title": "COP31 Bubar Tanpa Kesepakatan",
        "text": "Konferensi iklim PBB di Antalya, Turki, berakhir tanpa kesepakatan apa pun setelah lebih dari dua pekan perundingan. Uni Eropa dan sejumlah negara menolak draf akhir karena tidak menyebut bahan bakar fosil sama sekali. Ini kegagalan besar pertama sejak Kopenhagen 2009 dan KTT iklim terpanjang dalam sejarah.",
    },
    {
        "tag": "F1",
        "title": "Verstappen Menang Balapan Gila di Las Vegas",
        "text": "Max Verstappen memenangi Grand Prix Las Vegas setelah balapan 50 putaran yang penuh drama hingga akhir. Lando Norris finis kedua dan Oscar Piastri ketiga, sementara Mercedes tersingkir dari podium di putaran-putaran penutup.",
    },
    {
        "tag": "SEPAK BOLA",
        "title": "Kansas City Current Juara NWSL Pertama Kali",
        "text": "Kansas City Current merebut gelar juara liga sepak bola wanita Amerika untuk pertama kalinya dengan menang 2-1 atas Washington Spirit di Audi Field. Gol pembuka dicetak Vanessa DiBernardo langsung dari tendangan sudut, sebelum Trinity Rodman memperkecil skor.",
    },
    {
        "tag": "KONFLIK",
        "title": "Iran Serang Situs Industri di Bahrain",
        "text": "Bahrain menyebut proyektil Iran menghantam sebuah kawasan industri di Sitra dan melukai dua orang. Arab Saudi, Kuwait, dan Qatar mengecam serangan itu. Iran mengklaim telah menghancurkan dua radar Patriot Amerika, sementara tiga kapal tanker juga dilaporkan diserang di dekat Selat Hormuz.",
    },
    {
        "tag": "GEORGIA",
        "title": "Georgia Berkabung Nasional untuk Korban Ledakan",
        "text": "Georgia menetapkan 22 November sebagai hari berkabung nasional untuk enam korban ledakan gas di blok apartemen Kvemo Ponichala, Tbilisi, termasuk dua anak. Bendera negara diturunkan setengah tiang di seluruh negeri dan ibadah peringatan digelar untuk para korban.",
    },
    {
        "tag": "KEADILAN",
        "title": "Gembong Kartel El Chapo Isidro Ditangkap",
        "text": "Pasukan khusus Meksiko menangkap bos kartel Fausto Isidro Meza Flores di Sinaloa. Operasi itu menewaskan 11 orang, termasuk empat tentara, dalam baku tembak yang sengit.",
    },
    {
        "tag": "UKRAINA",
        "title": "Rudal Rusia Hantam Kampung Halaman Zelenskyy",
        "text": "Serangan rudal Rusia ke Kryvyi Rih, kota kelahiran Presiden Volodymyr Zelenskyy, menewaskan seorang anak tujuh tahun dan seorang perempuan 20 tahun serta melukai sekitar 60 orang.",
    },
    {
        "tag": "UKRAINA",
        "title": "Drone Rusia Hantam Apartemen Dekat Kyiv",
        "text": "Sebuah drone Rusia menghantam blok apartemen lima lantai di Dymer, utara Kyiv, hingga sebagian bangunan runtuh. Sedikitnya tiga orang tewas dan 14 lainnya masih hilang di bawah reruntuhan.",
    },
    {
        "tag": "EKONOMI",
        "title": "Saham AS Masuk Koreksi, Jual Beli AI Anjlok",
        "text": "Bursa Amerika jatuh ke wilayah koreksi setelah indeks S&P 500 merosot 3,7 persen dan Nasdaq anjlok tajam. Gelombang jual saham teknologi kecerdasan buatan menyebar ke Jepang dan Korea Selatan.",
    },
    {
        "tag": "BENCANA",
        "title": "Korban Badai Brazil Naik, Pemerintah Tetapkan Darurat",
        "text": "Jumlah korban badai di Tupancireta, Brasil selatan, naik menjadi lima tewas dan 265 luka-luka. Pemerintah federal resmi menetapkan status bencana di kota itu setelah badai merobohkan atap ribuan rumah dan memutus listrik serta air bersih.",
    },
    {
        "tag": "GAZA",
        "title": "Hamas Minta Pertemuan Darurat Mediator Usai Serangan Gaza",
        "text": "Hamas meminta pertemuan darurat para mediator gencatan senjata setelah serangan Israel menewaskan tiga pekerja dapur umum yang sedang mengantar makanan ke warga terlantar di Kota Gaza. Militer Israel menyebut kendaraan itu dipakai anggota Jihad Islam, sementara lembaga amal membantah truk itu miliknya.",
    },
    {
        "tag": "INDONESIA",
        "title": "Kebakaran Pabrik Permen di Cikande, 3 Tewas",
        "text": "Kebakaran besar di pabrik permen PT Fonusa Agung Mulia di Cikande, Banten, menewaskan tiga pekerja dan membuat 36 lainnya hilang. Sekitar 300 pekerja berada di dalam gedung saat api muncul dari unit pendingin di lantai tiga.",
    },
    {
        "tag": "TIMUR TENGAH",
        "title": "Pemukim Bakar Kendaraan di Tepi Barat",
        "text": "Pemukim Israel membakar 12 kendaraan milik warga Palestina dan mencoret grafiti di empat desa dekat Ramallah. Israel membuka penyelidikan, sementara pemimpin oposisi menyebut serangan itu sebagai terorisme.",
    },
    {
        "tag": "ANTARIKSA",
        "title": "BepiColombo Akhirnya Mengorbit Merkurius",
        "text": "Wahana gabungan Eropa-Jepang BepiColombo berhasil masuk orbit Merkurius setelah perjalanan delapan tahun melintasi tata surya bagian dalam. Dua wahana pengorbitnya akan berpisah pada 9-10 Desember untuk mempelajari planet terkecil itu.",
    },
    {
        "tag": "EROPA",
        "title": "Polandia: Rusia Dua Kali Incar Rapper Ukraina-Amerika",
        "text": "Polandia mengungkap Rusia diduga dua kali mencoba membunuh rapper Ukraina-Amerika Kyivstoner, sekali di Polandia pada Agustus dan sekali di Denmark. Denmark mengusir atase militer Rusia, dan Uni Eropa didesak memperketat perjalanan warga Rusia.",
    },
    {
        "tag": "SEPAK BOLA",
        "title": "Liverpool Bantai Man United 4-0 di Anfield",
        "text": "Liverpool menghancurkan Manchester United 4-0 di Anfield dalam laga pertama Mauricio Pochettino sebagai pelatih United. United bermain dengan sepuluh orang dan kini sembilan laga tanpa kemenangan di liga.",
    },
    {
        "tag": "SEPAK BOLA",
        "title": "Arsenal Imbang 2-2 di Newcastle, Tetap Puncak",
        "text": "Arsenal bermain imbang 2-2 melawan Newcastle United di St James Park namun tetap memimpin klasemen Liga Inggris dengan 28 poin, unggul enam angka dari Brighton.",
    },
    {
        "tag": "SEPAK BOLA",
        "title": "Leeds Kejutkan Chelsea 4-1 di Stamford Bridge",
        "text": "Leeds United bangkit dari ketertinggalan untuk menang 4-1 atas Chelsea di Stamford Bridge. Itu kemenangan pertama Leeds di markas Chelsea sejak 1999.",
    },
    {
        "tag": "SEPAK BOLA",
        "title": "Man City Imbang 1-1 Lawan Fulham",
        "text": "Manchester City mengakhiri tiga kekalahan beruntun di liga dengan hasil imbang 1-1 melawan Fulham di Etihad.",
    },
    {
        "tag": "TEKNOLOGI",
        "title": "Amazon Dekati Kesepakatan 7,5 Miliar Dolar Beli Decart",
        "text": "Amazon berada di tahap akhir pembicaraan untuk membeli perusahaan rintisan AI asal Israel, Decart, senilai sekitar 7,5 miliar dolar. Kesepakatan bisa diumumkan pekan depan, dan akan menjadi salah satu akuisisi termahal untuk perusahaan AI muda.",
    },
    {
        "tag": "INDIA",
        "title": "Minuman Oplosan di Manipur Tewaskan Belasan Orang",
        "text": "Sedikitnya 16 orang tewas dan sekitar 600 lainnya dirawat di Manipur, India, setelah menenggak minuman keras oplosan yang diduga mengandung metanol. Pemerintah negara bagian membentuk tim penyelidikan, sementara penyebab pastinya masih menunggu hasil laboratorium.",
    },
    {
        "tag": "TEKNOLOGI",
        "title": "Celah VMware Dieksploitasi, Batas Tambal 23 Nov",
        "text": "Badan keamanan siber Amerika mengonfirmasi celah kritis pada VMware vCenter sedang dieksploitasi dan menetapkan tenggat 23 November bagi instansi federal untuk menambalnya.",
    },
    {
        "tag": "CUACA",
        "title": "California Siaga Hadapi Pasang Tertinggi",
        "text": "Prakirawan memperingatkan pasang air laut yang bisa memecahkan rekor di pesisir California pekan ini. Wali Kota San Francisco mengimbau warga menghindari perjalanan yang tidak perlu.",
    },
    {
        "tag": "HIBURAN",
        "title": "GTA 6 Pecahkan Rekor Peluncuran 3,79 Miliar Dolar",
        "text": "Grand Theft Auto VI membukukan sekitar 3,79 miliar dolar pada hari peluncurannya, rekor baru untuk debut sebuah gim. Angka itu melampaui semua peluncuran gim sebelumnya dan menegaskan besarnya antusiasme pemain di seluruh dunia.",
    },
    {
        "tag": "ISRAEL",
        "title": "Eisenkot Ajak Likud Bicara Koalisi Pemerintahan",
        "text": "Pemimpin oposisi Israel Gadi Eisenkot mengundang partai Likud pimpinan Netanyahu ke pembicaraan koalisi, membuka kemungkinan susunan pemerintahan baru. Langkah itu muncul di tengah perdebatan sengit soal serangan pemukim di Tepi Barat.",
    },
    {
        "tag": "BUDAYA",
        "title": "Kastil Shuri Okinawa Kembali Berdiri",
        "text": "Okinawa merayakan pemugaran aula utama Kastil Shuri, tujuh tahun setelah kebakaran besar menghancurkan bangunan bersejarah itu.",
    },
    {
        "tag": "SUDAN",
        "title": "Drone Hantam Khartoum, Gedung PBB Rusak",
        "text": "Serangan drone di Khartoum merusak sebuah gedung Perserikatan Bangsa-Bangsa di tengah konflik Sudan yang terus berkecamuk.",
    },
    {
        "tag": "PBB",
        "title": "PBB Perpanjang Pembahasan Aturan Robot Pembunuh",
        "text": "Perundingan senjata PBB memperpanjang pekerjaan penyusunan aturan soal robot pembunuh hingga 2028. Negara-negara belum sepakat soal batasan senjata otonom yang bisa memilih target sendiri tanpa kendali manusia.",
    },
    {
        "tag": "SPANYOL",
        "title": "Spanyol Hadapi Ketidakpastian Jelang Pemilu",
        "text": "Spanyol menghadapi ketidakpastian politik menjelang pemilihan umum 29 November, dengan peta koalisi yang masih jauh dari kata pasti.",
    },
    {
        "tag": "NFL",
        "title": "Allen dan Cook Cetak Rekor di NFL",
        "text": "Bintang Buffalo Bills Josh Allen dan James Cook mengukir rekor langka dalam sejarah NFL saat timnya menghadapi Miami Dolphins pada pekan ke-11.",
    },
    {
        "tag": "UKRAINA",
        "title": "Kapal Kargo Rusia Terbakar di Teluk Finlandia",
        "text": "Kapal kargo Rusia Sparta II yang terkena sanksi masih terbakar di Teluk Finlandia sehari setelah diduga diserang drone Ukraina.",
    },
    {
        "tag": "ANTARIKSA",
        "title": "Bumi Punya Bulan Mini Baru, 2026 QQ8",
        "text": "Para astronom mengonfirmasi Bumi kedatangan bulan mini baru, asteroid 2026 QQ8, yang untuk sementara terperangkap oleh gravitasi planet kita.",
    },
    {
        "tag": "ASIA",
        "title": "Hubungan China-Jepang Memburuk Soal Taiwan",
        "text": "Hubungan China dan Jepang memburuk setelah perselisihan soal Taiwan dan mineral kritis. Kedua negara saling melontarkan pernyataan keras, menambah ketegangan di kawasan Asia Timur.",
    },
    {
        "tag": "OLAHRAGA",
        "title": "Maraton Philadelphia Pecahkan Rekor",
        "text": "Victor Shitsama dan Dayna Pidhoresky memenangi Maraton Philadelphia dengan catatan waktu yang memecahkan rekor lomba.",
    },
]

HIGHLIGHT = "COP31 BUBAR TANPA KESEPAKATAN  •  VERSTAPPEN MENANG DI LAS VEGAS  •  KC CURRENT JUARA NWSL  •  IRAN SERANG BAHRAIN  •  SAHAM AS MASUK KOREKSI"
