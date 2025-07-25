'use client';
import { useEffect, useState } from 'react';

interface Stock {
  symbol: string;
  name: string;
}

export default function HomePage() {
  const [stocks, setStocks] = useState<Stock[]>([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    async function fetchStocks() {
      setLoading(true);
      const url = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';
      const res = await fetch(`${url}/stocks?term=short&strategy=qualitative`);
      const data = await res.json();
      setStocks(data.data);
      setLoading(false);
    }
    fetchStocks();
  }, []);

  return (
    <main>
      <h1>Stock Strategies</h1>
      {loading ? (
        <p>Loading...</p>
      ) : (
        <ul>
          {stocks.map((s) => (
            <li key={s.symbol}>{s.symbol} - {s.name}</li>
          ))}
        </ul>
      )}
    </main>
  );
}
