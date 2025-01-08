import React from 'react'
import { Link } from 'react-router-dom'

const Footer = () => {
  return (
      <footer className="bg-violet-200 text-white py-12 mt-96">
          <div className="container mx-auto px-6 lg:px-20">
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-10">
              <div>
                <h3 className="text-2xl font-bold mb-4">About Us</h3>
                  <p className="text-gray-600">Rent a car and smile with us. We make traveling easier, convenient, and fun. Start your adventure today!</p>
                  <div className="flex gap-4 mt-6">
                    <Link href="#" className="text-gray-400 hover:text-gray-200">
                    <i className="ri-facebook-fill text-2xl"></i></Link>
                    <Link href="#" className="text-gray-400 hover:text-gray-200">
                      <i className="ri-instagram-fill text-2xl"></i></Link>
                    <Link href="#" className="text-gray-400 hover:text-gray-200">
                      <i className="ri-twitter-fill text-2xl"></i>
                    </Link>
                    <Link href="#" className="text-gray-400 hover:text-gray-200">
                      <i className="ri-linkedin-fill text-2xl"></i>
                    </Link>
                    </div>
                    </div>
                    <div>
                      <h3 className="text-2xl font-bold mb-4">Quick Links</h3>
                      <ul className="space-y-4 text-gray-600">
                      <li><Link href="#" className="hover:text-white">Home</Link></li>
                      <li><Link href="#" className="hover:text-white">About</Link></li>
                      <li><Link href="#" className="hover:text-white">Rent out your Car</Link></li>
                      <li><Link href="#" className="hover:text-white">Contact Us</Link></li></ul>
                    </div>
                    <div>
                      <h3 className="text-2xl font-bold mb-4">Contact Us</h3>
                      <ul className="space-y-4 text-gray-600">
                        <li>
                          <span className="font-semibold text-gray-600">Email:</span>
                          <Link href="mailto:sahayaatri@gmail.com" className="hover:text-white">             sahayaatri@gmail.com</Link>
                        </li>
                        <li>
                          <span className="font-semibold text-gray-600">Phone:</span>
                          <Link href="tel:9841753421" className="hover:text-white"> 9841753421</Link>
                        </li>
                        <li><span className="font-semibold text-gray-600">Address:</span> Sitapaila, Kathmandu
                        </li>
                      </ul>
                    </div>
                    <div>
                      <h3 className="text-2xl font-bold mb-4">Newsletter</h3>
                      <p className="text-gray-600 mb-6">Subscribe to get the latest offers and updates on new destinations.</p>
                      <form action="#" className="flex flex-col gap-4">
                        <input
                          type="email"
                          placeholder="Enter your email"
                          className="px-4 py-2 rounded-lg bg-gray-200 text-gray-600 focus:outline-none focus:ring-2 focus:ring-indigo-300"/>
                        <button
                          type="submit"
                          className="px-4 py-2 rounded-lg bg-indigo-600 hover:bg-indigo-400 text-white font-semibold transition">
                          Subscribe
                        </button>
                      </form>
              </div>
            </div>
                  <div className="border-t border-gray-700 mt-12 pt-8 text-center text-gray-500">
                    <p>&copy; 2024 SahaYaatri. All rights reserved.</p></div>
        </div>
      </footer>
   )
}

export default Footer