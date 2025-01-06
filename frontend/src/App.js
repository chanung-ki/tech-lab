import logo from './logo.svg';
import './App.css';
import axios from 'axios'

const axiosInstance = axios.create({
  baseURL: "http://localhost:8000",
});

function App() {

  const handleClick = async () => {
    try {
      const response = await axiosInstance.get("/api/test");
      if (response.status === 200) {
        console.log(response.data);
      }
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <div onClick={handleClick}>
          api 호출
        </div>
      </header>
    </div>
  );
}

export default App;
