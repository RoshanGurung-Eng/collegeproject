import React, {UseState} from 'react'

const UseStates = () => {
    const [num, setNum] = UseState(1);

  return (
    <>
      <div className="container flex flex-wrap items-center justify-center gap-4 p-4">
        
        {num < 10 && (
          <button
            className="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded"
            onClick={() => setNum(num + 1)}
          >
            Increment
          </button>
        )}

        {/* Display the current value */}
        <h1 className="text-green-500 text-xl font-bold">{num}</h1>

        {/* Decrement button (only shows if num > 1) */}
        {num > 1 && (
          <button
            className="bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded"
            onClick={() => setNum(num - 1)}
          >
            Decrement
          </button>
        )}
      </div>
    </>
  )
}

export default UseStates