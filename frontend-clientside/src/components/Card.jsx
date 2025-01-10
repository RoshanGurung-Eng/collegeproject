import React from 'react';
import { Link } from 'react-router-dom';

const Card = (props) => {
  const { image, title, price, id } = props.item;

  return (
    <div className="w-full sm:w-1/2 lg:w-1/4 p-4">
      <div className="bg-white rounded-lg shadow-md overflow-hidden flex flex-col h-full">
        <img 
          src={image} 
          alt={title} 
          className="object-cover h-48 w-full"
        />
        <div className="p-4 flex flex-col justify-between flex-grow">
          <h5 className="text-lg font-bold mb-2">{title}</h5>
          <p className="text-gray-600 mb-4">{price}</p>
          <Link 
            to={`/productdetails/${id}`} 
            className="mt-auto bg-blue-500 hover:bg-blue-600 text-white font-semibold py-2 px-4 rounded text-center"
          >
            View Details
          </Link>
        </div>
      </div>
    </div>
  );
};

export default Card;
