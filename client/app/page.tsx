'use client';
import { useEffect, useState } from 'react';

interface Stock {
  symbol: string;
  name: string;
}

const strategies = ['qualitative', 'quantitative', 'momentum'];

export default function HomePage() {
  const [stocks, setStocks] = useState<Stock[]>([]);
  const [loading, setLoading] = useState(false);
  const [strategy, setStrategy] = useState(strategies[0]);

  useEffect(() => {
    async function fetchStocks() {
      setLoading(true);
      const url = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';
      const res = await fetch(`${url}/stocks?term=short&strategy=${strategy}`);
      const data = await res.json();
      setStocks(data.data);
      setLoading(false);
    }
    fetchStocks();
  }, [strategy]);

  return (
    <main className="container">
      <h1 className="title">주식 전략 보기</h1>
      <select
        value={strategy}
        onChange={(e) => setStrategy(e.target.value)}
        className="select"
      >
        {strategies.map((s) => (
          <option key={s} value={s}>
            {s}
          </option>
        ))}
      </select>
      {loading ? (
        <p>로딩중...</p>
      ) : (
        <ul className="list">
          {stocks.map((s) => (
            <li key={s.symbol}>
              {s.symbol} - {s.name}
            </li>
          ))}
        </ul>
      )}
    </main>
  );
}
