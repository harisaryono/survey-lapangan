export default function DashboardPage() {
  const cards = [
    { title: "Survei Aktif", value: "0" },
    { title: "Menunggu Verifikasi", value: "0" },
    { title: "Perlu Revisi", value: "0" },
    { title: "Draft Berita Acara", value: "0" },
  ];

  return (
    <section>
      <h2>Dashboard Ketua Tim</h2>
      <div style={{ display: "grid", "grid-template-columns": "repeat(2, minmax(0, 1fr))", gap: "12px" }}>
        {cards.map((card) => (
          <div style={{ border: "1px solid #ddd", padding: "16px", "border-radius": "12px" }}>
            <div style={{ "font-size": "14px" }}>{card.title}</div>
            <div style={{ "font-size": "28px", "font-weight": 700 }}>{card.value}</div>
          </div>
        ))}
      </div>
    </section>
  );
}
