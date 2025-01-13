
import axios from 'axios'
import API_BASE_URL from '../config'

const Bike = () => {
  return (
  axios.get(`${API_BASE_URL}/search`)
  .then(response => console.log(response.data))
  .catch(error => console.error('Error:', error))
  )
}

export default Bike
