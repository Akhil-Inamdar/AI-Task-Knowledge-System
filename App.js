// import { BrowserRouter, Routes, Route } from "react-router-dom";

// import Login from "./pages/Login";
// import Dashboard from "./pages/Dashboard";
// import Tasks from "./pages/Tasks";
// import Documents from "./pages/Documents";
// import Search from "./pages/Search";
// import Analytics from "./pages/Analytics";

// function App() {

//     return (

//         <BrowserRouter>

//             <Routes>

//                 <Route
//                     path="/"
//                     element={<Login />}
//                 />

//                 <Route
//                     path="/dashboard"
//                     element={<Dashboard />}
//                 />

//             </Routes>

//         </BrowserRouter>

//     );

// }

// export default App;


import { BrowserRouter, Routes, Route } from "react-router-dom";

import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import Tasks from "./pages/Tasks";
import Documents from "./pages/Documents";
import Search from "./pages/Search";
import Analytics from "./pages/Analytics";

function App() {

    return (

        <BrowserRouter>

            <Routes>

                {/* Login */}
                <Route
                    path="/"
                    element={<Login />}
                />

                {/* Dashboard */}
                <Route
                    path="/dashboard"
                    element={<Dashboard />}
                />

                {/* Tasks */}
                <Route
                    path="/tasks"
                    element={<Tasks />}
                />

                {/* Documents */}
                <Route
                    path="/documents"
                    element={<Documents />}
                />

                {/* AI Search */}
                <Route
                    path="/search"
                    element={<Search />}
                />

                {/* Analytics */}
                <Route
                    path="/analytics"
                    element={<Analytics />}
                />

            </Routes>

        </BrowserRouter>

    );

}

export default App;