import React, { useState, useEffect } from 'react'
import { ColorRing } from 'react-loader-spinner'
import axios from 'axios'
import Card from '../components/Card'

const Bike = () => {
  const [bikes, setBikes] = useState([])
  const [loading, setLoading] = useState(true)
  const [limit, setLimit] = useState(8)

  useEffect(() => {
    const fetchBikes = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/vehicles')
        setBikes(response.data)
        setLoading(false)
      } catch (error) {
        console.error('Error fetching bikes:', error)
      }
    }

    setTimeout(() => {
      fetchBikes()
    }, 2000)
  }, [])

  return (
    <>
      <div className="container mx-auto my-5">
        <h1 className="text-3xl font-semibold text-center mb-6">New Arrivals</h1>
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
          {
            loading ? (
              <div className="flex justify-center items-center h-64">
                <ColorRing
                  visible={true}
                  height="80"
                  width="80"
                  ariaLabel="color-ring-loading"
                  wrapperStyle={{}}
                  wrapperClass="color-ring-wrapper"
                  colors={['#e15b64', '#f47e60', '#f8b26a', '#abbd81', '#849b87']}
                />
              </div>
            ) : (
              bikes.slice(0, limit).map((bike, i) => (
                <Card key={i} item={bike} />
              ))
            )
          }
        </div>
        <button
          onClick={() => setLimit(limit + 8)}
          className="mt-6 bg-blue-600 hover:bg-blue-700 text-white font-semibold py-2 px-4 rounded"
        >
          View More
        </button>
      </div>
    </>
  )
}

export default Bike
