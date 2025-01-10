import React,{useState, UseEffect} from 'react'

const UseEffects = () => {

    
        const [data, setData] = useState(1)
        const [num, setNum] = useState(1)
    
        UseEffect(() => {
            alert('This is from effect hook')
        }, [num, data])
    
        return (
            <>  
                <div className="container mx-auto p-4">
                    <h2 className="text-red-600 font-bold text-lg">{data}</h2>
                    <button 
                        className="bg-yellow-500 hover:bg-yellow-600 text-white font-semibold py-2 px-4 rounded mt-2"
                        onClick={() => setData(data + 1)}
                    >
                        Add
                    </button>
    
                    <h2 className="text-blue-500 font-bold text-lg mt-4">{num}</h2>
                    <button 
                        className="bg-gray-500 hover:bg-gray-600 text-white font-semibold py-2 px-4 rounded mt-2"
                        onClick={() => setNum(num + 1)}
                    >
                        Add
                    </button>
                </div>
            </>
        )
    }
    


export default UseEffects