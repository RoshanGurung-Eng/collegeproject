import React, { useEffect, useState } from 'react'
import axios from 'axios'
import Card from './Card'
import { ColorRing } from 'react-loader-spinner'

const Cardcontainer = () => {
  const [vehicles, setVehicles] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const fetchVehicles = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/vehicles') // Replace with your actual API endpoint
        setVehicles(response.data)
        setLoading(false)
      } catch (error) {
        console.error('Error fetching vehicles:', error)
      }
    }

    // Simulate a delay for loading spinner
    setTimeout(() => {
      fetchVehicles()
    }, 2000)
  }, [])

  return (
    <div className="container mx-auto my-4">
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
        {loading ? (
          <div className="flex items-center justify-center h-64 w-full col-span-full">
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
        ) : vehicles.length > 0 ? (
          vehicles.slice(0, 8).map((vehicle, i) => (
            <Card key={i} item={vehicle} />
          ))
        ) : (
          <p className="text-center col-span-full text-gray-500">
            No vehicles available.
          </p>
        )}
      </div>
    </div>
  )
}

export default Cardcontainer
