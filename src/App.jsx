import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Layout from './components/Layout';
import Dashboard from './pages/Dashboard';
import SubjectPage from './pages/SubjectPage';

function App() {
  return (
    <Router>
      <Layout>
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/subject/:id" element={<SubjectPage />} />
        </Routes>
      </Layout>
    </Router>
  );
}

export default App;
