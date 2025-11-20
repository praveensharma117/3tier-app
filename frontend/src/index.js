cat << 'EOF' > src/index.js
import React from 'react';
import ReactDOM from 'react-dom/client';

function App() {
  return (
    <h1>Hello from 3-Tier App Frontend!</h1>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);
EOF
