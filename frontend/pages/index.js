// function Home(){
//     return <h1>João é brabo de mais</h1>
// }

// export default Home;

import { useState } from "react";

export default function Home() {
  const [message, setMessage] = useState("");

  async function testarBackend() {
    const response = await fetch("/api/hello");
    const data = await response.json();

    setMessage(data.message);
  }

  return (
    <div>
      <button onClick={testarBackend}>
        Testar Backend
      </button>

      <p>{message}</p>
    </div>
  );
}