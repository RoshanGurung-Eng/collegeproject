import React,{useState, useEffect} from 'react'
import { useParams } from 'react-router-dom'
import {ToastContainer , toast } from 'react-toastify'
import axios from 'axios'

const BIkeDetails = () => {
    const [bike, setBike] = useState({})
    const params = useParams()
  
    useEffect(() => {
      const id = params.bike_id
  
      axios
        .get(`http://127.0.0.1:8000/vehicles/${id}`)
        .then(res => setBike(res.data))
        .catch(err => console.log(err))
    }, [params.bike_id])
  
    // handling addToCart function for localstorage
    const addToCart = () => {
      const cartItems = JSON.parse(localStorage.getItem('cartItems')) || []
  
      const bikeItem = {
        id: bike.id,
        title: bike.title,
        price: bike.price,
        image: bike.image,
        category: bike.category,
        rating: bike.rating,
        quantity: 1,
      }
      const existItem = cartItems.find(item => item.id === bike.id)
  
      if (existItem) {
        toast.error('Bike is already in cart')
      } else {
        cartItems.push(bikeItem)
        localStorage.setItem('cartItems', JSON.stringify(cartItems))
        toast.success(`${bikeItem.title} is successfully added to cart`)
      }
    }
  
    return (
      <>
        <ToastContainer
          position="top-center"
          autoClose={5000}
          hideProgressBar={false}
          newestOnTop={false}
          closeOnClick
          rtl={false}
          pauseOnFocusLoss
          draggable
          pauseOnHover
          theme="dark"
          transition="bounce"
        />
        <div className="container mx-auto my-5">
          <div className="flex flex-wrap justify-evenly py-2">
            <div className="w-full md:w-5/12">
              <img src={bike.image} alt={bike.title} className="w-full h-auto object-cover" />
            </div>
            <div className="w-full md:w-5/12 flex flex-col justify-between p-4">
              <h2 className="text-2xl font-semibold mb-4">{bike.title}</h2>
              <h4 className="text-xl font-bold text-blue-600 mb-4">${bike.price}</h4>
              <p className="text-gray-700 mb-4">{bike.description}</p>
              {bike.rating && (
                <h5 className="text-yellow-500 mb-4">Rating: {bike.rating.rate} ⭐</h5>
              )}
              <button
                className="bg-yellow-500 hover:bg-yellow-600 text-white font-semibold py-2 px-4 rounded"
                onClick={addToCart}
              >
                Add To Cart
              </button>
            </div>
          </div>
        </div>
      </>
    )
  }

export default BIkeDetails