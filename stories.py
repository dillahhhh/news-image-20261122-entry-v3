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
        "text": "Max Verstappen memenangi Grand Prix Las Vegas setelah balapan 50 putaran yang kacau dengan 352 kali salip-menyalip dan 35 kali pergantian pemimpin. Lando Norris finis kedua dan Oscar Piastri ketiga, setelah drama di putaran akhir menjatuhkan Mercedes dari podium.",
    },
    {
        "tag": "SEPAK BOLA",
        "title": "Kansas City Current Juara NWSL Pertama Kali",
        "text": "Kansas City Current merebut gelar juara liga sepak bola wanita Amerika untuk pertama kalinya dengan menang 2-1 atas Washington Spirit di Audi Field. Gol pembuka dicetak Vanessa DiBernardo langsung dari tendangan sudut, lalu Debinha menggandakan keunggulan sebelum Trinity Rodman memperkecil skor.",
    },
    {
        "tag": "KONFLIK",
        "title": "Iran Serang Situs Industri di Bahrain",
        "text": "Bahrain menyebut proyektil Iran menghantam sebuah kawasan industri di Sitra dan melukai dua orang. Arab Saudi, Kuwait, dan Qatar mengecam serangan itu. Iran mengklaim telah menghancurkan dua radar Patriot Amerika, sementara tiga kapal tanker juga dilaporkan diserang di dekat Selat Hormuz.",
    },
    {
        "tag": "DIPLOMASI",
        "title": "Trump, Xi, dan Putin Bertemu di Shenzhen",
        "text": "Presiden Amerika, China, dan Rusia menggelar pertemuan tiga pihak pertama dalam sejarah di Shenzhen. Ketiganya mengeluarkan pernyataan bersama soal risiko nuklir, namun tanpa batas senjata baru dan tanpa terobosan soal Ukraina.",
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
        "text": "Bursa Amerika jatuh ke wilayah koreksi setelah indeks S&P 500 merosot 3,7 persen dan Nasdaq 5,3 persen dalam sehari. Gelombang jual saham teknologi kecerdasan buatan menyebar ke Jepang dan Korea Selatan.",
    },
    {
        "tag": "HUKUM",
        "title": "Mahkamah Dunia: Myanmar Lakukan Genosida Rohingya",
        "text": "Mahkamah Internasional memutuskan Myanmar melakukan genosida terhadap etnis Rohingya pada 2017. Ini pertama kalinya pengadilan dunia menyatakan sebuah negara bertanggung jawab atas genosida.",
    },
    {
        "tag": "PERDAGANGAN",
        "title": "UE dan Indonesia Teken Kesepakatan Dagang",
        "text": "Uni Eropa dan Indonesia menandatangani perjanjian perdagangan setelah hampir sepuluh tahun berunding. Kesepakatan itu memangkas tarif hingga 98,5 persen barang dan membuka jalan bagi kerja sama ekonomi yang lebih luas.",
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
        "tag": "KESEHATAN",
        "title": "Terapi CRISPR Sekali Suntik Turunkan Kolesterol 52%",
        "text": "Terapi gen sekali pakai berbasis CRISPR berhasil memangkas kolesterol jahat hingga 52 persen dalam uji klinis. Temuan ini membuka jalan bagi pengobatan baru penyakit jantung tanpa obat harian.",
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
        "text": "Manchester City mengakhiri tiga kekalahan beruntun di liga dengan hasil imbang 1-1 melawan Fulham di Etihad. Gol Fulham dicetak Rodrigo Muniz sebelum City menyamakan kedudukan.",
    },
    {
        "tag": "NATO",
        "title": "NATO Janji Bela Polandia Usai Rudal Rusia",
        "text": "Sekretaris Jenderal NATO Mark Rutte berjanji membela Polandia setelah rudal dan drone Rusia memasuki wilayah udara Polandia. NATO menyebut pelanggaran itu serius dan akan membahasnya dalam pertemuan Dewan Atlantik Utara.",
    },
    {
        "tag": "AMERIKA",
        "title": "FBI Selidiki Dugaan Peretasan Basis Data Kriminal",
        "text": "FBI menyelidiki dugaan pembobolan Pusat Informasi Kejahatan Nasional, basis data yang dipakai polisi Amerika untuk memeriksa surat perintah, buronan, dan riwayat kriminal.",
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
        "tag": "OBITUARI",
        "title": "Paolo Bulgari Meninggal di Usia 89 Tahun",
        "text": "Paolo Bulgari, perajin perhiasan Italia yang mengubah bisnis keluarga menjadi merek mewah dunia, meninggal dunia pada usia 89 tahun.",
    },
    {
        "tag": "BENCANA",
        "title": "Kapal Tenggelam di Nigeria, 24 Tewas",
        "text": "Sedikitnya 24 orang tewas ketika sebuah perahu terbalik di Nigeria saat mengangkut rombongan menuju sebuah pemakaman.",
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
        "tag": "EROPA",
        "title": "UE dan Inggris Sepakati Reset Pasca-Brexit",
        "text": "Uni Eropa dan Inggris menyepakati penataan ulang hubungan pasca-Brexit dalam sebuah pertemuan puncak, menandai babak baru kerja sama kedua pihak.",
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
        "tag": "TIMUR TENGAH",
        "title": "Trump: Iran Ingin Kesepakatan; Houthi Serang Saudi",
        "text": "Presiden Trump mengatakan Iran menginginkan kesepakatan, sementara pemberontak Houthi Yaman dan Arab Saudi saling bertukar tembakan di tengah ketegangan kawasan.",
    },
    {
        "tag": "OLAHRAGA",
        "title": "Maraton Philadelphia Pecahkan Rekor",
        "text": "Victor Shitsama dan Dayna Pidhoresky memenangi Maraton Philadelphia dengan catatan waktu yang memecahkan rekor lomba.",
    },
]

HIGHLIGHT = "COP31 BUBAR TANPA KESEPAKATAN  •  VERSTAPPEN MENANG DI LAS VEGAS  •  KC CURRENT JUARA NWSL  •  IRAN SERANG BAHRAIN  •  SAHAM AS MASUK KOREKSI"
