import React from 'react'
import { Link } from 'react-router-dom'
const Header = () => {
  return (
    <header class="sticky top-0 h-[90px] shadow-xl z-30 bg-violet-200">
        <div class="container mx-auto flex justify-between h-full items-center ">
            <Link><img src="/docs/logo/logo.png" alt="" className="w-48 h-16" /> </Link> 
            <nav>
                <div class="cursor-pointer lg:hidden" id="nav_trigger_btn">
                <i class="ri-menu-4-fill text-4xl text-primary"></i>
                </div>
                    <ul class="fixed w-full h-0 p-0 bg-violet-200 overflow-hidden border-t top-[90px] left-0 right-0 flex flex-col gap-4 lg:relative lg:flex-row lg:p-0 lg:top-0 lg: border-none lg:h-full transition-all duration-300" id="nav_menu">
                      <li><Link href="index.html">Home</Link></li>
                      <li><Link href="vehicle.html">Vehicle</Link></li>
                      <li><Link href="driver.html">Hire Link Driver</Link></li>
                      <li><Link href="#">About</Link></li>
                      <li><Link href="#">Contact Us</Link></li>
                    </ul>
                </nav>
        </div>
    </header>
    )
}

export default Header