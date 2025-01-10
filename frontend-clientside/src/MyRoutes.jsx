import React from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Layout from './components/Layout'
import Homepage from './pages/Homepage'
import BIkeDetails from './pages/BIkeDetails'
import Cart from './pages/Cart'

const MyRoutes = () => {
  return (
    <Router>
      <Routes>
        <Route path='' element= {<Layout/>}>
          <Route index element = {<Homepage/>}/>
          <Route path = 'bike-details' element = {<BIkeDetails/>}/>
          <Route path='cart' element = {<Cart/>}/>
        </Route>
        
      </Routes>
    </Router>
  )
}

export default MyRoutes
