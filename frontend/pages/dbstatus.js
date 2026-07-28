export default async function DBStatusPage() {
  const response = await fetch("http://localhost:8000/database_status")

  if (!response.ok) {
    throw new Error("Erro ao consultar status do banco")
  }

  const data = await response.json()

  return <h1>Status do Banco de Dados: {data.status}</h1>
}