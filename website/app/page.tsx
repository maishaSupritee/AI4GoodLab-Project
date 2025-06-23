//home page for website
import Image from "next/image";
import Map from "@/components/Map";

export default function Home() {
  return (
    <main className="mx-auto sm:px-10 px-5 flex flex-col">
      <header className="flex items-center justify-between h-20 px-6 bg-white shadow-sm border-b border-[#373584]/20 z-10">
      <div className="flex items-center gap-4">
        <Image
          src="/streetscope.png"
          alt="StreetScope.ai Logo"
          width={80}
          height={80}
          className="flex-shrink-0"
        />
        <div className="flex flex-col">
          <h1 className="text-xl sm:text-3xl font-montserrat text-[#373584] font-bold">
            StreetScope.ai
          </h1>
          <h2 className="text-sm sm:text-base text-gray-600">
            A platform for data-driven urban planning
          </h2>
        </div>
        </div>
      
      <div className="flex items-center gap-3">
          <button className="px-4 py-2 bg-[#373584] text-white rounded-lg hover:bg-indigo-700 transition">
            Home
          </button>
          <button className="px-4 py-2 bg-[#FF9F1A] text-white rounded-lg hover:bg-brand-orange/90 transition">
            How to Use
          </button>
          <button className="px-4 py-2 bg-[#FF9F1A] text-white rounded-lg hover:bg-brand-orange/90 transition">
            About Us
          </button>
        </div>
      </header>

      <p
  className="absolute top-20 left-2 transform-none border-l-4 border-indigo-500 bg-indigo-50 text-indigo-700 italic pl-4 py-2 max-w-xs shadow-md"
  >
  <span className="font-semibold">Tip:</span>{" "}
  Click anywhere on the map to view that location’s accessibility details.
  </p>

      <div className="w-full h-[500px]">
        <Map />
      </div>
    </main>
  );
}
