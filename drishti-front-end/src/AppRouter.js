

import React from "react";
import { BrowserRouter as Router, Route} from "react-router-dom";

// pages
import App from './App';
import Refresh from './Refresh';
import StartupOverlay from './StartupOverlay';
import Analytics from './Analytics';

function AppRouter() {
  return (
    <Router>
      <div>
        <Route path="/" exact component={StartupOverlay} />
        <Route path="/refresh" exact component={Refresh} />
        <Route path="/app" exact component={App} />
        <Route path="/analytics" exact component={Analytics} />
      </div>
    </Router>
  );
}

export default AppRouter;

