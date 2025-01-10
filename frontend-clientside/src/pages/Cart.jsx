import React, { useState, useEffect, Fragment } from 'react'
import { FaTrash } from "react-icons/fa"
import { toast, ToastContainer } from 'react-toastify'
import 'react-toastify/dist/ReactToastify.css'

const Cart = () => {
  const [bike, setBike] = useState([])

  useEffect(() => {
    const cartData = JSON.parse(localStorage.getItem('cartItems')) || []
    setBike(cartData)
  }, [])

  const removeCartHandler = (id, title) => {
    const cartItems = JSON.parse(localStorage.getItem('cartItems'))

    // Remove from the cart using filter method
    const filterData = cartItems.filter(item => item.id !== id)
    
    // Update bike state after filter
    setBike(filterData)

    // Update localStorage after filter
    localStorage.setItem('cartItems', JSON.stringify(filterData))

    toast.success(`${title} is dead`)
  }

  // Decrease quantity
  const decreaseQty = (id) => {
    const updateBike = bike.map(item => {
      if (item.id === id && item.quantity) {
        return { ...item, quantity: item.quantity - 1 }
      } else {
        return item
      }
    })

    setBike(updateBike)
    localStorage.setItem('cartItems', JSON.stringify(updateBike))
  }

  // Increase quantity
  const increaseQty = (id) => {
    const updateBike = bike.map(item => {
      if (item.id === id && item.quantity < 15) {
        return { ...item, quantity: item.quantity + 1 }
      } else {
        return item
      }
    })

    setBike(updateBike)
    localStorage.setItem('cartItems', JSON.stringify(updateBike))
  }

  return (
    <>
      <ToastContainer position="top-right" theme="colored" />
      <div className="container mx-auto px-4">
        <div className="shadow my-4 p-4">
          {bike.length === 0 ? (
            <h2 className="my-5 text-red-500 text-center">Your Cart is empty</h2>
          ) : (
            <>
              <h2 className="text-center text-2xl">Your Cart Items</h2>
              <div className="flex flex-col space-y-4">
                {bike.map((item, i) => (
                  <Fragment key={i}>
                    <hr />
                    <div className="flex items-center justify-between p-4 shadow-md">
                      <div className="w-1/5">
                        <img src={item.image} alt={item.title} className="w-12 h-12 object-cover" />
                      </div>
                      <div className="w-1/3">
                        <span className="font-semibold">{item.title}</span>
                      </div>
                      <div className="w-1/5 text-yellow-500">${item.price}</div>
                      <div className="w-1/4">
                        <div className="flex items-center">
                          <button
                            className="btn bg-red-500 text-white p-2 rounded"
                            onClick={() => decreaseQty(item.id)}
                          >
                            -
                          </button>
                          <input
                            type="number"
                            className="mx-2 p-2 border-0 w-12 text-center"
                            value={item.quantity}
                            readOnly
                          />
                          <button
                            className="btn bg-blue-500 text-white p-2 rounded"
                            onClick={() => increaseQty(item.id)}
                          >
                            +
                          </button>
                        </div>
                      </div>
                      <div className="w-1/12">
                        <button
                          className="btn bg-red-500 text-white p-2 rounded"
                          onClick={() => removeCartHandler(item.id, item.title)}
                        >
                          <FaTrash />
                        </button>
                      </div>
                    </div>
                    <hr />
                  </Fragment>
                ))}
              </div>
              <div className="py-4 px-6 bg-gray-100 shadow-md">
                <h5 className="text-center text-xl">Cart Summary</h5>
                <hr />
                <span className="block">
                  <strong>Units:</strong> {bike.reduce((total, item) => total + item.quantity, 0)} units
                </span>
                <span className="block">
                  <strong>Total Price:</strong> ${bike.reduce((total, item) => total + item.price * item.quantity, 0).toFixed(2)}
                </span>
                <hr />
                <button className="w-full bg-red-500 text-white p-2 rounded">Check Out</button>
              </div>
            </>
          )}
        </div>
      </div>
    </>
  )
}

export default Cart
