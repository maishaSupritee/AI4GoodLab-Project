"use client";

import React, { use } from 'react'
import { useState } from 'react';

const Map = () => {
  const [view, setView] = useState("layered_map");

  return (
    <div>
      <select onChange={(e) => setView(e.target.value)} className="mb-4">
        <option value="layered_map">Base Map</option>
        <option value="layered_sidewalks">Sidewalk Improvements</option>
        <option value="layered_lighting">Lighting Upgrades</option>
      </select>
      <div className="w-full h-[600px] border border-gray-700 rounded-lg overflow-hidden">
        <iframe
          src="/maps/map.html"
          width="100%"
          height="100%"
          title="Folium Map with Layer Controls"
          style={{ border: "none" }}
        ></iframe>
      </div>
    </div>
  )
}

export default Map