import { BrowserRouter, Routes, Route } from "react-router-dom";
import Navbar from "@/components/Navbar";
import Landing from "@/pages/Landing";
import Demo from "@/pages/Demo";
import Contact from "@/pages/Contact";

function App() {
  return (
    <BrowserRouter>
      <div className="min-h-screen bg-background">
        <Routes>
          <Route
            path="/"
            element={
              <>
                <Navbar />
                <Landing />
              </>
            }
          />
          <Route
            path="/contact"
            element={
              <>
                <Navbar />
                <Contact />
              </>
            }
          />
          <Route path="/demo" element={<Demo />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
