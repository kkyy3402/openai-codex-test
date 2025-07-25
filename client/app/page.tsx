'use client';
import { useEffect, useState } from 'react';

interface Stock {
  symbol: string;
  name: string;
}

interface ChartData {
  labels: string[];
  values: number[];
}

export default function HomePage() {
  const [stocks, setStocks] = useState<Stock[]>([]);
  const [chart, setChart] = useState<ChartData>({ labels: [], values: [] });
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    async function fetchStocks() {
      setLoading(true);
      const url = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';
      const [stockRes, chartRes] = await Promise.all([
        fetch(`${url}/stocks?term=short&strategy=qualitative`),
        fetch(`${url}/chart`),
      ]);
      const stockData = await stockRes.json();
      const chartData = await chartRes.json();
      setStocks(stockData.data);
      setChart(chartData);
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
        <>
          <ul>
            {stocks.map((s) => (
              <li key={s.symbol}>{s.symbol} - {s.name}</li>
            ))}
          </ul>
          <div className="chart">
            {chart.labels.map((label, i) => (
              <div
                key={label}
                className="chart-bar"
                style={{ height: `${chart.values[i]}px` }}
              >
                <span className="sr-only">
                  {label}: {chart.values[i]}
                </span>
              </div>
            ))}
          </div>
        </>
      )}
    </main>
  );
}
