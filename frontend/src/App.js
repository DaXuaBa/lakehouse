import {BrowserRouter as Router, Routes, Route} from 'react-router-dom'
import Header from "./components/Header";
import Footer from "./components/Footer";
import {Container} from 'react-bootstrap'
import HomeScreen from "./screens/HomeScreen";
import PostSrceen from './screens/PostSrceen';
import LoginScreen from './screens/LoginScreen';
import RegisterScreen from './screens/RegisterScreen';
import StravaConnectedPage from './screens/StravaConnectedPage';

function App() {
  return (
    <Router>
      <Header/>
        <main className="py-3">
          <Container>
            <Routes>
              <Route path="/connectstrava" element={<StravaConnectedPage />} />
              <Route path="/login" element={<LoginScreen />} />
              <Route path="/register" element={<RegisterScreen />} />
              <Route path="/post/:id" element={<PostSrceen />} /> 
              <Route path="/" element={<HomeScreen />} /> 
            </Routes>
          </Container>
        </main>
      <Footer/>
    </Router>
  );
}

export default App;
