import React from 'react';
import { Link } from 'react-router-dom';
import './Home.css';

const tables = [
  { name: 'Users', route: '/users' },
  { name: 'Games', route: '/games' },
  { name: 'Chats', route: '/chats' },
  { name: 'Messages', route: '/messages' },
  { name: 'Posts', route: '/posts' },
  { name: 'Comments', route: '/comments' },
  { name: 'Teams', route: '/teams' },
  { name: 'Subscriptions', route: '/subscriptions' },
];

const Home = () => {
  return (
    <div className="container">
      <h1>Gamers</h1>
      <h2>Таблицы:</h2>
      <ul>
        {tables.map((table) => (
          <li key={table.route}>
            <Link to={table.route}>{table.name}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Home;
