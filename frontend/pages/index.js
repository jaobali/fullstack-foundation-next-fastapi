
export default function Home() {
  return (
    <main style={{
      fontFamily: "Arial",
      textAlign: "center",
      padding: "80px 20px"
    }}>
      <h1>Hub de Automações</h1>
      <p>Bem-vindo ao sistema!</p>

      <button style={{
        padding: "10px 20px",
        border: "none",
        borderRadius: "6px",
        backgroundColor: "#2563eb",
        color: "white",
        cursor: "pointer"
      }}>
        Acessar sistema
      </button>
    </main>
  );
}
