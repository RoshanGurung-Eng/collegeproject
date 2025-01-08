import React from 'react'
import { Link } from 'react-router-dom'
const Header = () => {
  return (
    
    <header className="sticky top-0 h-[90px] shadow-xl z-30 bg-violet-200">
        <div className="container mx-auto flex justify-between h-full items-center ">
            <nav>
                <div className="cursor-pointer lg:hidden" id="nav_trigger_btn">
                    <i className="ri-menu-4-fill text-4xl text-primary"></i></div>
                    <ul className="fixed w-full h-0 p-0 bg-violet-200 overflow-hidden border-t top-[90px] left-0 right-0 flex flex-col gap-4 lg:relative lg:flex-row lg:p-0 lg:top-0 lg:border-none lg:h-full transition-all duration-300" id="nav_menu">
                    <li><Link href="#">Home</Link></li>
                    <li><Link href="#">Vehicle</Link></li>
                    <li><Link href="#">Hire Link Driver</Link></li>
                    <li><Link href="#">About</Link></li>
                    <li><Link href="#">Contact Us</Link></li>
                </ul>
            </nav>
        </div>

    </header>
    )
}

export default Header