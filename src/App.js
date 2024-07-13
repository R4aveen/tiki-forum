import Error404 from 'containers/errors/Error404';
import React from 'react';
import { Provider } from 'react-redux';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import store from './store';
import Home from 'containers/pages/home';
function App() {
  return (
    <Provider store={store}>
      <Router>
        <Routes>
          {/* Error displaay */}
          <Route path='*' element={<Error404/>}/>

          {/*  Home Diusplay */}
          <Route path='/' element={<Home/>}/>

        </Routes>
      </Router>
    </Provider>
  );
}

export default App;
