import React from 'react'

const Map = () => {
  return (
    <div className="w-full h-full border border-gray-700 rounded-lg overflow-hidden">
      <iframe
        src="https://www.openstreetmap.org/export/embed.html?bbox=-0.127758%2C51.507351%2C-0.127758%2C51.507351&layer=mapnik"
        width="100%"
        height="100%"
        // style={{ border: '1px solid black' }}
        title="OpenStreetMap"
      ></iframe>
    </div>
  )
}

export default Map