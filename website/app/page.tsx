//home page for website
import Image from "next/image";
import Map from "@/components/Map";

export default function Home() {
  return (
    <main className="mx-auto sm:px-10 px-5 flex flex-col">
      <header className="w-full flex items-center justify-between gap-4 py-6">
      <div className="flex items-center gap-4">
        <Image
          src="/streetscope.png"
          alt="StreetScope.ai Logo"
          width={100}
          height={100}
          className="flex-shrink-0"
        />
        <div className="flex flex-col">
          <h1 className="text-2xl sm:text-4xl font-montserrat text-[#373584] font-bold">
            StreetScope.ai
          </h1>
          <h2 className="text-lg sm:text-xl text-gray-700">
            A platform for data-driven urban planning
          </h2>
        </div>
        </div>
      
      <div className="flex items-center gap-3">
          <button className="px-4 py-2 bg-[#373584] text-white rounded hover:bg-opacity-300">
            How to Use
          </button>
          <button className="px-4 py-2 bg-orange-300 text-gray-800 rounded hover:bg-gray-300">
            Mission
          </button>
          <button className="px-4 py-2 bg-orange-300 text-gray-800 rounded hover:bg-gray-300">
            About Us
          </button>
        </div>
      </header>
      <div className="w-full h-[500px]">
        <Map />
      </div>
    </main>
  );
}
