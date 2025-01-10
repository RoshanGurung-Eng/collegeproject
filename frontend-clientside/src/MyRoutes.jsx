import React from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Layout from './components/Layout'
import Homepage from './pages/Homepage'
import Signup from './pages/Authintication/Signup'
import Bike from './pages/Bike'

const MyRoutes = () => {
  return (
    <Router>
      <Routes>
        <Route path='' element= {<Layout/>}>
          <Route index element = {<Homepage/>}/>
          <Route path='bike' element = {<Bike/>}/>
          {/*<Route path = 'bike-details' element = {<BIkeDetails/>}/>*/}
          <Route path='register' element = {<Signup/>}/>
          {/*<Route path='cart' element = {<Cart/>}/>*/}
        </Route>
        
      </Routes>
    </Router>
  )
}

export default MyRoutes
