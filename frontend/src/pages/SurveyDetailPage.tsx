const points = [
  "Kelengkapan Perizinan",
  "Pengelolaan Sampah Padat",
  "Pengelolaan Limbah Cair",
  "Pengelolaan Limbah B3",
  "Pengelolaan RTH",
  "Pengelolaan Resapan Air Hujan",
  "Pengelolaan Bahaya Kebakaran",
];

export default function SurveyDetailPage() {
  return (
    <section>
      <h2>Detail Survei</h2>
      <p>Halaman ini disiapkan untuk menampilkan identitas survei, anggota tim, dan progres form per poin.</p>
      <ul>
        {points.map((point) => (
          <li>{point}</li>
        ))}
      </ul>
    </section>
  );
}
