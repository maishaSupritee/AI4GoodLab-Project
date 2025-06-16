import React from 'react'

const Map = () => {
  return (
    <div className="w-full h-[600px] border border-gray-700 rounded-lg overflow-hidden">
      <iframe
        src="/maps/map.html"
        width="100%"
        height="100%"
        title="Folium Map with Layer Controls"
        style={{ border: "none" }}
      ></iframe>
    </div>
  )
}

export default Map