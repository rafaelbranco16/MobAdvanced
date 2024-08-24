import './App.css'
import Home from './components/home/Home'
import HeaderNavbar from './components/navbar/Navbar'
import { BrowserRouter, Routes, Route } from "react-router-dom"
import FileUpload from './components/FileUpload'
import FileRetreival from './components/FileRetrieval/FileRetreival'
import Assassins from './components/Assassins/Assassins'
import Warriors from './components/Warriors/Warriors'
import Guardians from './components/Guardians/Guardians'
import Mages from './components/Mages/Mages'
import Carry from './components/Carries/Carry'

function App() {
  return (
    <>
      <BrowserRouter>
      <HeaderNavbar></HeaderNavbar>
        <Routes>
          <Route path='/' element=""/>
          <Route index element={<Home/>}/>
          <Route path="add-info" element={<FileUpload/>}/>
          <Route path="files" element={<FileRetreival/>}/>
          <Route path='assassin' element={<Assassins/>}/>
          <Route path='warrior' element={<Warriors/>}/>
          <Route path='guardian' element={<Guardians/>}/>
          <Route path='mage' element={<Mages/>}/>
          <Route path='carry' element={<Carry/>}/>
        </Routes> 
      </BrowserRouter>
    </>
  )
}

export default App
