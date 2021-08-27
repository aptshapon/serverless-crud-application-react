import './App.css';
import Create from './components/create';
import Read from './components/read';
import Update from './components/update';
import { BrowserRouter as Router, Route } from 'react-router-dom'
import { Link } from 'react-router-dom';
import { Button } from 'semantic-ui-react'

function App() {
  return (
    <Router>
      <div className="main">
      <Link to='/read'>
            <Button color="blue">Read Book</Button>
      </Link>
      <Link to='/create'>
            <Button color="blue">Add New Book</Button>
      </Link>
        <h2 className="main-header">Proof-of-Concept Project</h2>
        <div>
          <Route exact path='/create' component={Create} />
        </div>
        <div style={{ marginTop: 20 }}>
          <Route exact path='/read' component={Read} />
        </div>

        <Route path='/update' component={Update} />
      </div>
    </Router>
  );
}

export default App;
