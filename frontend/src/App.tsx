import { useState } from 'react'
import './App.css'
import Home from './components/home/Home'
import HeaderNavbar from './components/navbar/Navbar'
import { BrowserRouter, Routes, Route } from "react-router-dom"
import FileUpload from './components/FileUpload'
import FileRetreival from './components/FileRetrieval/FileRetreival'

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
        </Routes> 
      </BrowserRouter>
    </>
  )
}

export default App
