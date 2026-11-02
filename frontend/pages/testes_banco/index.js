import { useState } from "react";

export default function Home() {
  const [message, setMessage] = useState("");

  async function testarBackend() {
    const response = await fetch("/api/hello");
    const data = await response.json();

    setMessage(data.message);
  }

  async function testarBackendretornoDB() {
    const response = await fetch("/api/database_status");
    const data = await response.json();

    setMessage(JSON.stringify(data, null, 2));
  }

  return (
    <div>
      <button onClick={testarBackend}>
        Testar Backend
      </button>

      <button onClick={testarBackendretornoDB}>
        Testar Backend com Retorno do Banco
      </button>

      <pre>{message}</pre>
    </div>
  );
}