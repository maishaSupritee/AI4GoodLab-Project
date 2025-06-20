//only the map on the home page
import React from 'react'

const Map = () => {
  return (
    <div className="w-full h-full border border-purple-700 rounded-lg overflow-hidden">
      <iframe
        src="/maps/map.html"  
        width="100%"
        height="100%"
        style={{ border: 50, borderColor: '#373584' }}
        title="StreetScope map"
      />
    </div>
  )
}

export default Map