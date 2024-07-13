import React from 'react';
import { Provider } from 'react-redux';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

function App() {
  return (
    <Provider store={store}>
      <Router>
        <Routes>
          
        </Routes>
      </Router>
    </Provider>
  );
}

export default App;
