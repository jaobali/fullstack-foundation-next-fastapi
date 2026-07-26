test("sdgfnsdofgiosfg", async () => {
  const response = await fetch("http://localhost:8000/database_status")

  if (!response.ok) {
    throw new Error("Erro ao consultar status do banco")
  }

  const data = await response.json()

  console.log(data)

  expect(data.status).toBe("ok")
  expect(data.database.connected).toBe(true)
})