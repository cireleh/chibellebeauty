// package.json
{
  "name": "chibelle-frontend",
  "version": "1.0.0",
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start"
  },
  "dependencies": {
    "next": "^13.4.0",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "tailwindcss": "^3.3.0"
  }
}

// tailwind.config.js
module.exports = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx}',
    './components/**/*.{js,ts,jsx,tsx}'
  ],
  theme: { extend: {} },
  plugins: []
};

// pages/index.js
import Head from 'next/head';
export default function Home() {
  return (
    <div className="p-4">
      <Head><title>ChiBelle</title></Head>
      <h1 className="text-2xl font-bold text-pink-600">Welcome to ChiBelle</h1>
      <p className="mt-2 text-gray-700">Discover, book, and glow with Lagos’ finest beauty pros.</p>
    </div>
  );
}

// pages/login.js
export default function Login() {
  return (
    <div className="p-4 max-w-md mx-auto">
      <h2 className="text-xl font-semibold mb-4">Login</h2>
      <form className="space-y-2">
        <input className="border p-2 w-full" placeholder="Email" />
        <input className="border p-2 w-full" type="password" placeholder="Password" />
        <button className="bg-pink-600 text-white px-4 py-2 rounded w-full">Login</button>
      </form>
    </div>
  );
}

// components/ServiceCard.jsx
const ServiceCard = ({ title, desc }) => (
  <div className="border p-4 rounded-lg shadow-sm mb-4 bg-white">
    <h2 className="text-xl font-semibold text-pink-600">{title}</h2>
    <p className="text-gray-600">{desc}</p>
  </div>
);
export default ServiceCard;

// .env.example
NEXT_PUBLIC_API_URL=https://your-api-url
