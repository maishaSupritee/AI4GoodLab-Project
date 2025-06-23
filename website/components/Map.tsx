//only the map on the home page
import React from 'react'

const Map = () => {
  return (
    <div className="mx-auto w-full max-w-7x1 bg-gray-50 p-6 rounded-2x1 shadow-lg overflow-hidden h-[70vh]">
      <iframe
        src="/maps/map.html"  
        width="100%"
        height="100%"
        style={{ border: 0 }}
        title="StreetScope map"
      />
    </div>
  )
}

export default Map