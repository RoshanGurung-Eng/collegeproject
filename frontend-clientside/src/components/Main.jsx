import React from 'react'

const Main = () => {
  return (
    <>
        <main className="max-w-[1920px] mx-auto bg-violet-50 overflow-hidden">
            <section className="landing h-[640px] xl:h-[640px] bg-landing bg-center lg:bg-cover bg-no-repeat bg-fixed xl:rounded-bl-[290px] relative z-20">
                <div className="container absolute -right-1/4 h-full flex items-center justify-center xl:justify-start">

                    <div className="landing_text w-[500px] flex flex-col items-center text-center xl:text-left lg:items-start">
                        <h2 className="h2 -mt-52">Your Next Ride, Just a Click Away.</h2>
                        <a href="vehicle.html">
                            <button className="btn btn-primary mx-auto xl:mx-0 mt-6 ">Rent a Vehicle
                            <i className="ri-roadster-line text-violet-300"></i>
                            </button>
                        </a>
                    </div>
                </div>
                </section>
                <section className="steps mt-[80px] xl:mt-[200px] relative z-20">
                    <div className="container mx-auto">
                        <div className="grid grid-cols-1 gap-12 xl:grid-cols-3">
                            <div className="steps__step text-center bg-violet-100 border border-purple-300 rounded-xl shadow-xl p-10">
                                <div className="mb-4">
                                <i className="ri-taxi-line text-5xl text-indigo-400"></i>
                                </div>
                                <h3 className="h3 mb-5">Step 1: Choose your Favourite Vehicle</h3>
                                <p className="mb-5 max-w-md mx-auto">Select your preferred vehicle, tailored to your journey as per your requirement.</p>
                            </div>
                            
                            <div className="steps__step text-center  bg-violet-100 border border-purple-300 rounded-xl shadow-xl p-10">
                                <div className="mb-4">
                                <i className="ri-wallet-3-line text-5xl text-indigo-400"></i>
                                </div>
                                <h3 className="h3 mb-5">Step 2: Book your Favourite Vehicle</h3>
                                <p className="mb-5 max-w-md mx-auto">You can make easy bookings through our user-friendly app or a simple phone call.</p>
                            </div>

                            <div className="steps__step text-center  bg-violet-100 border border-purple-300 rounded-xl shadow-xl p-10">
                                <div className="mb-4">
                                <i className="ri-riding-line text-5xl text-indigo-400"></i>
                                </div>
                                <h3 className="h3 mb-5">Step 3: Pick-Up the Ride and Enjoy</h3>
                                <p className="mb-5 max-w-md mx-auto">Select your nearest location with the date and time. Sit back and begin your journey with SahaYaatri.</p>
                            </div>
                        </div>
                    </div>
                </section>
                <section className="bg-violet-200 mt-[80px] xl:mt-[200px] relative">
                    <div className="container mx-auto ">
                        <h3 className=" h4 text-center mb-2">Meet the Fleet</h3>
                        <div className="swiper-container  ">
                            <div className="swiper-wrapper">
                                <div className="swiper-slide">
                                <a href="bike.html">
                                    <img src="/docs/bike/bike0.png" alt=""/>
                                    <p className="text-center ">Urban Bikes</p>
                                </a>
                                </div>
                          
                                <div className="swiper-slide">
                                <a href="scooter.html">
                                    <img src="/docs/scooter/scosco.png"  alt=""/>
                                    <p className="text-center ">Swift Scooters</p>
                                </a>
                                </div>
                               
                                <div className="swiper-slide">
                                <a href="car.html">
                                    <img src="/docs/car/car0.png" alt=""/>
                                    <p className="text-center ">Compact Cars</p>
                                </a>
                                </div>
                           
                                <div className="swiper-slide">
                                <a href="suv.html">
                                    <img src="/docs/suv/suv0.png" alt=""/>
                                    <p className="text-center ">Standard SUVs</p>
                                </a>
                                </div>
                               
                                <div className="swiper-slide">
                                <a href="luxury.html">
                                    <img src="/docs/luxury/lux0.png" alt=""/>
                                    <p className="text-center ">Luxury Cars</p>
                                </a>
                                </div>
                                
                                <div className="swiper-slide">
                                <a href="truck.html">
                                    <img src="/docs/truck/pick1.png" alt=""/>
                                    <p className="text-center ">Pick-Up Trucks</p>
                                </a>
                                </div>
                            </div>

                            
                            <div className="swiper-button-next"></div>
                            <div className="swiper-button-prev"></div>
                        </div>

                     
                        <div className="flex justify-center mt-9">
                        <a href="vehicle.html">
                            <button className="px-6 py-2 mb-6 rounded-lg bg-indigo-400 hover:bg-indigo-600 text-white font-semibold transition">View all Vehicles
                            </button>
                        </a>
                        </div>
                    </div>
                </section>
            <div className="h-[50px]"></div>
        </main>

    </>
  )
}

export default Main