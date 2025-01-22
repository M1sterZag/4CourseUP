import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams, Link } from 'react-router-dom';
import './Table.css';

const Table = () => {
  const { tableName } = useParams();
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get(`http://localhost:8000/${tableName}`);
        setData(response.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      } finally {
        setLoading(false);
      }
    };
    fetchData();
  }, [tableName]);

  const formatValue = (value) => {
    if (value === true) return 'Да';
    if (value === false) return 'Нет';
    if (value === null) return 'Нет данных';
    return value;
  };

  if (loading) {
    return <div className="loading">Loading...</div>;
  }

  if (data.length === 0) {
    return <div className="no-data">No data available</div>;
  }

  const headers = Object.keys(data[0]);

  return (
    <div className="container">
      <Link to="/" className="back-link">На главную</Link>
      <h1>Таблица {tableName}</h1>
      <table>
        <thead>
          <tr>
            {headers.map((header) => (
              <th key={header}>{header}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {data.map((row, index) => (
            <tr key={index}>
              {headers.map((header) => (
                <td key={header}>{formatValue(row[header])}</td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Table;
